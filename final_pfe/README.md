# Tahkik --- Final PFE Report (Combined Edition)

This folder contains the LaTeX sources of the **combined** Tahkik
Final Year Project report. It merges three previously separate documents
into a single PDF:

| Part     | Title                                                     | Source(s)                                  |
|----------|-----------------------------------------------------------|--------------------------------------------|
| Part I   | Tahkik Mobile and Web Platform                            | `tahkik_pfe/*.tex`                         |
| Part II  | Tahkik Inference Server --- Technical Report              | `server_report.tex` + `server_report_part{2,3,4}.tex` |
| Part III | AI-Powered Quranic Recitation Analysis (Whisper / Warsh)  | `model train.tex`                          |

---

## Folder layout

```
final pfe/
├── main.tex                                   # Master file (entry point)
├── preamble.tex                               # Combined preamble for all 3 reports
├── README.md                                  # This file
│
├── front/
│   ├── cover.tex                              # Combined cover page
│   ├── dedication.tex                         # Project dedication
│   ├── acknowledgements.tex                   # Acknowledgements
│   └── abstract.tex                           # Combined Abstract / Resume
│
├── chapters_main/                             # Part I (Mobile + Web Platform)
│   ├── general_introduction.tex
│   ├── chapter1_state_of_art.tex
│   ├── chapter2_conceptual_study.tex
│   ├── chapter3_implementation.tex
│   ├── general_conclusion.tex                 # (kept for reference, not inputed)
│   └── general_conclusion_combined.tex        # Final conclusion of the merged doc
│
├── chapters_server/                           # Part II (Inference Server)
│   ├── server_part1.tex                       # Server chapters 1-5
│   ├── server_part2.tex                       # Server chapters 6-11
│   └── server_part3.tex                       # Server chapters 12-15
│
├── chapters_model/                            # Part III (Whisper / Warsh AI)
│   └── model_body.tex                         # Intro + 7 chapters + appendices
│
└── back/
    └── bibliography.tex                       # Merged bibliography (\thebibliography)
```

The figures live in the original location at `../tahkik_pfe/figures/`.
The `\graphicspath{...}` declaration in `preamble.tex` makes every
`\includegraphics{figures/...}` call resolve against that path
automatically, so **no figures need to be copied into this folder**.

---

## How to compile

### Option A --- Overleaf (recommended)

1. Create a new Overleaf project.
2. Upload the entire `final pfe/` folder **and** the `tahkik_pfe/figures/`
   folder (place the latter at `../tahkik_pfe/figures/` relative to the
   `final pfe/` root, mirroring the local layout).
3. Set `main.tex` as the main document.
4. Compile with **pdfLaTeX** (the standard engine).
5. Run the compile a second time so the table of contents,
   list of figures, and cross-references resolve.

> Tip: an even simpler Overleaf layout is to put `final pfe/`
> at the repo root (no parent folder) and edit the `\graphicspath{...}`
> entry in `preamble.tex` to point to `figures/` (a copy of
> `tahkik_pfe/figures/` placed alongside `main.tex`).

### Option B --- Local TeX Live / MacTeX

```bash
# From inside this folder:
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex   # second pass for refs
```

The output will be `main.pdf` in the same folder.

### Option C --- `latexmk` (fully automatic)

```bash
latexmk -pdf -interaction=nonstopmode main.tex
```

---

## What changed compared to the three original reports?

1. **Single visual identity.** All three reports already shared the
   same colour palette and tcolorbox styles, so they merge cleanly.
2. **Single front matter.** One cover, one dedication, one
   acknowledgements, one combined abstract (English + French).
3. **Three Parts** instead of three documents. `\part{...}` headings
   group the chapters; chapter numbering is continuous across the
   whole volume.
4. **Renamed Part III intro and conclusion** to avoid duplicate
   "General Introduction / General Conclusion" entries in the TOC:
   * `General Introduction` of model train.tex --> `Introduction --- AI/ML Pipeline`
   * `General Conclusion`   of model train.tex --> `Summary of Part III`
5. **`\phaseblock` shim.** The server report defines `\phaseblock`
   with a single-argument title, while the main dissertation and the
   model-training report use a 3-argument `\phaseblock{N}{Title}{body}`.
   The combined `preamble.tex` exposes both forms (`\phaseblock` and
   `\phaseblocks`) so all three sources keep working unchanged. The
   server report files in `chapters_server/` were rewritten to call
   `\phaseblocks` instead of `\phaseblock`.
6. **One bibliography.** The references from all three reports are
   merged into `back/bibliography.tex`. All `\cite{...}` calls from
   the model-training body still resolve. Server-report and
   tahkik_pfe entries are listed alongside (kept as `\bibitem`s for
   completeness).

---

## Authors

* Benhadjer Mohamed
* Bouziani Alaa Eddine

**Supervisor:** Mme. Meriem Ali Khoudja
**Institution:** Yahia Fares University of Medea --- L3 Computer Science --- 2025/2026
