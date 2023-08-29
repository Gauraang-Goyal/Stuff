from tkinter import *


root1 = Tk()
root1.title("Login")
root1.geometry('200x140')
root1.config(bg="sky blue")
lbl = Label(root1, text = "Are You A Existing Employee?")
lbl.grid(row=0, column=1, padx=10, pady=10)
e=StringVar()
en=Entry(root1,textvariable=e)
en.grid(row=1, column=1, padx=10, pady=10)
b = Button(root1, text = "Submit" , command= e.get())
b.grid(row=2, column=1, padx=10, pady=10)
root1.resizable(False,False)
root1.mainloop()
#e=e.get()
if b=='yes':
    print("y")
elif b.lower()=='no':
    print('n')
else:
    print('INVALID')