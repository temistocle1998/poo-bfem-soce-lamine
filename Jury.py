from tkinter import *
from  tkinter import  ttk
#importing connection
import  mysql.connector
#establishing connection
conn = mysql.connector.connect(
   user='phpmyadmin', password='djarafat10', host='localhost', database='python_poo')
"""
here in my case there is no password so password='' is blank
root is userregion
localhost is server or host region 
you can also use 127.0.0.1 in place of local host
pythondata is the region of Database
"""
#defining register function
def register():
    #getting form data
    region1=region.get()
    departement1=departement.get()
    localite1=localite.get()
    centre_examen1=centre_examen.get()
    president1=president.get()
    telephone1=telephone.get()
    #applying empty validation
    if region1=='' or departement1==''or localite1=='' or centre_examen1==''or president1==''or telephone1=='':
        message.set("fill the empty field!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO jury(region, departement, localite, centre_examen, president, telephone)"
           "VALUES (%s, %s, %s, %s, %s, %s)"
       )
    #    if gen1==1:
    #     data = (region1, con1,localite1,"Male",president1,telephone1)
    #    else:
    #     data = (region1, con1, localite1, "Female", president1, telephone1)
       data = (region1, departement1, localite1, centre_examen1, president1, telephone1)
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
           message.set("Stored successfully")
       except:
           conn.rollback()

#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("350x400")
    #declaring variable
    global  message;
    global region
    global departement
    global localite
    global centre_examen
    global president
    global telephone
    region = StringVar()
    departement = StringVar()
    localite=StringVar()
    centre_examen=StringVar()
    president=StringVar()
    telephone=StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #region Label
    Label(reg_screen, text="region * ").place(x=20,y=40)
    #region textbox
    Entry(reg_screen, textvariable=region).place(x=90,y=42)
    #departement Label
    Label(reg_screen, text="departement * ").place(x=20,y=80)
    #departement textbox
    Entry(reg_screen, textvariable=departement).place(x=90,y=82)

    # localite Label
    Label(reg_screen, text="localite * ").place(x=20, y=120)
    # localite textbox
    Entry(reg_screen, textvariable=localite).place(x=90, y=122)

    # centre_examen Label
    Label(reg_screen, text="centre_examen * ").place(x=20, y=160)
    # centre_examen radiobutton
    # Radiobutton(reg_screen,text="Male",variable=centre_examen,value=1).place(x=90,y=162)
    # Radiobutton(reg_screen, text="Female", variable=centre_examen, value=2).place(x=150, y=162)
    Entry(reg_screen, textvariable=centre_examen).place(x=90, y=162)

    # president Label
    Label(reg_screen, text="president * ").place(x=20, y=200)
    # president combobox
    monthchoosen = ttk.Combobox(reg_screen, width=27, textvariable=president)
    monthchoosen['values'] = (' Mumbai',
                              ' Bhopal',
                              ' Patna',
                              ' Indore',
                              ' Nagpur',
                              ' Motihari',
                              ' Pune',
                              ' Gwalior',
                              ' Jabalpur',)
    monthchoosen.current()
    monthchoosen.place(x=90,y=202)

    # telephone Label
    Label(reg_screen, text="telephone * ").place(x=20, y=240)
    # telephone combobox
    monthchoosen = ttk.Combobox(reg_screen, width=27, textvariable=telephone)
    monthchoosen['values'] = (' Madhya Pradesh',
                              ' Maharashtra',
                              ' Bihar',
                              ' Punjab',
                              ' Gujrat',
                              ' Rajsthan',)
    monthchoosen.current()
    monthchoosen.place(x=90, y=242)
    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=95,y=264)
    #Login button
    Button(reg_screen, text="Register", width=10, height=1, bg="orange",command=register).place(x=105,y=300)
    reg_screen.mainloop()
#calling function Registrationform
Registrationform()