from bitstring import BitArray


class Bitstream:
    def __init__(self, bit_array):
        self.bit_array = bit_array

    @staticmethod
    def get_bit_array(link):
        file = BitArray()

        with open(link, 'rb') as f:
            while True:
                byte = f.read(1)
                if not byte:
                    break
                file.append(byte)

        file.append(BitArray(uint=0, length=16))
        return file

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx >= len(self.bit_array):
            raise StopIteration
        result = self.bit_array[self.idx]
        self.idx += 1
        return result

    def __str__(self):
        return str(self.bit_array.bin)

    def __len__(self):
        return len(self.bit_array)


if __name__ == '__main__':
    data = Bitstream.get_bit_array('hackathon.txt')
    bs = Bitstream(data)

    for bit in bs:
        print(bit)
