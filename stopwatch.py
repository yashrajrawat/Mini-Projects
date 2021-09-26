import tkinter as tk
from random import choice
from datetime import datetime

root=tk.Tk()
root.config(bg='#123356')
root.wm_minsize(500,500)
run=False
count=-1

def get_time():
    global count
    if run:
        if count!=-1:
            d=datetime.fromtimestamp(count)
            l2.configure(text=d.strftime("%H:%M:%S"))
            count+=1
            l2.after(1000,get_time)

def start():
    global run,count
    if count==-1:
        run=True
        count=66600
        b1['state']='disabled'
        b2['state']='normal'
        b3['state']='normal'
        b4['state']='normal'
        l1.configure(text='Started.....')
        get_time()
    else:
        run=True
        b1['state']='disabled'
        b2['state']='normal'
        b3['state']='normal'
        b4['state']='normal'
        l1.configure(text='Started.....')
        get_time()

    
def stop():
    global run,count
    run=False
    count=-1
    l1.configure(text='Stoped.....')
    b2['state']='disabled'
    b1['state']='normal'
    b3['state']='normal'
    b4['state']='normal'

def reset():
    global run,count
    run=True
    l1.configure(text='Reset.....')
    count=66600
    b4['state']='normal'
    b3['state']='disabled'
    b2['state']='normal'
    b1['state']='normal'
    get_time()
    
def pause():
    global run,count
    run=False
    l1.configure(text='Paused.....')
    b4['state']='disabled'
    b1['state']='normal'
    b3['state']='normal'
    b2['state']='normal'
    
l1=tk.Label(root,text='StopWatch',bg='#123356',fg='white',font='times 30 italic')
l1.pack()

l2=tk.Label(root,text='Time',bg='#123356',fg='white',font='time 25 italic')
l2.pack(pady=20)

b1=tk.Button(root,text='Start',bg='black',fg='white',font='time 25 bold',command=start)
b1.pack(fill="x")

b2=tk.Button(root,text='Stop',bg='black',fg='white',font='time 25 bold',command=stop)
b2.pack(fill="x")

b3=tk.Button(root,text='Reset',bg='black',fg='white',font='time 25 bold',command=reset)
b3.pack(fill="x")

b4=tk.Button(root,text='Pause',bg='black',fg='white',font='time 25 bold',command=pause)
b4.pack(fill="x")
            
root.mainloop()
