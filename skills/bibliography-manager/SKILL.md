---
name: bibliography-manager
description: Generate and manage BibTeX bibliography entries for the Tahkik PFE mémoire — supports articles, books, websites, theses, and conference papers
inputs:
  - references: List of references with type, title, authors, year, and URL/DOI
  - citation_style: Citation style to use (default "IEEE numeric" — [1], [2], etc.)
outputs:
  - references.bib (BibTeX database file)
  - back/bibliography.tex (formatted bibliography chapter)
---

# Bibliography Manager

## Context

This skill manages the bibliography for the PFE mémoire. Algerian L3 PFE theses typically use a **numbered bibliography** ([1], [2], etc.) following IEEE or similar numeric style. The bibliography is split between:

1. **Bibliography** — published books, journal articles, conference papers, theses
2. **Webography** — online resources, documentation, tools

This skill can generate BibTeX entries from URLs/titles, format them correctly, and produce the bibliography chapter.

## Instructions

### Option A — Generate BibTeX File

When given a list of references, generate a `.bib` file:

```bibtex
% ═══════════════════════════════════════════════════════════════════════════
%  BIBLIOGRAPHY DATABASE — Tahkik PFE Mémoire
% ═══════════════════════════════════════════════════════════════════════════

% ─── JOURNAL ARTICLES ──────────────────────────────────────────────────────
@article{radford2023whisper,
  author    = {Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and McLeavey, Christine and Sutskever, Ilya},
  title     = {Robust Speech Recognition via Large-Scale Weak Supervision},
  journal   = {Proceedings of the 40th International Conference on Machine Learning},
  pages     = {28492--28518},
  year      = {2023}
}

% ─── CONFERENCE PAPERS ─────────────────────────────────────────────────────
@inproceedings{wolf2020transformers,
  author    = {Wolf, Thomas and Debut, Lysandre and Sanh, Victor and others},
  title     = {Transformers: State-of-the-Art Natural Language Processing},
  booktitle = {Proceedings of EMNLP 2020: System Demonstrations},
  pages     = {38--45},
  year      = {2020}
}

% ─── BOOKS ─────────────────────────────────────────────────────────────────
@book{goodfellow2016deep,
  author    = {Goodfellow, Ian and Bengio, Yoshua and Courville, Aaron},
  title     = {Deep Learning},
  publisher = {MIT Press},
  year      = {2016}
}

% ─── THESES / MÉMOIRES ────────────────────────────────────────────────────
@mastersthesis{student2024project,
  author  = {<Student Name>},
  title   = {<Thesis Title>},
  school  = {Yahia Fares University of Medea},
  year    = {2024},
  type    = {Licence Thesis}
}

% ─── ONLINE RESOURCES (WEBOGRAPHY) ────────────────────────────────────────
@misc{huggingface2024,
  author       = {{Hugging Face}},
  title        = {Hugging Face Model Hub},
  howpublished = {\url{https://huggingface.co}},
  year         = {2024},
  note         = {Accessed: 2025-04-15}
}

@misc{vscode2024,
  author       = {{Microsoft}},
  title        = {Visual Studio Code},
  howpublished = {\url{https://code.visualstudio.com}},
  year         = {2024},
  note         = {Accessed: 2025-04-15}
}
```

### BibTeX Entry Templates

Use these templates for each reference type:

**Journal Article:**
```bibtex
@article{<key>,
  author  = {<Last, First and Last, First>},
  title   = {<Title>},
  journal = {<Journal Name>},
  volume  = {<Vol>},
  number  = {<No>},
  pages   = {<Start--End>},
  year    = {<Year>},
  doi     = {<DOI>}
}
```

**Conference Paper:**
```bibtex
@inproceedings{<key>,
  author    = {<Last, First and Last, First>},
  title     = {<Title>},
  booktitle = {<Conference Name>},
  pages     = {<Start--End>},
  year      = {<Year>}
}
```

**Book:**
```bibtex
@book{<key>,
  author    = {<Last, First>},
  title     = {<Title>},
  publisher = {<Publisher>},
  year      = {<Year>},
  edition   = {<Edition>}
}
```

**Website/Online Resource:**
```bibtex
@misc{<key>,
  author       = {<Author or {Organization}>},
  title        = {<Page/Resource Title>},
  howpublished = {\url{<URL>}},
  year         = {<Year>},
  note         = {Accessed: <YYYY-MM-DD>}
}
```

**Thesis:**
```bibtex
@mastersthesis{<key>,
  author = {<Last, First>},
  title  = {<Title>},
  school = {<University>},
  year   = {<Year>},
  type   = {<Licence Thesis | Master Thesis | PhD Thesis>}
}
```

### Option B — Generate Manual Bibliography Chapter

If BibTeX compilation is not available, generate a manual bibliography:

```latex
\chapter*{Bibliography}
\addcontentsline{toc}{chapter}{Bibliography}

\section*{References}

\begin{enumerate}
  \item Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., \& Sutskever, I. (2023). Robust speech recognition via large-scale weak supervision. In \textit{Proceedings of the 40th International Conference on Machine Learning} (pp. 28492--28518).

  \item Wolf, T., Debut, L., Sanh, V., et al. (2020). Transformers: State-of-the-art natural language processing. In \textit{Proceedings of EMNLP 2020: System Demonstrations} (pp. 38--45).

  \item Goodfellow, I., Bengio, Y., \& Courville, A. (2016). \textit{Deep Learning}. MIT Press.
\end{enumerate}

\section*{Webography}

\begin{enumerate}
  \item Hugging Face. (2024). Hugging Face Model Hub. Available at: \url{https://huggingface.co} (Accessed: April 15, 2025).

  \item Microsoft. (2024). Visual Studio Code. Available at: \url{https://code.visualstudio.com} (Accessed: April 15, 2025).
\end{enumerate}
```

### Citation Usage in Text

When citing in the document body:

**Numeric style (default for Algerian PFE):**
```latex
% In text:
As demonstrated by Radford et al. [1], large-scale weak supervision...

% Or parenthetical:
...robust speech recognition has been achieved [1].
```

**If using BibTeX:**
```latex
% Requires \usepackage{cite} or natbib
\cite{radford2023whisper}          % → [1]
\cite{radford2023whisper,wolf2020transformers}  % → [1, 2]
```

### Key Naming Convention

BibTeX keys follow: `<firstauthorlast><year><firstwordoftitle>`
- `radford2023whisper`
- `wolf2020transformers`
- `goodfellow2016deep`

## Constraints

1. **Numbered citation style** `[1]`, `[2]` — this is the standard for Algerian L3 PFEs
2. **Separate Bibliography and Webography** sections — books/papers vs. online resources
3. **All URLs must use `\url{}`** for proper formatting and line-breaking
4. **Include access dates** for all online resources
5. **Author format**: `Last, First and Last, First` — use `and` between authors, not `&`
6. **Use `{Organization}` with braces** for corporate authors to prevent BibTeX from splitting the name
7. **Minimum 10 references** for a complete PFE mémoire bibliography
8. **For Tahkik specifically**: Must include Whisper paper, Transformers paper, Hugging Face, and Tahkik model hub entry
