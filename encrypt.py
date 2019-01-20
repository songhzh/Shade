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
    @staticmethod
    def open(link):
        return Image.open(link).convert("RGB").load()

    @staticmethod
    def xor_list(base, *img_list):
        rgb_list = []

        for y in range(200):
            for x in range(200):
                r1, g1, b1 = base[x, y]
                for img in img_list:
                    r2, g2, b2 = img[x, y]
                    r1 ^= r2
                    g1 ^= g2
                    b1 ^= b2
                rgb_list.append((r1, g1, b1))

        return rgb_list

    @staticmethod
    def create_image(rgb_list):
        out = Image.new("RGB", (200, 200))
        out.putdata(rgb_list)
        # out.save("images/out.png")
        return out

    @staticmethod
    def encode(base, *img_list, display=False):
        img = Pixels.create_image(Pixels.xor_list(base, *img_list))
        if display:
            img.show()
        return img


if __name__ == "__main__":
    kon = Pixels.open('images/kon.jpg')
    rnm = Pixels.open('images/rnm.png')
    homer = Pixels.open('images/homer.jpg')
    mixed = Pixels.encode(kon, rnm, homer)
    ret = Pixels.encode(mixed.load(), kon, rnm, display=True)

    # list_1 = pix.encode(pix.key, pix.img_1)
    # mid = pix.create_image(list_1)
    #
    # pix.show_image(mid)
    #
    # list_2 = pix.encode(mid.load(), pix.img_2)
    # out = pix.create_image(list_2)
    #
    # pix.show_image(out)
    #
    # list_3 = pix.encode(out.load(), pix.img_1)
    # out_1 = pix.create_image(list_3)
    #
    # pix.show_image(out_1)
    #
    # list_4 = pix.encode(out_1.load(), pix.key)
    # out_2 = pix.create_image(list_4)
    #
    # pix.show_image(out_2)
