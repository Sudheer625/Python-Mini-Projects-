user_name='sudheer'
password='sudheer998'

c_name=input("Enter Your Username :")
c_pass=str(input("Enter Your Password :"))
if c_name ==user_name and c_pass == password:
    print('''
          1. Deposit
          2. Withdraw
          3. Mini Statement
          4. Exit
          ''')
    amount=50000
    option=int(input("select your Options :"))
    if option ==1:
        dep=int(input("Enter The Amount To Depoist :"))
        amount+=dep
        print('Your Balance is /-',amount)
    elif option == 2:
        withd=int(input("Enter the Amount to Withdraw : "))
        amount-=withd
        print('Your  Remaining balance is / -',amount)
    elif option == 3:
        print("Mini Statement Printing.....")
        print("UserName :",user_name)
        print(amount)
        print("Collect Your Reciept......")
        print("*********THANKS FOR VISITING*********")
    elif option == 4:
        quit()
        print("Exited Portal")
else:
    print("Login Details Are Invalid ")