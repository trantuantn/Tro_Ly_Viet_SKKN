from pathlib import Path
import re
p=Path(__file__).resolve().parents[1]
errors=[]
s=(p/'SKILL.md').read_text()
if not s.startswith('---\nname: skkn-master-pro\ndescription:'): errors.append('frontmatter')
for f in p.rglob('*.md'):
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',f.read_text()):
        if '://' not in link and not link.startswith('#') and not (f.parent/link.split('#')[0]).exists(): errors.append(str(f.relative_to(p))+': '+link)
for f in ['references/'+x+'.md' for x in ['workflow','lessons-learned','error-knowledge-base','feedback-system','success-patterns','quality-rubric','legal-framework','evidence-policy']]:
    if not (p/f).exists(): errors.append('missing '+f)
weights=[int(x) for x in re.findall(r'^\|[^|]+\| (\d+) \|', (p/'references/quality-rubric.md').read_text(),re.M)]
if len(weights)!=8 or sum(weights)!=100:errors.append('rubric weights')
print('PASS: structure, relative links, rubric' if not errors else '\n'.join(errors))
raise SystemExit(bool(errors))
