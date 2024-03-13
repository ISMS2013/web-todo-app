def get_todos(file_path='todos.txt'):
    with open(file_path, 'r') as fp:
        todos = fp.readlines()
    return todos

def set_todos(todo_list, file_path='todos.txt'):
    with open(file_path, 'w') as fp:
        fp.writelines(todo_list)

if __name__ == "__main__":
    print('Hello')
    print(get_todos())