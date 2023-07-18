import database
        
def printAccount():
    print("Welcome to View Account Details!")
    account = database.getAccount()
    if account==False:
        return False
    database.printAccDetails(account)
    return True

def createNewAccount() :
    print("Welcome to Create a New Account!")
    fName=input("Enter Customer First Name: ")
    lName=input("Enter Customer Last Name: ")
    pin=input("Enter your pin: ")
    account = database.getNewAccount(fName,lName,pin)
    database.printAccDetails(account)
    return True

def transferFund():
    print("Welcome to Transfer Funds!")
    print("Input account details to transfer from")
    account1 = database.getAccount()
    if account1==False:
        return
    print("Input account details to transfer to")
    account2 = database.getAccount(False)
    if account2==False:
        return
    amount = float(input("Enter the amount to be transfered: "))
    if amount <= 0:
        print("Invalid amount!")
        return False
    if account1.balance < amount:
        print("Insufficient funds!")
        return False
    account1.balance-=amount
    account2.balance+=amount
    database.printAccDetails(account1)
    database.save_accounts_to_json(database.accountDatabase)
    print(f"#{amount} has been transferred successfully to {account2.fName} {account2.lName}")
    return True

def resetPassword():
    print("Welcome to Reset Password!")
    remember = input("Do you know the old password? Type 'y' for yes or any key for no: ")
    print("Input the account details")
    if remember=="y":
        account = database.getAccount()
    else:
        account = database.getAccount(False)
    if account==False:
        return False
    
    if remember!="y":
        fullName = account.fName+account.lName
        temp = account.fName[0]+'*'*(len(account.fName)-1)
        temp += account.lName[0]+'*'*(len(account.lName)-1)
        temp2 = input(f"Input the full text replacing the * with correct letters: {temp}\n")
        if temp2!=fullName:
            print("Wrong answer")
            return False
    newPin = input("Enter your new pin (Type 'c' to quit): ")
    if newPin=='c':
        return False
    newPin2 = input("Confirm your new pin (Type 'c' to quit): ")
    if newPin2=='c':
        return False
    if newPin!=newPin2:
        print("Pins do not match!")
        return False
    account.pin = newPin
    database.printAccDetails(account)
    database.save_accounts_to_json(database.accountDatabase)
    return True

def exitProgram():
    print("Thanks for visiting, see you next time!")
    return

def printStart():
    print("Welcome to Bank Management System for Customers!")
    print("0 = Exit the Program")
    print("1 = Create a new Account")
    print("2 = View Account Info")
    print("3 = Transfer to an Account")
    print("4 = Reset Password")
    key = input("Type a key to choose your option: ")
    return int(key)

def customer_main():
    print("")
    key = 1
    while key!=0:
        key = printStart()
        print("")
        if key==0:
            exitProgram()
        elif key==1:
            createNewAccount()
        elif key==2:
            printAccount()
        elif key==3:
            transferFund()
        elif key==4:
            resetPassword()
        else:
            print("That is an invalid option")
        print("")
        
