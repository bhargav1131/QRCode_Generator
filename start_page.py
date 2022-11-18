from tkinter import *

ws = Tk()
ws.geometry("575x569")
ws.title('QRCude Generator')
ws.resizable(False, False)
image_icon = PhotoImage(file="/home/bhargav/QR_code/project_images/icon.png")
ws.iconphoto(False, image_icon)


backg = PhotoImage(file="/home/bhargav/QR_code/project_images/wlcme.png")
label1 = Label(image=backg)
label1.image = backg
label1.pack()

def nextPage():
    ws.destroy()
    import main
    
# continue button
continue_img = PhotoImage(file="/home/bhargav/QR_code/project_images/Arrow 1.png")
continue1 = Button(ws, image=continue_img, bd=0, command=nextPage, bg="#FFF6C9")
continue1.place(x=268, y=528)

ws.mainloop()