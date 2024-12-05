from tkinter import *
import ast

# Constants
BUTTON_WIDTH = 2
BUTTON_HEIGHT = 2
DISPLAY_ROW = 1
DISPLAY_COLUMNSPAN = 6
BUTTON_GRID_ROWS = 3
BUTTON_GRID_COLUMNS = 3
OPERATIONS_COLUMN = 3

# Function to create a button
def create_button(root, text, row, column, command):
    button = Button(root, text=text, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=command)
    button.grid(row=row, column=column)
    return button

# Function to get the number clicked and add it to the display
def get_number(num):
    display.insert(END, num)

# Function to get the operation clicked and add it to the display
def get_operation(operator):
    display.insert(END, operator)

# Function to clear the display
def clear_all():
    display.delete(0, END)

# Function to calculate the result
def calculate():
    try:
        entire_string = display.get()
        node = ast.parse(entire_string, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except SyntaxError:
        clear_all()
        display.insert(0, "Syntax Error")
    except Exception as e:
        clear_all()
        display.insert(0, str(e))

# Function to undo the last character
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")

# Create the main window
root = Tk()

# Create the display field
display = Entry(root)
display.grid(row=DISPLAY_ROW, columnspan=DISPLAY_COLUMNSPAN, sticky=W+E)

# Create the number buttons
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(BUTTON_GRID_ROWS):
    for j in range(BUTTON_GRID_COLUMNS):
        button_text = numbers[i * BUTTON_GRID_COLUMNS + j]
        create_button(root, button_text, i + 2, j, lambda text=button_text: get_number(text))

# Create the zero button
create_button(root, "0", 5, 1, lambda: get_number(0))

# Create the AC and = buttons
create_button(root, "AC", 5, 0, clear_all)
create_button(root, "=", 5, 2, calculate)

# Create the undo button
create_button(root, "<-", 5, 4, undo)

# Create the operation buttons
operations = ['+', '-', '', '/', '*3.14', "%", "(", "", ")", "*2"]
for i in range(BUTTON_GRID_ROWS):
    for j in range(BUTTON_GRID_COLUMNS):
        if i * BUTTON_GRID_COLUMNS + j < len(operations):
            button_text = operations[i * BUTTON_GRID_COLUMNS + j]
            create_button(root, button_text, i + 2, j + OPERATIONS_COLUMN, lambda text=button_text: get_operation(text))

# Start the main loop
root.mainloop()