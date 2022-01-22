import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("1200x720") 
my_connect = mysql.connector.connect(
  host="localhost",
  user="phpmyadmin", 
  password="djarafat10",
  database="python_poo"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM jury")
i=1
e=Label(my_w,width=10,text='id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='Region',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='Departement',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='Localité',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
e=Label(my_w,width=10,text='Centre',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=4)
e=Label(my_w,width=10,text='President',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=5)
e=Label(my_w,width=10,text='Telephone',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=6)
for jury in my_conn: 
    for j in range(len(jury)):
        e = Label(my_w,width=10, text=jury[j], anchor='w',borderwidth=2) 
        e.grid(row=i, column=j) 
    i=i+1
my_w.mainloop()