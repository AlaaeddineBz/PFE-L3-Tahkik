---
name: general-intro-conclusion
description: Generate the General Introduction and General Conclusion sections for the Tahkik PFE mémoire
inputs:
  - project_title: Full project title
  - domain: The domain (e.g., "Quranic ASR", "Web Development")
  - problem: The core problem being solved
  - objectives: List of project objectives
  - methodology: The approach/methodology used
  - chapter_summaries: Brief summary of each chapter's content (for document organization section)
  - contributions: List of key project contributions/achievements
  - limitations: Known limitations of the current implementation
  - future_work: Planned extensions and improvements
outputs:
  - chapters/general_introduction.tex
  - chapters/general_conclusion.tex
---

# General Introduction & Conclusion Generator

## Context

This skill generates the two bookend sections of the PFE mémoire — the General Introduction and General Conclusion. These are unnumbered chapters (`\chapter*{}`) that frame the entire document. Based on L3 PFE standards from Yahia Fares University:

- **General Introduction** presents: context → problematic → objectives → methodology → document organization
- **General Conclusion** presents: summary of work → contributions → limitations → future perspectives

Both sections must be written in a formal academic tone and should be 1-2 pages each.

## Instructions

### Part 1 — General Introduction

Generate `chapters/general_introduction.tex`:

```latex
% ════════════════════════════════════════════════════════════════════════════
%  GENERAL INTRODUCTION
% ════════════════════════════════════════════════════════════════════════════
\chapter*{General Introduction}
\addcontentsline{toc}{chapter}{General Introduction}
\label{ch:general_intro}

% ── Context (1-2 paragraphs) ──
% Introduce the broad domain. Start wide, then narrow down to the specific area.
% Example for Tahkik: Start with AI/ML in speech recognition → narrow to Arabic ASR
% → narrow further to Quranic recitation → arrive at Warsh specifically.

<Context paragraphs>

% ── Problematic (1 paragraph) ──
% State the problem clearly. What gap exists? What doesn't work well?
% Use a warnbox for emphasis:

\begin{warnbox}[title=Problem Statement]
<Concise problem statement in 3-5 sentences>
\end{warnbox}

% ── Objectives (1 paragraph + enumeration) ──
% List the specific, measurable objectives of this project.

The main objectives of this project are:
\begin{enumerate}
  \item <Objective 1>
  \item <Objective 2>
  \item <Objective 3>
  \item <Objective 4>
\end{enumerate}

% ── Methodology (1 paragraph) ──
% Briefly describe the approach taken to achieve these objectives.

<Methodology paragraph>

% ── Document Organization (1 paragraph) ──
% Preview each chapter's content.

This document is organized as follows:

\begin{itemize}
  \item \textbf{Chapter~\ref{ch:state_of_art} --- State of the Art}: <Brief summary of Chapter 1>
  \item \textbf{Chapter~\ref{ch:conceptual} --- Conceptual Study}: <Brief summary of Chapter 2>
  \item \textbf{Chapter~\ref{ch:implementation} --- Implementation}: <Brief summary of Chapter 3>
\end{itemize}
```

### Part 2 — General Conclusion

Generate `chapters/general_conclusion.tex`:

```latex
% ════════════════════════════════════════════════════════════════════════════
%  GENERAL CONCLUSION
% ════════════════════════════════════════════════════════════════════════════
\chapter*{General Conclusion}
\addcontentsline{toc}{chapter}{General Conclusion}
\label{ch:general_conclusion}

% ── Summary of Work (2-3 paragraphs) ──
% Recap what was done in each chapter, emphasizing the logical progression.

<Summary paragraphs — reference each chapter's contributions>

% ── Key Contributions (emeraldbox) ──

\begin{emeraldbox}[title=Key Contributions]
\begin{enumerate}
  \item <Contribution 1>
  \item <Contribution 2>
  \item <Contribution 3>
  \item <Contribution 4>
\end{enumerate}
\end{emeraldbox}

% ── Limitations (1 paragraph) ──

Despite these achievements, certain limitations remain:
\begin{itemize}
  \item <Limitation 1>
  \item <Limitation 2>
  \item <Limitation 3>
\end{itemize}

% ── Future Perspectives (goldbox) ──

\begin{goldbox}[title=Future Perspectives]
\begin{itemize}
  \item <Future work item 1>
  \item <Future work item 2>
  \item <Future work item 3>
  \item <Future work item 4>
\end{itemize}
\end{goldbox}

% ── Closing Statement (emeraldbox) ──

\begin{emeraldbox}[title=Closing Statement]
\begin{center}
\large\itshape
``<Inspirational or relevant quote>''\\[6pt]
\normalsize\normalfont\color{slategray} --- <Attribution>
\end{center}
\vspace{6pt}
\normalsize
<Final 2-3 sentence closing statement about the project's impact and significance>
\end{emeraldbox}
```

## Writing Guidelines

### General Introduction Structure
1. **Context** (wide → narrow funnel approach):
   - Sentence 1: Broad domain statement
   - Sentences 2-3: Narrow to specific sub-domain
   - Sentences 4-5: Arrive at the exact problem area
2. **Problematic**: Must clearly state what is missing/broken/inadequate
3. **Objectives**: Must be specific and measurable (avoid vague goals)
4. **Methodology**: Brief, 3-5 sentences on the approach
5. **Document Organization**: One sentence per chapter, using `\ref{}` for cross-references

### General Conclusion Structure
1. **Summary**: Mirror the document organization but in past tense ("In Chapter 1, we presented...")
2. **Contributions**: Concrete, tangible results (not aspirations)
3. **Limitations**: Honest assessment — reviewers respect candor
4. **Future Work**: Realistic extensions, not fantasy features
5. **Closing Statement**: A meaningful quote related to the domain, followed by a brief impact statement

## Constraints

1. **Use `\chapter*{}`** for both sections (unnumbered) with `\addcontentsline` to appear in TOC
2. **General Introduction should be 400-600 words** (approximately 1-1.5 pages)
3. **General Conclusion should be 400-600 words** (approximately 1-1.5 pages)
4. **Cross-reference all chapters** using `\ref{ch:...}` in the document organization section
5. **The closing statement** must use an `emeraldbox` with an italicized quote — this is a design system convention from the Tahkik templates
6. **Tone**: Formal academic English, third-person or first-person plural ("we")
7. **The problematic in the introduction must use a `warnbox`** for visual emphasis
8. **Contributions use `emeraldbox`**, future work uses `goldbox`** — follow the box semantics
