import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText

#function to send email
def send_email(email_address):
    #E-mail Configurtaion
    smtp_server='smtp.gmail.com'
    smtp_port=465
    smtp_username="darshan0302parmar@gmail.com"
    smtp_password=""
    subject="Registration Successful"
    body=f'Hello,\n\nThank you for rugistering your email {email_address} has Successfully rugistered.'

    msg=MIMEText(body)
    msg['Subject']=subject
    msg['From']=smtp_username
    msg['To']=email_address

    #connect to the server and send email

    with smtplib.SMTP_SSL(smtp_server,smtp_port) as server:
       # server.starttls() # secure connection
        server.login(smtp_username,smtp_password)
        server.sendmail(smtp_username,email_address, msg.as_string())

    messagebox.showinfo("Success",f"Rugistration email sent to{email_address} successfully!!")

#Function to handle button click

def on_send_button_click():
    email_address=email_entry.get()
    if email_address:
        send_email(email_address)
    else:
        messagebox.showwarning("INput Error","Please enter an email address.")
    
#set up the Tkinter GUI
root=tk.Tk()
root.title("Send registration Email")

#create and place widgets

email_label=tk.Label(root,text="Enter EMail Addres: aa")

#Create and place widgets
email_label=tk.Label(root,text="Enter Email Address:")
email_label.pack(pady=5)

email_entry=tk.Entry(root,width=40)
email_entry.pack(pady=5)

send_button=tk.Button(root,text="Send Email",command=on_send_button_click)
send_button.pack(pady=20)


root.mainloop()