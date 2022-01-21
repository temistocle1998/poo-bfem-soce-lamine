from glob import glob
from tkinter import *
from  tkinter import  ttk
#importing connection
import  mysql.connector
#establishing connection
conn = mysql.connector.connect(
   user='phpmyadmin', password='djarafat10', host='localhost', database='python_poo')

#defining register function
def register():
    #getting form data
    numero_table1=numero_table.get()
    prenom_s1=prenom_s.get()
    nom1=nom.get()
    date_naissance1=date_naissance.get()
    lieu_naissance1=lieu_naissance.get()
    sexe1=sexe.get()
    nationalite1=nationalite.get()
    choix_epr_facultative1 = choix_epr_facultative.get()
    epreuve_facultative1 = epreuve_facultative.get()
    aptitude_sportive1 = aptitude_sportive.get()
    #applying empty validation
    if numero_table1=='' or prenom_s1==''or nom1=='' or date_naissance1==''or lieu_naissance1==''or sexe1=='':
        message.set("remplissez tous les champs!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO jury(numero_table, prenom_s, nom, date_naissance, lieu_naissance, sexe, nationalite, choix_epr_facultative, epreuve_facultative, aptitude_sportive)"
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    #    if gen1==1:
    #     data = (numero_table1, con1,nom1,"Male",lieu_naissance1,sexe1)
    #    else:
    #     data = (numero_table1, con1, nom1, "Female", lieu_naissance1, sexe1)
       data = (numero_table1, prenom_s1, nom1, date_naissance1, lieu_naissance1, sexe1, nationalite1, choix_epr_facultative1, epreuve_facultative1, aptitude_sportive1)
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Stored successfully")

#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("750x400")
    #declaring variable
    global  message;
    global numero_table
    global prenom_s
    global nom
    global date_naissance
    global lieu_naissance
    global sexe
    global nationalite
    global choix_epr_facultative
    global aptitude_sportive
    global epreuve_facultative
    numero_table = StringVar()
    prenom_s = StringVar()
    nom=StringVar()
    date_naissance=StringVar()
    lieu_naissance=StringVar()
    sexe=StringVar()
    nationalite = StringVar()
    choix_epr_facultative = StringVar()
    epreuve_facultative = StringVar()
    aptitude_sportive = StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="orange",fg="white")
    #numero_table Label
    Label(reg_screen, text="numero_table * ").grid(row = 0,column = 0)
    #numero_table textbox
    Entry(reg_screen, textvariable=numero_table).grid(row = 0,column = 1)
    #prenom_s Label
    Label(reg_screen, text="prenom_s * ").grid(row = 1,column = 0)
    #prenom_s textbox
    Entry(reg_screen, textvariable=prenom_s).grid(row = 1,column = 1)

    # nom Label
    Label(reg_screen, text="nom * ").grid(row = 2,column = 0)
    # nom textbox
    Entry(reg_screen, textvariable=nom).grid(row = 2,column = 1)

    # date_naissance Label
    Label(reg_screen, text="date de naissance * ").grid(row = 3,column = 0)
    # date_naissance radiobutton
    Entry(reg_screen, textvariable=date_naissance).grid(row = 3,column = 1)

    Label(reg_screen, text="lieu de naissance * ").grid(row = 4,column = 0)
    # lieu_naissance combobox
    Entry(reg_screen, textvariable=lieu_naissance).grid(row = 4,column = 1)
    # sexe Label
    Label(reg_screen, text="sexe * ").grid(row = 5,column = 0)
    Radiobutton(reg_screen,text="Male",variable=sexe,value="Masculin").grid(row = 5,column = 1)
    Radiobutton(reg_screen, text="Female", variable=sexe, value="Feminin").grid(row = 5,column = 2)
    # sexe combobox
    Label(reg_screen, text="nationalite * ").grid(row = 6,column = 0)
    monthchoosen = ttk.Combobox(reg_screen, width=27, textvariable=nationalite)
    monthchoosen['values'] = (' Senegalaise',
                              ' Guinneene',
                              ' Malienne',)
    monthchoosen.current()
    monthchoosen.grid(row = 6,column = 1)

    Label(reg_screen, text="Apte * ").grid(row = 7,column = 0)
    Radiobutton(reg_screen,text="oui",variable=aptitude_sportive,value="1").grid(row = 7,column = 1)
    Radiobutton(reg_screen, text="non", variable=aptitude_sportive, value="0").grid(row = 7,column = 2)

    Label(reg_screen, text="choix epreuve facultative ").grid(row = 8,column = 0)
    # lieu_naissance combobox
    Radiobutton(reg_screen,text="oui",variable=choix_epr_facultative,value="1").grid(row = 8,column = 1)
    Radiobutton(reg_screen, text="non", variable=choix_epr_facultative, value="0").grid(row = 8,column = 2)

    Label(reg_screen, text="epreuve facultative ").grid(row = 9,column = 0)
    # lieu_naissance combobox
    Entry(reg_screen, textvariable=epreuve_facultative).grid(row = 9,column = 1)
    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=95,y=264)
    #Login button
    Button(reg_screen, text="Register", width=10, height=1, bg="orange",command=register).place(x=105,y=300)
    reg_screen.mainloop()
#calling function Registrationform
Registrationform()
