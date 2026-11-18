"""Create a deterministic, allowlisted plugin ZIP and SHA-256 digest."""
import hashlib,json,zipfile
from pathlib import Path
from validate_release import validate,ROOT

PLUGIN=ROOT/'plugins/atlas-payments-english'
ALLOW={
    'plugin.json','.codex-plugin/plugin.json','.claude-plugin/plugin.json',
    'assets/icon.png','README.md',
    'skills/atlas-payments-english/SKILL.md',
    'skills/atlas-payments-english/agents/openai.yaml',
    'skills/atlas-payments-english/references/writing-rules.md',
    'skills/atlas-payments-english/references/payments-glossary.md',
    'skills/atlas-payments-english/references/terms.json',
    'skills/atlas-payments-english/references/examples.md',
    'skills/atlas-payments-english/references/output.schema.json',
    'LICENSE','NOTICE.md','PRIVACY.md'
}

def package(outdir=None):
    errors=validate()
    if errors:raise ValueError('; '.join(errors))
    version=json.loads((PLUGIN/'plugin.json').read_text())['version']
    outdir=Path(outdir)if outdir else ROOT/'dist';outdir.mkdir(parents=True,exist_ok=True)
    archive=outdir/f'atlas-payments-english-{version}.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9)as z:
        for name in sorted(ALLOW):
            path=(ROOT/name)if name in {'LICENSE','NOTICE.md','PRIVACY.md'}else PLUGIN/name
            info=zipfile.ZipInfo(name,date_time=(2026,11,18,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
            z.writestr(info,path.read_bytes())
    digest=hashlib.sha256(archive.read_bytes()).hexdigest()
    (outdir/'SHA256SUMS').write_text(digest+'  '+archive.name+'\n')
    return archive,digest

if __name__=='__main__':
    archive,digest=package();print(archive.name,digest)
