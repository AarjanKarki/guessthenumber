from tkinter import *
import random

def showguess():
    window2=Toplevel()
    window2.config(background='white')
    window2.geometry('500x300')

    number=random.randint(0,20)

    lab=Label(window2,width=20,textvariable=name'your number is'number)
    lab.grid(row=1,column=1)

    window2.mainloop

if __name__=='__main__':
    window=Tk()
    window.geometry('500x300')

    name=StringVar()
    guess_=StringVar()

    labelname=Label(window,text='Please enter your name')
    labelname.grid(row=1,column=1,padx=5,pady=5)

    ntryname=Entry(window)
    ntryname.grid(row=2,column=1,padx=5,pady=5)

    def ok():
        name=ntryname.get()

    btnok=Button(window,text='ok',command=ok)
    btnok.grid(row=2,column=2,padx=5,pady=10)

    labelguess=Label(window,text='take a guess:')
    labelguess.grid(row=4,column=1)

    ntryguess=Entry(window)
    ntryguess.grid(row=4,column=2)
    guess_=ntryguess.get()


    btnguess=Button(window,text='guess',command=showguess)
    btnguess.grid(row=4,column=3)



    window.mainloop()
