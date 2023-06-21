from tkinter import *
import time
window = Tk()
window.title("Cumulative GPA calculator for all grades")
window.geometry("1590x630")

title = Label(window, text="Cumulative GPA Calculator", font=("SF Pro Display", 35))
title.pack()

firstTerm = Label(window, text="First term GPA: ", font=("SF Pro Display", 20))
firstTerm.place(relx=0, rely=0.3)

firstTermEntry = Entry(window, width=10)
firstTermEntry.place(relx=0.2, rely=0.31)


secondTerm = Label(window, text="Second term GPA: ", font=("SF Pro Display", 20))
secondTerm.place(relx=0, rely=0.4)

secondTermEntry = Entry(window, width=10)
secondTermEntry.place(relx=0.2, rely=0.41)


thirdTerm = Label(window, text="Third term GPA: ", font=("SF Pro Display", 20))
thirdTerm.place(relx=0, rely=0.5)

thirdTermEntry = Entry(window, width=10)
thirdTermEntry.place(relx=0.2, rely=0.51)


def calcbtn():
    firstGet = firstTermEntry.get()
    secondGet = secondTermEntry.get()
    thirdGet = thirdTermEntry.get()

    initialCumulative = float(firstGet) + float(secondGet) + float(thirdGet)
    cumulative = initialCumulative / 3

    if cumulative <2.5:
        notice = Label(window, text="Your cumulative is " +str(cumulative)+" Since your cumulative GPA is below 2.5, you will have to repeat the grade or" + "\ntake a re-exam if you attended remedial classes", fg="Red", font=("SF Pro Display", 15))
        notice.place(relx=0.3, rely=0.4)
        
    elif cumulative >=2.5:
        
        notice = Label(window, text="Your cumulative is "+str(cumulative)+" Congratulations! you have passed", font=("SF Pro Display", 
15), fg="Green")
        notice.place(relx = 0.3, rely=0.4)
    
    def clearNoice():
      notice.destroy()
    
    returnBtn = Button(window, text="Clear Result", font=("SF Pro Display", 15), command=clearNoice)
    returnBtn.place(relx=0.3, rely=0.6)
        


calculate = Button(window, text="Calculate", font=("SF Pro Display", 15), command=calcbtn)
calculate.place(relx=0.1, rely=0.65)

window.mainloop()