import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Display (Entry box)
display = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
display.pack(fill="both", padx=10, pady=10)

# Store current expression
expression = ""

# Functions
def press(key):
    global expression
    expression += str(key)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# Button frame
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "C":
        action = clear
    elif text == "=":
        action = calculate
    else:
        action = lambda x=text: press(x)

    tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

# Run app
root.mainloop()