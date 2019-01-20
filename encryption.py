from PIL import Image
import os
import random
import Pixels

class Encryption:
    def __init__(self, public_key):
        self.key = public_key.convert()
        self.key_bits = []

    @staticmethod
    def convert_message_bits(message):
        out_bits = ""
        for x in message:
            out_bits += "{0:b}".format(ord(x))
        return int(out_bits, 2)

    @staticmethod
    def convert_bits_message(bits):
        out_message = ""
        for b in bits:

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
    encrypt = Encryption(Pixels.open("images/out.png"))
    encrypt.convert_message_bits()
