"""Dependency-free package validation. This does not evaluate an LLM."""
import json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins'/'atlas-payments-english'
RULES={'STYLE-01','PAY-01','PAY-02','PAY-03'}

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def validate(root=ROOT):
    root=Path(root).resolve(); plugin=root/'plugins'/'atlas-payments-english'
    failures=[]
    def require(ok,message):
        if not ok:failures.append(message)
    manifests=[plugin/'plugin.json',plugin/'.codex-plugin/plugin.json',plugin/'.claude-plugin/plugin.json']
    parsed=[]
    for path in manifests:
        try:parsed.append(read(path))
        except (OSError,ValueError) as exc:failures.append(f'{path.name}: {exc}')
    if len(parsed)!=3:return failures
    identity={(m.get('name'),m.get('version'))for m in parsed}
    require(len(identity)==1,'Plugin identity/version differ across hosts')
    require(parsed[0].get('$schema')=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json','Portable manifest schema missing')
    require(parsed[1].get('skills')=='./skills/','Codex skill path missing')
    require(re.fullmatch(r'\d+\.\d+\.\d+',parsed[0]['version']) is not None,'Version must use semver')
    for m in parsed:
        require(m.get('license')=='MIT','Unexpected license')
        require(not any(k in m for k in ['mcpServers','hooks','apps','userConfig']),'Unexpected executable/service capabilities')
        require('email'not in m.get('author',{}),'Author email must not be bundled')
    ext=parsed[0].get('extensions',{}).get('com.openai',{})
    require(set(ext)<={'interface','publication','review'}and 'interface'in ext,'Unexpected OpenAI extensions')
    require(ext['interface']==parsed[1]['interface'],'Codex presentation differs from portable presentation')
    interface=ext['interface']
    for key,limit in [('displayName',30),('shortDescription',30),('longDescription',4000),('developerName',80)]:
        require(isinstance(interface.get(key),str)and 0<len(interface[key])<=limit,f'Invalid listing length: {key}')
    for key in ['websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL']:
        require(interface.get(key,'').startswith('https://')and len(interface.get(key,''))<=1024,f'Invalid listing URL: {key}')
    readme=plugin/'README.md'
    require(readme.is_file()and len(readme.read_text().split())>=40,'Plugin-local README must contain at least 40 words')
    for parent in ['.agents/plugins','.claude-plugin']:
        try:
            market=read(root/parent/'marketplace.json')
            require(market.get('name')=='atlas-payments','Marketplace identity differs')
            entries=market.get('plugins',[])
            require(len(entries)==1,'Expected one marketplace entry')
            if len(entries)==1:
                entry=entries[0];source=entry['source'];path=source['path']if isinstance(source,dict)else source
                require(path=='./plugins/atlas-payments-english','Marketplace path must target the packaged plugin')
                require(entry['name']==parsed[0]['name'],'Marketplace plugin name differs')
                require((root/path).resolve().is_relative_to(root),'Marketplace path escapes release root')
        except (OSError,ValueError,KeyError,TypeError)as exc:failures.append(f'Marketplace: {exc}')
    skill=plugin/'skills'/'atlas-payments-english'/'SKILL.md'
    try:
        body=skill.read_text();front=body.split('---',2)[1]
        require('name: atlas-payments-english'in front,'Skill name missing')
        require('description:'in front,'Skill description missing')
        for target in re.findall(r'\]\((references/[^)]+)\)',body):
            dest=(skill.parent/target).resolve()
            require(dest.is_relative_to(plugin),'Reference escapes plugin')
            require(dest.is_file(),f'Missing referenced file: {target}')
    except (OSError,IndexError)as exc:failures.append(f'Skill: {exc}')
    refs=skill.parent/'references'
    try:
        terms=read(refs/'terms.json')['terms'];ids=[t['id']for t in terms]
        require(len(terms)==255 and len(set(ids))==255,'Expected 255 unique terminology records')
        for t in terms:
            require(t['status']=='editorial_proposal',f'Unreviewed approval-state change: {t["id"]}')
            require(bool(t['definition'])and bool(t['usage']),f'Incomplete term: {t["id"]}')
            require(bool(t['sources']),f'Missing evidence: {t["id"]}')
            require(all(s['url'].startswith('https://')for s in t['sources']),f'Invalid source link: {t["id"]}')
        rules=(refs/'writing-rules.md').read_text()
        require(set(re.findall(r'^### (STYLE-\d+|PAY-\d+)$',rules,re.M))==RULES,'Rule registry mismatch')
        read(refs/'output.schema.json')
    except (OSError,ValueError,KeyError)as exc:failures.append(f'Reference data: {exc}')
    for path in root.rglob('*'):
        if any(p in {'.git','dist','__pycache__'}for p in path.relative_to(root).parts):continue
        require(not path.is_symlink(),f'Symlink prohibited: {path.relative_to(root)}')
        if not path.is_file():continue
        rel=str(path.relative_to(root))
        require(path.suffix not in {'.pdf','.docx','.xlsx','.pem','.key'},f'Unapproved binary or credential file: {rel}')
        if path.suffix in {'.pyc','.pyo'}:continue
        if rel=='plugins/atlas-payments-english/assets/icon.png':
            data=path.read_bytes()
            require(data.startswith(b'\x89PNG\r\n\x1a\n'),'Invalid project icon')
            require(len(data)<2000000,'Project icon exceeds size limit')
            continue
        try:text=path.read_text()
        except UnicodeDecodeError:failures.append(f'Unexpected binary: {rel}');continue
        require(not re.search(r'(?im)^\s*(?:#{1,6}\s*)?step\s+[3-6]\s*[:.\-–•]',text),f'Internal build-stage heading in public copy: {rel}')
        # Match real private paths and documents without embedding an actual path.
        require(not re.search(r'/U[s]ers/|/ho[m]e/|docs[.]google[.]com/(?:document|spreadsheets)/d/',text),f'Private-location marker: {rel}')
        require(not re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',text),f'Private-key marker: {rel}')
        require(not re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|sk[-_]live[-_][A-Za-z0-9]{16,}',text),f'Credential marker: {rel}')
    return failures

if __name__=='__main__':
    errors=validate()
    if errors:
        for error in errors:print('FAIL:',error)
        raise SystemExit(1)
    print('Release structure, references and selected privacy/security checks passed.')
    print('This does not establish model behavior, full STE conformance or operational correctness.')
