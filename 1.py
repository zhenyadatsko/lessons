from tkinter import *

counter = 0

def add_label():
    global counter
    
    user_text = entry.get()
    label_new = Label(root, text=user_text, padx="30", pady="20")
    
    if counter % 2:
         label_new.configure(fg='white', bg='black')
    else:
        label_new.configure(bg='white', fg='black')
    label_new.pack(side=BOTTOM, fill=X)
    
    counter += 1

root = Tk()
root.geometry("300x500")
root.resizable(False, False)
root.title("Simple tk")

Label(root, text="Just a test", padx="30", pady="20").pack(side=BOTTOM)
entry = Entry(root, width='15')
entry.pack()
Button(root, text="Click me", command=add_label).pack()

root.mainloop()