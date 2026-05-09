---
name: rapport-technique
description: Generate a standalone technical rapport following the Tahkik server report design patterns — shorter than a full mémoire, focused on technical documentation
inputs:
  - report_title: Title of the technical report
  - report_subtitle: Subtitle or focus area
  - authors: List of author names
  - system_components: List of system components to document (e.g., "Go API Server", "Python Inference Backend")
  - api_endpoints: List of API endpoints with methods, paths, and descriptions
  - environment_variables: List of env vars with defaults and purposes
  - setup_instructions: Installation and setup steps
  - troubleshooting_items: Common issues and their solutions
outputs:
  - A standalone .tex file (single-file report, not multi-file)
---

# Technical Rapport Generator

## Context

This skill generates a standalone technical report following the design patterns from `tahkik_server_report.tex`. Unlike the full mémoire (which is multi-file with chapters), a rapport technique is a **single self-contained `.tex` file** focused on technical documentation.

The rapport is structured for developers and technical reviewers, not academic committees. It documents system architecture, API contracts, setup instructions, and troubleshooting — essentially a comprehensive technical reference.

## Instructions

### Document Structure

Generate a single `.tex` file with this structure:

```latex
\documentclass[12pt,a4paper]{report}

% ═══ Full preamble (identical to mémoire) ═══
% Include all packages, colors, tcolorbox definitions, etc.
% (Copy from the latex-scaffold skill's preamble section)

\begin{document}

% ─── COVER PAGE ──────────────────────────────────────────────────────────────
\begin{titlepage}
% Same TikZ cover design as the mémoire but with "Technical Report" label
\end{titlepage}

% ─── TABLE OF CONTENTS ──────────────────────────────────────────────────────
\tableofcontents
\newpage

% ─── CHAPTER 1: INTRODUCTION ────────────────────────────────────────────────
\chapter{Introduction}
% Project overview, system purpose, report scope

% ─── CHAPTER 2: SYSTEM ARCHITECTURE ─────────────────────────────────────────
\chapter{System Architecture}
% Component diagrams, data flow, technology choices

% ─── CHAPTER 3: COMPONENT DETAILS ───────────────────────────────────────────
\chapter{Component Details}
% Detailed documentation for each system component

% ─── CHAPTER 4: DATA PIPELINE ───────────────────────────────────────────────
\chapter{Data Pipeline}
% Data flow, processing stages, file formats

% ─── CHAPTER 5: SETUP & DEPLOYMENT ──────────────────────────────────────────
\chapter{Setup and Deployment}
% Installation, configuration, environment variables

% ─── CHAPTER 6: API REFERENCE ───────────────────────────────────────────────
\chapter{API Reference}
% Endpoint documentation with request/response examples

% ─── CHAPTER 7: TROUBLESHOOTING ─────────────────────────────────────────────
\chapter{Troubleshooting}
% Common issues and solutions

% ─── CONCLUSION ─────────────────────────────────────────────────────────────
\chapter{Conclusion}
% Summary, key features, future enhancements

% ─── REFERENCES ─────────────────────────────────────────────────────────────
\chapter{References}
% Numbered reference list

\end{document}
```

### Architecture Chapter Pattern

Use TikZ flow diagrams to show system architecture:

```latex
\section{System Overview}

\begin{figure}[H]
\centering
\begin{tikzpicture}[
  component/.style={
    draw=teal!60!black, rounded corners=8pt, minimum width=3.5cm,
    minimum height=1.8cm, fill=tealbg, font=\small\bfseries,
    text=teal!80!black, align=center
  },
  arrow/.style={-latex, thick, teal!60!black},
  label/.style={font=\scriptsize, color=slategray}
]

\node[component] (client) at (0, 0) {Mobile Client\\(Flutter)};
\node[component] (api) at (5.5, 0) {API Server\\(Go)};
\node[component] (ml) at (11, 0) {Inference\\(Python/Whisper)};
\node[component] (db) at (5.5, -3.5) {Database\\(PostgreSQL)};
\node[component] (hf) at (11, -3.5) {HF Spaces\\(Production)};

\draw[arrow] (client) -- node[label, above] {REST API} (api);
\draw[arrow] (api) -- node[label, above] {HTTP Proxy} (ml);
\draw[arrow] (api) -- node[label, right] {SQL} (db);
\draw[arrow] (api.south east) -- node[label, right, pos=0.3] {Fallback} (hf.north west);

\end{tikzpicture}
\caption{High-level system architecture}
\label{fig:architecture_overview}
\end{figure}
```

### Component Detail Pattern

For each system component, use this structure:

```latex
\section{<Component Name>}
\label{sec:<component_slug>}

\subsection{Overview}
<Brief description of the component's purpose and responsibilities>

\subsection{Technology}
\begin{infobox}[title=Technology Stack]
\begin{itemize}
  \item \textbf{Language}: <Language> <Version>
  \item \textbf{Framework}: <Framework> <Version>
  \item \textbf{Key Libraries}: <lib1>, <lib2>, <lib3>
\end{itemize}
\end{infobox}

\subsection{Key Implementation Details}
<Technical details, algorithms, design decisions>

\begin{lstlisting}[language=Go, caption={<Code description>}]
// Example code snippet
func handleRequest(w http.ResponseWriter, r *http.Request) {
    // Implementation details
}
\end{lstlisting}
```

### API Reference Pattern

Document each endpoint thoroughly:

```latex
\section{<Endpoint Group>}

\subsection{<METHOD> <path>}

<Brief description>

\begin{infobox}[title=Request Format]
Content-Type: \texttt{multipart/form-data}

Field: \texttt{audio} (file)

Supported formats: \texttt{.wav}, \texttt{.mp3}, \texttt{.m4a}, \texttt{.flac}, \texttt{.ogg}

Max size: 50 MB
\end{infobox}

\begin{emeraldbox}[title=Success Response (200 OK)]
\begin{verbatim}
{
  "status": "success",
  "data": {
    "transcription": "[Arabic transcription]",
    "confidence_score": 0.9423,
    "processing_time_ms": 1350
  }
}
\end{verbatim}
\end{emeraldbox}

\begin{warnbox}[title=Error Response (4xx/5xx)]
\begin{verbatim}
{
  "status": "error",
  "message": "unsupported audio format: .xyz"
}
\end{verbatim}
\end{warnbox}
```

### Environment Variables Table

```latex
\section{Environment Variables}

\begin{table}[H]
  \centering
  \caption{Configuration environment variables}
  \label{tab:env}
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{lll}
    \toprule
    \textbf{Variable} & \textbf{Default} & \textbf{Purpose} \\
    \midrule
    \texttt{INFERENCE\_SERVER\_URL} & \texttt{http://localhost:8081} & Backend URL \\
    \texttt{PORT} & \texttt{8080} & Server port \\
    \bottomrule
  \end{tabular}
\end{table}
```

### Troubleshooting Pattern

Use `phaseblock` for diagnosis and resolution:

```latex
\subsection{<Issue Name>}

\phaseblock[title=Diagnosis]{<Context for when this issue occurs>}

\begin{itemize}
  \item Step 1 to diagnose
  \item Step 2 to diagnose
\end{itemize}

\phaseblock[title=Resolution]{<How to fix}

\begin{verbatim}
<Fix command or configuration>
\end{verbatim}
```

### Conclusion Pattern

```latex
\chapter{Conclusion}

\section{Summary}
<Recap of what the report documented>

\section{Key Features}
\begin{emeraldbox}[title=System Capabilities]
\begin{itemize}
  \item Feature 1
  \item Feature 2
\end{itemize}
\end{emeraldbox}

\section{Future Enhancements}
\begin{goldbox}[title=Planned Extensions]
\begin{itemize}
  \item Enhancement 1
  \item Enhancement 2
\end{itemize}
\end{goldbox}

\begin{emeraldbox}[title=Closing Statement]
\begin{center}
\large\itshape
``<Quote>''\\[6pt]
\normalsize\normalfont\color{slategray} --- <Attribution>
\end{center}
\vspace{6pt}
\normalsize
<Closing paragraph>
\end{emeraldbox}
```

## Constraints

1. **Single file format** — the entire report is one `.tex` file (not multi-file like the mémoire)
2. **Same design system** — uses identical colors, tcolorbox styles, and formatting as the mémoire
3. **API documentation must use the box semantics**: `infobox` for requests, `emeraldbox` for success responses, `warnbox` for error responses
4. **`phaseblock`** is used for troubleshooting steps (diagnosis → resolution pattern)
5. **Code listings must use `verbatim` or `lstlisting`** — never raw monospace text
6. **Environment variables table** must include Variable, Default, and Purpose columns
7. **The cover page label** should say "Technical Report" instead of "Mémoire de Licence"
8. **For Tahkik specifically**: Document the Go API server, Python inference backend, HF Space deployment, and audio processing pipeline
