from cgitb import text
from curses import raw
import qrcode
from PIL import Image
import tkinter as tk
window=tk.Tk()
window.title("USER LOGIN")
window.geometry('449x200')
l1=tk.Label(window,text='    Paste your URL or any String to generate QR code  ',bg='orange',fg='white',font=('comic sans ms',12,'bold')).grid(row=0,column=1)
e2=tk.Entry(window,bg="white",fg='blue')
#e2.grid(row=1,column=1)
e2.grid(row=1,column=1,ipadx=100, ipady=2)
e2.bind('<return>') or e2.bind('<Tab>') or e2.bind('<Leave>')
def QrCode():
    qrtext=e2.get()
    img=qrcode.make(qrtext)
    img.save("generatedQrCode.jpg")
    im = Image.open(r"generatedQrCode.jpg")
    im.show()
b1=tk.Button(window,text="Generate QR code",command=QrCode,bg='green',fg='white').grid(row=5,column=1)


#print(e2)

#inp1=input("Paste your URL or any String to generate QR code\n------->")

#img.save("generatedQrCode.jpg")

#print(e2)
# Imports PIL module


# open method used to open different extension image file
#im = Image.open(r"generatedQrCode.jpg")

# This method will show image in any image viewer
#im.show()
window.mainloop()