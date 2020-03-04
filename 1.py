from tkinter import *

counter = 0

def add_label(event=NONE):
    global counter
    
    user_text = entry.get()
    if len(user_text) <= 2:
        hint.configure(text="enter text more of then 3 symbols")
        return

    entry.delete(0, END)
    label_new = Label(root, text=user_text, padx="30", pady="20")
    
    if counter % 2:
         label_new.configure(fg='white', bg='black')
    else:
        label_new.configure(bg='white', fg='black')
    
    if counter > 6:
        counter = 0
        children = root.winfo_children()
        for i in children:
            if isinstance(i, Label):
                i.destroy()
    
    
    
    label_new.pack(side=BOTTOM, fill=X)
    
    counter += 1

root = Tk()
root.geometry("300x500")
root.resizable(False, False)
root.title("Simple tk")


Label(root, text="Just a test", padx="30", pady="20").pack(side=BOTTOM)
imput_frame = Frame(root)
imput_frame.pack()

hint = Label(imput_frame,
            text='', 
            fg="red2",
            font=('Times New Roman', 6))
hint.pack(side=BOTTOM)

entry = Entry(imput_frame, width='15')
entry.pack(side=LEFT)


button = Button(imput_frame, text="Click me", command=add_label)
button.pack(side=LEFT)

entry.bind('<Return>', add_label)


root.mainloop()