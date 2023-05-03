import calendar
import tkinter
import mysql.connector
from tkinter import *
from subprocess import call
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import font


root = Tk()
root.title("O (Java)")
root.geometry('550x600')
root.iconbitmap("OIP.jpeg")
        
#Define fontStyles
fontStyle_h = "arial 15 bold underline"
fontStyle_p = "arial 14 bold"
fontStyle_d = "arial 13"
fontStyle_t = "arial 13 bold"
fontStyle_p1 = "arial 10"

#Attached image
img_s = Image.open("OIP.jpeg")
img_s = img_s.resize((180,100))
img = ImageTk.PhotoImage(img_s)
lable = Label(image = img).grid(column=1,row=0)

#label header
l1 = Label(root, text="CLASS ATTENDANCE", font=fontStyle_h).grid(column=1, row=1)
blank = Label(root, text="").grid(column=1, row=2)   
 
#function for go home  
def home():
    root.destroy()
    call(["python", "attendance.py"])
#Go back home screen button
home = Button(root, text="Home Page", command=home)
home.configure(font=('arial', 11, 'bold'), bg='yellow', fg='black')
home.grid(row=3, column=1)

#blank row  
blank = Label(root, text="").grid(column=0, row=4) 
   
#Label for date
date = Label(root, text="Select Date: ", font=fontStyle_p)
date.grid(column=0, row=5)

#Entry of date
e_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, font=fontStyle_d)
e_date.grid(column=1, row=5)

#blank row  
blank = Label(root, text="").grid(column=3, row=6) 

#ttk labels for student attendance table header
ttk.Label(root, text="Enrollment No. ", background="green", foreground="white", font=fontStyle_t).grid(row=7, column=0, sticky="nsew")
ttk.Label(root, text="Name", background="green", foreground="white", font=fontStyle_t).grid(row=7, column=1, sticky="nsew")
ttk.Label(root, text="Roll No.", background="green", foreground="white", font=fontStyle_t).grid(row=7, column=2, sticky="nsew")
ttk.Label(root, text="Status", background="green", foreground="white", font=fontStyle_t).grid(row=7, column=3, sticky="nsew")
ttk.Label(root, text="", background="green", foreground="white").grid(row=7, column=4, sticky="nsew")

#connect database to fetch record
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="attendance"
    )
mycursor = mydb.cursor()
query = "SELECT * FROM mTech_o"
mycursor.execute(query)
records = mycursor.fetchall()
var = []
for i, attendance in enumerate(records):
    sEnroll, sName, sRoll = attendance
    var.append(StringVar())
    var[i].set('Present')
    ttk.Label(root, text=sEnroll, font=fontStyle_p1).grid(row=i+8, column=0, sticky="nsew")
    ttk.Label(root, text=sName, font=fontStyle_p1).grid(row=i+8, column=1, sticky="nsew")
    ttk.Label(root, text=sRoll, font=fontStyle_p1).grid(row=i+8, column=2, sticky="nsew")   
    present = ttk.Radiobutton(root, text="Present", variable=var[i], value="Present")
    present.grid(row=i+8, column=3, sticky="nsew")
    absent = ttk.Radiobutton(root, text="Absent", variable=var[i], value="Absent")
    absent.grid(row=i+8, column=4, sticky="nsew")


#function for the submit button to save records in the database
def submit_attendance():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="attendance")
    mycursor = mydb.cursor()
    for i, attendance in enumerate(records):
        sEnroll, sName, sRoll = attendance
        query = "INSERT INTO o_java (date, sEnroll, sName, sRoll, status) VALUES (%s, %s, %s, %s, %s)"
        values = (e_date.get(), sEnroll, sName, sRoll, var[i].get())
        mycursor.execute(query, values)
        mydb.commit()
    
    messagebox.showinfo("Success", "Attendance Submitted Successfully")
    root.destroy()
    call(["python", "attendance.py"])
 
#Submit attendance data button
submit = Button(root, text="Submit Attendance", command=submit_attendance)
submit.configure(font=('arial', 14, 'bold'), bg='blue', fg='white')
submit.grid(row=60, column=1)

#blank row  
blank = Label(root, text="").grid(column=0, row=61)  


#function of add new student
def add_student():
    root.destroy()
    call(["python", "add_o.py"])   
    
#add new student button
insert = Button(root, text="Add Student", command=add_student)
insert.configure(font=('arial', 13, 'bold'), bg='green', fg='white')
insert.grid(row=62, column=1)


#function of remove existing student
def remove_student():
    call(["python", "rm_o.py"])  
    
#remove existing button
remove = Button(root, text="Remove Student", command=remove_student)
remove.configure(font=('arial', 13, 'bold'), bg='red', fg='white')
remove.grid(row=62, column=0)

#run code in GUI
root.mainloop()