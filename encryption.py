class Encryption:
    def __init__(self, file_to_encrypt):
        self.file_to_encrypt = file_to_encrypt
        self.image_info = dict()

    def get_file_type(self, file):
        return file.split('.')[-1]
