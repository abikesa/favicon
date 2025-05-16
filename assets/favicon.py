from PIL import Image

# Load your base image (preferably PNG, square, with transparency)
img = Image.open("favicon-dark.png")

# Save as .ico with multiple sizes for best browser support
img.save("favicon-dark.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])