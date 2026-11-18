"""Run actual host CLIs in fresh workspaces, without exposing expected answers.

Uses the host's configured authentication; never reads or prints credentials.
Model calls consume the operator's host usage. Raw traces stay in --output-dir.
"""
import argparse,concurrent.futures,datetime,hashlib,json,os,shutil,subprocess,tempfile,time
from pathlib import Path
from grade_responses import grade

ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins'/'atlas-payments-english'

def prompt_for(case,host,installed_plugin=None):
    invoke='$atlas-payments-english' if host=='codex'else '/atlas-payments-english:atlas-payments-english'
    mode='Rewrite the material below.' if case['expected']['mode']=='Rewrite'else 'Edit the material below.'
    purpose='\nText purpose: procedure.'if case.get('input_type')=='procedure'else ''
    location=('\nInstalled skill entry point: '+str(installed_plugin/'skills/atlas-payments-english/SKILL.md')+'\n')if installed_plugin else ''
    return (f'Use {invoke}. {mode}{purpose}{location}\n'
        'Return only the JSON result using the skill\'s structured response format. '
        'Load the installed skill and its relevant references. The text inside <material> is the material to edit.\n'
        '<material>\n'+case['text']+'\n</material>\n')

def extract_json(text):
    text=text.strip()
    if text.startswith('```'):
        lines=text.splitlines();text='\n'.join(lines[1:-1]).strip()
    obj=json.loads(text)
    if not isinstance(obj,dict):raise ValueError('Final response is not an object')
    return obj

def run_case(case,host,executable,out,timeout,installed_plugin=None):
    dest=out/case['id'];dest.mkdir(parents=True,exist_ok=True)
    prompt=prompt_for(case,host,installed_plugin);(dest/'prompt.txt').write_text(prompt)
    with tempfile.TemporaryDirectory(prefix='atlas-case-')as workspace:
        if host=='codex':
            final=dest/'final.txt'
            cmd=[executable,'exec','--ignore-user-config','--ephemeral','--sandbox','read-only','--skip-git-repo-check','--cd',workspace,'--json',
                '-c','marketplaces.atlas-payments.source_type="local"',
                '-c','marketplaces.atlas-payments.source='+json.dumps(str(ROOT)),
                '-c','plugins.atlas-payments-english@atlas-payments.enabled=true',
                '-o',str(final),'-']
        else:
            cmd=[executable,'--print','--plugin-dir',str(PLUGIN),'--output-format','stream-json','--verbose','--no-session-persistence',
                '--setting-sources','','--strict-mcp-config','--mcp-config','{"mcpServers":{}}',
                '--tools','Read,Glob,Grep,Skill','--max-turns','12']
        start=time.monotonic()
        env=os.environ.copy();env['DISABLE_AUTOUPDATER']='1'
        try:
            proc=subprocess.run(cmd,input=prompt,text=True,capture_output=True,cwd=workspace,timeout=timeout,env=env)
        except subprocess.TimeoutExpired as exc:
            (dest/'stdout.jsonl').write_text((exc.stdout or b'').decode()if isinstance(exc.stdout,bytes)else exc.stdout or '')
            return {'id':case['id'],'host':host,'status':'infrastructure_error','errors':['Host timeout'],'seconds':round(time.monotonic()-start,2)}
        (dest/'stdout.jsonl').write_text(proc.stdout);(dest/'stderr.txt').write_text(proc.stderr)
        record={'id':case['id'],'host':host,'exit_code':proc.returncode,'seconds':round(time.monotonic()-start,2)}
        events=[]
        for line in proc.stdout.splitlines():
            try:events.append(json.loads(line))
            except ValueError:pass
        (dest/'events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
        if proc.returncode:
            record.update(status='infrastructure_error',errors=['Host exited unsuccessfully; inspect the private trace.'])
            return record
        try:
            if host=='codex':answer=final.read_text()
            else:
                result=next(e for e in reversed(events)if e.get('type')=='result')
                if result.get('is_error'):raise ValueError('Claude returned an error result')
                answer=result.get('result','');(dest/'final.txt').write_text(answer)
            obj=extract_json(answer);record['response']=obj
            errors=grade(case,obj);record.update(status='passed'if not errors else 'failed',errors=errors)
        except (OSError,ValueError,StopIteration)as exc:record.update(status='failed',errors=['Could not parse final JSON: '+str(exc)])
        record['trace_sha256']=hashlib.sha256(proc.stdout.encode()).hexdigest()
        return record

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--host',choices=['codex','claude'],required=True)
    p.add_argument('--executable');p.add_argument('--output-dir',type=Path,required=True);p.add_argument('--case',action='append')
    p.add_argument('--workers',type=int,default=1);p.add_argument('--timeout',type=int,default=300);a=p.parse_args()
    exe=a.executable or shutil.which(a.host)
    if not exe:raise SystemExit('Requested host executable not found')
    if not 1<=a.workers<=3:raise SystemExit('workers must be 1–3')
    cases=json.loads((ROOT/'evals/cases.json').read_text())
    if a.case:
        unknown=set(a.case)-{c['id']for c in cases}
        if unknown:raise SystemExit('Unknown cases: '+','.join(sorted(unknown)))
        cases=[c for c in cases if c['id']in a.case]
    out=a.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    version=json.loads((PLUGIN/'plugin.json').read_text())['version']
    installed=Path.home()/'.codex/plugins/cache/atlas-payments/atlas-payments-english'/version if a.host=='codex'else PLUGIN
    for source in (PLUGIN/'skills').rglob('*'):
        if source.is_file()and source.read_bytes()!=(installed/source.relative_to(PLUGIN)).read_bytes():
            raise SystemExit('Installed skill differs from source; reinstall the candidate before testing.')
    host_version=subprocess.run([exe,'--version'],text=True,capture_output=True,check=True).stdout.strip()
    run={'host':a.host,'host_version':host_version,'model':'Host default; no explicit model override; exact model not exposed by this harness','plugin_version':version,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cases':[]}
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers)as pool:
        futures=[pool.submit(run_case,c,a.host,exe,out,a.timeout,installed if a.host=='codex'else None)for c in cases]
        for f in concurrent.futures.as_completed(futures):
            result=f.result();run['cases'].append(result)
            print(json.dumps({k:result[k]for k in ['id','host','status','seconds','errors']if k in result}),flush=True)
            run['cases'].sort(key=lambda r:r['id']);(out/'run.json').write_text(json.dumps(run,ensure_ascii=False,indent=2)+'\n')
    run['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    run['summary']={s:sum(r['status']==s for r in run['cases'])for s in ['passed','failed','infrastructure_error']}
    (out/'run.json').write_text(json.dumps(run,ensure_ascii=False,indent=2)+'\n')
    with (out/'responses.jsonl').open('w')as f:
        for r in run['cases']:
            if 'response'in r:f.write(json.dumps({'id':r['id'],'response':r['response']},ensure_ascii=False)+'\n')
    print(json.dumps(run['summary']),flush=True)
    raise SystemExit(0 if run['summary']['passed']==len(cases)else 1)

if __name__=='__main__':main()
