from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import random
import string



# Add database name and password here
mypass = "python"
mydatabase="vamsi"

con = pymysql.connect(host="localhost",user="pjdata",password=mypass,database=mydatabase)
cur = con.cursor()

#enter table names
bdetails = "register"  #Booking Details

def close_window():
    root.destroy()
def bookingRegister():
    def idnum():
        global bid
        size = 8
        chars = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        chars = (string.ascii_uppercase + string.digits)
        bid=''.join(random.choice(chars) for x in range(size))
        print(bid)
    
    cusid = en1.get()
    cylinders = en2.get()
    address = en3.get()
    idnum()
    insert = "insert into "+bdetails+" values('"+bid+"','"+cusid+"','"+cylinders+"','"+address+"')"
    try:
        
            cur.execute(insert)
            con.commit()
            messagebox.showinfo("success","booked successflly")
    except:
        messagebox.showinfo("Error","cannot book LPG")

    print(cusid)
    print(cylinders)
    print(address)
    

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    
    
    
        
    

def booking():
    global en1,en2,en3,issueBtn,quitBtn,root,Canvas1,lableFrame,lb1,status
    root =Tk()
    root.title("BOOKNOW")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

        

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

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#706fd3",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.3)
        
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="BOOKNOW", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)   
        
    # email id:
    lb1 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.2, relwidth=0.62)

    # no of cylinders:
    lb2 = Label(labelFrame,text="no of cylinders :", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.4, relwidth=0.62)

    #delivary address:
    lb3 = Label(labelFrame,text="delivary address : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.6)
        
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.6, relwidth=0.62)
        
    #order Button
    issueBtn = Button(root,text="order",bg='#d1ccc0', fg='black',command=bookingRegister)
    issueBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=close_window)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)

    
    root.mainloop()


