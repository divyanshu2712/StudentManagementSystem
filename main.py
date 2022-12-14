from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
con=pymysql.connect(host='127.0.0.1',user='root',password='divyanshu')
mycursor=con.cursor()
# Creating database
# query='create database sms'
# mycursor.execute(query)
# query='create  table admin(Username varchar(10),Password varchar(10))'
# mycursor.execute(query)
# Connect Database

query='use sms'
mycursor.execute(query)
query='select * from admin'
mycursor.execute(query)
rows=mycursor.fetchall()
user__name=[]
pass__word=[]
for row in rows:
    user__name.append(row[0])
    pass__word.append(row[1])


# Login Function
def loginfunction() :
    if username_entry.get()=='' or ps_entry.get()=='':
        messagebox.showerror('Error','Feild cannot be empty')
    elif username_entry.get() in user__name and ps_entry.get()in pass__word:
        window.destroy()
        import management
    else:
        messagebox.showerror('Error','Please enter correct credentials')

#creating instance of tk class
window=Tk()
# giving title to the window 
window.title('Student Management System')
# specifying the window size
window.geometry('1280x700+50+70') 
# Setting Icon
window.iconbitmap(r"images\database-storage.ico")
# specifying that window size cannot be changed 
window.resizable(False,False)
# Adding Background Image
bg_org=Image.open(r"images\bg.jpg")
bg_org.resize((1600,900))
bg=ImageTk.PhotoImage(bg_org)
bglabel=Label(window,image=bg)
bglabel.place(x=0,y=0)



# Creating a login container(Frame) that is a container for various widgets
loginframe=Frame(window,padx=15,pady=15)
loginframe.place(x=380,y=185)
# Opening the Studnet login image Converting it to image for tkinter
login=Image.open(r"images\student_login.png")
login_ico=ImageTk.PhotoImage(login)
# making the label 
login_label_img=Label(loginframe,image=login_ico)
login_label_img.grid(row=0,column=0,columnspan=2)
# adding username text
user=ImageTk.PhotoImage(file=r"images\user.png")
usernamelabel=Label(loginframe,image=user,text="Username",font=('times new roman',20,'bold'),compound=LEFT) # compound shift image to left 
usernamelabel.grid(row=1,column=0,padx=10,pady=20)
username_entry=Entry(loginframe,font=('times new roman',20,'bold'),bd=5,foreground='royalblue',justify=CENTER)
username_entry.grid(row=1,column=1,padx=10,pady=20)
# making password text
password=ImageTk.PhotoImage(file=r"images\password.png")
pslabel=Label(loginframe,image=password,text="Password",font=('times new roman',20,'bold'),compound=LEFT) # compound shift image to left 
pslabel.grid(row=2,column=0,padx=10,pady=5)
ps_entry=Entry(loginframe,font=('times new roman',20,'bold'),bd=5,foreground='royalblue',justify=CENTER)
ps_entry.grid(row=2,column=1,padx=10,pady=5)
#making login button
loginbutton=Button(loginframe,text='Login',font=('times new roman',15),width=10,foreground='white',background='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=loginfunction)
loginbutton.grid(row=3,column=1,pady=10)

window.mainloop()