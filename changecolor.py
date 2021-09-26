import tkinter as tk
root=tk.Tk()
root.config(bg='black')
root.wm_minsize(500,500)
from random import choice
run=False

def on_enter(e):
    global run
    run=False
    color()
    
def on_leave(e):
    global run
    run=True
    color()

def color():
    if run==True:
        l2.configure(fg=give_color())
        l2.after(1000,color)

def give_color():
    code=['1','2','3','4','5','6','a','b','c','d','e','f']
    c='#'
    for i in range(6):
        c+=choice(code)
    return c
    
def changecolor():
    global run
    run=True
    b1['state']='disabled'
    color()

    
l1=tk.Label(root,text='WELCOME',bg='black',fg='white',font='times 30 italic')
l1.pack()

l2=tk.Label(root,text='Colors',bg='black',fg='white',font='time 25 italic')
l2.pack(pady=20)

b1=tk.Button(root,text='Start',bg='#123456',fg='white',font='time 25 bold',command=changecolor)
b1.pack(fill="x")

l2.bind('<Enter>',on_enter)
l2.bind('<Leave>',on_leave)

root.mainloop()
