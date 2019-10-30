from tkinter import *





def register_user():
    
    username_info = username.get()
    password_info = password.get()
    if(len(password_info)<8):
        invalid_password_register()
    
    address_info = address.get()
    aadhar_info = aadhar.get()
    print(type(aadhar_info))
    if(len(str(aadhar_info))!=12):
        invalid_aadhar_register()

    radiobutton_info = var.get()
    print(radiobutton_info)






    

def invalid_aadhar_register():
    global invalid_aadhar_screen
    invalid_aadhar_screen = Toplevel(register_screen)
    invalid_aadhar_screen.title("Unscuccessful")
    invalid_aadhar_screen.geometry("300x100")
    Label(invalid_aadhar_screen,text = "Enter valid UID").pack()
    Button(invalid_aadhar_screen,text = "OK",command = delete_invalid_aadhar_register).pack()

def delete_invalid_aadhar_register():
    invalid_aadhar_screen.destroy()


        
       

def invalid_password_register():
    global invalid_password_screen
    invalid_password_screen = Toplevel(register_screen)
    invalid_password_screen.title("Unsuccessful")
    invalid_password_screen.geometry("300x100")
    Label(invalid_password_screen,text = "Minimum 8 character password").pack()
    Button(invalid_password_screen,text = "OK",command = delete_invalid_password_register).pack()


def delete_invalid_password_register():
    invalid_password_screen.destroy()

    



def register():
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("500x500")
 
# Set text variables
    global username
    username = StringVar()
    global password 
    password = StringVar()
    global address 
    address = StringVar()
    global aadhar 
    aadhar = StringVar()

 
# Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="#fcb603").pack()
    Label(register_screen, text="").pack()
    
# Set username label
    username_lable = Label(register_screen, text="Username ")
    username_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
# Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()


#  set address label
    address_lable = Label(register_screen,text = "Billing Address")
    address_lable.pack()


#set address entry
    address_entry = Entry(register_screen,textvariable=address)
    address_entry.pack()


#set Aadhar label
    aadhar_lable = Label(register_screen,text = "Aadhar Number")
    aadhar_lable.pack()

#set Aadhar entry
    aadhar_entry = Entry(register_screen,textvariable=aadhar)
    aadhar_entry.pack()


#set radio button and label
    set_radioButton()

    
    Label(register_screen, text="").pack()
    
    # Set register button
    Button(register_screen, text="Register", width=10, height=1, bg="#fcb603",command = register_user).pack()


def set_radioButton():
    global var
    var = IntVar()

    Label(register_screen,text = "Enter Payment mode")
    R1 = Radiobutton(register_screen, text="Prepaid", variable=var, value=1)
    R1.pack()
    R2 = Radiobutton(register_screen, text="Postpaid", variable=var, value=2)
    R2.pack()




def login_verification():
    print("working...")


# define login function
def login():
    
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
   
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()




def main_account_screen():
    global main_screen
 
# add command=register in button widget
 
    
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("main_screen")
 
    # create a Form label 
    Label(text="Vssut Electricity Billing system", bg="#fcb603", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    
    # create Login Button 
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack() 
    
   



    Button(text="Register", height="2", width="30", command=register).pack()
    
    
    main_screen.mainloop()
 
main_account_screen()


