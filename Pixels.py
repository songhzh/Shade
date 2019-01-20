from PIL import Image

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


# if __name__ == "__main__":
#     kon = Pixels.open('images/kon.jpg')
#     rnm = Pixels.open('images/rnm.png')
#     homer = Pixels.open('images/homer.jpg')
#     mixed = Pixels.encode(kon, rnm, homer)
#     ret = Pixels.encode(mixed.load(), kon, rnm, display=True)
