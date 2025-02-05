from meme_generator import generate_caption, create_meme

def main():
    print("Welcome to the AI Meme Generator!")
    
    # Prompt user for meme details
    meme_template = input("Enter the meme template name (e.g., 'Distracted Boyfriend'): ").strip()
    image_url = input("Enter the URL of the meme template image: ").strip()

    if not meme_template or not image_url:
        print("Both meme template and image URL are required. Exiting.")
        return

    # Generate a caption using the AI engine
    caption = generate_caption(meme_template)
    print("Generated caption:", caption)

    # Create and save the meme
    create_meme(image_url, caption)

if __name__ == "__main__":
    main()
