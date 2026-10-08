#!/usr/bin/env python3
"""Check discovery paths, references, metadata and install/update behaviour."""
from pathlib import Path
from urllib.parse import unquote
import re, json, tempfile, importlib.util
ROOT = Path(__file__).resolve().parents[1]
count = 0
for skill in sorted((ROOT / 'skills').iterdir()):
    if not skill.is_dir():
        continue
    text = (skill / 'SKILL.md').read_text()
    match = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---', text)
    assert match and match[1] == skill.name and len(match[2]) <= 1024
    count += 1
for file in ROOT.rglob('*.md'):
    if '.git' in file.parts:
        continue
    text = file.read_text()
    assert '/Users/' not in text, file
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if not link.startswith(('http:', 'https:', '#')):
            assert (file.parent / unquote(link.split('#')[0])).exists(), (file, link)
manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
assert manifest['name'] == marketplace['plugins'][0]['name']
assert (ROOT / marketplace['plugins'][0]['source']).resolve() == ROOT
assert all(p.suffix.lower() != '.pdf' for p in ROOT.rglob('*') if p.is_file())
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
with tempfile.TemporaryDirectory() as scratch:
    target = Path(scratch) / 'skills'
    module.install(ROOT, target, dry_run=True)
    assert not target.exists()
    module.install(ROOT, target)
    original = target / 'paper1-marker/SKILL.md'
    original.write_text('LOCAL EDIT')
    try:
        module.install(ROOT, target)
    except FileExistsError:
        pass
    else:
        raise AssertionError('Existing skill was overwritten without update')
    assert original.read_text() == 'LOCAL EDIT'
    module.install(ROOT, target, update=True)
    assert original.read_text() == (ROOT / 'skills/paper1-marker/SKILL.md').read_text()
    backups = list(target.glob('.paper1-marker-backup-*'))
    assert len(backups) == 1 and (backups[0] / 'SKILL.md').read_text() == 'LOCAL EDIT'
print(f'Checks passed: {count} skill(s), relative references, manifests, installer and update backups.')
