from PIL import Image

# img_1 = Image.open('images/rnm.png').convert("RGB")
# img_2 = Image.open('images/kon.jpg').convert("RGB")
# pix_1 = img_1.load()
# pix_2 = img_2.load()
#
# for i in range(200):
#     for j in range(200):
#         r_1, g_1, b_1 = pix_1[i, j]
#         r_2, g_2, b_2 = pix_2[i, j]
#         print("(", r_1, g_1, b_1, ")", "or", "(", r_2, g_2, b_2, ")")
#         mix = (r_1 ^ r_2, g_1 ^ g_2, b_1 ^ b_2)
#         print(mix)


class Pixels:
    def __init__(self):
        # images
        self.key = Image.open('images/kon.jpg').convert("RGB").load()
        self.img_1 = Image.open('images/rnm.png').convert("RGB").load()
        self.img_2 = Image.open('images/homer.jpg').convert("RGB").load()

    def encode(self, image1, image2):
        rgb_list = []
        for i in range(200):
            for j in range(200):
                keyR, keyG, keyB = image1[j, i]
                r, g, b = image2[j, i]
                print("(", keyR, keyG, keyB, ")", "or", "(", r, g, b, ")")
                mix = (keyR ^ r, keyG ^ g, keyB ^ b)
                print(mix)
                rgb_list.append(mix)

        return rgb_list

    def create_image(self, rgb_list):
        out = Image.new("RGB", (200, 200))
        out.putdata(rgb_list)
        out.save("images/out.png")
        # out.show()
        return out

    def show_image(self, image):
        image.show()


if __name__ == "__main__":
    pix = Pixels()
    list_1 = pix.encode(pix.key, pix.img_1)
    mid = pix.create_image(list_1)

    pix.show_image(mid)

    list_2 = pix.encode(mid.load(), pix.img_2)
    out = pix.create_image(list_2)

    pix.show_image(out)

    list_3 = pix.encode(out.load(), pix.img_1)
    out_1 = pix.create_image(list_3)

    pix.show_image(out_1)

    list_4 = pix.encode(out_1.load(), pix.key)
    out_2 = pix.create_image(list_4)

    pix.show_image(out_2)
