


def get_todos(filepath='todos.txt'):
    try:
        with open(filepath, 'r') as file:
            Todos_local = file.readlines()
            return Todos_local
    except FileNotFoundError:
        print("No file found")
        return []
    
def write_todos(Todos, filepath = 'todos.txt',):
    with open(filepath, 'w') as file:
        for task in Todos:
            file.write(task)
            
if __name__ == "__main__":
    print("you are running function.py directly")
