---
name: implementation
description: Generate Chapter 3 (Implementation and Realization) for the Tahkik PFE mémoire — development environment, technology stack, code listings, screenshots, testing, and deployment
inputs:
  - dev_environment: IDE and OS details (e.g., "VS Code on Ubuntu 22.04")
  - languages: List of programming languages used with versions
  - frameworks: List of frameworks/libraries with versions and descriptions
  - databases: Database systems used with versions
  - modeling_tools: Tools used for UML/design (e.g., "StarUML", "TikZ")
  - project_directories: Key directories in the project codebase to reference
  - key_screens: List of application screens/interfaces to showcase
  - testing_tools: Testing frameworks and methodologies used
  - deployment_target: Deployment platform details (e.g., "Hugging Face Spaces", "AWS", "Local server")
  - security_measures: Security implementations (e.g., "JWT", "bcrypt", "HTTPS")
outputs:
  - chapters/chapter3_implementation.tex
---

# Implementation Chapter Generator

## Context

This skill generates Chapter 3 of the PFE mémoire, documenting the practical technical execution of the project. Based on L3 PFE standards from Yahia Fares University, this chapter covers the development environment, technology stack, database implementation, application presentation (with labeled screenshots), security measures, and testing.

This is the most code-heavy and screenshot-heavy chapter. It should demonstrate that the student has practical knowledge of the tools and can produce working software.

## Instructions

### Section 1 — Introduction

```latex
\chapter{Implementation and Realization}
\label{ch:implementation}

\section{Introduction}

This chapter details the practical implementation of the system designed in the previous chapter. We begin by presenting the development environment and tools, then describe the technology stack, database implementation, and the key interfaces of the application. The chapter concludes with security measures and testing methodology.
```

### Section 2 — Development Environment

Present each tool with a brief description:

```latex
\section{Development Environment}
\label{sec:impl_devenv}

\subsection{Integrated Development Environment}

\begin{infobox}[title=Visual Studio Code]
Visual Studio Code is a lightweight, extensible source-code editor developed by Microsoft. It supports debugging, syntax highlighting, intelligent code completion, and integrated version control with Git. It is available for Windows, macOS, and Linux.
\end{infobox}

\subsection{Version Control}

\begin{infobox}[title=Git \& GitHub]
Git is a distributed version control system for tracking changes in source code. GitHub provides cloud-based hosting for Git repositories with collaboration features including pull requests, issues, and CI/CD pipelines.
\end{infobox}

\subsection{Modeling Tools}

<Describe StarUML, TikZ, or other tools used for UML diagrams>
```

### Section 3 — Technology Stack

Present languages, frameworks, and databases in a structured format:

```latex
\section{Technology Stack}
\label{sec:impl_techstack}

\subsection{Programming Languages}

\begin{table}[H]
  \centering
  \caption{Programming languages used}
  \label{tab:impl_languages}
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{llp{8cm}}
    \toprule
    \textbf{Language} & \textbf{Version} & \textbf{Purpose} \\
    \midrule
    Python & 3.11 & Machine learning, model training, inference server \\
    Go & 1.22 & API proxy server, request handling \\
    Dart & 3.x & Mobile application (Flutter framework) \\
    \bottomrule
  \end{tabular}
\end{table}

\subsection{Frameworks and Libraries}

\begin{table}[H]
  \centering
  \caption{Frameworks and libraries used}
  \label{tab:impl_frameworks}
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{llp{8cm}}
    \toprule
    \textbf{Framework} & \textbf{Version} & \textbf{Purpose} \\
    \midrule
    PyTorch & 2.x & Deep learning model training \\
    Transformers & 4.x & Whisper model fine-tuning \\
    Flutter & 3.x & Cross-platform mobile application \\
    Gin/Echo & latest & Go HTTP server framework \\
    \bottomrule
  \end{tabular}
\end{table}
```

For each major technology, include a brief description paragraph followed by the table.

### Section 4 — Database Implementation

```latex
\section{Database Implementation}
\label{sec:impl_database}

\subsection{Database System}

\begin{infobox}[title=<Database Name>]
<Description of the database system and why it was chosen>
\end{infobox}

\subsection{Database Structure}

<Show the actual table structures. Use either:>
- A screenshot placeholder for phpMyAdmin/pgAdmin views
- Or a code listing showing the schema:

\begin{lstlisting}[language=SQL, caption={Database schema}, label={lst:impl_schema}]
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
\end{lstlisting}
```

### Section 5 — Application Presentation

This is the core of the chapter — showcase the application with labeled screenshots:

```latex
\section{Application Presentation}
\label{sec:impl_presentation}

In this section, we present the main interfaces of our application through screenshots and descriptions.

\subsection{<Screen Name> Interface}

<Description of what this screen does and how the user interacts with it>

\begin{figure}[H]
  \centering
  % \includegraphics[width=0.85\textwidth]{figures/impl_<screen_slug>.png}
  \fbox{\parbox{0.75\textwidth}{\centering\vspace{3cm}
    \textit{Screenshot: <Screen Description>}\vspace{3cm}}}
  \caption{<Screen Name> interface}
  \label{fig:impl_<screen_slug>}
\end{figure}

<Explanation of the key UI elements visible in the screenshot>
```

For each key screen, follow the pattern: description → screenshot → explanation.

**Use `phaseblock` for multi-step workflows:**

```latex
\phaseblock{1}{User Registration}{
  The user fills in the registration form with their name, email, and password.
  The system validates the input and creates a new account.
}

\phaseblock{2}{Audio Upload}{
  The authenticated user selects an audio file from their device.
  The system validates the format and size before processing.
}
```

### Section 6 — Security

```latex
\section{Security Measures}
\label{sec:impl_security}

\begin{emeraldbox}[title=Security Implementation]
\begin{itemize}
  \item \textbf{Authentication}: <JWT/Session-based/OAuth>
  \item \textbf{Password Hashing}: <bcrypt/argon2>
  \item \textbf{Data Encryption}: <HTTPS/TLS>
  \item \textbf{Input Validation}: <Sanitization approach>
  \item \textbf{Access Control}: <Role-based/Attribute-based>
\end{itemize}
\end{emeraldbox}
```

### Section 7 — Testing

```latex
\section{Testing}
\label{sec:impl_testing}

\subsection{Testing Methodology}

<Describe the testing approach: unit tests, integration tests, manual testing>

\begin{table}[H]
  \centering
  \caption{Test summary}
  \label{tab:impl_tests}
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{llcc}
    \toprule
    \textbf{Test Type} & \textbf{Tool} & \textbf{Tests} & \textbf{Pass Rate} \\
    \midrule
    Unit Tests & Jest/pytest & 45 & 100\% \\
    API Tests & Postman & 12 & 100\% \\
    \bottomrule
  \end{tabular}
\end{table}
```

### Section 8 — Deployment

```latex
\section{Deployment}
\label{sec:impl_deployment}

\begin{figure}[H]
\centering
\begin{tikzpicture}[
  server/.style={
    draw=teal!60!black, rounded corners, minimum width=3cm,
    minimum height=1.5cm, fill=tealbg, font=\small\bfseries,
    text=teal!80!black
  },
  arrow/.style={-latex, thick, teal!60!black},
  label/.style={font=\scriptsize, color=slategray}
]
% Deployment architecture diagram
\node[server] (dev) at (0, 0) {Developer\\Machine};
\node[server] (ci) at (5, 0) {CI/CD\\Pipeline};
\node[server] (prod) at (10, 0) {Production\\Server};

\draw[arrow] (dev) -- node[label, above] {git push} (ci);
\draw[arrow] (ci) -- node[label, above] {deploy} (prod);
\end{tikzpicture}
\caption{Deployment pipeline}
\label{fig:impl_deployment}
\end{figure}
```

### Section 9 — Conclusion

```latex
\section{Conclusion}

This chapter presented the complete implementation of the system, from development environment setup through technology selection, database design, and application interface development. The security measures and testing methodology ensure the reliability and safety of the deployed application. The results demonstrate a functional system that meets the requirements defined in the conceptual study.
```

## Constraints

1. **Technology descriptions must be factual** — include actual version numbers and accurate descriptions
2. **Screenshots use placeholder boxes** — never reference non-existent image files
3. **Code listings** must use `lstlisting` environment with proper `language` and `caption` parameters
4. **Minimum content**: 5+ technology descriptions, 5+ application screenshots, security section, testing section
5. **Use `phaseblock`** for documenting multi-step processes and workflows
6. **Tables must use `booktabs`** (`\toprule`, `\midrule`, `\bottomrule`) — never `\hline`
7. **For Tahkik specifically**: Reference Python/PyTorch/Transformers for ML, Go for API, Flutter for mobile, Hugging Face for deployment
8. **Scan the actual project directories** to extract real file names, folder structures, and code snippets when generating content
