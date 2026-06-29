from pathlib import Path

required = [
    'AGENTS.md',
    'SKILL.md',
    'USAGE.md',
    'conventions/TEMPLATE.md',
    'references/gunplay-framework.md',
    'references/weapon-balance.md',
    'references/ttk-etk-model.md',
    'references/shooting-skill-design.md',
    'templates/blank-weapon-design.md',
    'templates/blank-skill-design.md',
    'prompts/codex-task-prompts.md',
]

root = Path(__file__).resolve().parents[1]
missing = [p for p in required if not (root / p).exists()]
if missing:
    print('Missing files:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('Repo structure OK.')
