# vieiraphv2.github.io

Paulo Vieira Silva's CV, live at [vieiraphv2.github.io](https://vieiraphv2.github.io/) (English) and [/pt/](https://vieiraphv2.github.io/pt/) (Portuguese).

- `resume.json` is the single source of truth (JSON Resume schema); `resume.pt.json` overlays the Portuguese translations.
- `python3 build.py && python3 build.py pt` renders `index.html`, `pt/index.html`, `cv.md` and `llms.txt`. No dependencies beyond the Python standard library.
- The same build prints the ATS-friendly PDFs (`Paulo-Vieira-Silva-CV.pdf`, `pt/Paulo-Vieira-Silva-Curriculo.pdf`) with headless Chrome; set `CHROME=/path/to/chrome` if it is not found, otherwise the PDF step is skipped.
- Machine-readable versions for AI tools: [cv.md](cv.md), [resume.json](resume.json), [llms.txt](llms.txt).
