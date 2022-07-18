# Data

Account = {'Mr.A' : 10000, 'Mrs.B' : 5000}

def getBalance():
    print('Balance: ', Account)

def deposit(money):
    if not type(money) is int:
        raise Exception('Number Only')
    if money < 100:
        raise Exception('minimum deposit 100 BATH')
    print('Deposit money Mr.A: ', money)
    Account['Mr.A'] += money

def withdraw(money):
    if not type(money) is int:
        raise Exception('Number Only')
    if money < 100:
        raise Exception('minimum withdraw 100 BATH')
    if money >= Account['Mr.A']:
        raise Exception('Insufficient account balance')
    print('withdraw Mr.A: ', money)
    Account['Mr.A'] -= money

def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception('Number Only')
    if money < 1:
        raise Exception('minimum transfer 1 BATH')
    if money >= Account['Mr.A']:
        raise Exception('Insufficient account balance')
    print('transfer to Mrs.B: ', money)
    Account['Mrs.B'] += money   
    Account['Mr.A'] -= money 

try:
    getBalance()
    deposit(500)
    getBalance()
    withdraw(6000)
    getBalance()
    transfer(200)
    getBalance()
except Exception as error:
    print(error)