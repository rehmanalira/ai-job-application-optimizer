def build_latex_resume(data, ai_content):

    latex = rf"""
\documentclass[10.5pt,a4paper]{{article}}

\usepackage[left=1.25cm, right=1.25cm, top=1.2cm, bottom=1.2cm]{{geometry}}
\usepackage{{enumitem}}
\usepackage[hidelinks]{{hyperref}}
\usepackage{{titlesec}}
\usepackage{{setspace}}

\pagenumbering{{gobble}}
\setstretch{{1.0}}

\titleformat{{\section}}
  {{\normalsize\bfseries}}
  {{}}
  {{0pt}}
  {{}}
  [\titlerule]

\begin{{document}}

\begin{{center}}
    {{\Large \textbf{{{data.name.upper()}}}}}\\
    Full Stack Developer\\
    {data.location} \;|\;
    \href{{mailto:{data.email}}}{{{data.email}}} \;|\;
    {data.phone}
\end{{center}}

\vspace{{-6pt}}

{ai_content}

\end{{document}}
"""

    return latex