from tkinter import *
root = Tk()
root.title("Калькулятор")
ent = Entry(root,width=42,bd=6, font='Arial 14')
def insert1():
    ent.insert(END,"1")
def insert2():
    ent.insert(END,"2")
def insert3():
    ent.insert(END,"3")
def insert4():
    ent.insert(END,"4")
def insert5():
    ent.insert(END,"5")
def insert6():
    ent.insert(END,"6")
def insert7():
    ent.insert(END,"7")
def insert8():
    ent.insert(END,"8")
def insert9():
    ent.insert(END,"9")
def insert0():
    ent.insert(END,"0")
def clear_text():
     ent.delete(0, 'end')
def insertg():
    ent.insert(END,"+")
def insertj():
    ent.insert(END,"-")
def insertf():
    ent.insert(END,"*")
def insertff():
    ent.insert(END,"/")
btn = Button(root,
text="1",
width=10,height=1,
bg="black",fg="red", command=insert1, font='Arial 14')
btnt = Button(root,
text="2",
width=10,height=1,
bg="black",fg="red", command=insert2, font='Arial 14')
btng = Button(root,
text="3",
width=10,height=1,
bg="black",fg="red", command=insert3, font='Arial 14')
btnh = Button(root,
text="4",
width=10,height=1,
bg="black",fg="red", command=insert4, font='Arial 14')
btnj = Button(root,
text="5",
width=10,height=1,
bg="black",fg="red", command=insert5, font='Arial 14')
btnv = Button(root,
text="6",
width=10,height=1,
bg="black",fg="red", command=insert6, font='Arial 14')
btnb = Button(root,
text="7",
width=10,height=1,
bg="black",fg="red", command=insert7, font='Arial 14')
btnn = Button(root,
text="8",
width=10,height=1,
bg="black",fg="red", command=insert8, font='Arial 14')
btnr = Button(root,
text="9",
width=10,height=1,
bg="black",fg="red", command=insert9, font='Arial 14')
btna = Button(root,
text="0",
width=10,height=1,
bg="black",fg="red", command=insert0, font='Arial 14')
btnd = Button(root,
text="C",
width=10,height=1,
bg="black",fg="red", command=clear_text, font='Arial 14')
btngt = Button(root,
text="=",
width=10,height=1,
bg="black",fg="red", command=insert0, font='Arial 14')
btngr = Button(root,
text="+",
width=10,height=1,
bg="black",fg="red", command=insertg, font='Arial 14')
btngg = Button(root,
text="-",
width=10,height=1,
bg="black",fg="red", command=insertj, font='Arial 14')
btnggg = Button(root,
text="*",
width=10,height=1,
bg="black",fg="red", command=insertf, font='Arial 14')
btngggg = Button(root,
text="/",
width=10,height=1,
bg="black",fg="red", command=insertff, font='Arial 14')
root.geometry('481x193')
root["bg"] = "green"
ent.grid(column=0,row=3,columnspan=4)
btn.grid(column=0,row=4)
btnt.grid(column=1,row=4)
btngr.grid(column=3,row=4)
btng.grid(column=2,row=4)
btnh.grid(column=0,row=5)
btnj.grid(column=1,row=5)
btnv.grid(column=2,row=5)
btngg.grid(column=3,row=5)
btnb.grid(column=0,row=6)
btnn.grid(column=1,row=6)
btnr.grid(column=2,row=6)
btnggg.grid(column=3,row=6)
btna.grid(column=1,row=7)
btnd.grid(column=0,row=7)
btngt.grid(column=2,row=7)
btngggg.grid(column=3,row=7)
root.mainloop()


# from tkinter import *
# def Button_print(event):
# 	print("Как всегда'Hello World!'")
# root = Tk()
# but = Button(root)
# but["text"]="Печать"
# but.bint("<Button-1>",Button_print)
# but.pack()
# root.mainloop()
