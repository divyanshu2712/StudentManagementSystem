from tkinter import *
from tkinter import messagebox,filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import ttkthemes
import pandas as pd
import datetime
import pymysql
# Connect Database
con=pymysql.connect(host='127.0.0.1',user='root',password='divyanshu')
mycursor=con.cursor()
# Creating Student table
query='use sms'
mycursor.execute(query)
# query='create table student(id int not null primary key,name varchar(30),mobile int,email varchar(30),address varchar(100),gender varchar(20),DOB varchar(20),Enrolldate varchar(50))'
# mycursor.execute(query)

# global
text = ''
count = 0
s = 'Student Management System'


def clock():
    dT = datetime.datetime.now()
    date = dT.strftime('%d/%m/%y')
    time = dT.strftime('%I:%M:%S')
    datelabel.config(text=f'Date : {date}')
    timelabel.config(text=f'Time: {time}')
    timelabel.after(1000, clock)

def export_stu():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=student_tab.get_children()
    export_list=[]
    for i in indexing:
        content_ex=student_tab.item(i)
        export_list.append(content_ex['values'])
    export_file=pd.DataFrame(export_list,columns=['Enrollment ID','Name','Class',"Father's Name",'Mobile No.','Email id','Address','Gender','Date of Birth','Enrollment Date'])
    export_file.to_csv(url,index=False)

def update_stu():
    indexing=student_tab.focus()
    content=student_tab.item(indexing)
    listdata_up=content['values']
    try:
        def update_data():
            query='update student set name=%s,class=%s,Fathername=%s,mobile=%s,email=%s,address=%s,gender=%s,DOB=%s,Enrolldate=%s where id=%s'
            mycursor.execute(query,(name_entry.get(),class_entry.get(),father_entry.get(),mobile_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),enrolldate_entry.get(),identry.get()))
            con.commit()
            messagebox.showinfo('Success','Data has been updated')
            update_window.destroy()
            show_stu()


        update_window=Toplevel()
        update_window.resizable(False,False)
        update_window.title('Update Student Data')
        update_window.iconbitmap(r'images\database-storage.ico')


        idLabel=Label(update_window,text='Enrollment No. :',font=('times new roman',15,'bold'))
        idLabel.grid(row=0,column=0,padx=10,pady=10)
        identry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        identry.grid(row=0,column=1,padx=10,pady=10)

        name_label=Label(update_window,text='Name :',font=('times new roman',15,'bold'))
        name_label.grid(row=1,column=0,padx=10,pady=10)
        name_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        name_entry.grid(row=1,column=1,padx=10,pady=10)

        class_label=Label(update_window,text='Class :',font=('times new roman',15,'bold'))
        class_label.grid(row=2,column=0,padx=10,pady=10)
        class_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        class_entry.grid(row=2,column=1,padx=10,pady=10)

        father_label=Label(update_window,text='Father Name :',font=('times new roman',15,'bold'))
        father_label.grid(row=3,column=0,padx=10,pady=10)
        father_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        father_entry.grid(row=3,column=1,padx=10,pady=10)

        mobile_Label=Label(update_window,text='Mobile No. :',font=('times new roman',15,'bold'))
        mobile_Label.grid(row=4,column=0,padx=10,pady=10)
        mobile_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        mobile_entry.grid(row=4,column=1,padx=10,pady=10)

        email_Label=Label(update_window,text='Email Id. :',font=('times new roman',15,'bold'))
        email_Label.grid(row=5,column=0,padx=10,pady=10)
        email_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        email_entry.grid(row=5,column=1,padx=10,pady=10)

        address_Label=Label(update_window,text='Address :',font=('times new roman',15,'bold'))
        address_Label.grid(row=6,column=0,padx=10,pady=10)
        address_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        address_entry.grid(row=6,column=1,padx=10,pady=10)

        gender_Label=Label(update_window,text='Gender :',font=('times new roman',15,'bold'))
        gender_Label.grid(row=7,column=0,padx=10,pady=10)
        gender_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        gender_entry.grid(row=7,column=1,padx=10,pady=10)

        dob_Label=Label(update_window,text='Date of Birth :',font=('times new roman',15,'bold'))
        dob_Label.grid(row=8,column=0,padx=10,pady=10)
        dob_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        dob_entry.grid(row=8,column=1,padx=10,pady=10)

        enrolldate_Label=Label(update_window,text='Enrollment Date :',font=('times new roman',15,'bold'))
        enrolldate_Label.grid(row=9,column=0,padx=10,pady=10)
        enrolldate_entry=Entry(update_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
        enrolldate_entry.grid(row=9,column=1,padx=10,pady=10)

        identry.insert(0,listdata_up[0])
        name_entry.insert(0,listdata_up[1])
        class_entry.insert(0,listdata_up[2])
        father_entry.insert(0,listdata_up[3])
        mobile_entry.insert(0,listdata_up[4])
        email_entry.insert(0,listdata_up[5])
        address_entry.insert(0,listdata_up[6])
        gender_entry.insert(0,listdata_up[7])
        dob_entry.insert(0,listdata_up[8])
        enrolldate_entry.insert(0,listdata_up[9])

        identry.config(state=DISABLED)

        update_btn=Button(update_window,text='Update Data',command=update_data,width=20)
        update_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10)

    except:
        messagebox.showerror('Error','Wrong values given')



def show_stu():
    query='select * from student'
    mycursor.execute(query)
    show_fetch=list(mycursor.fetchall())
    student_tab.delete(*student_tab.get_children())
    for i in show_fetch:
        student_tab.insert('',END,values=i)

def delete_stu():
    try:
        indexing=student_tab.focus()
        content=student_tab.item(indexing)
        contentid=content['values'][0]
        query='delete from student where id=%s'
        mycursor.execute(query,contentid)
        con.commit()
        query='select * from student'
        mycursor.execute(query)
        search_fetch=list(mycursor.fetchall())
        student_tab.delete(*student_tab.get_children())
        for i in search_fetch:
            student_tab.insert('',END,values=i)
    except:
        messagebox.showerror("Error","Please select a row to delete")
def search_stu():
    def search_data():
        if identry.get()=='' and name_entry.get()=='' and class_entry.get()=='' and father_entry.get()=='' and gender_entry.get()=='':    
            messagebox.showerror('Error','Please enter values')
        else:
            query='select * from student where id=%s or name=%s or class=%s or Fathername=%s or gender=%s'
            mycursor.execute(query,(identry.get(),name_entry.get(),class_entry.get(),father_entry.get(),gender_entry.get()))
        search_fetch=list(mycursor.fetchall())
        if search_fetch==[]:
            messagebox.showerror('Error','This student does not exist in database. Please add it.')
        student_tab.delete(*student_tab.get_children())
        for i in search_fetch:
            student_tab.insert('',END,values=i)
        identry.delete(0,END)
        name_entry.delete(0,END)
        class_entry.delete(0,END)
        father_entry.delete(0,END)
        gender_entry.delete(0,END)
    search_window=Toplevel()
    search_window.resizable(False,False)
    search_window.title("Search Student's")
    search_window.iconbitmap(r'images\database-storage.ico')

    idLabel=Label(search_window,text='Enrollment No. :',font=('times new roman',15,'bold'))
    idLabel.grid(row=0,column=0,padx=10,pady=10)
    identry=Entry(search_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    identry.grid(row=0,column=1,padx=10,pady=10)

    name_label=Label(search_window,text='Name :',font=('times new roman',15,'bold'))
    name_label.grid(row=1,column=0,padx=10,pady=10)
    name_entry=Entry(search_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    name_entry.grid(row=1,column=1,padx=10,pady=10)

    class_label=Label(search_window,text='Class :',font=('times new roman',15,'bold'))
    class_label.grid(row=2,column=0,padx=10,pady=10)
    class_entry=Entry(search_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    class_entry.grid(row=2,column=1,padx=10,pady=10)

    father_label=Label(search_window,text='Father Name :',font=('times new roman',15,'bold'))
    father_label.grid(row=3,column=0,padx=10,pady=10)
    father_entry=Entry(search_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    father_entry.grid(row=3,column=1,padx=10,pady=10)

    gender_Label=Label(search_window,text='Gender :',font=('times new roman',15,'bold'))
    gender_Label.grid(row=7,column=0,padx=10,pady=10)
    gender_entry=Entry(search_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    gender_entry.grid(row=7,column=1,padx=10,pady=10)

    search_btn=Button(search_window,text='Search Data',command=search_data,width=20)
    search_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10)

def add_stu():

    def add_data():
        try:
            if identry.get()=='' or name_entry.get()=='' or class_entry.get()=='' or mobile_entry.get()=='' or email_entry.get()=='' or address_entry.get()=='' or gender_entry.get()=='' or dob_entry.get()=='' or enrolldate_entry.get()==''or father_entry.get()=='' or class_entry.get()=='':
                messagebox.showerror('Error','Please enter data')
            else:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(identry.get(),name_entry.get(),class_entry.get(),father_entry.get(),mobile_entry.get(),email_entry.get(),address_entry.get(),gender_entry.get(),dob_entry.get(),enrolldate_entry.get()))
                con.commit()
                result=messagebox.askyesno('Success','Data has been added . \n Do you want to add more?..')
                if result:
                    identry.delete(0,END)
                    name_entry.delete(0,END)
                    class_entry.delete(0,END)
                    father_entry.delete(0,END)
                    mobile_entry.delete(0,END)
                    email_entry.delete(0,END)
                    address_entry.delete(0,END)
                    gender_entry.delete(0,END)
                    dob_entry.delete(0,END)
                    enrolldate_entry.delete(0,END)
                else:
                    add_window.destroy()
                query='select * from student'
                mycursor.execute(query)
                student_tab.delete(*student_tab.get_children())
                fetchdata=mycursor.fetchall()
                data_list=list(fetchdata)
                for i in data_list:
                    student_tab.insert('',END,values=i)
        except:
            messagebox.showerror("Error","Please Check the entered Values...")            
            
    add_window=Toplevel()
    add_window.resizable(False,False)
    add_window.title('Add Student Data')
    add_window.iconbitmap(r'images\database-storage.ico')

    idLabel=Label(add_window,text='Enrollment No. :',font=('times new roman',15,'bold'))
    idLabel.grid(row=0,column=0,padx=10,pady=10)
    identry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    identry.grid(row=0,column=1,padx=10,pady=10)

    name_label=Label(add_window,text='Name :',font=('times new roman',15,'bold'))
    name_label.grid(row=1,column=0,padx=10,pady=10)
    name_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    name_entry.grid(row=1,column=1,padx=10,pady=10)

    class_label=Label(add_window,text='Class :',font=('times new roman',15,'bold'))
    class_label.grid(row=2,column=0,padx=10,pady=10)
    class_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    class_entry.grid(row=2,column=1,padx=10,pady=10)

    father_label=Label(add_window,text='Father Name :',font=('times new roman',15,'bold'))
    father_label.grid(row=3,column=0,padx=10,pady=10)
    father_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    father_entry.grid(row=3,column=1,padx=10,pady=10)

    mobile_Label=Label(add_window,text='Mobile No. :',font=('times new roman',15,'bold'))
    mobile_Label.grid(row=4,column=0,padx=10,pady=10)
    mobile_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    mobile_entry.grid(row=4,column=1,padx=10,pady=10)

    email_Label=Label(add_window,text='Email Id. :',font=('times new roman',15,'bold'))
    email_Label.grid(row=5,column=0,padx=10,pady=10)
    email_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    email_entry.grid(row=5,column=1,padx=10,pady=10)

    address_Label=Label(add_window,text='Address :',font=('times new roman',15,'bold'))
    address_Label.grid(row=6,column=0,padx=10,pady=10)
    address_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    address_entry.grid(row=6,column=1,padx=10,pady=10)

    gender_Label=Label(add_window,text='Gender :',font=('times new roman',15,'bold'))
    gender_Label.grid(row=7,column=0,padx=10,pady=10)
    gender_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    gender_entry.grid(row=7,column=1,padx=10,pady=10)

    dob_Label=Label(add_window,text='Date of Birth :',font=('times new roman',15,'bold'))
    dob_Label.grid(row=8,column=0,padx=10,pady=10)
    dob_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    dob_entry.grid(row=8,column=1,padx=10,pady=10)

    enrolldate_Label=Label(add_window,text='Enrollment Date :',font=('times new roman',15,'bold'))
    enrolldate_Label.grid(row=9,column=0,padx=10,pady=10)
    enrolldate_entry=Entry(add_window,font=('times new roman',15),foreground='royalblue',bd=2,justify=CENTER)
    enrolldate_entry.grid(row=9,column=1,padx=10,pady=10)

    add_btn=Button(add_window,text='Add Data',command=add_data,width=20)
    add_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10)





def slider():
    global text, count, s
    if count == len(s):
        count = 0
        text = ''
    text = text+s[count]
    sliderLabel.config(text=text)
    count = count+1
    sliderLabel.after(150, slider)


def on_enter_add(e):
    add_student.config(background='lightgreen', foreground='black')


def on_leave_add(e):
    add_student.config(background='lightblue',foreground='black')

def on_enter_search(e):
    search_student.config(background='lightgreen', foreground='black')


def on_leave_search(e):
    search_student.config(background='lightblue',foreground='black')

def on_enter_update(e):
    update_student.config(background='lightgreen', foreground='black')


def on_leave_update(e):
    update_student.config(background='lightblue',foreground='black')

def on_enter_delete(e):
    delete_student.config(background='crimson', foreground='black')


def on_leave_delete(e):
    delete_student.config(background='lightblue',foreground='black')

def on_enter_export(e):
    export_data.config(background='lightgreen', foreground='black')


def on_leave_export(e):
    export_data.config(background='lightblue',foreground='black')

def on_enter_exit(e):
    exit_btn.config(background='crimson', foreground='black')


def on_leave_exit(e):
    exit_btn.config(background='lightblue',foreground='black')

def on_enter_show(e):
    show_student.config(background='lightgreen', foreground='black')


def on_leave_show(e):
    show_student.config(background='lightblue',foreground='black')


# Initializing
root = ttkthemes.ThemedTk()
root.set_theme('breeze')
# Setting Icon
root.iconbitmap(r"images\database-storage.ico")
# Setting Title
root.title("Student Management System")
# Set Geometry
root.geometry('1280x700+50+70')
# Set Resizable
root.resizable(False, False)
# background image load and show
bg1 = Image.open(r"images\bg.jpg")
bg_manage = ImageTk.PhotoImage(bg1)
bg = Label(root, image=bg_manage)
bg.place(x=0, y=0)
# Date Time Label
datelabel = Label(root, font=('times new roman', 18, 'bold'))
datelabel.place(x=10, y=10)
timelabel = Label(root, font=('times new roman', 18, 'bold'))
timelabel.place(x=10, y=50)
clock()
# Slider
sliderLabel = Label(root, font=('times new roman', 35, 'bold',
                    'italic'), foreground='royalblue', width=30)
sliderLabel.place(x=400, y=25)
slider()

# Left Frame
left = Frame(root, width=300, height=550, pady=10)
left.place(x=20, y=100)
logo_img = ImageTk.PhotoImage(
    file=r"images\profile.png")
logo = Label(left, image=logo_img)
logo.grid(row=0, column=0, pady=20)

add_student = Button(left, text='Add', background='lightblue', foreground='black', activebackground='white',
                     activeforeground='black', command=add_stu, width=20, height=1, font=('times new roman', 12))
add_student.grid(row=1, column=0, padx=50, pady=15)

search_student = Button(left, text='Search', background='lightblue', foreground='black', activebackground='white',
                        activeforeground='black', command=search_stu, width=20, height=1, font=('times new roman', 12))
search_student.grid(row=2, column=0, padx=50, pady=15)

delete_student = Button(left, text='Delete', background='lightblue', foreground='black', activebackground='white',
                        activeforeground='black', command=delete_stu, width=20, height=1, font=('times new roman', 12))
delete_student.grid(row=3, column=0, padx=50, pady=15)

update_student = Button(left, text='Update', background='lightblue', foreground='black', activebackground='white',
                        activeforeground='black', command=update_stu, width=20, height=1, font=('times new roman', 12))
update_student.grid(row=4, column=0, padx=50, pady=15)

show_student = Button(left, text='Show Student', background='lightblue', foreground='black', activebackground='white',
                      activeforeground='black', command=show_stu, width=20, height=1, font=('times new roman', 12))
show_student.grid(row=5, column=0, padx=50, pady=15)

export_data = Button(left, text='Export Data', background='lightblue', foreground='black', activebackground='white',
                     activeforeground='black', command=export_stu, width=20, height=1, font=('times new roman', 12))
export_data.grid(row=6, column=0, padx=50, pady=15)

exit_btn = Button(left, text='Exit', background='lightblue', foreground='black', activebackground='white',
                  activeforeground='black', command=root.destroy, width=20, height=1, font=('times new roman', 12))
exit_btn.grid(row=7, column=0, padx=50, pady=15)

# Right Frame
right=Frame(root)
right.place(x=350,y=100,width=900,height=570)

scroll_x=Scrollbar(right,orient=HORIZONTAL)
scroll_y=Scrollbar(right,orient=VERTICAL)

student_tab=ttk.Treeview(right,columns=('ID','Name','Class','Father Name','Mobile No.','Email id','Address','Gender','D.O.B','Enrollment Date'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
student_tab.pack(fill=BOTH,expand=TRUE)

scroll_x.config(command=student_tab.xview)
scroll_y.config(command=student_tab.yview)
# 'ID','Name','Class','Mobile No.','Email id','Address','Gender','D.O.B','Enrollment Date'
student_tab.heading('ID',text='Enrollment Id')
student_tab.heading('Name',text='Name')
student_tab.heading('Class',text='Class')
student_tab.heading('Father Name',text='Father Name')
student_tab.heading('Mobile No.',text='Mobile No.')
student_tab.heading('Email id',text='Email id')
student_tab.heading('Address',text='Address')
student_tab.heading('Gender',text='Gender')
student_tab.heading('D.O.B',text='Date of Birth')
student_tab.heading('Enrollment Date',text='Enrollement Date')


student_tab.column('ID',width=180,anchor=CENTER)
student_tab.column('Name',width=180,anchor=CENTER)
student_tab.column('Class',width=100,anchor=CENTER)
student_tab.column('Father Name',width=180,anchor=CENTER)
student_tab.column('Mobile No.',width=150,anchor=CENTER)
student_tab.column('Email id',width=150,anchor=CENTER)
student_tab.column('Address',width=400,anchor=CENTER)
student_tab.column('Gender',width=150,anchor=CENTER)
student_tab.column('D.O.B',width=180,anchor=CENTER)
student_tab.column('Enrollment Date',width=200,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('times new roman',15),foreground='royalblue',background='white')
style.configure('Treeview.Heading',font=('times new roman',17,'bold'))

student_tab.config(show='headings')





# Binding Button

add_student.bind("<Enter>", on_enter_add)
add_student.bind("<Leave>", on_leave_add)

search_student.bind("<Enter>", on_enter_search)
search_student.bind("<Leave>", on_leave_search)

update_student.bind("<Enter>", on_enter_update)
update_student.bind("<Leave>", on_leave_update)

export_data.bind("<Enter>", on_enter_export)
export_data.bind("<Leave>", on_leave_export)

exit_btn.bind("<Enter>", on_enter_exit)
exit_btn.bind("<Leave>", on_leave_exit)

show_student.bind("<Enter>", on_enter_show)
show_student.bind("<Leave>", on_leave_show)

delete_student.bind("<Enter>", on_enter_delete)
delete_student.bind("<Leave>", on_leave_delete)


root.mainloop()
