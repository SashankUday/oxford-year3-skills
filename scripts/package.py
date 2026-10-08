#!/usr/bin/env python3
"""Build a ZIP per completed skill, with one skill folder at its root."""
from pathlib import Path
import zipfile
ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'downloads'
DEST.mkdir(exist_ok=True)
for skill in sorted((ROOT / 'skills').iterdir()):
    if not skill.is_dir() or not (skill / 'SKILL.md').is_file():
        continue
    path = DEST / (skill.name + '.zip')
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for source in sorted(skill.rglob('*')):
            if source.is_file():
                archive.write(source, skill.name + '/' + str(source.relative_to(skill)))
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        assert skill.name + '/SKILL.md' in archive.namelist()
    print(path.relative_to(ROOT))
