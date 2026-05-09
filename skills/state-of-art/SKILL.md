---
name: state-of-art
description: Generate Chapter 1 (State of the Art) for the Tahkik PFE mémoire — domain overview, existing solutions, comparative analysis, and problem statement
inputs:
  - project_domain: The domain of the project (e.g., "Quranic ASR", "Web Development", "Mobile App")
  - project_description: Brief description of what the project does
  - existing_solutions: List of existing tools/systems to analyze and compare
  - problem_statement: The core problem the project addresses
  - host_organization: (Optional) Organization where the internship/project is hosted
outputs:
  - chapters/chapter1_state_of_art.tex
---

# State of the Art Chapter Generator

## Context

This skill generates Chapter 1 of the PFE mémoire, which provides the theoretical foundation and contextual background for the project. Based on analysis of L3 PFE examples from Yahia Fares University, this chapter typically covers:

1. **Domain presentation** — definitions, history, and key concepts
2. **Organizational context** — presentation of the host organization (if applicable)
3. **Existing solutions analysis** — review and critique of current systems
4. **Comparative study** — side-by-side comparison table
5. **Problem statement and motivation** — justification for the proposed solution

## Instructions

### Section 1 — Introduction

Write 2-3 paragraphs introducing the chapter's purpose. State what will be covered: domain overview, existing solution analysis, and identification of the gap this project fills.

```latex
\chapter{State of the Art}
\label{ch:state_of_art}

\section{Introduction}

<Introduction text explaining the chapter scope and structure>
```

### Section 2 — Domain Presentation

Provide a thorough overview of the project's domain:

```latex
\section{Domain Overview}
\label{sec:soa_domain}

\subsection{Definition and Context}
<Define the domain. For Tahkik: ASR, Quranic recitation, Warsh riwaya>

\subsection{Historical Background}
<Brief history of the domain and its evolution>

\subsection{Key Concepts}
<Define technical terms the reader needs to understand>
```

Use `emeraldbox` for key definitions:
```latex
\begin{emeraldbox}[title=Automatic Speech Recognition (ASR)]
ASR is the computational task of converting spoken language into written text...
\end{emeraldbox}
```

### Section 3 — Organizational Context (Optional)

If a host organization is involved, include:

```latex
\section{Organizational Context}
\label{sec:soa_org}

\subsection{Organization Presentation}
<Name, mission, structure>

\subsection{Organization Chart}
<TikZ organigram or description>
```

For TikZ organigrams:
```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  every node/.style={draw, rounded corners, minimum width=3cm, minimum height=0.8cm,
    text centered, font=\small},
  level 1/.style={sibling distance=4cm, level distance=2cm},
  level 2/.style={sibling distance=3cm, level distance=1.5cm},
  edge from parent/.style={draw, -latex}
]
\node[fill=teal!20] {Director General}
  child { node[fill=emerald!15] {Department A} }
  child { node[fill=emerald!15] {Department B} }
  child { node[fill=emerald!15] {Department C} };
\end{tikzpicture}
\caption{Organization chart}
\label{fig:soa_orgchart}
\end{figure>
```

### Section 4 — Existing Solutions Analysis

Review 3-5 existing solutions/tools. For each:

```latex
\section{Existing Solutions}
\label{sec:soa_existing}

\subsection{<Solution Name>}
<Description, features, technology stack>

\begin{infobox}[title=Key Features of <Solution>]
\begin{itemize}
  \item Feature 1
  \item Feature 2
  \item Feature 3
\end{itemize}
\end{infobox}

<Strengths and weaknesses analysis>
```

### Section 5 — Comparative Study

Create a comparison table:

```latex
\section{Comparative Analysis}
\label{sec:soa_comparison}

\begin{table}[H]
  \centering
  \caption{Comparison of existing solutions}
  \label{tab:soa_comparison}
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{l*{4}{c}}
    \toprule
    \textbf{Criteria} & \textbf{Solution A} & \textbf{Solution B} & \textbf{Solution C} & \textbf{Our Solution} \\
    \midrule
    Open Source       & \checkmark & $\times$ & \checkmark & \checkmark \\
    Feature X         & \checkmark & \checkmark & $\times$ & \checkmark \\
    Feature Y         & $\times$ & \checkmark & \checkmark & \checkmark \\
    \bottomrule
  \end{tabular}
\end{table}
```

### Section 6 — Problem Statement

State the problem clearly and justify the proposed solution:

```latex
\section{Problem Statement}
\label{sec:soa_problem}

<Describe the gap in existing solutions>

\begin{warnbox}[title=Identified Limitations]
\begin{itemize}
  \item Limitation 1 of existing solutions
  \item Limitation 2
  \item Limitation 3
\end{itemize}
\end{warnbox}

\section{Proposed Solution}
\label{sec:soa_solution}

<Describe how this project addresses the identified limitations>

\begin{emeraldbox}[title=Project Objectives]
\begin{enumerate}
  \item Objective 1
  \item Objective 2
  \item Objective 3
\end{enumerate}
\end{emeraldbox}
```

### Section 7 — Conclusion

```latex
\section{Conclusion}

In this chapter, we presented <domain overview>, analyzed <existing solutions>, and identified <key limitations>. These findings motivate the design of our solution, which will be detailed in the conceptual study presented in Chapter~\ref{ch:conceptual}.
```

## Constraints

1. **Minimum 3 existing solutions** must be analyzed in the comparative section
2. **The comparison table must include "Our Solution"** as the final column to show advantages
3. **Use `\checkmark` and `$\times$`** for boolean comparison cells
4. **emeraldbox** for definitions and objectives, **warnbox** for limitations, **infobox** for feature lists
5. **Each solution review** should be 150-300 words with specific technical details
6. **Academic citations** should use `[number]` format (e.g., `[1]`, `[2]`) matching the bibliography
7. **For Tahkik specifically**: Compare against Tarteel AI, Standard Whisper, Google Speech-to-Text, and relevant Quranic ASR tools
