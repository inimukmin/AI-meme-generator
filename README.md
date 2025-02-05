# AI Meme Generator 🤖+😂

This project is an AI-powered meme generator that uses OpenAI's GPT to generate a funny caption for a meme based on a provided template and then overlays that caption onto an image.

## Requirements

- Python 3.8 or higher
- The packages listed in [requirements.txt](requirements.txt)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/inimukmin/AI-meme-generator.git
   cd AI-meme-generator
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key:**

   Open config.py and replace "your_openai_api_key_here" with your actual OpenAI API key.

4. **Run the application:**

   ```bash
   python main.py
   ```

## Usage

When you run the program, you’ll be prompted to enter a meme template name (for generating a caption) and the URL for a meme template image.

The generated meme will be saved as output_meme.jpg in the repository folder.

Enjoy your meme generator!
