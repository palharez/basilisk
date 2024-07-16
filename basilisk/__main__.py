import sys

if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 8):
        print(
            f"Basilisk requires Python 3.8+\nYou are using Python {python_version}, which is not supported by Basilisk."
        )
        sys.exit(1)
