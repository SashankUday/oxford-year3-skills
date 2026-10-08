#!/usr/bin/env python3
"""Install the complete available skill collection without silent overwrites."""
import argparse, shutil, tempfile, time
from pathlib import Path

def install(repo, destination, update=False, dry_run=False):
    skills = sorted(p for p in (repo / 'skills').iterdir() if p.is_dir() and (p / 'SKILL.md').is_file())
    if not skills:
        raise ValueError('No completed skills found')
    for source in skills:
        target = destination / source.name
        if target.exists() and not update:
            raise FileExistsError(f'{target} already exists; use --update to replace it with a backup')
    if dry_run:
        for source in skills:
            print(f'Would install {source.name} to {destination / source.name}')
        return
    destination.mkdir(parents=True, exist_ok=True)
    for source in skills:
        target = destination / source.name
        stage = Path(tempfile.mkdtemp(prefix=f'.{source.name}-', dir=destination))
        backup = None
        try:
            shutil.copytree(source, stage, dirs_exist_ok=True)
            if target.exists():
                backup = destination / f'.{source.name}-backup-{time.time_ns()}'
                target.rename(backup)
            stage.rename(target)
        except Exception:
            if backup is not None and not target.exists():
                backup.rename(target)
            shutil.rmtree(stage, ignore_errors=True)
            raise
        print(f'Installed {source.name} to {target}')
        if backup:
            print(f'Previous version saved at {backup}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--platform', choices=['codex', 'claude'], required=True)
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--update', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    destination = args.destination or Path.home() / ('.agents/skills' if args.platform == 'codex' else '.claude/skills')
    install(Path(__file__).resolve().parents[1], destination.expanduser(), args.update, args.dry_run)
