from tkinter import *
#import main


root1 = Tk()
root1.title("Employee Login")
root1.geometry('350x200')
frame1=Frame(root1,bg = "light blue",bd=10,width=350,height=200)
frame1.grid()
lbl = Label(frame1, text = "Are You A Existing Employee?")
lbl.grid(row=0, column=1, padx=10, pady=10)
e=StringVar()
en=Entry(frame1,textvariable=e)
en.grid(row=1, column=1, padx=10, pady=10)
b = Button(frame1, text = "Submit")
b.grid(row=2, column=1, padx=10, pady=10)
root1.mainloop()
e=e.get()
if e.lower()=='yes':
    print("y")
    #open_login()
elif e.lower()=='no':
    print('n')
