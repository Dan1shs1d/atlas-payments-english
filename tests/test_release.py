import copy,importlib.util,json,sys,tempfile,unittest,zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
from grade_responses import grade
from validate_release import validate
from package_release import package,ALLOW

CASES={c['id']:c for c in json.loads((ROOT/'evals/cases.json').read_text())}

def rewrite(text):
    return dict(label='Reviewed against Atlas Payments English',mode='Rewrite',revised_text=text,questions=[],checks_not_completed=['Full STE and operational validation not completed.'])

def review():
    return dict(label='Reviewed against Atlas Payments English',mode='Review',findings=[],optional_suggestions=[],questions=[],checks_not_completed=['Full STE and operational validation not completed.'])

class ReleaseTests(unittest.TestCase):
    def test_release_structure_and_boundaries(self):self.assertEqual(validate(),[])
    def test_core_and_host_manifests_agree(self):
        p=ROOT/'plugins/atlas-payments-english';ms=[json.loads((p/x).read_text())for x in ['plugin.json','.codex-plugin/plugin.json','.claude-plugin/plugin.json']]
        self.assertEqual(len({(m['name'],m['version'])for m in ms}),1)
    def test_packaging_is_reproducible_and_allowlisted(self):
        with tempfile.TemporaryDirectory()as d:
            a,h1=package(Path(d)/'a');b,h2=package(Path(d)/'b');self.assertEqual(h1,h2)
            with zipfile.ZipFile(a)as z:
                self.assertEqual(set(z.namelist()),ALLOW)
                self.assertFalse(any('..'in Path(x).parts or x.startswith('/')for x in z.namelist()))
    def test_canonical_fixture_passes(self):
        self.assertEqual(grade(CASES['EX-01'],rewrite(CASES['EX-01']['expected']['canonical_rewrite'])),[])
    def test_permission_to_obligation_fails(self):
        r=rewrite(CASES['EX-01']['expected']['canonical_rewrite'].replace('may','must'));self.assertTrue(grade(CASES['EX-01'],r))
    def test_removed_shipping_condition_fails(self):
        self.assertTrue(grade(CASES['EX-01'],rewrite('If the authorization is approved, the merchant may capture the payment.')))
    def test_changed_currency_fails(self):
        self.assertTrue(grade(CASES['EX-04'],rewrite(CASES['EX-04']['text'].replace('USD','EUR'))))
    def test_changed_enum_fails(self):
        self.assertTrue(grade(CASES['EX-04'],rewrite(CASES['EX-04']['text'].replace('requires_capture','succeeded'))))
    def test_invented_outcome_fails(self):
        self.assertTrue(grade(CASES['EX-05'],rewrite('The merchant received an approved authorization request.')))
    def test_recommendation_strength_fails(self):
        self.assertTrue(grade(CASES['EX-06'],rewrite('The operator must retain the dispute record.')))
    def test_boundary_change_fails(self):
        self.assertTrue(grade(CASES['EX-12'],rewrite('If the amount is at least USD 100, send the case for review.')))
    def test_event_order_change_fails(self):
        self.assertTrue(grade(CASES['EX-13'],rewrite('The acquirer received the settlement report before clearing.')))
    def test_ambiguous_rewrite_must_retain_input_and_ask(self):
        self.assertTrue(grade(CASES['EX-03'],rewrite('Refund the payment.')))
        r=rewrite('Reverse the payment.');r['questions']=['What is the current payment state and intended operation?'];self.assertEqual(grade(CASES['EX-03'],r),[])
    def test_default_review_has_focused_question(self):
        r=review();r['findings']=[dict(excerpt='Reverse the payment.',rule_id='PAY-03',issue='Payment state and intended operation missing.',severity='blocker',suggested_edit='What is the current payment state and intended operation?')]
        self.assertEqual(grade(CASES['EX-02'],r),[])
    def test_hallucinated_excerpt_fails(self):
        r=review();r['findings']=[dict(excerpt='Refund the payment.',rule_id='PAY-03',issue='Missing state',severity='blocker',suggested_edit='Which state?')];self.assertTrue(grade(CASES['EX-02'],r))
    def test_unknown_rule_id_fails(self):
        r=review();r['findings']=[dict(excerpt='Reverse the payment.',rule_id='PAY-99',issue='Missing state',severity='blocker',suggested_edit='Which state?')];self.assertTrue(grade(CASES['EX-02'],r))
    def test_valid_source_does_not_need_invented_findings(self):self.assertEqual(grade(CASES['EX-14'],review()),[])
    def test_incomplete_check_disclosure_required(self):
        r=review();r['checks_not_completed']=[];self.assertTrue(grade(CASES['EX-14'],r))
    def test_invalid_response_type_rejected(self):self.assertTrue(grade(CASES['EX-01'],'not structured output'))
    def test_refund_questions_must_cover_amount_currency_and_deadline(self):
        r=review();r['findings']=[dict(excerpt='within five days',rule_id='PAY-03',issue='Missing basis',severity='blocker',suggested_edit='What event starts the period; calendar or business days?')]
        self.assertTrue(grade(CASES['EX-16'],r))
        r['questions']=['What amount and currency should be refunded?']
        self.assertEqual(grade(CASES['EX-16'],r),[])
    def test_case_ids_are_unique(self):self.assertEqual(len(CASES),20)
    def test_semantic_equivalents_pass(self):
        for key,text in [('EX-10','The merchant may refund EUR 50 only after the customer has returned the goods.'),('EX-12','If the amount exceeds USD 100, send the case for review.'),('EX-13','After clearing, the acquirer received the settlement report.'),('EX-20','The provider returned `authentication_required`. No authorization approval was received.')]:
            with self.subTest(key=key):self.assertEqual(grade(CASES[key],rewrite(text)),[])
    def test_removed_necessary_condition_fails(self):
        self.assertTrue(grade(CASES['EX-10'],rewrite('The merchant may refund EUR 50 after the customer has returned the goods.')))
    def test_lost_negation_fails(self):
        self.assertTrue(grade(CASES['EX-20'],rewrite('The provider returned `authentication_required`. Authorization approval was received.')))
    def test_inclusive_exceeds_wording_fails(self):
        self.assertTrue(grade(CASES['EX-12'],rewrite('If the amount exceeds USD 100 or equals USD 100, send the case for review.')))
    def test_prompt_does_not_expose_gold_answers(self):
        from run_acceptance import prompt_for
        prompt=prompt_for(CASES['EX-01'],'codex')
        self.assertNotIn(CASES['EX-01']['expected']['canonical_rewrite'],prompt)
        self.assertIn(CASES['EX-01']['text'],prompt)
    def test_default_mode_is_not_supplied_by_harness(self):
        from run_acceptance import prompt_for
        self.assertNotIn('Review',prompt_for(CASES['EX-02'],'codex'))

if __name__=='__main__':unittest.main()
