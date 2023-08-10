import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

# Function to update the Entry widget
def update_entry(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Creating buttons and adding them to the grid
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_index = 1
col_index = 0

for button_value in buttons:
    if button_value == 'C':
        tk.Button(root, text=button_value, command=lambda: entry.delete(0, tk.END)).grid(row=row_index, column=col_index)
    elif button_value == '=':
        tk.Button(root, text=button_value, command=lambda: calculate()).grid(row=row_index, column=col_index)
    else:
        tk.Button(root, text=button_value, command=lambda val=button_value: update_entry(val)).grid(row=row_index, column=col_index)

    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Function to evaluate and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Start the main event loop
root.mainloop()
