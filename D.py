from tkinter import*
def prov1():
    a = ea.get()
    dot = 0
    if a != "":
        for i in range(len(a)):
            if (a[i] >= "0" and a[i] <= "9") or a[i] == "-" or a[i] == "." or a[i] == "+":
                if a[i] == "-":
                    if i != 0:
                        lr.config(text = "Error: в a минус не там")
                        return False
                if a[i] == "+":
                    if  i != 0:
                        lr.config(text = "Error: в a плюс не там")
                        return False
                if a == '0':
                    lr.config(text = "Error: деление на 0")
                    return False
                if a[i] == ".":
                    dot += 1
            else:
                lr.config(text = "Error: в a не цифры")
                return False
            if dot > 1:
                lr.config(text = "Error: в a много точек")
                return False
        return True
    else:
       lr.config(text = "Error: в a нету ничего")
def prov2():
    a = eb.get()
    dot = 0
    if a != "":
        for i in range(len(a)):
            if (a[i] >= "0" and a[i] <= "9") or a[i] == "-" or a[i] == "." or a[i] == "+":
                if a[i] == "-":
                    if i != 0:
                        lr.config(text = "Error: в b минус не там")
                        return False
                if a[i] == "+":
                    if  i != 0:
                        lr.config(text = "Error: в b плюс не там")
                        return False
                if a[i] == ".":
                    dot += 1
            else:
                lr.config(text = "Error: в b не цифры")
                return False
            if dot > 1:
                lr.config(text = "Error: в b много точек")
                return False
        return True
    else:
       lr.config(text = "Error: в b нету ничего")    
def prov3():
    a = ec.get()
    dot = 0
    if a != "":
        for i in range(len(a)):
            if (a[i] >= "0" and a[i] <= "9") or a[i] == "-" or a[i] == "." or a[i] == "+":
                if a[i] == "-":
                    if i != 0:
                        lr.config(text = "Error: в c минус не там")
                        return False
                if a[i] == "+":
                    if  i != 0:
                        lr.config(text = "Error: в c плюс не там")
                        return False
                if a[i] == ".":
                    dot += 1
            else:
                lr.config(text = "Error: в c не цифры")
                return False
            if dot > 1:
                lr.config(text = "Error: в c много точек")
                return False
        return True
    else:
       lr.config(text = "Error: в c нету ничего")
def reshit():
    if prov1():
        if prov2():
            if prov3():
                D = (float(eb.get())**2)-(4*float(ea.get())*float(ec.get()))
                D = round(D, 4)
                if D > 0:
                    x1 = (-1*float(eb.get())+(D**0.5))/(2*float(ea.get()))
                    x2 = (-1*float(eb.get())-(D**0.5))/(2*float(ea.get()))
                    lx1.config(text="x1="+str(round(x1,4)))
                    lx2.config(text="x2="+str(round(x2,4)))
                    lx1.grid(row = 8, column = 1, columnspan = 6)
                    lx2.grid(row = 9, column = 1, columnspan = 6)
                    ld.config(text="D = b^2-4ac = "+str(D))
                elif D == 0:
                    x1 = (-1*float(eb.get())+(D**0.5))/(2*float(ea.get()))
                    x2 = (-1*float(eb.get())-(D**0.5))/(2*float(ea.get()))
                    lx1.config(text="x1="+str(round(x1,4)))
                    lx2.config(text="x2="+str(round(x2,4)))
                    lx1.grid(row = 8, column = 1, columnspan = 6)
                    lx2.grid(row = 9, column = 1, columnspan = 6)
                    ld.config(text="D = b^2-4ac = "+str(D))
                else:
                    lr.config(text="Error: Дискриминант меньше 0")
                    lx1.config(text="x1єØ")
                    lx2.config(text="x2єØ")
                    lx1.grid(row = 8, column = 1, columnspan = 6)
                    lx2.grid(row = 9, column = 1, columnspan = 6)
                    ld.config(text="D = b^2-4ac < 0")
    else:
        lx1.config(text = '')
        lx2.config(text = '')
        ld.config(text = '')
root = Tk()
ltxt = Label(root,height = 1, width = 30, text = 'Введите коэффиценты)',font = 'Verdana 14',cursor = 'trek')
la = Label(root,height = 1, width = 5, text = 'a =',font = 'Verdana 14',cursor = 'trek')

lb = Label(root,height = 1, width = 5, text = 'b =',font = 'Verdana 14',cursor = 'trek')
lc = Label(root,height = 1, width = 5, text = 'c =',font = 'Verdana 14',cursor = 'trek')
ld = Label(root,height = 1, width =20, text = 'D = b^2-4ac = ???',font = 'Verdana 14',cursor = 'trek')
cnt = Button(root,height = 1, width = 5, text = 're:shit', bg = 'black',fg = 'pink',command = reshit,font = 'Verdana 14',cursor = 'dotbox')
ea = Entry(root, width = 5,font = 'Verdana 14',bg = 'green', fg = 'red',cursor = 'dotbox')
eb = Entry(root, width = 5,font = 'Verdana 14',bg = 'green', fg = 'red',cursor = 'dotbox')
ec = Entry(root, width = 5,font = 'Verdana 14',bg = 'green', fg = 'red',cursor = 'dotbox')
lx1 = Label(root,height = 1, width = 10,font = 'Verdana 14',bg = 'green', fg = 'red',cursor = 'trek')
lx2 = Label(root,height = 1, width = 10,font = 'Verdana 14',bg = 'green', fg = 'red',cursor = 'trek')
lr = Label(root,height = 1, width = 30, text = 'Error: None',font = 'Verdana 14',cursor = 'trek')
lr.grid(row = 7, column = 1, columnspan =30)
ltxt.grid(row = 1, column = 1,columnspan = 30)
la.grid(row = 2, column = 1,columnspan = 3)
lb.grid(row = 3, column = 1,columnspan = 3)
lc.grid(row = 4, column = 1,columnspan = 3)
ld.grid(row = 5, column = 1,columnspan = 20) 
cnt.grid(row = 6, column = 1,columnspan = 5)
ea.grid(row = 2, column = 4,columnspan = 5)
eb.grid(row = 3, column = 4,columnspan = 5)
ec.grid(row = 4, column = 4,columnspan = 5)
