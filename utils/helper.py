import os


def get_absolute_path(relative_path):
    current_directory = os.path.dirname(os.path.dirname(__file__))
    absolute_path = os.path.join(current_directory, relative_path)
    return absolute_path