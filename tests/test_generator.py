# tests/test_generator.py
from src.text_generator import generate_caption

def test_text_generation():
    caption = generate_caption("Python programmers")
    assert len(caption) > 10