from subprocess import call
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter import font
import mysql.connector

#defining functions
#creating window
root = Tk()
root.geometry("600x100")
root.title("Remove Student")

#Define fontStyles
fontStyle_p = "arial 16 bold"
fontStyle_e = "arial 16"

#label of Enrollment no.
lbl1 = Label(root, text="Enter Enrollment No. :", font=fontStyle_p)
lbl1.grid(column=0, row=0)
#Entry box for Enrollment no.
enroll = StringVar()
e_enroll = Entry(root, textvariable=enroll, font=fontStyle_e)
e_enroll.grid(column=1, row=0)


#funtion to remove student from the database
def remove():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="attendance"
        )
    mycursor = mydb.cursor()
    query = "DELETE FROM mTech_o WHERE sEnroll=%s"
    sEnroll = enroll.get()
    values = (sEnroll,)
    mycursor.execute(query, values)
    mydb.commit()
    messagebox.showinfo("Student Removed", "Student Removed Successfully!")
    root.destroy()

#blank row  
blank = Label(root, text="").grid(column=0, row=3) 
#student remove button
submit = Button(root, text="Remove Student", command=lambda:remove())
submit.configure(font=('arial', 14, 'bold'), bg='red', fg='white')
submit.grid(column=1, row=4) 
    
root.mainloop()
    
    
