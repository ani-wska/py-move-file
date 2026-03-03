import os


def move_file(command: str) -> None:
    splitted_command = command.split()
    src = splitted_command[1]
    dest = splitted_command[2]

    if dest.endswith("/"):
        dest = os.path.join(os.getcwd(), dest)

    directory = os.path.dirname(dest)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(src, "rb") as first_src:
        with open(dest, "wb") as first_dst:
            first_dst.write(first_src.read())

    os.remove(src)
