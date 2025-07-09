import os, numpy as np, pandas as pd, pathlib, webbrowser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import plotly.express as px

WORKS = {
    "Post Office": "Autobiographical novel...",
    "Ham on Rye": "Semi-autobiographical coming-of-age tale...",
    "Women": "Older Chinaski's chaotic carousel...",
    "Factotum": "Picaresque drift through menial jobs...",
    "Pulp": "A meta-noir parody...",
    "Love Is a Dog from Hell": "Poems (1974-1977)...",
    "Tales of Ordinary Madness": "Short stories of LA low-lifes...",
    "Notes of a Dirty Old Man": "Underground newspaper columns...",
    "You Get So Alone at Times…": "Mid‑career poems on solitude...",
    "The Last Night of the Earth Poems": "Late‑life poems confronting death..."
}

def generate_projection(use_openai=False, api_key=None):
    """
    Build a 3-D Plotly scatter of Bukowski works.

    Parameters
    ----------
    use_openai
        If *True*, call the OpenAI embedding endpoint.
    api_key
        Override for the `OPENAI_API_KEY` env var.

    Returns
    -------
    plotly.graph_objects.Figure
        The 3-D scatter plot.
    """
    titles, texts = list(WORKS.keys()), list(WORKS.values())
    if use_openai:
        import openai
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
        embeds = [openai.embeddings.create(model="text-embedding-3-small",
                                           input=txt, encoding_format="float").data[0].embedding
                  for txt in texts]
        X = np.array(embeds)
    else:
        X = TfidfVectorizer(stop_words="english").fit_transform(texts).toarray()
    coords = PCA(n_components=3, random_state=42).fit_transform(X)
    df = pd.DataFrame(coords, columns=["PC1", "PC2", "PC3"]); df["Title"] = titles
    fig = px.scatter_3d(df, x="PC1", y="PC2", z="PC3",
                        text="Title", hover_name="Title",
                        title="Charles Bukowski – 3‑D projection of key works")
    fig.update_traces(marker=dict(size=6))
    return fig

def main(theme=None, use_openai=False):
    fig = generate_projection(use_openai=use_openai)
    outfile = pathlib.Path("bukowski_3d.html")
    fig.write_html(outfile, include_plotlyjs="cdn")
    print(f"✓ Written → {outfile.resolve()}")
    webbrowser.open(outfile.resolve().as_uri())

if __name__ == "__main__":
    main()
