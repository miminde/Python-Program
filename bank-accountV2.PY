#Bank Account Application Program (controlling flow and managing database)
#1)create a new account by collecting an individuals first name, last name, start balance
#read the data in at the start of the Program
accounts=[]
transactions=[]
#populate these 2 lists using the csv files
def readSavedData():
    try:
        with open('accounts.csv') as f:
            for line in f:
                account = line.split(',')
                account[3] = float(account[3])
                account[4] = float(account[4])
                accounts.append(account)
        with open('transactions.csv') as f:
            for line in f:
                transaction = line.split(',')
                transaction[1] = float(transaction[1])
                transactions.append(transaction)
    except FileNotFoundError: #except filenotfounderror specifically
        print('Data Files Not Found. New Files will be created on exit')

def saveData():
    with open('accounts.csv', 'w') as f:
        for account in accounts:
            f.write(','.join([str(x) for x in account]) + '\n') #creating a new array to represent all the elts in account lists

    with open('transactions.csv','w') as f:
        for transaction in transactions:
            f.write(','.join([str(x) for x in account]) + '\n')


def createAccount(firstName, lastName, startBalance):
    accountNumber=len(accounts)
    account=[accountNumber,firstName, lastName, startBalance,startBalance]
    accounts.append(account)
    return account

#2)Allow Debits and Credits to be taken against the Account
def createTransaction(accountNumber, amount):
    transaction=[accountNumber,amount]
    transactions.append(transaction)
    accountNumber=int(accountNumber)
    account=accounts[accountNumber]
    account[-1]=account[-1] + amount
    return account

def showMainMenu():
    print('Bank Account Application')
    print('\t1. Create New Account')
    print('\t2. Credit/Debit An Account')
    print('\t3. List All Accounts')
    print('\t4. List Account History')
    print('\tq. Quit')

def showCreateNewAccount():
    print('Creating A New Account')
    print('Please enter the individuals')
    firstName = input('\t\tFirst Name: ')
    lastName = input('\t\tLast Name: ')
    balance = float(input('\t\tBeginning Balance(USD): '))
    account = createAccount(firstName, lastName, balance)
    print('New Account Created for', firstName, lastName, '(Account#', account[0], ')')

def showCreditDebitAccount():
    print('Debiting/Crediting An Account')
    accountNumber = input('Please Enter The Account Number: ')
    amount = float(input('Please Enter The Amount: '))
    account = createTransaction(accountNumber, amount)
    if amount < 0:
        action = 'debited'
    else:
        action = 'credited'
    print(account[1], account[2], '(Account#', account[0], ')', action, '$', abs(amount))
    print('New Balance:', account[-1])

def showListAllAccounts():
    print('Listing Accounts')
    for account in accounts:  #for each item in accounts
        print(account[0], account[1] + ' ' + account[2], '$' + str(account[-1]), sep = '\t') #seperate items by a tab

def showAccountHistory():
    print('Transaction History')
    for account in accounts:
        print(account[0], account[1] + ' ' + account[2], sep = '\t')
        balance = account[3]
        for transaction in transactions: #create for loop to iterate over all transactions
            if str(transaction[0]) == str(account[0]): #to make sure it only happens to the correct account
                print('$' + str(balance), transaction[1], sep = '\t')
                balance = balance + transaction[1]
        print('$' + str(balance))

def main():  #functions that runs the program
    readSavedData()  #Call fn that reads saved data, and enter in loop and save it
    while True:
        showMainMenu() #call mainmenu function. will show main menu while true
        inp = input('What would you like to do:')

        if inp == 'q':
            break   #if users input equals q, then we break out of the loop
        elif inp == '1':
            showCreateNewAccount()
        elif inp == '2':
            showCreditDebitAccount()
        elif inp == '3':
            showListAllAccounts()
        elif inp == '4':
            showAccountHistory()

    saveData()

if __name__ == '__main__':  #checking to see if the file is being imported or run as stand alone program
    main()
