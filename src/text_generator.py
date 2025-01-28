from transformers import pipeline

def generate_caption(prompt):
    generator = pipeline(
        "text-generation",
        model="distilgpt2",
        max_length=50,
        temperature=0.9
    )
    result = generator(prompt, num_return_sequences=1)
    return result[0]['generated_text']