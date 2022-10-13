import os


def get_path_name_file(file):
    name = os.path.split(file)[1].split(".")[0]
    root = os.path.abspath(os.path.join(file, "../.."))
    return root, name
