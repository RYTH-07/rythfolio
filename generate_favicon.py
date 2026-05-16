from PIL import Image, ImageDraw, ImageFont

sizes = [16, 32, 48, 64, 128, 180]

for size in sizes:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = size // 5
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill="#1a1a1a")
    font_size = int(size * 0.52)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    text = "CR"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) // 2
    y = (size - th) // 2 - int(size * 0.04)
    draw.text((x, y), text, font=font, fill="#ffffff")
    img.save(f"public/favicon-{size}x{size}.png")
    print(f"Generated favicon-{size}x{size}.png")

img_32 = Image.open("public/favicon-32x32.png")
img_32.save("public/favicon.ico")
print("Generated favicon.ico")

img_180 = Image.open("public/favicon-180x180.png")
img_180.save("public/apple-touch-icon.png")
print("All done!")