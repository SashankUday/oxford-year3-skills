# Oxford Year 3 Skills

Reusable AI study workflows for incoming Oxford third-year medics, created by Sashank Uday. The available skill is **Paper 1 marking and essay-plan feedback**. Paper 2/Paper 3 markers and other skills are planned, not yet included.

[Read Sashank's third-year workflow](advice/year-3-workflow.md): early project completion, choosing your own five options then narrowing to four, tutorial/evidence preparation, Paper 3 from Michaelmas, and spreading revision with breaks. This is personal advice, not official course guidance or a grade guarantee.

## Install all available skills

### Claude Code — one collection

After this repository is published, run:

```text
/plugin marketplace add SashankUday/oxford-year3-skills
/plugin install oxford-year3-skills@oxford-year3-skills
```

Use `/oxford-year3-skills:paper1-marker` to invoke the marker. The plugin contains every completed skill under skills/. Update the marketplace/plugin to receive future versions; newly added skills are not silently installed into unrelated accounts.

### Codex or Claude Code — download and install locally

Clone or download this repository, then from its folder run:

```text
python3 scripts/install.py --platform codex
```

or:

```text
python3 scripts/install.py --platform claude
```

The installer copies **all completed skills** into the appropriate user skills directory. It has no network dependency and will not replace existing skills unless you request `--update`; updates save a backup. `--dry-run` previews the destinations. For Codex, use `$paper1-marker`.

### Claude app and ChatGPT

Run `python3 scripts/package.py` to create an upload ZIP for each completed skill under downloads/. In Claude's custom-skills interface, upload the individual skill ZIP. For ChatGPT, use the compatible skill-import route available to your account, or attach SKILL.md and its compact references to a chat/project and ask it to follow them. Attaching files is a manual-context fallback, not installation or automatic skill discovery. A public GitHub repo alone does not install every skill into every ChatGPT or Claude account. Distribution through the ChatGPT plugin directory is a separate step.

## Available skill

[paper1-marker](skills/paper1-marker/SKILL.md) assesses an essay against its exact question, gives a justified indicative band and priorities, and reviews mind maps as full essay plans. Historical official descriptors, tutor comments, derived interpretations and personal preparation advice remain distinguishable. Two tutorial grades informed the design; its marking accuracy has not been independently validated.

Provide your **exact question**, essay/plan and whether it is timed practice or tutorial work. Supply current criteria where available.

## Structure

```text
skills/paper1-marker/    Skill and supporting text references
advice/                 Sashank's Year 3 workflow and mind-map example
scripts/                Install all skills; create upload ZIPs
.claude-plugin/          Claude Code collection/plugin metadata
.github/workflows/      Structural checks for contributions
ROADMAP.md              Proposed skills, clearly marked as unfinished
```

## Source material

The public edition includes summarised tutor lessons and a historical criteria summary. Full marked PDFs, tutor identity metadata, lecture slides, exported decks and the roughly 486 MB Year 3 collection remain local. Read the [source provenance](skills/paper1-marker/references/provenance.md) for the assessment sources and limits.

## Development

Run `python3 scripts/check.py` and `python3 scripts/package.py` before publishing. Add a new completed skill under skills/ with a SKILL.md and only the references it needs; keep source provenance explicit. The all-skills installer discovers it automatically.

Installation mechanics follow [OpenAI's skills documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code's marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces). This repository is an independent student resource, not an Oxford-endorsed marking service.
