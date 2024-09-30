class Employee:
    def _init_(self,smtp_server,smtp_port,smtp_username,smtp_password):
        self.smtp_server=smtp_server
        self.smtp_port=smtp_port
        self.smtp_username=smtp_username
        self.smtp_password=smtp_password
        
    def send_email(email_address):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 465
        smtp_username = ""
        smtp_password = ""
        subject = 'Registration Succesfull!'
        body = f'Hello,\n\nThank you for registering! your email {email_address} has been successfully registred.'
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_username
        msg['To'] = email_address
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            #server.strttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, email_address,msg.as_string())
            messagebox.showinfo("Success", f"Registration email sent to {email_address} successfully!")