from PIL import Image

img = Image.open('images/kon.jpg').convert("RGB")
pixels = img.load()

print(img)