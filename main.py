from tkinter import*  #tkinter is a python lib form making GUI's
from tkinter import ttk #ttk contains some stylish toolkits
from PIL import Image,ImageTk #it is used inorder to crop or fix size of images

class Face_Recognition_System:
    def __init__(self,root): #constructor
        self.root=root
        self.root.geometry("1530x790+0+0") #set width and height of page window
        self.root.title("face Recognition System") 

        # r is written because in pyhton we have to convert backsloash to forward slash
        # img is to get images in college_images folder
        # first image
        img1=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\PSIT.jpg")
        img1=img1.resize((500,150),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=150)

        #second image
        img2=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\facialrecognition.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=550,height=150)

        #third image
        img3=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\PSIT.jpg")
        img3=img3.resize((500,150),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=1000,y=0,width=550,height=150)

        # bg image
        img4=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\blue.png")
        img4=img4.resize((1530,710),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg3=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold",),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        # student button
        img5=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\student.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # detection button
        img6=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\Face_detector.png")
        img6=img6.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        
        # detection button
        img7=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\attendance.png")
        img7=img7.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Help desk button
        img8=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\help_desk.png")
        img8=img8.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        # Training button
        img9=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\train_data.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        # Photos button
        img10=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\camera.png")
        img10=img10.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        # Developer button
        img11=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\developer.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        # Exit Face button
        img12=Image.open(r"C:\Users\vishn\OneDrive\Desktop\face recognition system\college_images\exit1.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS) # ANTILIAS converts High level image to Low level image
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold",),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()