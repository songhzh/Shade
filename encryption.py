from PIL import Image
from bitstring import BitArray
import os
import random
from Pixels import Pixels
from Bitstream import Bitstream


class Encryption:
    def __init__(self, public_key="images/key.png"):
        self.key = Image.open(public_key)
        self.key_bitstream = Bitstream(self.convert_key())
        self.message_bitstream = None

    def convert_key(self):
        return Pixels.get_bit_array(self.key)

    def get_message(self, message):
        message_bit_array = Bitstream.get_bit_array(message + ".txt")
        self.message_bitstream = Bitstream(message_bit_array)

    def encode(self):
        ret = BitArray()
        it = iter(self.message_bitstream)
        for kb in self.key_bitstream:
            try:
               app = BitArray(uint=next(it), length=1) if kb == 1 else BitArray(uint=0, length=1)
               ret.append(app)
            except StopIteration:
                app = BitArray(uint=0, length=1)
                ret.append(app)
        return ret

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
    encrypt = Encryption()

    encrypt.get_message("hackathon")
    ba = encrypt.encode()

    # public_key = "images/key.png"
    # key = Image.open(public_key)
    # key_bitstream = Bitstream(Pixels.get_bit_array(key))
    # ls = Pixels.get_img(key_bitstream)
    # Pixels.create_image(ls, display=True)

    ls = Pixels.get_img(ba)
    Pixels.create_image(ls, display=True)
