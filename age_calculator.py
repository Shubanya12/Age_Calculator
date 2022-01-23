from tkinter import*
from datetime import date
t=Tk()
t.config(bg="black")
t.title("AGE CALCULATOR")

#main Function....
def age():
    today=date.today()

    age=today.year-int(e.get())
    months=(today.month,today.day)<(int(e1.get()),int(e2.get()))

    if months==True:
        months=1
    else:
        months=0
        
    real_age=(age-months,"Years")
    myText.set(real_age)

myText=StringVar()

Label(t,text="AGE CALCULATOR",foreground="black",background="white").place(x=50,y=10)

#LABELING...
Label(t,text="YEAR",foreground="black",background="red",font="arial 8 bold").place(x=10,y=100)
e=Entry(t,font="arial 10 bold")
e.place(x=60,y=100)

Label(t,text="MONTH",foreground="black",background="red",font="arial 8 bold").place(x=10,y=150)
e1=Entry(t,font="arial 10 bold")
e1.place(x=60,y=150)

Label(t,text="DATE",foreground="black",background="red",font="arial 8 bold").place(x=10,y=200)
e2=Entry(t,font="arial 10 bold")
e2.place(x=60,y=200)

Button(t,text="CALCULATE",foreground="black",background="white",command=age).place(x=60,y=240)

Label(t,text="AGE = ",foreground="black",background="cyan",font="arial 9 bold").place(x=10,y=280)
Entry(t,font="arial 12 bold",textvariable=myText).place(x=60,y=280,height=20,width=100)

t.geometry("300x400")
t.mainloop()

