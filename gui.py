import functions
import FreeSimpleGUI as fsg

add_lable = fsg.Text("Add a task: ")
add_input = fsg.InputText(tooltip="Enter the task you want to add")
add_button = fsg.Button("Add")

window = fsg.Window("TODOs App", layout=[[add_lable],[add_input, add_button]])
window.read()
window.close()
