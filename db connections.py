from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector



def saveData():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="trisha@123",
        database="customerdata"
    )
    if(usernameEntry.get()==''or emailEntry.get()=='' or passwordEntry.get()==''):
        messagebox.showerror('error',"all fields are mandatory!")
    else:
      mycur = conn.cursor()
    query="insert into studentreg(username,email,password)values(%s,%s,%s);"
    data = (usernameEntry.get(), emailEntry.get(), passwordEntry.get())
    mycur.execute(query, data)
    messagebox.showinfo("Success", "Data saved successfully!")
    conn.commit()

window = Tk()
background = ImageTk.PhotoImage(file='cartoon.jpg')
blabel = Label(window,image=background)
blabel.grid()
frame  = Frame(window)
frame.place(x=600,y=100)

usernameLabel = Label(frame, text="username",font=('Arial',15,'bold'),bg='white',fg='firebrick')
usernameLabel.grid(row=0, column=0)

usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)

emailLabel = Label(frame, text="email",font=('Arial',15,'bold'),bg='white',fg='firebrick')
emailLabel.grid(row=2, column=0)
emailEntry = Entry(frame, width=30)
emailEntry.grid(row=2, column=1)

passwordLabel = Label(frame, text="password",font=('Arial',15,'bold'),bg='white',fg='firebrick')
passwordLabel.grid(row=1, column=0)
passwordEntry = Entry(frame, width=30)
passwordEntry.grid(row=1, column=1)

submit_button = Button(window, text="Save", command=saveData)
submit_button.grid(row=4,column=1)


window.mainloop()
















#emailLabel = Label(frame,text="email")
#emailLabel.grid(row=1,column=0)
#emailEntry = Entry(frame,width=30)
#emailEntry.grid(row=1,column=1)


#window.mainloop()