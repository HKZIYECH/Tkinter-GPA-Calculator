from tkinter import *

window = Tk()
window.geometry("940x940")
window.title("GPA Calculator")

title= Label(text="GPA Calculator", font=("SF Pro Display", 35), fg="Blue")
title.pack()

#Defining Subject and their position

english = Label(text="English")
english.place(relx=0, rely=0.1)

eng = Entry(window, width=4, borderwidth=2)
eng.place(relx=0.2, rely= 0.1)


amharic = Label(text="Amharic")
amharic.place(relx=0, rely=0.2)

amh = Entry(window, width=4, borderwidth=2)
amh.place(relx=0.2, rely= 0.2)

math = Label(text="Math")
math.place(relx=0, rely=0.3)

mat = Entry(window, width=4, borderwidth=2)
mat.place(relx=0.2, rely= 0.3)

biology = Label(text="Biology")
biology.place(relx=0, rely=0.4)

bio = Entry(window, width=4, borderwidth=2)
bio.place(relx=0.2, rely= 0.4)

chemistry = Label(text="Chemistry")
chemistry.place(relx=0, rely=0.5)

che = Entry(window, width=4, borderwidth=2)
che.place(relx=0.2, rely= 0.5)

physics = Label(text="Physics")
physics.place(relx=0.7, rely=0.1)

phy = Entry(window, width=4, borderwidth=2)
phy.place(relx=0.8, rely= 0.1)

history = Label(text="History")
history.place(relx=0.7, rely=0.2)

his = Entry(window, width=4, borderwidth=2)
his.place(relx=0.8, rely= 0.2)

geography = Label(text="Geography")
geography.place(relx=0.7, rely=0.3)

geo = Entry(window, width=4, borderwidth=2)
geo.place(relx=0.8, rely= 0.3)

civics = Label(text="Civics")
civics.place(relx=0.7, rely=0.4)

civ = Entry(window, width=4, borderwidth=2)
civ.place(relx=0.8, rely= 0.4)

ict = Label(text="ICT")
ict.place(relx=0.7, rely=0.5)

it = Entry(window, width=4, borderwidth=2)
it.place(relx=0.8, rely= 0.5)

pe = Label(text="PE")
pe.place(relx=0.4, rely=0.5)

ppe = Entry(window, width=4, borderwidth=2)
ppe.place(relx=0.5, rely= 0.5)


 #DONE WITH THE DECLARATION AND PLACEMENT'


#MAIN CODE

def mainExec():
    enget = eng.get()
    if enget == "A+":
        reseng = 1*4
    elif enget == "A":
        reseng = 1*4
    elif enget == "A-":
        reseng = 1*3.67
    elif enget == "B+":
        reseng = 1*3.33
    elif enget == "B":
        reseng = 1*3
    elif enget == "B-":
        reseng = 1*2.67
    elif enget == "C+":
        reseng = 1*2.33
    elif enget == "C":
        reseng = 1*2
    elif enget == "C-":
        reseng = 1*1.67
    elif enget == "D+":
        reseng = 1*1.33
    elif enget == "D":
        reseng = 1*1
    elif enget == "D-":
        reseng = 1*0.67
    elif enget == "F":
        reseng = 1*0



    amget = amh.get()
    if amget == "A+":
        resamh = 1*4
    elif amget == "A":
        resamh = 1*4
    elif amget == "A-":
        resamh = 1*3.67
    elif amget == "B+":
        resamh = 1*3.33
    elif amget == "B":
        resamh = 1*3
    elif amget == "B-":
        resamh = 1*2.67
    elif amget == "C+":
        resamh = 1*2.33
    elif amget == "C":
        resamh = 1*2
    elif amget == "C-":
        resamh = 1*1.67
    elif amget == "D+":
        resamh = 1*1.33
    elif amget == "D":
        resamh = 1*1
    elif amget == "D-":
        resamh = 1*0.67
    elif amget == "F":
        resamh = 1*0



    matget = mat.get()
    if matget == "A+":
        resmat = 1*4
    elif matget == "A":
        resmat = 1*4
    elif matget == "A-":
        resmat = 1*3.67
    elif matget == "B+":
        resmat = 1*3.33
    elif matget == "B":
        resmat = 1*3
    elif matget == "B-":
        resmat = 1*2.67
    elif matget == "C+":
        resmat = 1*2.33
    elif matget == "C":
        resmat = 1*2
    elif matget == "C-":
        resmat = 1*1.67
    elif matget == "D+":
        resmat = 1*1.33
    elif matget == "D":
        resmat = 1*1
    elif matget == "D-":
        resmat = 1*0.67
    elif matget == "F":
        resmat = 1*0


    bioget = bio.get()
    if bioget == "A+":
        resbio = 1*4
    elif bioget == "A":
        resbio = 1*4
    elif bioget == "A-":
        resbio = 1*3.67
    elif bioget == "B+":
        resbio = 1*3.33
    elif bioget == "B":
        resbio = 1*3
    elif bioget == "B-":
        resbio = 1*2.67
    elif bioget == "C+":
        resbio = 1*2.33
    elif bioget == "C":
        resbio = 1*2
    elif bioget == "C-":
        resbio = 1*1.67
    elif bioget == "D+":
        resbio = 1*1.33
    elif bioget == "D":
        resbio = 1*1
    elif bioget == "D-":
        resbio = 1*0.67
    elif bioget == "F":
        resbio = 1*0



    chemget = che.get()
    if chemget == "A+":
        reschem = 1*4
    elif chemget == "A":
        reschem = 1*4
    elif chemget == "A-":
        reschem = 1*3.67
    elif chemget == "B+":
        reschem = 1*3.33
    elif chemget == "B":
        reschem = 1*3
    elif chemget == "B-":
        reschem = 1*2.67
    elif chemget == "C+":
        reschem = 1*2.33
    elif chemget == "C":
        reschem = 1*2
    elif chemget == "C-":
        reschem = 1*1.67
    elif chemget == "D+":
        reschem = 1*1.33
    elif chemget == "D":
        reschem = 1*1
    elif chemget == "D-":
        reschem = 1*0.67
    elif chemget == "F":
        reschem = 1*0


    phyget = phy.get()
    if phyget == "A+":
        resphy = 1*4
    elif phyget == "A":
        resphy = 1*4
    elif phyget == "A-":
        resphy = 1*3.67
    elif phyget == "B+":
        resphy = 1*3.33
    elif phyget == "B":
        resphy = 1*3
    elif phyget == "B-":
        resphy = 1*2.67
    elif phyget == "C+":
        resphy = 1*2.33
    elif phyget == "C":
        resphy = 1*2
    elif phyget == "C-":
        resphy = 1*1.67
    elif phyget == "D+":
        resphy = 1*1.33
    elif phyget == "D":
        resphy = 1*1
    elif phyget == "D-":
        resphy = 1*0.67
    elif phyget == "F":
        resphy = 1*0


    hisget = his.get()
    if hisget == "A+":
        reshis = 0.75*4
    elif hisget == "A":
        reshis = 0.75*4
    elif hisget == "A-":
        reshis = 0.75*3.67
    elif hisget == "B+":
        reshis = 0.75*3.33
    elif hisget == "B":
        reshis = 0.75*3
    elif hisget == "B-":
        reshis = 0.75*2.67
    elif hisget == "C+":
        reshis = 0.75*2.33
    elif hisget == "C":
        reshis = 0.75*2
    elif hisget == "C-":
        reshis = 0.75*1.67
    elif hisget == "D+":
        reshis = 0.75*1.33
    elif hisget == "D":
        reshis = 0.75*1
    elif hisget == "D-":
        reshis = 0.75*0.67
    elif hisget == "F":
        reshis = 0.75*0



    geoget = geo.get()
    if geoget == "A+":
        resgeo = 0.5*4
    elif geoget == "A":
        resgeo = 0.5*4
    elif geoget == "A-":
        resgeo = 0.5*3.67
    elif geoget == "B+":
        resgeo = 0.5*3.33
    elif geoget == "B":
        resgeo = 0.5*3
    elif geoget == "B-":
        resgeo = 0.5*2.67
    elif geoget == "C+":
        resgeo = 0.5*2.33
    elif geoget == "C":
        resgeo = 0.5*2
    elif geoget == "C-":
        resgeo = 0.5*1.67
    elif geoget == "D+":
        resgeo = 0.5*1.33
    elif geoget == "D":
        resgeo = 0.5*1
    elif geoget == "D-":
        resgeo = 0.5*0.67
    elif geoget == "F":
        resgeo = 0.5*0


    civget = civ.get()
    if civget == "A+":
        resciv = 0.5*4
    elif civget == "A":
        resciv = 0.5*4
    elif civget == "A-":
        resciv = 0.5*3.67
    elif civget == "B+":
        resciv = 0.5*3.33
    elif civget == "B":
        resciv = 0.5*3
    elif civget == "B-":
        resciv = 0.5*2.67
    elif civget == "C+":
        resciv = 0.5*2.33
    elif civget == "C":
        resciv = 0.5*2
    elif civget == "C-":
        resciv = 0.5*1.67
    elif civget == "D+":
        resciv = 0.5*1.33
    elif civget == "D":
        resciv = 0.5*1
    elif civget == "D-":
        resciv = 0.5*0.67
    elif civget == "F":
        resciv = 0.5*0


    ictget = it.get()
    if ictget == "A+":
        resit = 0.5*4
    elif ictget == "A":
        resit = 0.5*4
    elif ictget == "A-":
        resit = 0.5*3.67
    elif ictget == "B+":
        resit = 0.5*3.33
    elif ictget == "B":
        resit = 0.5*3
    elif ictget == "B-":
        resit = 0.5*2.67
    elif ictget == "C+":
        resit = 0.5*2.33
    elif ictget == "C":
        resit = 0.5*2
    elif ictget == "C-":
        resit = 0.5*1.67
    elif ictget == "D+":
        resit = 0.5*1.33
    elif ictget == "D":
        resit = 0.5*1
    elif ictget == "D-":
        resit = 0.5*0.67
    elif ictget == "F":
        resit = 0.5*0


    peget = ppe.get()
    if peget == "A+":
        respee = 0.5*4
    elif peget == "A":
        respee = 0.5*4
    elif peget == "A-":
        respee = 0.5*3.67
    elif peget == "B+":
        respee = 0.5*3.33
    elif peget == "B":
        respee = 0.5*3
    elif peget == "B-":
        respee = 0.5*2.67
    elif peget == "C+":
        respee = 0.5*2.33
    elif peget == "C":
        respee = 0.5*2
    elif peget == "C-":
        respee = 0.5*1.67
    elif peget == "D+":
        respee = 0.5*1.33
    elif peget == "D":
        respee = 0.5*1
    elif peget == "D-":
        respee = 0.5*0.67
    elif peget == "F":
        respee = 0.5*0
    
    mreslt = float(reseng)+ float(resamh) + float(resmat) + float(resbio) + float(resphy) + float(reschem) + float(reshis) + float(resgeo) + float(resciv) + float(resit) + float(respee)
    mainResult = mreslt / 8.75
    gpaa = Label(text="Your GPA is: " + str(mainResult), font=("SF Pro Display", 15))
    gpaa.place(relx=0, rely=0.7)


    
#Creating the calculate button

calcbtn = Button(text="Calculate", font=("SF Pro Display", 15), command=mainExec)
calcbtn.place(relx=	0.4, rely=0.6)

credit = Label(window, text="©️ 2023 Made by Sofonias Alemayehu", font=("SF Pro Display", 15))
credit.place(relx=0.25, rely= 0.9)
window.mainloop()