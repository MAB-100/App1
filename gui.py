import functions
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


fsg.theme("DarkAmber")

clock = fsg.Text("", key="clock")
label = fsg.Text("Welcome to our TODOs app.")
add_lable = fsg.Text("Add a task: ")
add_input = fsg.InputText(tooltip="Enter the task you want to add", key="todo") 
list_box = fsg.Listbox(values=functions.get_todos(), size=[45, 10], key="todos", enable_events=True)

add_button = fsg.Button("Add",key="Add")
edit_button = fsg.Button("Edit",key="Edit")
complete_button = fsg.Button("Complete",key="Complete")
exit_button = fsg.Button("Exit",key="Exit")



window = fsg.Window("TODOs App", 
                    layout=[[clock],
                            [add_lable],
                            [add_input, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]
                            ], 

                    font=("Helvetica", 20))

while True:
    event , values = window.read(timeout=200)
    window["clock"].update(time.strftime("%Y-%m-%d %H:%M:%S"))
    match event:
        case "Add":
            if values["todo"] == "":
                fsg.popup("Please enter a task")
                continue            
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update("")


        case "Edit":
            try:
                todos = functions.get_todos()
                todo_to_edit = values["todos"][0]

                index = todos.index(todo_to_edit)
                if values["todo"] != "":
                    new_todo = values["todo"] + "\n"
                else:
                    new_todo = fsg.popup_get_text("Edit task", default_text=todo_to_edit) + "\n"
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update("")
            except IndexError:
                fsg.popup("Please select a task to edit")

        case "Complete":
            try:
                todos = functions.get_todos()
                todo_to_complete = values["todos"][0]
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                fsg.popup("Please select a task to complete")

        case "Exit":
            break

window.close()
