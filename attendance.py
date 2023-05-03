import calendar
from subprocess import call
from tkcalendar import DateEntry
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import mysql.connector as mysql

root = Tk()
root.title("Home")
root.geometry('550x420')
root.iconbitmap("OIP.jpeg")
        
def insert():
    branch = e_branch.get()
    division = e_division.get()
    subject = e_subject.get()
    
    if(branch=="B.Tech" and division=="A" and subject=="Python"):
        root.destroy()
        call(["python", "a_python.py"])
    elif(branch=="B.Tech" and division=="A" and subject=="Java"):
        root.destroy()
        call(["python", "a_java.py"])
        
    elif(branch=="M.Tech" and division=="O" and subject=="Python"):
        root.destroy()
        call(["python", "o_python.py"]) 
    elif(branch=="M.Tech" and division=="O" and subject=="Java"):
        root.destroy()
        call(["python", "o_java.py"]) 
    else:
        messagebox.showinfo("Alert", "Please select right choices!") 


fontStyle_h = "arial 20 bold underline"
fontStyle_p = "arial 14 bold"

img_s = Image.open("OIP.jpeg")
img_s = img_s.resize((250,150))
img = ImageTk.PhotoImage(img_s)
lable = Label(image = img).grid(column=1,row=0)

l1 = Label(root, text="Student Attendence", font=fontStyle_h).grid(column=1, row=1)
blank = Label(root, text="").grid(column=0, row=2)   
   
#Label's  
branch = Label(root, text="Select Branch: ", font=fontStyle_p)
branch.grid(column=0, row=3)
division = Label(root, text="Select Division: ", font=fontStyle_p)
division.grid(column=0, row=5)
subject = Label(root, text="Select Subject: ", font=fontStyle_p)
subject.grid(column=0, row=4)

#Entry's
e_branch = StringVar(root)
e_branch.set("Select Branch") # default value
w = OptionMenu(root, e_branch, "B.Tech", "M.Tech")
w.configure(font=('arial', 12))
w.grid(column=1, row=3)
e_division = StringVar(root)
e_division.set("Select Division") # default value
w1 = OptionMenu(root, e_division, "A", "O")
w1.configure(font=('arial', 12))
w1.grid(column=1, row=5)
e_subject = StringVar(root)
e_subject.set("Select Subject") # default value
w = OptionMenu(root, e_subject, "Python", "Java")
w.configure(font=('arial', 12))
w.grid(column=1, row=4)

blank = Label(root, text="").grid(column=1, row=6)   
insert = Button(root, text="Attendance", command =insert, font="arial 12 bold")
insert.configure(font=('arial', 16, 'bold'))
insert.grid(column=1, row=7)


root.mainloop()