from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#ecf0f8")
        
        #---ALL VARIABLES
        #for frame 1
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        #for frame 2
        self.search_by_var=StringVar()
        self.search_entry_var=StringVar()

        title=Label(self.root, text="St. Joseph's Convent School",font=("trebuchet ms",40),fg="white",bg="#0369ac")
        title.pack(side=TOP, fill=X)
        self.img=ImageTk.PhotoImage(file="images/school.png")
        img_lbl=Label(self.root, image=self.img)
        img_lbl.place(x=0,y=0, height=75)

        #frame 1
        manage_frame=Frame(self.root, bg="#454849")
        manage_frame.place(x=15,y=90, width=450, height=580)
        
        m_title=Label(manage_frame, text="Manage Students",font=("trebuchet ms",30),fg="white",bg="#454849")
        m_title.grid(row=0, columnspan=2, pady=20, padx=90)

        roll=Label(manage_frame, text="Roll Number :",font=("trebuchet ms",15),fg="white",bg="#454849")
        roll.place(x=5,y=100)

        roll_entry=Entry(manage_frame,textvariable=self.roll_var,font=("trebuchet ms",15))
        roll_entry.place(x=145, y=100, width=268)

        name=Label(manage_frame, text="Name :",font=("trebuchet ms",15),fg="white",bg="#454849")
        name.place(x=5,y=150)

        name_entry=Entry(manage_frame,textvariable=self.name_var,font=("trebuchet ms",15))
        name_entry.place(x=145, y=150, width=268)

        email=Label(manage_frame, text="Email id :",font=("trebuchet ms",15),fg="white",bg="#454849")
        email.place(x=5,y=200)

        email_entry=Entry(manage_frame,textvariable=self.email_var,font=("trebuchet ms",15))
        email_entry.place(x=145, y=200, width=268)

        gender=Label(manage_frame, text="Gender :",font=("trebuchet ms",15),fg="white",bg="#454849")
        gender.place(x=5,y=250)

        gender_entry=ttk.Combobox(manage_frame,font=("trebuchet ms",15), textvariable=self.gender_var,state="readonly", justify=CENTER)
        gender_entry['values']=('Select Gender','male', 'female', 'other')
        gender_entry.current(0)
        gender_entry.place(x=145, y=250, width=268)

        contact=Label(manage_frame, text="Contact :",font=("trebuchet ms",15),fg="white",bg="#454849")
        contact.place(x=5,y=300)

        contact_entry=Entry(manage_frame,textvariable=self.contact_var,font=("trebuchet ms",15))
        contact_entry.place(x=145, y=300, width=268)

        dob=Label(manage_frame, text="D. O. B. :",font=("trebuchet ms",15),fg="white",bg="#454849")
        dob.place(x=5,y=350)

        dob_entry=Entry(manage_frame,textvariable=self.dob_var,font=("trebuchet ms",15))
        dob_entry.place(x=145, y=350, width=268)

        address=Label(manage_frame, text="Address :",font=("trebuchet ms",15),fg="white",bg="#454849")
        address.place(x=5,y=400)

        self.address_entry=Text(manage_frame, font=("trebuchet ms",15))
        self.address_entry.place(x=145, y=400,width=268, height=80)

        #Button frame
        btn_frame=Frame(manage_frame, bg="#454849", bd=4, relief=RAISED)
        btn_frame.place(x=0,y=490, width=550, height=580)

        add_btn=Button(btn_frame,command=self.add_students, text="Add",bd=1,font=("trebuchet ms",15),cursor="hand2",activebackground="black",fg="white",bg="black") 
        add_btn.place(x=20, y=20)

        update_btn=Button(btn_frame,command=self.update_data, text="Update",bd=1,font=("trebuchet ms",15),cursor="hand2",activebackground="black",fg="white",bg="black") 
        update_btn.place(x=105, y=20)

        delete_btn=Button(btn_frame,command=self.delete_data, text="Delete",bd=1,font=("trebuchet ms",15),cursor="hand2",fg="white",activebackground="black",bg="black") 
        delete_btn.place(x=225, y=20)

        clear_btn=Button(btn_frame,command=self.clear_data, text="Clear",bd=1,font=("trebuchet ms",15),cursor="hand2",activebackground="black",fg="white",bg="black") 
        clear_btn.place(x=340, y=20)
        


        #frame 2
        detail_frame=Frame(self.root, bg="#cfe5ec")
        detail_frame.place(x=450,y=90, width=880, height=580)

        search=Label(detail_frame, text="Search By :",font=("trebuchet ms",25),fg="black",bg="#cfe5ec")
        search.place(x=5,y=5)
        
        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by_var,font=("trebuchet ms",15), state="readonly", justify=CENTER)
        combo_search['values']=('roll_no', 'name', 'contact')
        combo_search.current(0)
        combo_search.place(x=180, y=18, width=150)
         
        search_entry=Entry(detail_frame,textvariable=self.search_entry_var,font=("trebuchet ms",15))
        search_entry.place(x=350, y=18, width=170)

        search_btn=Button(detail_frame,command=self.search_data, text="Search",bd=1,font=("trebuchet ms",15),cursor="hand2",fg="white",activebackground="black",bg="black") 
        search_btn.place(x=550, y=10, width=100)


        show_btn=Button(detail_frame,command=self.fetch_data, text="Show All",bd=1,font=("trebuchet ms",15),cursor="hand2",fg="white",activebackground="black",bg="black") 
        show_btn.place(x=690, y=10, width=120)


        #Table frame in detail frame
        table_frame=Frame(detail_frame,bd=10, bg="#cfe5ec")
        table_frame.place(x=2,y=65, width=880, height=520)

        scroll_x=Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, columns=('roll', 'name','email', 'gender','contact','dob',   'address'), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,  fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email id")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D. O. B.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'

        self.student_table.column("roll", width=50)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=140)
        self.student_table.column("contact", width=50)
        self.student_table.column("dob", width=50)
        self.student_table.column("gender", width=50)
        self.student_table.column("address", width=120)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor_data)
        self.fetch_data()



    def add_students(self):
        conn=pymysql.connect("localhost", "root", "", "student_mgmnt", port=3307)
        my_cursor=conn.cursor()
        my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s)",(self.roll_var.get(), 
        self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(),
        self.dob_var.get(), self.address_entry.get('1.0', END)))
        conn.commit()
        self.fetch_data()
        self.clear_data()
        conn.close()


    def fetch_data(self):
        conn=pymysql.connect("localhost", "root", "", "student_mgmnt", port=3307)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def clear_data(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.dob_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.address_entry.delete("1.0",END)


    def get_cursor_data(self, event):      #data pr cursor touch krne se frame 1 me display ho jaaye
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']

        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.address_entry.delete("1.0",END)
        self.address_entry.insert(END,row[6])
     
    def update_data(self):
        conn=pymysql.connect("localhost", "root", "", "student_mgmnt", port=3307)
        my_cursor=conn.cursor()
        my_cursor.execute("update student set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll_no=%s",( 
                                                        self.name_var.get(), 
                                                        self.email_var.get(), 
                                                        self.gender_var.get(), 
                                                        self.contact_var.get(),
                                                        self.dob_var.get(), 
                                                        self.address_entry.get('1.0', END),
                                                        self.roll_var.get()))
        conn.commit()
        self.fetch_data()
        self.clear_data()
        conn.close()

    def delete_data(self):
        conn=pymysql.connect("localhost", "root", "", "student_mgmnt", port=3307)
        my_cursor=conn.cursor()
        my_cursor.execute("delete from student where roll_no=%s", self.roll_var.get())
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear_data()

    def search_data(self):
        conn=pymysql.connect("localhost", "root", "", "student_mgmnt", port=3307)
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student where "+str(self.search_by_var.get())+" LIKE '%' " +str(self.search_entry_var.get())+"'%'") 
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
            conn.commit()
        conn.close()


root=Tk()
obj=Student(root)
root.mainloop()