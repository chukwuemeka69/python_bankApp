import database
    
def depositFund():
    print("Welcome to Deposit Funds!")
    print("Input the account details you want to deposit to")
    account = database.getAccount(False)
    if account==False:
        return False
    amount = float(input("Enter the amount to be deposited: "))
    if amount <= 0:
        print("Invalid amount!")
        return False
    account.balance+=amount
    database.printAccDetails(account)
    database.save_accounts_to_json(database.accountDatabase)
    return True

def resetPassword():
    print("Welcome to Change Pin!")
    print("Input your account details")
    account = database.getAccount()
    newPin = input("Enter your new pin: ")
    newPin2 = input("Confirm your new pin: ")
    if newPin!=newPin2:
        print("Pins do not match!")
        return False
    account.pin = newPin
    database.printAccDetails(account)
    database.save_accounts_to_json(database.accountDatabase)
    return

def exitProgram():
    print("Thanks for visiting, see you next time!")
    return

def printStart():
    print("Welcome to Bank Management System for Agents!")
    print("0 = Exit the Program")
    print("1 = Deposit to an Account")
    print("2 = Change Customer Account Pin")
    key = input("Type a key to choose your option: ")
    return int(key)

def agent_main():
    print("")
    key = 1
    while key!=0:
        key = printStart()
        print("")
        if key==0:
            exitProgram()
        elif key==1:
            depositFund()
        elif key==2:
            resetPassword()
        else:
            print("That is an invalid option")
        print("")
