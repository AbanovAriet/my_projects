import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("320x400")

entry = tk.Entry(root, font=("Arial", 24))
entry.place(x=10, y=10, width=300, height=50)

def click(symbol):
    entry.insert(tk.END, str(symbol))

def equal():
    expression = entry.get()
    try:
        result = eval(expression)
    except:
        result = "Error"
    entry.delete(0, tk.END)
    entry.insert(0, result)

def clear():
    entry.delete(0, tk.END)

def delete_last():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)


buttons = [
    ('7', 10, 80), ('8', 90, 80), ('9', 170, 80), ('/', 250, 80),
    ('4', 10, 150), ('5', 90, 150), ('6', 170, 150), ('*', 250, 150),
    ('1', 10, 220), ('2', 90, 220), ('3', 170, 220), ('-', 250, 220),
    ('0', 10, 290), ('.', 90, 290), ('=', 170, 290), ('+', 250, 290),
    ('C', 10, 360), ('Del', 90, 360),
]

for (text, x, y) in buttons:
    if text == '=':
        cmd = equal
    elif text == 'C':
        cmd = clear
    elif text == 'Del':
        cmd = delete_last
    else:
        cmd = lambda t=text: click(t)
    btn = tk.Button(root, text=text, font=("Arial", 18), command=cmd)
    btn.place(x=x, y=y, width=70, height=60)

root.mainloop()
