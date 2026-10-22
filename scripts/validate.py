from pathlib import Path
import re, json
p=Path(__file__).resolve().parents[1]
errors=[]
s=(p/'SKILL.md').read_text()
if not s.startswith('---\nname: skkn-master-pro\ndescription:'): errors.append('frontmatter')
for f in p.rglob('*.md'):
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',f.read_text()):
        if '://' not in link and not link.startswith('#') and not (f.parent/link.split('#')[0]).exists(): errors.append(str(f.relative_to(p))+': '+link)
for f in ['references/'+x+'.md' for x in ['workflow','lessons-learned','error-knowledge-base','feedback-system','success-patterns','quality-rubric','legal-framework','evidence-policy']]:
    if not (p/f).exists(): errors.append('missing '+f)
for f in ['README.md','CHANGELOG.md','LICENSE','references/provenance.md','examples/sample-skkn.md','tests/test-cases.md','tests/acceptance-criteria.md']+['templates/'+x+'.md' for x in ['standard-skkn','promotion-skkn','ai-innovation-skkn','survey-template','impact-report']]:
    if not (p/f).is_file() or not (p/f).read_text().strip(): errors.append('missing/empty '+f)
try:
    feedback=json.loads((p/'templates/feedback-record.json').read_text())
    if feedback.get('status')!='received' or not isinstance(feedback.get('history'),list): errors.append('feedback template schema')
except (OSError,ValueError,AttributeError): errors.append('feedback template invalid')
weights=[int(x) for x in re.findall(r'^\|[^|]+\| (\d+) \|', (p/'references/quality-rubric.md').read_text(),re.M)]
if len(weights)!=8 or sum(weights)!=100:errors.append('rubric weights')
print('PASS: structure, relative links, rubric' if not errors else '\n'.join(errors))
raise SystemExit(bool(errors))
