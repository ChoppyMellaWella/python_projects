# using this guide online as a reference: https://www.pythonguis.com/tutorials/create-gui-tkinter/

import tkinter as tk # we import tkinter and alias to 'tk'

root = tk.Tk() # this creates a main window called 'root'. serves as our parent window

# setting configs for root window
root.title("Pomodoro Timer")
root.configure(background="white")
root.minsize(300,300)
root.maxsize(600,600)
root.geometry("600x600+50+50")

# some labels
pomodoro_test_label = tk.Label(root, text="Pomodoro Timer Test").pack() # pack() method places widget on current window
hello_label = tk.Label(root, text="Hello world!").pack()



root.mainloop() # allows for mouse/keyboard inputs and 'communicates with OS'- not sure what that means
