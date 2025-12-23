from PIL import Image, ImageDraw, ImageFont
import os

def draw_text(draw, text, font, image_width, y):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    x = (image_width - text_width) // 2

    # outline hitam
    for dx in [-2, -1, 0, 1, 2]:
        for dy in [-2, -1, 0, 1, 2]:
            draw.text((x + dx, y + dy), text, font=font, fill="black")

    draw.text((x, y), text, font=font, fill="white")

def make_meme(image_path, top_text, bottom_text):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    width, height = img.size

    try:
        font = ImageFont.truetype("arial.ttf", size=int(height / 10))
    except:
        font = ImageFont.load_default()

    if top_text:
        draw_text(draw, top_text.upper(), font, width, 10)

    if bottom_text:
        draw_text(draw, bottom_text.upper(), font, width, height - int(height / 6))

    output_path = image_path.replace(".png", "_meme.png")
    img.save(output_path)

    return output_path
