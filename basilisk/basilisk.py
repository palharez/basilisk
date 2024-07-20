from uuid import uuid4
from glob import glob
from basilisk.__init__ import __directory__
from basilisk.password import Password
from basilisk.cipher import Cipher
from basilisk.utils import encode_password, get_password_directory
from pathlib import Path
from configparser import RawConfigParser
from os.path import isfile


class Basilisk:
    def __init__(self):
        self.passwords = []

        key = self._get_config_key()
        self.cipher = Cipher(key)

        self.mount()

    def _get_config_file(self):
        current_dir = Path.cwd()
        config_dir = current_dir / "config"
        config_file = config_dir / "config.ini"

        if not isfile(config_file):
            raise ValueError("Configuration file not found")

        return config_file

    def _get_config_key(self):
        config_file = self._get_config_file()
        parser = RawConfigParser()
        parser.read(str(config_file))
        return parser.get("default", "key")

    def mount(self):
        passwords_files_paths = glob(get_password_directory() + "/*.json")
        for password_file_path in passwords_files_paths:
            with open(password_file_path, "r") as file:
                content = file.read()
                self.passwords.append(Password(content, password_file_path))

    def find(self, idx):
        password = self.passwords[idx]

        return {
            "name": password.name,
            "password": self.cipher.decrypt(password.hashed_password),
        }

    def show(self):
        return [
            f"idx: {idx}, password: {password}"
            for idx, password in enumerate(self.passwords)
        ]

    def create_password(self, name, password):
        file_name = f"jararaca-{uuid4()}.json"
        file_path = f"{get_password_directory()}/{file_name}"
        encrypted_password = self.cipher.encrypt(password)
        encoded_password = encode_password(name, encrypted_password)

        with open(file_path, "w") as file:
            file.write(encoded_password)

        password = Password(encoded_password, file_path)
        self.passwords.append(password)

        return password
