import gradio as gr
from bukowski_3d.main import generate_projection

def show(use_openai):
    return generate_projection(use_openai)

demo = gr.Interface(fn=show,
                    inputs=gr.Checkbox(label="Use OpenAI embeddings", value=False),
                    outputs=gr.Plot(),
                    title="Bukowski 3D - Gradio",
                    description="Explore Bukowski works in 3‑D")
if __name__ == "__main__":
    demo.launch()
