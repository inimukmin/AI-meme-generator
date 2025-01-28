# AI Meme Generator 🤖+😂

[![Streamlit Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-huggingface-space-link.com)

Generate memes using GPT-2 for text generation and CLIP to match captions with meme templates.

## Features
- Custom meme caption generation
- Preloaded meme templates
- Simple web interface

## Project Structure
```bash
├── .gitignore
├── README.md              # Project overview, setup, demo
├── requirements.txt       # Dependencies
├── app.py                 # Main Streamlit/Gradio app
│
├── src/                   # Modular code (optional but recommended)
│   ├── text_generator.py  # Caption generation logic
│   └── image_matcher.py   # CLIP-based image matching
│
├── images/                # Store meme templates
│   ├── meme1.jpg
│   ├── meme2.jpg
│   └── ...                # Add 10-20 sample memes
│
├── data/                  # (Optional) Dataset/example prompts
│   └── sample_prompts.csv
│
├── tests/                 # (Optional) Simple test scripts
│   └── test_generator.py
│
├── assets/                # Screenshots/GIFs for README
│   └── demo.gif
│
├── Dockerfile             # (Optional) For containerization
└── docker-compose.yml     # (Optional) Bonus for deployment
```

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/ai-meme-generator.git
   cd ai-meme-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add meme templates to the images/ folder (download from Imgflip)
   

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Troubleshooting
1. CLIP Model Errors:
   If you get OSError: Couldn't reach server…, manually download the model:
   ```bash
   # Add this to src/image_matcher.py before loading the model
   from sentence_transformers import util
   util.http_get("https://huggingface.co/sentence-transformers/clip-ViT-B-32/resolve/main/pytorch_model.bin", "model.bin")   
   ```
   
2. Out of Memory:
   Reduce the number of images in images/ (start with 5-10)

3. Streamlit Port Conflicts:
   ```bash
   streamlit run app.py --server.port 8502
   ```
   
