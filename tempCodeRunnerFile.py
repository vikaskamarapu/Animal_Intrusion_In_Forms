def send_email(label):

#     Sender_Email = "@gmail.com"
#     Reciever_Email = "@gmail.com"
#     # Password = input('Enter your email account password: ')
#     Password = ''   #ENTER GOOGLE APP PASSWORD HERE

#     newMessage = EmailMessage()    #creating an object of EmailMessage class
#     newMessage['Subject'] = "Animal Detected" #Defining email subject
#     newMessage['From'] = Sender_Email  #Defining sender email
#     newMessage['To'] = Reciever_Email  #Defining reciever email
#     newMessage.set_content('An animal has been detected') #Defining email body

#     with open('images/' + label + '.png', 'rb') as f:
#         image_data = f.read()
#         image_type = imghdr.what(f.name)
#         image_name = f.name[7:]

#     newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(Sender_Email, Password) #Login to SMTP server
#         smtp.send_message(newMessage)      #Sending email using send_message method by passing EmailMessage object


# def async_email(label):
#     threading.Thread(target=send_email, args=(label,), daemon=True).start()
