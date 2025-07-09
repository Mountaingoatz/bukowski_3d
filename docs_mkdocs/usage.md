# 🚀 Usage Guide

Everything here assumes you have cloned/unzipped **`bukowski_3d`** and are in the
project root.

---

## 1 · Install dependencies (Poetry)

```bash
poetry install           # creates & populates a virtual-env
poetry shell             # optional: drop into that environment

Need OpenAI embeddings?
export OPENAI_API_KEY="sk-YOURKEY" before you run anything.

⸻

2 · Command-Line Interface

Render the plot to bukowski_3d.html and open it in your browser:

poetry run bukowski-3d                 # TF-IDF mode
poetry run bukowski-3d --use-openai    # semantic mode (env key required)


⸻

3 · Streamlit GUI

poetry run streamlit run gui/streamlit_app.py

	•	Local URL appears (default localhost:8501).
	•	Tick the “Use OpenAI embeddings” checkbox to switch modes.

⸻

4 · Gradio UI

poetry run python gui/gradio_app.py

	•	Opens a Gradio interface with the same checkbox and embedded Plotly chart.

⸻

5 · Jupyter Notebook

poetry run jupyter notebook bukowski_3d.ipynb

Run the cells to generate the 3-D plot inline.

⸻

6 · Docker (optional, no Python setup needed)

docker build -t bukowski_3d .
docker run --rm -p 8501:8501 bukowski_3d     # runs CLI by default

Adjust the CMD in Dockerfile if you’d rather start Streamlit.

⸻

7 · Running Tests

poetry run pytest tests/


⸻

8 · Building Docs

Format	Command	Result
Sphinx	poetry run sphinx-build docs_sphinx docs_sphinx/_build	HTML docs in _build/
MkDocs (live)	poetry run mkdocs serve	Browse at localhost:8000


⸻

Troubleshooting Tips
	•	Kernel not found in Notebook? Click Select Kernel → choose the Poetry env.
	•	OpenAI 401 error? Key missing/invalid → echo $OPENAI_API_KEY to confirm.

Happy exploring!

---

