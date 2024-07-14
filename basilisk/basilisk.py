from uuid import uuid4
from glob import glob
from basilisk.__init__ import __directory__
from basilisk.password import Password
from basilisk.utils import encode_password, get_password_directory


class Basilisk:
    def __init__(self):
        self.passwords = []
        self.mount()

    def mount(self):
        passwords_files_paths = glob(get_password_directory() + "/*.json")
        for password_file_path in passwords_files_paths:
            with open(password_file_path, "r") as file:
                content = file.read()
                self.passwords.append(Password(content, password_file_path))

    def show(self):
        for password in self.passwords:
            print(password)

    def create_password(self, name, password):
        file_name = f"jararaca-{uuid4()}.json"
        file_path = f"{get_password_directory()}/{file_name}"
        encoded_password = encode_password(name, password)

        with open(file_path, "w") as file:
            file.write(encoded_password)

        self.passwords.append(Password(encoded_password, file_path))


def run():
    print("Running Basilisk")
    baselisk = Basilisk()
    baselisk.create_password("SamplesPassName", "SamplesPass")
    baselisk.show()
