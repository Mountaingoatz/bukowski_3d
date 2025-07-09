import streamlit as st
from bukowski_3d.main import generate_projection
st.title("Bukowski 3D - Streamlit")
use_openai = st.checkbox("Use OpenAI embeddings")
if st.button("Generate"):
    st.plotly_chart(generate_projection(use_openai=use_openai))
