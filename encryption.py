from PIL import Image
from bitstring import BitArray
import os
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

        # message_ended = False
        # message_iterator = iter(self.message_bitstream)
        # for bit in self.key_bitstream:
        #     # if bit == 1 and not message_ended:
        #     #     try:
        #     #         return_message.append(next(message_iterator))
        #     #     except StopIteration:
        #     #         return_message.append(random.getrandbits(1))
        #     #         message_ended = True
        #     # else:
        #     #     return_message.append(random.getrandbits(1))
        #     if bit == 1:
        #         return_message.append(1)
        #     else:
        #         return_message.append(0)
        #
        # return return_message

    # @staticmethod
    # def convert_key(public_key):
    #     public_key
    #
    # @staticmethod
    # def convert_message_bits(message_file):
    #     message_bits = Bitstream(Bitstream.get_bit_array(message_file))
    #     out_bits = []
    #     for x in message_bits:
    #         out_bits.append(x)
    #         # out_bits += "{0:b}".format(ord(x))
    #     # return int(out_bits, 2)
    #     return out_bits
    #
    # @staticmethod
    # def convert_bits_message(bit_list):
    #     for
    #     out_message = ""
    #     for b in bits:
    #         pass
    #
    # @staticmethod
    # def encrypt(self, message):
    #     message_bits = self.convert_message_bits(message)
    #     out_encrypted_message = ""
    #     if next_key_bit() == 1:
    #         out_encrypted_message += next_message_bit()
    #     else:
    #         out_encrypted_message += random.getrandbits(1)
    #
    #     return out_encrypted_message
    #
    # @staticmethod
    # def decrypt(self, public_message):
    #     out_message = ""
    #     if next_key_bit() == 1:
    #         out_message += next_message_bit()
    #
    #     return out_message.convert()


if __name__ == "__main__":
    ba = Encryption.encode('images/out.png', 'hackathon.txt')
    Pixels.create_image(Pixels.get_img(ba), display=True, save='images/enc.png')

    bb = Encryption.decode('images/out.png', 'images/enc.png')
    for byte in bb.bytes:
        print(chr(byte), end='')

    # for byte in ba.bytes:
    #     print(byte)
    # public_key = "images/key.png"
    # key = Image.open(public_key)
    # key_bitstream = Bitstream(Pixels.get_bit_array(key))
    # ls = Pixels.get_img(key_bitstream)
    # Pixels.create_image(ls, display=True)


