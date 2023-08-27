
from email.message import EmailMessage
from tkinter import *
from tkinter.ttk import *
import random
import smtplib

email_sender = 'trisharaj452@gmail.com'
passwrd = 'xmdzzzxhdtnjywmg'
OTP = ''.join(str(random.randint(0, 9)) for i in range(6))

def connection():
    receiver = get_mail.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, passwrd)
    server.sendmail(email_sender, receiver, OTP)
    server.quit()
print("OTP is sent successfully")

def check_OTP():
    code = get_code.get()
    if OTP == code:
        a = Label(window, text="successful verification", background="green", foreground="white", font="Arial 22 bold")
        a.place(x=150, y=275)
    else:
        a = Label(window, text="failed verification", background='black', foreground='red', font="Arial 22 bold")
        a.place(x=190, y=275)

window = Tk(className='Verification')
window.geometry("600x350")
window.configure(background="#000000")

label_email = Label(window, text="Enter your email:", background='#0000FF', foreground='#FFFFFF', font='Arial 18 bold')
label_email.place(x=15, y=40)
get_mail = StringVar()
write_email = Entry(window, textvariable=get_mail, background='#FFFFFF', foreground='#000000', width=21, font='Arial 17 bold')
write_email.place(x=230, y=40)

send_button = Button(window, text="SEND ME OTP", width=18, command=connection)
send_button.place(x=260, y=100)

label_code = Label(window, text='received OTP:', background='#0000FF', foreground='#FFFFFF', font='Arial 16 bold')
label_code.place(x=15, y=180)

get_code = StringVar()
write_code = Entry(window, textvariable=get_code, background='#FFFFFF', foreground='#000000', width=10, font='Arial 17 bold')
write_code.place(x=230, y=180)

verify_button = Button(window, text='verify', command=check_OTP, width=15)
verify_button.place(x=270, y=240)

window.mainloop()