# -*- coding: utf-8 -*-
from tkinter import*
from math import cos, sin
def pr1():
    global text1
    text1 += "1"
    lable.config(text = text1)
def pr2():
    global text1
    text1 += "2"
    lable.config(text = text1)
def pr3():
    global text1
    text1 += "3"
    lable.config(text = text1)
def pr4():
    global text1
    text1 += "4"
    lable.config(text = text1)
def pr5():
    global text1
    text1 += "5"
    lable.config(text = text1)
def pr6():
    global text1
    text1 += "6"
    lable.config(text = text1)
def pr7():
    global text1
    text1 += "7"
    lable.config(text = text1)
def pr8():
    global text1
    text1 += "8"
    lable.config(text = text1)
def pr9():
    global text1
    text1 += "9"
    lable.config(text = text1)
def pr0():
    global text1
    text1 += "0"
    lable.config(text = text1)
def ce():
    global text1, op, pred
    pred = 0
    text1 = ""
    lable.config(text = text1)
    op = None
    pred = None
def backs():
    global text1
    text1 = text1[0:len(text1)-1:1]
    lable.config(text = text1)
def make_op():
    global text1, pred, op, root
    if text1 == "":
        return True
    if op == None:
        pred = float(text1)
        text1 = ""
        lable.config(text = text1)
    elif op == "=":
        text1 = float(pred)
        lable.config(text = text1)
    elif op == "+":
        pred += float(text1)
        text1 = ""
        lable.config(text = text1)
    elif op == "-":
        pred -= float(text1)
        text1 = ""
        lable.config(text = text1)
    elif op == "*":
        pred *= float(text1)
        text1 = ""
        lable.config(text = text1)
    elif op == "**":
        pred **= float(text1)
        text1 = ""
        lable.config(text = text1)
    elif op == "/":
        if int(text1) != 0:
            pred /= float(text1)
            text1 = ""
            lable.config(text = text1)
        else:
            lable.config(text = "error")
            def ret():
                lable.config(text = text1)
            root.after(1000, ret)
            return False
    return True
def plus():
    global op
    if make_op():
        op = "+"
def minus():
    global op
    if make_op():
        op = "-"    
def umn():
    global op
    if make_op():
        op = "*"
def delit():
    global op
    if make_op():
        op = "/"
def step():
    global op
    if make_op():
        op = "**"
def plmin():
    global op, text1
    text1 = float(text1) * -1
    text1 = str(text1)
    lable.config(text = text1)
    op = None
def step2():
    global op, text1
    text1 = float(text1) ** 2
    text1 = str(text1)
    lable.config(text = text1)
    op = None
def kor():
    global op, text1
    text1 = float(text1) ** 0.5
    text1 = str(text1)
    lable.config(text = text1)
    op = None
def Ms():
    global M, text1
    M = float(text1)
    text1 = ""
    lable.config(text = text1)
def Mc():
    global M
    M = 0
def Mr():
    global M, text1
    text1 = str(M)
    lable.config(text = text1)
def Mpl():
    global M, text1
    M += float(text1)
    text1 = ""
    lable.config(text = text1)
def Mmin():
    global M, text1
    M -= float(text1)
    text1 = ""
    lable.config(text = text1)
def ravno():
    global op, text1
    if make_op():
        op = "="
        make_op()
        op = None
        lable.config(text = pred)
root = Tk()
button1=Button(root,text='1',width=3,height=1,command=pr1)
button2=Button(root,text='2',width=3,height=1,command=pr2)
button3=Button(root,text='3',width=3,height=1,command=pr3)
button4=Button(root,text='4',width=3,height=1,command=pr4)
button5=Button(root,text='5',width=3,height=1,command=pr5)
button6=Button(root,text='6',width=3,height=1,command=pr6)
button7=Button(root,text='7',width=3,height=1,command=pr7)
button8=Button(root,text='8',width=3,height=1,command=pr8)
button9=Button(root,text='9',width=3,height=1,command=pr9)
button0=Button(root,text='0',width=3,height=1,command=pr0)
buttonce=Button(root,text='CE',width=3,height=1,command=ce)
buttonbacks=Button(root,text='<-',width=3,height=1,command=backs)
buttonpl=Button(root,text='+',width=3,height=1,command=plus)
buttonmin=Button(root,text='-',width=3,height=1,command=minus)
buttonumn=Button(root,text='*',width=3,height=1,command=umn)
buttondel=Button(root,text='/',width=3,height=1,command=delit)
buttonrav=Button(root,text='=',width=3,height=1,command=ravno)
buttonstep=Button(root,text='^',width=3,height=1,command=step)
buttonplmin=Button(root,text='+/-',width=3,height=1,command=plmin)
buttonstep2=Button(root,text='^2',width=3,height=1,command=step2)
buttonkor=Button(root,text='v',width=3,height=1,command=kor)
buttonMs=Button(root,text='Ms',width=3,height=1,command=Ms)
buttonMr=Button(root,text='Mr',width=3,height=1,command=Mr)
buttonMc=Button(root,text='Mc',width=3,height=1,command=Mc)
buttonMpl=Button(root,text='M+',width=3,height=1,command=Mpl)
buttonMmin=Button(root,text='M-',width=3,height=1,command=Mmin)
M = 0
op = None
pred = 0
text1 = ""
lable = Label(root,bd = 4,width=15,height=1,fg='black',font='arial 14')
lable.place(x=0, y=0)
button1.place(x=0, y=30)
button2.place(x=40, y=30)
button3.place(x=80, y=30)
button4.place(x=0, y=60)
button5.place(x=40, y=60)
button6.place(x=80, y=60)
button7.place(x=0, y=90)
button8.place(x=40, y=90)
button9.place(x=80, y=90)
button0.place(x=40, y=120)
buttonce.place(x=0, y=120)
buttonbacks.place(x=80, y=120)
buttonpl.place(x=120, y=30)
buttonmin.place(x=120, y=60)
buttonumn.place(x=120, y=90)
buttondel.place(x=120, y=120)
buttonrav.place(x=120, y=150)
buttonstep.place(x=0, y=150)
buttonplmin.place(x=40, y=150)
buttonstep2.place(x=80, y=150)
buttonkor.place(x=160, y=30)
buttonMs.place(x=160, y=60)
buttonMr.place(x=160, y=90)
buttonMc.place(x=160, y=120)
buttonMpl.place(x=160, y=150)
buttonMmin.place(x=160, y=180)
root.mainloop()
