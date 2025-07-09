from bukowski_3d.main import generate_projection

def test_generate_projection():
    fig = generate_projection(use_openai=False)
    assert fig.data, "Figure should contain data"
    