from PIL import Image, ImageDraw, ImageFont
from get_random_quote import get_random_quote
import textwrap

def generate_meme(image_path="cat.jpeg", output_path="generated_meme.jpeg", quote = None):
    # Load image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Load font (fallback to default if custom font not available)
    try:
        font = ImageFont.truetype("arial.ttf", size=75)  # Windows
    except:
        font = ImageFont.load_default()
    
    # Get a quote
    if not quote:
        quote = get_random_quote()
    
    # Wrap the text to fit in the image width
    wrapped_text = textwrap.fill(quote, width=70)

    # Position: near bottom
    width, height = img.size
    text_x = 20
    text_y = height - 200

    # Add text
    draw.text((text_x, text_y), wrapped_text, font=font, fill="white")

    # Save image
    img.save(output_path)
    # print(f"✅ Meme saved as {output_path}")

if __name__ == "__main__":
    generate_meme()
