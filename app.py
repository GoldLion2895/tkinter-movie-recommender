from tkinter import *
from func import mr
from tkinter import ttk
from pil import Image, ImageTk


win=Tk()
win.title("Movie Recommendation")
win.geometry('1500x800')
res=StringVar()

msg=StringVar()

l=StringVar()
l.set("Select language")

g=StringVar()
g.set("Select a genre")

a=StringVar()
a.set("Select an age group")


def rec():
    r=mr(l.get(),g.get(),a.get())
    res.set(r)
    msg.set("Here are some movies for you to watch")

def movies():
    top= Toplevel(win)
    top.geometry("300x450")
    top.title("Movie Options")
    pd=ttk.Panedwindow(top,orient=HORIZONTAL)
    pd.pack(fill=BOTH,expand=True)
    f1=ttk.Frame(pd,width=100,height=400,relief=SUNKEN)
    f1.pack()
    f2=ttk.Frame(pd,width=400,height=400,relief=SUNKEN)
    f2.pack()
    pd.add(f1,weight=1)
    pd.add(f2,weight=4)

    o1=OptionMenu(f1,l,"english","hindi").place(x = 70, y = 220)
    o2=OptionMenu(f1,g,"action","comedy","crime and mystery","documentary","fantasy","horror","romance","sci-fi","family fun").place(x = 75, y = 260)
    o3=OptionMenu(f1,a,"kids","teenagers","adult","family").place(x = 55, y = 300)

    b1=Button(f2,text="Get recommendations!",command=rec).place(x = 400, y = 100)
    
    l1=Label(f2,textvariable=msg, font='Helvetica 14').place(x = 300, y = 200)
    l2=Label(f2,textvariable=res,font='Helvetica 14').place(x = 300, y = 300)



canvas = Canvas(win, width = 1500, height = 800)
canvas.pack()
#img = PhotoImage(file="download.png")
img=(Image.open("collage.jpg"))
ri=img.resize((1300,900), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(ri)
canvas.create_image(0,0, anchor=NW, image=new_image)

label1=Label(win, fg = "red", text="WELCOME TO THE MOVIE RECOMMENDER", font=('Mistral 30 bold')).place(x = 340, y = 70)

label2=Label(win, fg = "green", text="Click Here to Get Started!", font=('Helvetica 14 bold')).place(x = 540, y = 300)

Button(win, text="Movies!", command=movies,relief=RAISED,font='Helvetica 14').place(x = 620, y = 400)


win.update()
win.mainloop()