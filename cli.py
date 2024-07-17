import time
from functions import get_todos, write_todos

time_now = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Today's date and time: {time_now}")

print("Welcome to our TODOs app.")

while True:
    user_input = input("Type add, show, complete, exit\n")
    user_input = user_input.strip()
    user_input = user_input.lower()
    
    
    if user_input.startswith('add'):
        if user_input[4:] != '':
            todo = user_input[4:]
        else:
            todo = input("Please enter the task you want to add: ")            
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)
        
    elif user_input.startswith('show'):
        todos = get_todos()
        for i, task in enumerate(todos):
            task = task.strip("\n") 
            print(f"\t{i + 1}. {task}")
        #print("\n")
        
    elif user_input.startswith('complete'):
        if user_input[9:] != '':
            task_number = int(user_input[9:])
        else:
            task_number = int(input("Please enter the task number you want to remove: "))
        try:
            todos = get_todos()
            del todos[task_number - 1]
            write_todos(todos)
        except IndexError:
            print("Invalid task number. Please try again.")
        
    elif user_input.startswith('exit'):
        break
    else:
        print("Invalid input. Please try again.")
