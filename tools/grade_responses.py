"""Grade saved structured model outputs against explicit fixtures, offline.

Usage: python3 tools/grade_responses.py --responses responses.jsonl
Each line: {"id":"EX-01","response":{...matching output.schema.json...}}
No model or network calls are made. A pass covers the fixture, not all semantics.
"""
import argparse,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RULES={'STYLE-01','PAY-01','PAY-02','PAY-03'}

def grade(case,response):
    errors=[]
    if not isinstance(response,dict):return ['Response must be an object']
    mode=response.get('mode')
    fields={'label','mode','questions','checks_not_completed'}
    if mode=='Review':fields|={'findings','optional_suggestions'}
    elif mode=='Rewrite':fields|={'revised_text'}
    if set(response)!=fields:errors.append('Unexpected or missing response fields')
    if response.get('label')!='Reviewed against Atlas Payments English':errors.append('Result label differs')
    if mode!=case['expected']['mode']:errors.append('Wrong mode')
    for name in ['questions','checks_not_completed']:
        if not isinstance(response.get(name),list)or not all(isinstance(s,str)and s.strip()for s in response.get(name,[])):errors.append(f'{name} must be an array of nonempty strings')
    if not response.get('checks_not_completed'):errors.append('Disclose unchecked conformance/operational checks')
    expected=case['expected']
    if expected.get('questions_required')and not response.get('questions'):
        questions=' '.join(f.get('suggested_edit','')for f in response.get('findings',[])if isinstance(f,dict))
        if '?'not in questions:errors.append('Required clarification missing')
    if mode=='Rewrite':
        text=response.get('revised_text')
        if not isinstance(text,str):return errors+['Missing revised_text']
        for literal in expected.get('preserve',[]):
            if literal not in text:errors.append(f'Protected content missing: {literal}')
        for value in expected.get('forbid_in_rewrite',[]):
            if value.lower()in text.lower():errors.append(f'Forbidden meaning change: {value}')
        if expected.get('canonical_rewrite')and text!=expected['canonical_rewrite']:errors.append('Canonical regression fixture differs; human semantic review needed')
        if expected.get('retain_input')and text!=case['text']:errors.append('Ambiguous passage changed without clarification')
    elif mode=='Review':
        findings=response.get('findings')
        if not isinstance(findings,list):return errors+['Missing findings array']
        for finding in findings:
            if not isinstance(finding,dict):errors.append('Finding must be an object');continue
            if not finding.get('excerpt')or finding['excerpt']not in case['text']:errors.append('Excerpt is not verbatim source text')
            if finding.get('rule_id')not in RULES:errors.append('Unknown rule ID')
            if finding.get('severity')not in ['error','blocker']:errors.append('Unknown severity')
            if not all(isinstance(finding.get(k),str)and finding[k].strip()for k in ['issue','suggested_edit']):errors.append('Finding lacks an issue or suggested edit')
        found={f.get('rule_id')for f in findings if isinstance(f,dict)}
        if not set(expected.get('rules',[]))<=found:errors.append('Expected finding missing')
        if expected.get('no_findings')and findings:errors.append('Invented violation for this fixture')
        if not isinstance(response.get('optional_suggestions'),list):errors.append('Missing optional_suggestions array')
    else:errors.append('Unsupported mode')
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--responses',type=Path,required=True);args=p.parse_args()
    cases={c['id']:c for c in json.loads((ROOT/'evals/cases.json').read_text())}
    failed=0;seen=set()
    for line in args.responses.read_text().splitlines():
        if not line.strip():continue
        item=json.loads(line);key=item['id']
        if key not in cases:raise SystemExit(f'Unknown case ID: {key}')
        if key in seen:raise SystemExit(f'Duplicate case ID: {key}')
        seen.add(key);errors=grade(cases[key],item.get('response'))
        print(json.dumps({'id':key,'pass':not errors,'errors':errors}));failed+=bool(errors)
    missing=set(cases)-seen
    if missing:print('NOT RUN:',', '.join(sorted(missing)))
    if not seen:raise SystemExit('No model responses supplied')
    raise SystemExit(1 if failed or missing else 0)

if __name__=='__main__':main()
