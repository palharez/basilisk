# Basilisk

This Python package provides a lightweight command-line tool to manage passwords.

## Installation

We recommend using the CLI using [poetry](https://python-poetry.org/) to manage dependencies.

```bash
poetry install
```

## Configuration

The way that this CLI encrypt and decrypt the passwords is by using a key defined in a configuration file `./config/config.ini`.

The CLI only looks for the default profile. This is what a configuration file would look like:

```ini
[default]

key=SampleKey
```

You can just update our `sample.config.ini` to `config.ini` and set your credentials.

## Usage

You just need to call in the terminal.

```bash
python -m basilisk
```

You can obtain help by using the --help option.

```bash
python -m basilisk --help
```

Simple usage of the CLI.

```bash
python -m basilisk list
```
