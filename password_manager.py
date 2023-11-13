# most advanced mini project for beginners 
'''
if you want to login in any website like google , netflix , book my show etc we have to enter our login details
but multiple times we can't enter or remember our login details 
in this project our passwords will be managed 
'''
master_pwd=input("What is the password ?")
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw = data.split("|")
            print("User:",user,"Password:",passw)
def add():
    name=input("UserName:")
    pwd = input("Password :")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
        
        

while True:
    mode = input("would you like to add a new password or view existing one.... press q to exit ! ")
    if mode =='q':
        break
    if mode =='view':
        view()
    elif mode =='add':
        add()
    else:
        print("Invalid Choice !")
        continue