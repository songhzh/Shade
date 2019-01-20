from PIL import Image
from bitstring import BitArray
import random
from Pixels import Pixels
from Bitstream import Bitstream


class Encryption:
    @staticmethod
    def get_img(link):
        return Bitstream(Pixels.get_bit_array(Image.open(link)))

    @staticmethod
    def get_msg(link):
        return Bitstream.get_bit_array(link)

    @staticmethod
    def get_bit(bit):
        return BitArray(uint=bit, length=1)

    @staticmethod
    def encode(key, msg):
        return_arr = BitArray()
        msg_it = iter(Encryption.get_msg(msg))

        for key_bit in Encryption.get_img(key):
            bit = Encryption.get_bit(random.getrandbits(1))
            try:
                if key_bit == 1:
                    bit = Encryption.get_bit(next(msg_it))
            except StopIteration:
                pass
            finally:
                return_arr.append(bit)

        return return_arr

    @staticmethod
    def decode(key, enc):
        return_arr = BitArray()
        enc_it = iter(Encryption.get_img(enc))
        bits = 0
        for key_bit in Encryption.get_img(key):
            bit = BitArray(uint=next(enc_it), length=1)
            if key_bit == 0:
                continue
            return_arr.append(bit)

            bits = (bits + 1) % 8
            if bits != 0:
                continue
            if return_arr[-16:].uint == 0:
                break

        return return_arr
    
if __name__ == "__main__":
    ba = Encryption.encode('images/out.png', 'hackathon.txt')
    Pixels.create_image(Pixels.get_img(ba), display=True, save='images/enc.png')
    
    for byte in bb.bytes:
        print(chr(byte), end='')



