File = "todos.txt"

def open_todo(path=File):
    """Read txt file and return the list"""

    with open(path, 'r') as file:
        todos_file = file.readlines()
    return todos_file


def write_todo(todos_arg, path=File):
    """write the items list in txt file"""

    with open(path, 'w') as file:
        file.writelines(todos_arg)