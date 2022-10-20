from tkinter import *
from tkinter.ttk import *
import random
from time import strftime
import time
from tkcalendar import Calendar

x1 = 250
y1 = 10
x2 = 88
y2 = 290
x3 = 412
y3 = 290
x = x1
y = y1

a1 = 0
b1 = 0
a = 125
b = 25

g = 1

m = 1

root = Tk()
root.title('Clock')



def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time)
    
lbl = Label(root, font = ('calibri', 80, 'bold'),
            background = 'black',
            foreground = 'white')

def trapinski():
    global g
    if g == 1:
        
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        global x
        global y
        
        i = random.randint(1,3)

        if i == 1:
            x = (x + x1)//2
            y = (y + y1)//2
        if i == 2:
            x = (x + x2)//2
            y = (y + y2)//2
        if i == 3:
            x = (x + x3)//2
            y = (y + y3)//2

        canvas.create_line(x, y, x+1, y+1, fill="white")
        canvas.after(15, trapinski)
    
    if g == 2:
        global a1
        global b1
        global a2
        global b2
        global a3
        global b3
        global a4
        global b4
        global a5
        global b5
        global a6
        global b6
        global a7
        global b7
        global a8
        global b8
        global a
        global b
        
        global m
        
        if m==1:
            a +=1
            if a >= 375 - a1:
                m = 2
            if a1 >= 125:
                a = 125
                b = 25
                a1 = 0
        if m==2:
            b +=1
            if b >= 275 - a1:
                m = 3
        if m == 3:
            a -=1
            if a <= 125 + a1:
                m = 4
        if m > 3:
            b -=1
            if (b <= 25 + a1 + 5) and m > 3:
                m = 1
                a1 += 5



        
        canvas.create_line(a, b, a+1, b+1, fill="white")
        canvas.after(10, trapinski)

def cleancanvas():
    canvas.delete("all")
    global g
    g = random.randint(1,2)  
    canvas.after(60000, cleancanvas)

lbl.pack(anchor = 'center')
time()

 
canvas=Canvas(root, width=500, height=300)
canvas.pack()
trapinski()


root.geometry("800x400")
root.attributes('-fullscreen', True)
canvas.configure(bg='black', bd=0, highlightthickness=0)
root.configure(bg="black", cursor="none")
cleancanvas()
mainloop()

                   