from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk,Image
bg_color='#ffffff'
co1="#566FC6"

root=Tk()
root.title("Alarm clock")
root.geometry("350x150")
root.configure(bg=bg_color)

frame_line=Frame(root,width=400,height=5,bg=co1)
frame_line.grid(row=0,column=0)

frame_body=Frame(root,width=400,height=290,bg=bg_color)
frame_body.grid(row=1,column=0)

img=Image.open("icon.png")
img.resize((100,100))
img=ImageTk.PhotoImage(img)

app_image=Label(frame_body,height=100,image=img,bg=bg_color)
app_image.place(x=10,y=10)

name=Label(root,text="Alarm",height=1,font=("Ivy 18 bold"),bg=bg_color)
name.place(x=125,y=10)

hour=Label(root,text="hour",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=co1)
hour.place(x=127,y=40)
c_h=Combobox(root,width=2,font=("Arial 15"))
c_h["values"]=["00","01","02","03","04","05","06","07","08","09","10","11","12"]
c_h.current(0) 
c_h.place(x=130,y=58)

min=Label(root,text="min",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=co1)
min.place(x=177,y=40)
c_m=Combobox(root,width=2,font=("Arial 15"))
c_m["values"]=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
c_m.current(0) 
c_m.place(x=180,y=58)

sec=Label(root,text="sec",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=co1)
sec.place(x=227,y=40)
c_sec=Combobox(root,width=2,font=("Arial 15"))
c_sec["values"]=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
c_sec.current(0) 
c_sec.place(x=230,y=58)

period=Label(root,text="period",height=1,font=("Ivy 10 bold"),bg=bg_color,fg=co1)
period.place(x=277,y=40)
c_period=Combobox(root,width=3,font=("Arial 15"))
c_period["values"]=("AM","PM")
c_period.current(0) 
c_period.place(x=280,y=58)

selected=IntVar()

rad1=Radiobutton(root,font=("Arial 10 bold"),text="Activate",bg=bg_color)
rad1.place(x=125,y=95)
root.mainloop()
