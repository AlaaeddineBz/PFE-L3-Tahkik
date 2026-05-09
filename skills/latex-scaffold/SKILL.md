---
name: latex-scaffold
description: Generate the complete LaTeX project skeleton for a PFE L3 mémoire (Tahkik project)
inputs:
  - project_title: The main project title
  - subtitle: A short subtitle or tagline
  - authors: List of author names with group info
  - supervisor: Name of the supervisor
  - university: University name (default "University of Yahia Fares Medea")
  - department: Department name (default "Department of Computer Science")
  - faculty: Faculty name (default "Faculty of Sciences & Technology")
  - academic_year: Academic year string (default "2025 / 2026")
  - badge_keywords: Keywords for the cover page badge (e.g., "AI · Deep Learning · NLP · Tajweed")
  - abstract_en: English abstract text
  - abstract_fr: French abstract text
  - abstract_ar: Arabic abstract text
  - keywords_en: English keywords
  - keywords_fr: French keywords
  - dedication_text: Dedication message
  - acknowledgements_text: Acknowledgements message
outputs:
  - main.tex (root document with \input{} calls)
  - preamble.tex (all packages, colors, styles, boxes)
  - chapters/ directory with placeholder .tex files
---

# LaTeX Scaffold Generator

## Context

This skill generates the complete LaTeX project skeleton for an L3 PFE mémoire at Yahia Fares University of Medea. It produces a compilable document structure following the Tahkik project's established design system, including the full preamble, cover page, front matter (dedication, acknowledgements, trilingual abstract), table of contents, and chapter file stubs.

The design system uses a `report` document class with custom `tcolorbox` styles, `titlesec` formatting, and `fancyhdr` headers. All visual tokens (colors, box styles, section formats) are centralized in `preamble.tex` for reuse across all chapters.

## Instructions

When invoked, perform the following steps:

### Step 1 — Create `preamble.tex`

Generate a standalone preamble file containing ALL of the following:

```latex
% ─── PACKAGES ───────────────────────────────────────────────────────────────
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{setspace}
\usepackage{array}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{parskip}
\usepackage{mdframed}
\usepackage{tikz}
\usetikzlibrary{positioning, shapes.geometric, arrows.meta, calc, fit}
\usepackage{amsmath}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{float}
\usepackage{makecell}
\usepackage{listings}
\usepackage{longtable}

% ─── PAGE GEOMETRY ──────────────────────────────────────────────────────────
\geometry{
    a4paper,
    left=2.5cm,
    right=2.5cm,
    top=2.5cm,
    bottom=2.5cm,
    headheight=15pt
}

% ─── COLOURS ────────────────────────────────────────────────────────────────
\definecolor{darkbg}{HTML}{0f172a}
\definecolor{emerald}{HTML}{10b981}
\definecolor{teal}{HTML}{0d9488}
\definecolor{gold}{HTML}{d4af37}
\definecolor{goldlt}{HTML}{b8920a}
\definecolor{slategray}{HTML}{64748b}
\definecolor{lightblue}{HTML}{2563eb}
\definecolor{warshgreen}{HTML}{059669}
\definecolor{warnred}{HTML}{ea580c}
\definecolor{violet}{HTML}{7c3aed}
\definecolor{cardbg}{HTML}{f0f9ff}
\definecolor{tealbg}{HTML}{f0fdfa}
\definecolor{goldbg}{HTML}{fffbeb}
\definecolor{redbg}{HTML}{fff7ed}

% ─── HYPERREF ───────────────────────────────────────────────────────────────
\hypersetup{
    colorlinks=true,
    linkcolor=teal,
    urlcolor=emerald,
    citecolor=gold,
    pdftitle={<PROJECT_TITLE>},
    pdfauthor={<AUTHORS>}
}

% ─── SECTION TITLE STYLES ───────────────────────────────────────────────────
\titleformat{\chapter}[block]
  {\normalfont\LARGE\bfseries\color{teal}}
  {\thechapter.}{12pt}{}
  [\vspace{2pt}\color{gold}\rule{\textwidth}{1.5pt}]

\titleformat{\section}
  {\normalfont\large\bfseries\color{teal!80!black}}
  {\thesection}{10pt}{}

\titleformat{\subsection}
  {\normalfont\normalsize\bfseries\color{goldlt}}
  {\thesubsection}{8pt}{}

\titlespacing*{\chapter}{0pt}{0pt}{20pt}

% ─── HEADER / FOOTER ────────────────────────────────────────────────────────
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{slategray}\textit{<SHORT_TITLE>}}
\fancyhead[R]{\small\color{slategray}L3 Computer Science --- <ACADEMIC_YEAR>}
\fancyfoot[C]{\small\color{slategray}\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{teal}\leaders\hrule height \headrulewidth\hfill}}

% ─── TCOLORBOX STYLES ───────────────────────────────────────────────────────
\newtcolorbox{emeraldbox}[1][]{
  enhanced, colback=tealbg, colframe=emerald!70!black,
  fonttitle=\bfseries\color{white}, colbacktitle=emerald!70!black,
  attach boxed title to top left={yshift=-2mm,xshift=6mm},
  boxed title style={sharp corners}, sharp corners, breakable, #1
}

\newtcolorbox{goldbox}[1][]{
  enhanced, colback=goldbg, colframe=gold!80!black,
  fonttitle=\bfseries\color{white}, colbacktitle=gold!80!black,
  attach boxed title to top left={yshift=-2mm,xshift=6mm},
  boxed title style={sharp corners}, sharp corners, breakable, #1
}

\newtcolorbox{warnbox}[1][]{
  enhanced, colback=redbg, colframe=warnred!80!black,
  fonttitle=\bfseries\color{white}, colbacktitle=warnred!80!black,
  attach boxed title to top left={yshift=-2mm,xshift=6mm},
  boxed title style={sharp corners}, sharp corners, breakable, #1
}

\newtcolorbox{infobox}[1][]{
  enhanced, colback=cardbg, colframe=teal!70!black,
  fonttitle=\bfseries\color{white}, colbacktitle=teal!70!black,
  attach boxed title to top left={yshift=-2mm,xshift=6mm},
  boxed title style={sharp corners}, sharp corners, breakable, #1
}

% ─── CUSTOM PHASE BLOCK ────────────────────────────────────────────────────
\newcommand{\phaseblock}[3]{%
  \begin{tcolorbox}[
    enhanced, colback=tealbg, colframe=teal!60!black,
    leftrule=5pt, sharp corners, before upper={\parindent0pt}
  ]
  {\bfseries\color{teal}Phase #1 --- #2}\\[4pt]
  \small #3
  \end{tcolorbox}%
}

% ─── CODE LISTING STYLE ────────────────────────────────────────────────────
\lstset{
  basicstyle=\ttfamily\small,
  backgroundcolor=\color{cardbg},
  frame=single,
  rulecolor=\color{slategray!30},
  breaklines=true,
  numbers=left,
  numberstyle=\tiny\color{slategray},
  tabsize=2
}
```

### Step 2 — Create `main.tex`

Generate the root document file:

```latex
\documentclass[12pt,a4paper]{report}

\input{preamble}

\begin{document}

% ─── COVER PAGE ──────────────────────────────────────────────────────────────
\input{front/cover}

% ─── FRONT MATTER ────────────────────────────────────────────────────────────
\pagenumbering{roman}
\input{front/dedication}
\input{front/acknowledgements}
\input{front/abstract}

\tableofcontents
\listoffigures
\listoftables

% ─── MAIN MATTER ─────────────────────────────────────────────────────────────
\pagenumbering{arabic}
\input{chapters/general_introduction}
\input{chapters/chapter1_state_of_art}
\input{chapters/chapter2_conceptual_study}
\input{chapters/chapter3_implementation}
\input{chapters/general_conclusion}

% ─── BACK MATTER ─────────────────────────────────────────────────────────────
\input{back/bibliography}
\input{back/appendices}

\end{document}
```

### Step 3 — Create Cover Page (`front/cover.tex`)

Use the TikZ-based cover page design from the design system with the following structure:
1. Gold accent line at top, teal accent line at bottom (using `tikzpicture` overlay)
2. University logo placeholder
3. University name, faculty, department, academic year (centered, color-coded)
4. Badge with keywords (TikZ rounded node)
5. Main project title (large, bold, darkbg color) + subtitle (teal)
6. Short description line (slategray)
7. Gold horizontal rule separator
8. Authors table (name, group, program)
9. University location
10. PFE label badge (TikZ rounded node)

Replace all `<PLACEHOLDER>` tokens with the provided inputs.

### Step 4 — Create Front Matter Files

Generate these files in `front/`:

- **`dedication.tex`**: A centered dedication page with the user's dedication text, styled with italic and slategray color.
- **`acknowledgements.tex`**: An acknowledgements chapter (`\chapter*{Acknowledgements}`) with the user's text.
- **`abstract.tex`**: Three abstracts in sequence:
  1. English abstract with keywords
  2. French abstract (Résumé) with keywords
  3. Arabic abstract (ملخص) with keywords — use `\begin{otherlanguage}{arabic}` if `arabxetex` is available, otherwise plain UTF-8

### Step 5 — Create Chapter Stubs

Generate placeholder `.tex` files in `chapters/`:
- `general_introduction.tex` — `\chapter*{General Introduction}`
- `chapter1_state_of_art.tex` — `\chapter{State of the Art}`
- `chapter2_conceptual_study.tex` — `\chapter{Conceptual Study}`
- `chapter3_implementation.tex` — `\chapter{Implementation and Realization}`
- `general_conclusion.tex` — `\chapter*{General Conclusion}`

Each stub should contain:
```latex
\chapter{<Chapter Title>}
% TODO: Generate content using the corresponding skill
```

### Step 6 — Create Back Matter Stubs

- `back/bibliography.tex` — `\chapter*{Bibliography}` with a `\begin{enumerate}` placeholder
- `back/appendices.tex` — `\appendix` with a placeholder appendix chapter

## Constraints

1. **All output must compile** with `pdflatex` without errors
2. **No external image files** are required — use `[Logo Placeholder]` text for images
3. **Color scheme must exactly match** the defined palette (emerald, teal, gold, slategray, etc.)
4. **tcolorbox definitions must be identical** to those in the design system — do not modify them
5. **Front matter pages** use `\pagenumbering{roman}`, main matter uses `\pagenumbering{arabic}`
6. **The abstract MUST include all three languages** (English, French, Arabic) as required by Algerian university standards
7. **Use `\chapter*{}` for unnumbered sections** (General Introduction, General Conclusion, Bibliography, Acknowledgements)
8. **File encoding**: UTF-8 throughout
