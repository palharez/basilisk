from basilisk.utils import decode_password, encode_password


class Password:
    def __init__(self, content, path):
        self.path = path
        self.name, self.hashed_password = decode_password(content)

    def update(self, hashed_password):
        self.hashed_password = hashed_password

        try:
            with open(self.path, "w") as file:
                file.write(encode_password(self.name, self.hashed_password))
        except IOError:
            print("Error while writing to the file.")

    def __str__(self):
        return f"{self.path}, {self.name}, {self.hashed_password}"
