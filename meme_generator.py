import openai
from config import OPENAI_API_KEY
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_caption(meme_template: str) -> str:
    """
    Uses OpenAI's GPT engine to generate a funny caption for a given meme template.

    Args:
        meme_template (str): The name or description of the meme template.

    Returns:
        str: A generated meme caption.
    """
    prompt = f"Generate a witty and humorous caption for a meme with the template '{meme_template}'."
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=20,
            n=1,
            stop=None,
            temperature=0.8,
        )
        caption = response.choices[0].text.strip()
        return caption
    except Exception as e:
        print("Error generating caption:", e)
        # Fallback caption in case of error
        return "When you try your best, but you don't succeed."

def create_meme(image_url: str, caption: str, output_path: str = "output_meme.jpg"):
    """
    Downloads an image from the given URL, overlays the caption onto it, and saves the final meme.

    Args:
        image_url (str): URL to the meme template image.
        caption (str): Caption text to overlay on the image.
        output_path (str, optional): File path to save the meme. Defaults to "output_meme.jpg".
    """
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an error on a bad status
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        print("Error loading image:", e)
        return

    draw = ImageDraw.Draw(image)
    width, height = image.size

    # Dynamically determine font size relative to image height
    font_size = max(20, int(height / 15))
    
    try:
        # Try using a TTF font (ensure arial.ttf is available on your system or change to a valid path)
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size and position it at the bottom center
    text_width, text_height = draw.textsize(caption, font=font)
    x = (width - text_width) / 2
    y = height - text_height - 10  # 10 pixels from the bottom

    # Add a black outline for readability
    outline_range = 2
    for adj_x in range(-outline_range, outline_range + 1):
        for adj_y in range(-outline_range, outline_range + 1):
            draw.text((x + adj_x, y + adj_y), caption, font=font, fill="black")
    
    # Draw the main text in white
    draw.text((x, y), caption, font=font, fill="white")

    try:
        image.save(output_path)
        print(f"Meme saved to {output_path}")
    except Exception as e:
        print("Error saving meme:", e)
