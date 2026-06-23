from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
import threading

root = Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title='Select file',
                                              filetype=(('file_type', '*.txt'), ('all files', '*.*')))

    def sender():
        try:
            s = socket.socket()
            host = socket.gethostname()
            port = 8080
            s.bind((host, port))
            s.listen(1)
            print(host)
            print('waiting for any incoming connections....')
            conn, addr = s.accept()
            file = open(filename, 'rb')
            file_data = file.read(1024)
            conn.send(file_data)
            print("Data has been transmitted successfully..")
        except Exception as e:
            print(f"Error: {e}")

    try:
        # icon
        image_icon1 = PhotoImage(file="image/send.png")
        window.iconphoto(False, image_icon1)
        window.image_icon1 = image_icon1
    except:
        pass

    try:
        Sbackground = PhotoImage(file="Image/sender.png")
        Label(window, image=Sbackground).place(x=-2, y=0)
        window.Sbackground = Sbackground
    except:
        pass

    try:
        Mbackground = PhotoImage(file="image/id.png")
        Label(window, image=Mbackground, bg='#f4fdfe').place(x=100, y=260)
        window.Mbackground = Mbackground
    except:
        pass

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white', fg='black').place(x=140, y=290)

    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file).place(x=160, y=150)
    Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg="#000", fg="#fff", command=sender).place(x=300, y=150)

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        try:
            s = socket.socket()
            port = 8080
            s.connect((ID, port))
            file = open(filename1, 'wb')
            file_data = s.recv(1024)
            file.write(file_data)
            print("File has been received successfully")
        except Exception as e:
            print(f"Error: {e}")
    
    try:
        # icon
        image_icon1 = PhotoImage(file="image/C:/Users/USER/Downloads/Image/receiver.png")
        main.iconphoto(False, image_icon1)
        main.image_icon1 = image_icon1
    except:
        pass

    try:
        Hbackground = PhotoImage(file="image/C:/Users/USER/Downloads/Image/receiver.png")
        Label(main, image=Hbackground).place(x=-2, y=0)
        main.Hbackground = Hbackground
    except:
        pass

    try:
        logo = PhotoImage(file='Image/profile.png')
        Label(main, image=logo, bg="#f4fdfe").place(x=10, y=250)
        main.logo = logo
    except:
        pass

    Label(main, text="Receive", font=('arial', 20), bg="#f4fdfe").place(x=100, y=280)

    Label(main, text="Input sender id", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=340) 
    SenderID = Entry(main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(main, text="filename for the incoming file: ", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=420) 
    incoming_file = Entry(main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    incoming_file.place(x=20, y=450)

    try:
        imageicon = PhotoImage(file="image/arrow.png")
        rr = Button(main, text="receive", compound=LEFT, image=imageicon, width=130, bg="#39c790", font="arial 14 bold", command=receiver)
        rr.place(x=20, y=500)
        main.imageicon = imageicon
    except:
        rr = Button(main, text="receive", width=130, bg="#39c790", font="arial 14 bold", command=receiver)
        rr.place(x=20, y=500)

try:
    # Icon
    image_icon = PhotoImage(file=r"C:\Users\USER\Downloads\Image\icon.png")
    root.iconphoto(False, image_icon)
except:
    pass

Label(root, text="File Transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").place(x=20, y=30)
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

try:
    Send_image = PhotoImage(file="Image/Send.png")
    Send_btn = Button(root, image=Send_image, bg="#f4fdfe", bd=0, command=Send)
    Send_btn.place(x=50, y=100)
    root.Send_image = Send_image
except:
    Send_btn = Button(root, text="Send", bg="#f4fdfe", bd=0, command=Send)
    Send_btn.place(x=50, y=100)

try:
    Receive_image = PhotoImage(file="Image/Receive.png")
    Receive_btn = Button(root, image=Receive_image, bg="#f4fdfe", bd=0, command=Receive)
    Receive_btn.place(x=300, y=100)
    root.Receive_image = Receive_image
except:
    Receive_btn = Button(root, text="Receive", bg="#f4fdfe", bd=0, command=Receive)
    Receive_btn.place(x=300, y=100)

# label
Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)

try:
    background = PhotoImage(file="image/C:/Users/USER/Downloads/Image/background.png")
    Label(root, image=background).place(x=-2, y=323)
    root.background = background
except:
    pass

root.mainloop()
