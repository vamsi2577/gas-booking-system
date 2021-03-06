from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from booknow import *
from view import *
 
#Database name and password
mypass="python"
mydatabase="vamsi"

# Enter Table Names here
cusTable = "cusdetails" #customer

root = Tk()
root.title("LPG BOOKING")
root.minsize(width=400,height=400)
root.geometry("600x500")
count = 0
empFrameCount = 0

con= pymysql.connect(host="localhost",user="pjdata",password=mypass,database=mydatabase)
cur= con.cursor()
def close_window():
    root.destroy()

def cusMenu():
    
    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,btn1,btn2,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#dff9fb",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="LPG BOOKING SYSTEM", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="BOOK LPG",bg='black', fg='white',command=booking)
    btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="PAST BOOKINGS",bg='black', fg='white',command=searchBook)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="<  BACK",bg='#455A64', fg='white', command=back)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def back():
    btn1.destroy()
    backBtn.destroy()
    Login()

    
#deals with customer login checks password and customerid
def gettingLoginDetails():
    login =en1.get()
    password =en2.get()

    sqlLoginID= "select custid from "+cusTable+" where password ='"+password+"'"
    try:
        cur.execute(sqlLoginID)
        for i in cur:
            getLoginID = i[0]

        if(getLoginID == login):
            cusMenu()
            messagebox.showinfo("SUCCESS","you have successfully loged in")
        else:
            messagebox.showerror("Failure","can't log in, check your credentials")
    except:
        messagebox.showinfo("FAILED","Please check your credentials")

    print(login)
    print(password)
    en1.delete(0, END)
    en2.delete(0, END)
    
    
#deals with storing of customer details in data base
def gettingCusDetails():
    custid =en1.get()
    cusname =en2.get()
    password= en3.get()
    address= en4.get()
    mobnum= en5.get()

    try:
        if (type(int(custid)) == int):
            pass
        else:
            messagebox.showinfo("Invail Value","Customer ID should be an integer")
            return
    except:
        messagebox.showinfo("Invalid value","Customer ID should be an integer")
        return

    
        
   
    sql = "insert into "+cusTable+" values ('"+custid+"','"+cusname+"','"+password+"','"+address+"','"+mobnum+"')"
    try:
        cur.execute(sql)
        con.commit()
        messagebox.showinfo("SUCCESS","you have successfully registered")
    except:
        messagebox.showinfo("Error inserting","cannot add data to Database")
    print(custid)
    print(cusname)
    print(password)
    print(address)
    print(mobnum)
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)

# register home page
def Register():
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,en5
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)
    
    # customer ID
    lb1 = Label(labelFrame,text="customer ID : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.05)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.35,rely=0.05, relwidth=0.62)
    
    #customer Name
    lb2 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.2)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.35,rely=0.2, relwidth=0.62)
    
    #customer Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.35)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.35,rely=0.35, relwidth=0.62)
    
    #customer adress
    lb4 = Label(labelFrame,text="address : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05,rely=0.5)
    
    en4 = Entry(labelFrame)
    en4.place(relx=0.35,rely=0.5, relwidth=0.62,)
    
   
    
    # customer moblie number
    lb5 = Label(labelFrame,text="mobile number : ", bg='#044F67', fg='white')
    lb5.place(relx=0.05,rely=0.8)
    
    en5 = Entry(labelFrame)
    en5.place(relx=0.35,rely=0.8, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingCusDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)


#login home page
def Login():
    
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,SubmitBtn,btn1,btn2,backBtn
    
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)
    
    # Login ID
    lb1 = Label(labelFrame,text="Login ID : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.1)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)
    
    
    
    # Paswword
    lb2 = Label(labelFrame,text="Password : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.5)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.5, relwidth=0.62)
   
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingLoginDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    



    
same=True
n=0.3

# Adding a background image
background_image =Image.open("lpgimg1.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Welcome to myLPG BOOKING", fg='black')
headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="Register",bg='black', fg='white', command=Register)
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Login",bg='black', fg='white', command=Login)
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)



root.mainloop()

