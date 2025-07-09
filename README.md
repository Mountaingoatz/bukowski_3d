# 📚 Bukowski 3D

> Visualise Charles Bukowski’s key works in an interactive 3-D space  
> - built with Python + Plotly, shipped with CLI, Streamlit, Gradio, Jupyter,
> and auto-generated docs (Sphinx / MkDocs).

---

## ✨ Features

| Pillar | What you get |
|--------|--------------|
| **Vectorisation** | TF-IDF by default, optional OpenAI embeddings |
| **3-D Projection** | PCA → Plotly 3-D scatter with hover labels |
| **Multiple UIs** | CLI, Streamlit dashboard, Gradio demo, Notebook |
| **Docs** | Sphinx & MkDocs sites, ready for GitHub Pages |
| **Packaging** | Poetry project, Dockerfile, pytest suite |

---

## 🚀 Quick Start

### 0. Clone & install

```bash
git clone <repo_url> bukowski_3d
cd bukowski_3d

# install deps in an isolated Poetry env
poetry install

<details>
<summary>Need OpenAI semantic embeddings?</summary>


export OPENAI_API_KEY="sk-yourRealKey"

</details>


1. Run the CLI

poetry run bukowski-3d               # TF-IDF mode
poetry run bukowski-3d --use-openai  # OpenAI mode

HTML goes to bukowski_3d.html and auto-opens in your browser.

2. Launch Streamlit

poetry run streamlit run gui/streamlit_app.py

3. Launch Gradio

poetry run python gui/gradio_app.py

4. Open the Notebook

poetry run jupyter notebook bukowski_3d.ipynb


⸻

🧪 Tests

poetry run pytest tests/


⸻

📚 Documentation

Generator	Command	Output
Sphinx	poetry run sphinx-build docs_sphinx docs_sphinx/_build	Static HTML in _build/
MkDocs (live)	poetry run mkdocs serve	Browse at http://localhost:8000


⸻

🐳 Docker (optional)

docker build -t bukowski_3d .
docker run --rm -p 8501:8501 bukowski_3d    # runs CLI by default

Edit CMD in Dockerfile if you’d rather start Streamlit or Gradio inside the container.

⸻

🗄️ Project Layout

bukowski_3d/            ← core package
gui/
  ├─ streamlit_app.py
  └─ gradio_app.py
docs_sphinx/
docs_mkdocs/
tests/
bukowski_3d.ipynb
Dockerfile
pyproject.toml
requirements.txt


⸻

🤝 Contributing
	1.	Fork & clone
	2.	poetry install
	3.	Make changes + add tests
	4.	pytest must stay green
	5.	Open a PR 🤘

⸻

📜 License

MIT — do what you want, just keep the copyright notice.