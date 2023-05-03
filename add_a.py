from subprocess import call
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter import font
import mysql.connector

#creating window
add_student_window = Tk()
add_student_window.geometry('500x300')
add_student_window.title('Add New Student')

#Define fontStyles
fontStyle_p = "arial 16 bold"
fontStyle_e = "arial 16"

#function of back button to move back to the previous page
def back():
    add_student_window.destroy()
    call(("python", "attendance.py"))
    
#creating back button
back_btn = Button(add_student_window, text="Home Page", command = lambda : back())
back_btn.configure(font=('arial', 12, 'bold'), bg='yellow', fg='black')
back_btn.grid(column=1, row=0)


#blank row  
blank = Label(add_student_window, text="").grid(column=0, row=1) 
#label of Enrollment no.
lbl1 = Label(add_student_window, text="Enrollment No. :", font=fontStyle_p)
lbl1.grid(column=0, row=2)
#Entry box for Enrollment no.
enroll = StringVar()
e_enroll = Entry(add_student_window, textvariable=enroll, font=fontStyle_e)
e_enroll.grid(column=1, row=2)

#blank row  
blank = Label(add_student_window, text="").grid(column=0, row=3) 
#label of student name
lbl2 = Label(add_student_window, text="Student Name   : ", font=fontStyle_p)
lbl2.grid(column=0, row=4)
#Entry box student name
name = StringVar()
e_name = Entry(add_student_window, textvariable=name, font=fontStyle_e)
e_name.grid(column=1, row=4)

#blank row  
blank = Label(add_student_window, text="").grid(column=0, row=5) 
#label of student roll no.
lbl3 = Label(add_student_window, text="Student Roll      : ", font=fontStyle_p)
lbl3.grid(column=0, row=6)
#Entry box student roll no.
roll = StringVar()
e_roll = Entry(add_student_window, textvariable=roll, font=fontStyle_e)
e_roll.grid(column=1, row=6)


#function of submit button to add new student into database
def submit_student():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="attendance"
            )
    mycursor = mydb.cursor()
    sql = "INSERT INTO bTech_a (sEnroll, sName, sRoll) VALUES (%s, %s, %s)"
    val = (enroll.get(), name.get(), roll.get())
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

    messagebox.showinfo("Student Added", "Student added successfully!")

#blank row  
blank = Label(add_student_window, text="").grid(column=0, row=7) 
#creating submit button
submit_btn = Button(add_student_window, text="Submit", command = lambda : submit_student())
submit_btn.configure(font=('arial', 14, 'bold'), bg='blue', fg='white')
submit_btn.grid(column=1, row=8)


add_student_window.mainloop()
    