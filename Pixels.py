from PIL import Image
from bitstring import BitArray

class Pixels:
    @staticmethod
    def open(link):
        return Image.open(link).convert('RGB').load()

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
    def create_image(rgb_list, display=False, save=''):
        out = Image.new("RGB", (200, 200))
        out.putdata(rgb_list)
        if display:
            out.show()
        if save != '':
            out.save(save)
        return out

    @staticmethod
    def encode(base, *img_list, display=False):
        return Pixels.create_image(Pixels.xor_list(base, *img_list), display=display)

    @staticmethod
    def get_bit_array(image):
        bits = BitArray()
        data = image.getdata()

        for (r, g, b) in data:
            bits.append(BitArray(uint=r, length=8))
            bits.append(BitArray(uint=g, length=8))
            bits.append(BitArray(uint=b, length=8))

        return bits

    @staticmethod
    def get_img(bit_array):
        rgb_list = []
        idx = 0
        rgb = [None] * 3

        for byte in bit_array.bytes:
            rgb[idx] = byte
            idx = (idx + 1) % 3
            if idx == 0:
                rgb_list.append(tuple(rgb))

        return rgb_list


if __name__ == "__main__":
    kon = Pixels.open('images/kon.jpg')
    rnm = Pixels.open('images/rnm.png')
    homer = Pixels.open('images/homer.jpg')

    key = Pixels.encode(kon, rnm, homer)
    key.save('images/key.png')

    # ret = Pixels.encode(mixed.load(), kon, rnm, display=True)
    ba = Pixels.get_bit_array(key)
    print(ba)
    ls = Pixels.get_img(ba)
    Pixels.create_image(ls, display=True)

