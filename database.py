import random
import json

random.seed(1234) # fixed seed to make random sequence reproducable during re-run
minRand = 10000
maxRand = minRand*10
numbers = list(range(minRand, maxRand))
numbers2 = list(range(0, maxRand))
random.shuffle(numbers)
random.shuffle(numbers2)
totNum1,totNum2,totAccCreated = 0,0,0
accountDatabase, accountDict = [],{}
# To prevent using an already used random account number, I do this:
# Generate 2 random numbers of 5 digits each, and append them to get the account number
# Just fix the arrays for the 2 rands at the start and pick the next available pair
# This leads to a total of (100000-10000) * 100000 possible accounts = 9,000,000,000(all possible 10-digit nums)

class Account:
    def __init__(self, fName, lName, pin, accNum, balance):
        self.fName = fName
        self.lName = lName
        self.pin = pin
        self.accNum = accNum
        self.balance = balance
        
    def __str__(self):
        return f"Account Number: {self.accNum}, Account Name: {self.fName} {self.lName}, Account Balance: {self.balance}"

def increaseCounter(): # move to the next pair of random numbers(it actually goes through all possible pairs)
    global totNum1,totNum2,totAccCreated
    totNum2+=1
    if totNum2==len(numbers2):
        totNum2=0
        totNum1+=1
        random.shuffle(numbers2) # Reshuffle numbers2 once you've exhausted current rand1 to prevent prediction of next acc number
    totAccCreated+=1
    
def save_accounts_to_json(account_list):
    account_dicts = []
    for account in account_list:
        account_dict = {
            "fName": account.fName,
            "lName": account.lName,
            "pin": account.pin,
            "accNum": account.accNum,
            "balance": account.balance
        }
        account_dicts.append(account_dict)
    json_data = json.dumps(account_dicts, indent=4)
    with open("accounts.json", "w") as file:
        file.write(json_data)
        
def load_accounts_from_json():
    try:
        with open("accounts.json", "r", encoding="utf-8") as file:
            json_data = file.read()
            account_dicts = json.loads(json_data)
            account_list, account_dict = [], {}
            for index, cur_account_dict in enumerate(account_dicts):
                increaseCounter()
                account = Account(cur_account_dict["fName"], cur_account_dict["lName"],
                cur_account_dict["pin"],cur_account_dict["accNum"], cur_account_dict["balance"])
                account_list.append(account)
                account_dict[account.accNum] = index
            return account_list, account_dict
    except FileNotFoundError:
        return [], {}
    
accountDatabase, accountDict = load_accounts_from_json()

#after 3 trials it returns
def getAccNumber():
    accNum,num = False,3
    while num and accNum==False:
        accNum = int(input("Enter Account Number: "))
        if accNum not in accountDict:
            print("Account does not exist")
            num-=1
            accNum = False
    return accNum

def getPin(index):
    pin,num = False,3
    while num and pin==False:
        pin=input("Enter Account Pin: ")
        if pin != accountDatabase[index].pin:
            print("Pin is not correct")
            num-=1
            pin = False
    return pin

def printAccDetails(account):
    print("")
    print("Account Details: ")
    print(f"Name: {account.fName} {account.lName}")
    print(f"Account Number: {account.accNum}")
    print(f"Balance: #{account.balance}")
    print("")
    
def getAccount(withPin=True): #you can either get account with or without pin required depending on the situation
    accNumber = getAccNumber()
    if accNumber==False:
        print("You have failed too many times")
        return False
    index = accountDict[accNumber]
    account = accountDatabase[index]
    if withPin==False:
        return account
    accPin = getPin(index)
    if accPin == False:
        print("You have failed too many times")
        return False
    return account
    
def getNewAccount(fName,lName,pin,balance=0.00):
    global totAccCreated,totNum1,totNum2
    rand = numbers[totNum1]*100000+numbers2[totNum2]
    increaseCounter()
    accountDatabase.append(Account(fName,lName,pin,rand,balance))
    accountDict[rand]=len(accountDict)-1
    save_accounts_to_json(accountDatabase)
    return accountDatabase[-1]