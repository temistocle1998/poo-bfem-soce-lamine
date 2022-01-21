import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

from DB import DB

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e0.insert(0,select['id'])
    e1.insert(0,select['numero_table'])
    e2.insert(0,select['prenom_s'])
    e3.insert(0,select['nom'])
    e4.insert(0,select['date_naissance'])
    e5.insert(0,select['lieu_naissance'])
    e6.insert(0,select['sexe'])
    e7.insert(0,select['nationalite'])
    e8.insert(0,select['choix_epr_facultative'])
    e9.insert(0,select['epreuve_facultative'])
    e10.insert(0,select['aptitude_sportive'])


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    see = e5.get()
    tee = e6.get()
    lee = e7.get()
    dee = e8.get()
    ree = e9.get()
    vee = e10.get()
    mysqldb=mysql.connector.connect(host="localhost",user="phpmyadmin",password="djarafat10",database="python_poo")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  candidat (numero_table, prenom_s, nom, date_naissance, lieu_naissance, sexe, nationalite, choix_epr_facultative, epreuve_facultative, aptitude_sportive) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
       val = (studid,studname,coursename,feee, see, tee, lee, dee, ree, vee)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Candidat enregistré...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e8.delete(0, END)
       e9.delete(0, END)
       e10.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


def update():
    id= e0.get()
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    see=e5.get()
    tee=e6.get()
    lee=e7.get()
    dee=e8.get()
    ree=e9.get()
    vee=e10.get()
    mysqldb=mysql.connector.connect(host="localhost",user="phpmyadmin",password="djarafat10",database="python_poo")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  candidat set numero_table=%s, prenom_s=%s, nom=%s, date_naissance=%s, lieu_naissance=%s, sexe=%s, nationalite=%s, choix_epr_facultative=%s, epreuve_facultative=%s, aptitude_sportive=%s where id = %s"
       val = (studid,studname,coursename,feee, see, tee, lee, dee, ree, vee, id)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Candidat à jour...")
       print(lastid)
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    id = e0.get()

    mysqldb=mysql.connector.connect(host="localhost",user="phpmyadmin",password="djarafat10",database="python_poo")
    mycursor=mysqldb.cursor()

    try:
       sql = "DELETE FROM `candidat` WHERE id= ?"
       val = (id)
       mycursor.execute(sql, (id,))
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Candidat supprimé ...")
       print(val)
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e8.delete(0, END)
       e9.delete(0, END)
       e10.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="phpmyadmin", password="djarafat10", database="python_poo")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id, numero_table,prenom_s,nom,date_naissance, lieu_naissance, sexe, nationalite, choix_epr_facultative, epreuve_facultative, aptitude_sportive FROM candidat")
        records = mycursor.fetchall()
        print(records)

        for i, (id,stname, course,fee, three, elem, epr, apt, fac, test, sec) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, stname, course, fee, three, elem, epr, apt, fac, test, sec))
            mysqldb.close()

root = Tk()
root.geometry("1200x760")
global e0
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8

tk.Label(root, text="Candidat", fg="red", font=(None, 30)).place(x=400, y=5)
Label(root, text="Numero_table").grid(row = 1,column = 0)
Label(root, text="prenom").grid(row = 2,column = 0)
Label(root, text="nom").grid(row = 3,column = 0)
Label(root, text="date de naissance").grid(row = 4,column = 0)
Label(root, text="lieu de naissance").grid(row = 5,column = 0)
Label(root, text="nationalite").grid(row = 6,column = 0)
Label(root, text="sexe").grid(row = 7,column = 0)
Label(root, text="choix epreuve").grid(row = 8,column = 0)
Label(root, text="epreuve fac").grid(row = 9,column = 0)
Label(root, text="aptitude").grid(row = 10,column = 0)

e0 = Entry(root)
e0.grid(row = 1,column = 1)

e1 = Entry(root)
e1.grid(row = 1,column = 1)

e2 = Entry(root)
e2.grid(row = 2,column = 1)

e3 = Entry(root)
e3.grid(row = 3,column = 1)

e4 = Entry(root)
e4.grid(row = 4,column = 1)
e5 = Entry(root)

e5.grid(row = 5,column = 1)

e6 = Entry(root)
e6.grid(row = 6,column = 1)

e7 = Entry(root)
e7.grid(row = 7,column = 1)
e8 = Entry(root)

e8.grid(row = 8,column = 1)
e9 = Entry(root)

e9.grid(row = 9,column = 1)

e10 = Entry(root)

e10.grid(row = 10,column = 1)

Button(root, text="ajout",command = Add,height=3, width= 13).grid(row = 11,column = 1)
Button(root, text="modifier",command = update,height=3, width= 13).grid(row = 11,column = 2)
Button(root, text="supprimer",command = delete,height=3, width= 13).grid(row = 11,column = 3)

cols = ('id','numero_table', 'prenom_s', 'nom','date_naissance', 'lieu_naissance', 'sexe', 'nationalite', 'choix_epr_facultative', 'epreuve_facultative', 'aptitude_sportive')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=12, column=0, columnspan=1)
    listBox.place(x=10, y=400)
show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()
