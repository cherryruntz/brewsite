from app.brewsite import hello_world

def test__home():
    assert "Hello" in hello_world()