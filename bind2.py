import tkinter
from tkinter import messagebox
#from PIL import Image,ImageTk


def login1():
    user = usr.get()
    psd = pwd.get()
    rpsd = rpwd.get()

    if user == "":
        messagebox.showinfo("Error","Please Enter Username")
    elif psd == "":
        messagebox.showinfo("Error","Please Enter Password")
    elif rpwd == "":
        messagebox.showinfo("Error","Please Enter Password")
    elif psd !=rpsd:
        messagebox.showinfo("Error","Please enter same password")
    else:
        messagebox.showinfo("SUCESS","Account created successfully")

def reg():

    frm1 = tkinter.Frame(obj,width=900,height=500)
    frm1.place(x=0,y=0)
    tkinter.Label(frm1,image=img1,bg="blue").place(x=0,y=0)
    

    
    
    '''= tkinter.Frame(obj,width=500,height=415)
    frame1.place(x=350,y=55)'''
    lable1=tkinter.Label(frm1,text="Registration",fg="#050905",bg="#7CADD9",font=("Mongolian Baiti",29))
    lable1.place(x=390,y=38)

    lable2 = tkinter.Label(frm1,text="Moblie no.:",fg="#020202",bg="#A99AA0",font=("Times New Roman",15,"bold"))
    lable2.place(x=300,y=130)
    mob = tkinter.Entry(frm1,width=25,border=1,fg="#161A3D",bg="white",font=("Times New Roman",14,"bold"))
    mob.place(x=420,y=130)
    mob.insert(1,"")

    lable3 = tkinter.Label(frm1,text="Username:",fg="#020202",bg="#A99AA0",font=("Times New Roman",15,"bold"))
    lable3.place(x=300,y=180)
    global usr
    usr = tkinter.Entry(frm1,width=25,border=1,fg="#161A3D",bg="white",font=("Times New Roman",14,"bold"))
    usr.place(x=420,y=180)

    lable4 = tkinter.Label(frm1,text="Password:",fg="#020202",bg="#A99AA0",font=("Times New Roman",15,"bold"))
    lable4.place(x=300,y=230)
    global pwd 
    pwd = tkinter.Entry(frm1,show="x",width=25,border=1,fg="#161A3D",bg="white",font=("Times New Roman",14,"bold"))
    pwd.place(x=420,y=230)

    lable5 = tkinter.Label(frm1,text="Re-Password:",fg="#020202",bg="#A99AA0",font=("Times New Roman",15,"bold"))
    lable5.place(x=280,y=280)
    global rpwd
    rpwd = tkinter.Entry(frm1,show="x",width=25,border=1,fg="#161A3D",bg="white",font=("Times New Roman",14,"bold"))
    rpwd.place(x=420,y=280)

    lable5 = tkinter.Label(frm1,text="E-mail:",fg="#020202",bg="#A99AA0",font=("Times New Roman",15,"bold"))
    lable5.place(x=310,y=330)
    mail = tkinter.Entry(frm1,width=25,border=1,fg="#161A3D",bg="white",font=("Times New Roman",14,"bold"))
    mail.place(x=420,y=330)

     
    tkinter.Button(frm1, image=sub,command=login1,bg="black",border=0).place(x=310,y=410)
 
    tkinter.Button(frm1,image=can,command=frm1.destroy,bg="black",border=0).place(x=480,y=410)


def login():
    user = usr.get()
    pswd = pwd.get()
    
    if user == "admin" and pswd == "admin@123":
        messagebox.showinfo("Success","Welcome Admin")
    elif user == "":
        messagebox.showinfo("Error","Please Enter Username")
    elif pswd == "":
        messagebox.showinfo("Error","Please Enter Password")
    else:
        messagebox.showinfo("Error","Please Enter Valid Username/Password")


def login2():
    frm = tkinter.Frame(obj,width=900,height=500)
    frm.place(x=0,y=0)

    tkinter.Label(frm,image=img,bg="white").place(x=0,y=0)

    frame1 = tkinter.Frame(frm,width=350,height=350,bg="#57a1f8")
    frame1.place(x=480,y=70)
    lable1 = tkinter.Label(frame1,text="Login",fg="white",bg="#57a1f8",font=("Times New Roman",25,"bold"))
    lable1.place(x=100,y=5)

    lable2 = tkinter.Label(frame1,text="Username",fg="white",bg="#57a1f8",font=("Times New Roman",15,"bold"))
    lable2.place(x=50,y=70)
    global usr 
    usr = tkinter.Entry(frame1,width=25,border=1,fg="#161A3D",bg="white",font=("Times New Roman",12,"bold"))
    usr.place(x=50,y=100)
    usr.insert(1,"")

    lable3 = tkinter.Label(frame1,text="Password",fg="white",bg="#57a1f8",font=("Times New Roman",15,"bold"))
    lable3.place(x=50,y=140)
    global pwd
    pwd = tkinter.Entry(frame1,show="*",width=25,border=1,fg="#161A3D",bg="white",font=("Times New Roman",12))
    pwd.place(x=50,y=170)
    pwd.insert(1,"")

    tkinter.Button(frame1,text = "Login",command=login,border=0,fg="#57a1f8",bg="white",font=("Times New Roman",15,"bold")).place(x=60,y=220)
    tkinter.Button(frame1,text = "Cancel",command=obj.destroy,border=0,fg="#57a1f8",bg="white",font=("Times New Roman",15,"bold")).place(x=170,y=220)
    tkinter.Button(frame1,text = "Register",command=reg,border=0,fg="#57a1f8",bg="white",font=("Times New Roman",15,"bold")).place(x=101,y=280)

obj = tkinter.Tk()
obj.title("Login")
obj.geometry("900x500+250+170")
obj.resizable(False,False)
img = tkinter.PhotoImage(file="images//img3.png")
img1 = tkinter.PhotoImage(file="images//reg1.png")
sub =tkinter.PhotoImage(file="images//submit1.png")
can =tkinter.PhotoImage(file="images//cancel1.png")
obj.iconphoto(False,img)
login2()
obj.mainloop()




