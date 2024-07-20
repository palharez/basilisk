import typer
from pprint import pprint
from basilisk.basilisk import Basilisk

app = typer.Typer()


@app.command(name="list")
def list_basilisk_passwords():
    basilisk = Basilisk()
    pprint(basilisk.show())


@app.command(name="decrypt")
def decrypt_basilisk_password(
    idx: int = typer.Argument(..., help="Idx of the password in the list return")
):
    basilisk = Basilisk()
    pprint(basilisk.find(idx))


@app.command(name="create")
def create_basilisk_passwords():
    password_name = typer.prompt("name", type=str)
    password_value = typer.prompt("password", hide_input=True, type=str)

    if not password_name or not password_value:
        return pprint("Receive invalid password")

    basilisk = Basilisk()
    password = basilisk.create_password(name=password_name, password=password_value)
    pprint(password)


if __name__ == "__main__":
    app()
