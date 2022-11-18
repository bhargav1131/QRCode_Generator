from tkinter import *
import png
from tkinter import messagebox
import pyqrcode
from pyqrcode import QRCode

ws = Tk()
ws.title("QRCude Generator")
ws.geometry('514x640')
ws.config(bg="#FFF6C9")
ws.resizable(0,0)
image_icon = PhotoImage(file="/home/bhargav/QR_code/project_images/icon.png")
ws.iconphoto(False, image_icon)

backg = PhotoImage(file="/home/bhargav/QR_code/project_images/background.png")
label1 = Label(image=backg)
label1.image = backg
label1.pack()

def generate_QR():
    if len(user_input.get()) != 0:
        global qr, img
        file = file_name.get()
        qr = pyqrcode.create(user_input.get())
        qr.png(f'{file}.png', scale = 6)
        img = BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass


def display_code():
    img_lbl.config(image=img)
    output.config(text="QR code of " + user_input.get())



user_input = StringVar()
entry = Entry(ws,textvariable=user_input, width=25, border=0).place(x=210, y=120)


file_name = StringVar()
Entry(ws, textvariable=file_name, width=25, border=0).place(x=210, y=200)


gen_img = PhotoImage(file="/home/bhargav/QR_code/project_images/generate.png")
button = Button(ws,image=gen_img,command=generate_QR, bg="#FFF6C9")
button.place(x=200,y=280)

img_lbl = Label(ws,bg='#FFF6C9')
img_lbl.place(x=130, y=340)
output = Label(ws,text="",bg='#FFF6C9')
output.place(x=160, y=595)

ws.mainloop()
