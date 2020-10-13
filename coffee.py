'''CoffeeMachine: Abstraction of the outer machine, holding all the parts. 
Responsible for constructing machine, capturing external input.
+ oneAction() 
+ totalCash()'''

class CoffeeMachine():
    def __init__(self):
        self.cb = CashBox()
        self.s = Selector()
        self.p = Product(name = None, price = None, recipe = None)
    def oneAction(self):
        print("______________________________________"+'\n'
        "PRODUCT LIST: all 35 cents, except bouillon (25 cents)"+'\n'
        "1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon"+'\n'
        "Sample commands: insert 25, select 1."'\n' )
        command = input(">>> Your command: " )
        self.yourCommand = command
        if self.yourCommand[0:6] == "insert":
            amount = self.yourCommand[7:]
            self.cb.deposit(int(amount))
        elif self.yourCommand[0:6] == "select":
            if 0 < int(self.yourCommand[7:]) < 6:
                self.s.select(self.s.products(self.yourCommand), self.cb)
            else:
                print("INPUT ERROR >>> \nPlease make a valid selection.\n")
        elif self.yourCommand == "cancel":
            self.cb.returnCoins()
        elif self.yourCommand == "quit":
            return False
        else:
            print("Invalid command.\n")
        return True
    def totalCash(self):
        return self.cb.total()

    
'''Abstraction of a change maker or cashbox on a real machine. 
Responsible for making change, accepting coins
+ deposit(amount: int) 
+ returnCoins( ) 
+ haveYou(amount): bool 
+ deduct(amount) 
+ total(): int'''

class CashBox():
    def __init__(self):
        self.credit = 0
        self.totalReceived = 0
    def deposit(self, amount):
        if amount == 5 or amount == 10 or amount == 25 or amount == 50:
            self.credit += amount
            print(f"Depositing {amount} cents. You have {self.credit} cents credit.\n")
        else:
            print("INPUT ERROR >>> \nWe only take half-dollars, quarters, dimes, and nickels. \nCoin(s) returned.\n")
            self.credit = 0
    def haveYou(self, amount):
        if self.credit < amount:
            return True
    def returnCoins(self):
        print(f"Returning {self.credit} cents.\n")
        self.credit = 0
    def deduct(self, price):
        self.credit = self.credit - price
        self.totalReceived = self.totalReceived + price
        print(f"Returning {self.credit} cents.\n")
        self.credit = 0
    def total(self):
        return self.totalReceived

    
'''Abstraction of the internal selector and controller. 
Knows products & selection, coordinates payment and drink making.
+ select(choiceIndex: int)'''

class Selector():
    def products(self, selection):
        self.selection = selection
        if self.selection == "select 1": 
            self.name = "black"
            self.price = 35
            self.recipe = ["cup","coffee","water"]
        elif self.selection == "select 2":
            self.name = "white"
            self.price = 35
            self.recipe = ["cup","coffee","creamer","water"]
        elif self.selection == "select 3":
            self.name = "sweet"
            self.price = 35
            self.recipe = ["cup","coffee","sugar","water"]
        elif self.selection == "select 4":
            self.name = "white & sweet"
            self.price = 35
            self.recipe = ["cup","coffee","sugar","creamer","water"]
        elif self.selection == "select 5":
            self.name = "bouillon"
            self.price = 25
            self.recipe = ["cup","bouillonPowder","water"]
    def select(self, selection, cb):
        p = Product(self.name,self.price,self.recipe)
        if cb.haveYou(p.getPrice()) == True:
           print("Sorry. Not enough money deposited.\n")
        else: 
            p.make()
            cb.deduct(self.price)

            
'''Abstraction of the drink. 
Responsible for knowing its price and recipe. 
Dispenses the drink.
+ getPrice( ): int 
+ make( )'''

class Product():
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe
    def getPrice(self):
        return self.price
    def make(self):
        print("Making",self.name+':')
        for ingredient in self.recipe:
            print("\tDispensing",ingredient)

            
def main():  
    cm = CoffeeMachine()     
    while cm.oneAction():         
        pass       
    total = cm.totalCash()    
    print(f"Total cash: ${total/100:.2f}") 

    
if __name__ == "__main__":
    main()
