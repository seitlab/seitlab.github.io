# Physical AI Survey — Companion Website

Static companion site for the survey **"Physical AI: A Comprehensive Survey of
Enabling Technologies From a Systems Perspective."**

## Local preview

```bash
python -m http.server 8000
# then open http://127.0.0.1:8000
```

No build step is required — `index.html`, `styles.css`, and `script.js` are
served directly.

## Structure

```
.
├── index.html              # all sections of the survey as a single page
├── styles.css              # warm parchment theme, serif headlines, card grids
├── script.js               # active-section nav highlighting
└── assets/figures/         # SVG figures from the paper
```

## Deployment

The site is deployed via **GitHub Pages** from the `main` branch (root).
The `.nojekyll` file disables Jekyll processing so any future filenames
beginning with an underscore are served unchanged.
