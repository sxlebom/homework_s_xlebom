from tkinter import*
def pls():
    lb2.config(text = '+')
def mnzh():
    lb2.config(text = '*')
def mns():
    lb2.config(text = '-')
def dlt():
    lb2.config(text = '/')    
def equal(): 
    if (lb2.cget('text') == '') or ((lb3.cget('text') == '0') and (lb3.cget('text')=='/')) or (lb3.cget('text') == ''):
        lb5.config(text = 'error')
    elif (lb1.cget('text') == ''):
        if (lb2.cget('text') == '+'):
            lb5.config(text = str(0+int(lb3.cget('text'))))
        elif (lb2.cget('text') == '-'):
            lb5.config(text = str(0-int(lb3.cget('text'))))
        elif (lb2.cget('text') == '*'):
            lb5.config(text = str(0*int(lb3.cget('text'))))
        elif (lb2.cget('text') == '/'):
            lb5.config(text = str(0/int(lb3.cget('text'))))
    else:
        if (lb2.cget('text') == '+'):
            lb5.config(text = str(int((lb1.cget('text')))+int(lb3.cget('text'))))
        elif (lb2.cget('text') == '-'):
            lb5.config(text = str(int((lb1.cget('text')))-int(lb3.cget('text'))))
        elif (lb2.cget('text') == '*'):
            lb5.config(text = str(int((lb1.cget('text')))*int(lb3.cget('text'))))
        elif (lb2.cget('text') == '/'):
            lb5.config(text = str(int((lb1.cget('text')))/int(lb3.cget('text'))))
def one():
    global text1
    global text2
    text1 += '1'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '1'
        lb3.config(text = text2)
def tw():
    global text1
    global text2
    text1 += '2'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '2'
        lb3.config(text = text2)
def thr():
    global text1
    global text2
    text1 += '3'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '3'
        lb3.config(text = text2)
def fr():
    global text1
    global text2
    text1 += '4'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '4'
        lb3.config(text = text2)
def fv():
    global text1
    global text2
    text1 += '5'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '5'
        lb3.config(text = text2)
def sx():
    global text1
    global text2
    text1 += '6'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '6'
        lb3.config(text = text2)
def svn():
    global text1
    global text2
    text1 += '7'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '7'
        lb3.config(text = text2)
def eit():
    global text1
    global text2
    text1 += '8'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '8'
        lb3.config(text = text2)
def nne():
    global text1
    global text2
    text1 += '9'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '9'
        lb3.config(text = text2)
def zer():
    global text1
    global text2
    text1 += '0'
    if (lb2.cget('text')) == '':
        lb1.config(text = text1)
    elif ((lb2.cget('text')) == '') and ((lb3.cget('text')) == ''):
        text2 = ''
        lb3.config(text = text2)
    else:
        text2 += '0'
        lb3.config(text = text2)
def clr():
    global text1
    global text2
    text1 = ''
    text2 = ''
    lb1.config(text = '')
    lb2.config(text = '')
    lb3.config(text = '')
    lb5.config(text = '')
root = Tk()
btnpls = Button(root, height = 1, width = 2,text = '+',command = pls)
btnmns = Button(root, height = 1, width = 2,text = '-',command = mns)
btnmnzh = Button(root, height = 1, width = 2,text = '*',command = mnzh)
btndlt = Button(root, height = 1, width = 2,text = '/',command = dlt)
btnclr = Button(root, height = 1, width = 2,text = 'CE',command = clr)
text1 = ''
text2 = ''
lb1 = Label(root, height = 1, width = 5, bd=4, relief = GROOVE,text='')
lb2 = Label(root, height = 1, width = 2, bd=4,relief= GROOVE)
lb3 = Label(root, height = 1, width = 5, bd=4,relief= GROOVE)
lb4 = Label(root, height = 1, width = 2, bd=4,relief= GROOVE,text = '=')
lb5 = Label(root, height = 1, width = 5, bd=4,relief= GROOVE,text = '')
btnone = Button(root, height = 1, width = 2,text = '1',command = one)
btntw = Button(root, height = 1, width = 2,text = '2',command = tw)
btnthr = Button(root, height = 1, width = 2,text = '3',command = thr)
btnfr = Button(root, height = 1, width = 2,text = '4',command = fr)
btnfv = Button(root, height = 1, width = 2,text = '5',command = fv)
btnsx = Button(root, height = 1, width = 2,text = '6',command = sx)
btnsvn = Button(root, height = 1, width = 2,text = '7',command = svn)
btneit = Button(root, height = 1, width = 2,text = '8',command = eit)
btnnne = Button(root, height = 1, width = 2,text = '9',command = nne)
btnzer = Button(root, height = 3, width = 2,text = '0',command = zer)
btnequal = Button(root, height = 1, width = 2,text = '=',command = equal)
lb1.grid(row = 1,column =1, columnspan = 5, sticky = W)
lb2.grid(row = 1,column =3, columnspan = 1)
lb3.grid(row = 1,column =4, columnspan = 5, sticky = W)
lb4.grid(row = 1,column =6, columnspan = 1, sticky = W)
lb5.grid(row = 1,column =7, columnspan = 1, sticky = W)
btnpls.grid(row = 2, column = 1,columnspan = 1)
btnmns.grid(row = 2, column = 2,columnspan = 1)
btnmnzh.grid(row = 2, column = 3,columnspan = 1)
btndlt.grid(row = 2, column = 4,columnspan = 1)
btnclr.grid(row = 2, column = 5,columnspan = 1)
btnone.grid(row = 5, column = 1, columnspan = 1)
btntw.grid(row = 5, column = 2, columnspan = 1)
btnthr.grid(row = 5, column = 3, columnspan = 1)
btnfr.grid(row = 4, column = 1, columnspan = 1)
btnfv.grid(row = 4, column = 2, columnspan = 1)
btnsx.grid(row = 4, column = 3, columnspan = 1)
btnsvn.grid(row = 3, column = 1, columnspan = 1)
btneit.grid(row = 3, column = 2, columnspan = 1)
btnnne.grid(row = 3, column = 3, columnspan = 1)
btnzer.grid(row = 4, column = 4, rowspan = 2)
btnequal.grid(row = 3, column = 4, columnspan = 1)
root.mainloop()
