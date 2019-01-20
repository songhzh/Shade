from Pixels import Pixels
from Bitstream import Bitstream
from encryption import Encryption

def get_shared_key():
    kon = Pixels.open('images/kon.jpg')
    rnm = Pixels.open('images/rnm.png')
    homer = Pixels.open('images/homer.jpg')

    key = Pixels.encode(kon, rnm, homer)
    key.save('images/key.png')

    ba = Pixels.get_bit_array(key)
    ls = Pixels.get_img(ba)
    Pixels.create_image(ls, display=True)

def encode_file(filename):
    ba = Encryption.encode('images/key.png', filename)
    Pixels.create_image(Pixels.get_img(ba), display=True, save='images/enc.png')


def main():
    print("Creating Shared Key")
    get_shared_key()
    
    filename = input("Enter name of file you want to encode: ")

    
    print("Encoding...")

    encode_file(filename)

    print("Encryption Complete")


if __name__ == "__main__":
    print("Starting...")
    main() 