from PIL import Image

img = Image.open('images/rnm.png').convert("RGB")
pix = img.load()
img.show()

for i in range(200):
    for j in range(200):
        # r, g, b = pix[i, j]
        # print(r, g, b)
        print('%02x%02x%02x' % pix[i, j])
