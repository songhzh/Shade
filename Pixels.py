from PIL import Image
import io

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

    def get_byte_array(link):

        img = Image.open(link, mode='r')

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        return img_byte_arr

    @staticmethod
    def encode(base, *img_list, display=False):
        img = Pixels.create_image(Pixels.xor_list(base, *img_list))
        if display:
            img.show()
        return img



if __name__ == "__main__":
    # kon = Pixels.open('images/kon.jpg')
    # rnm = Pixels.open('images/rnm.png')
    # homer = Pixels.open('images/homer.jpg')
    # mixed = Pixels.encode(kon, rnm, homer)
    # ret = Pixels.encode(mixed.load(), kon, rnm, display=True)
    print(Pixels.get_byte_array('images/kon.jpg'))