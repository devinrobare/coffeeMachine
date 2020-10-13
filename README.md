# coffeeMachine
Polymorphism used to create an old school coffee machine!

PRODUCT LIST: all 35 cents, except bouillon (25 cents)
  + 1 = black  (cup + coffee + water)
  + 2 = white  (cup + coffee + creamer + water)
  + 3 = sweet  (cup + coffee + sugar + water)
  + 4 = white & sweet  (cup + coffee + sugar + creamer + water)
  + 5 = bouillon  (cup + bouillon powder + water)
 
 The coffeeMachine only takes half-dollars (50), quarters (25), dimes (10), and nickels (5).
        
 (Sample commands: insert 25, select 1)

CoffeeMachine: Abstraction of the outer machine, holding all the parts. 
Responsible for constructing machine, capturing external input.
  + oneAction: the coffee machine interface that presents the options and accepts input 
              (command "cancel" returns coins, command "quit" ends session)
  + totalCash: displays the total amount inserted in one session

CashBox: Abstraction of a change maker or cashbox on a real machine. 
Responsible for making change, accepting coins.
  + deposit: takes inserted coins, rejects incorrect coins
  + returnCoins: returns all coins that have been inserted
  + haveYou: has enough money been inserted to ourchase the selection (bool)
  + deduct: takes the cost of the selection from the amount inserted and tallies the total
  + total(): returns the total amount spent in one session

Selector: Abstraction of the internal selector and controller. 
Knows products & selection, coordinates payment and drink making.
  + products: supplies the recipes
  + select: determines if enough money has been inserted. If yes, takes the order. 
            If not, notifies user they haven't inserted enough money.

Product: Abstraction of the drink. 
Responsible for knowing its price and recipe. 
Dispenses the drink.
  + getPrice: reurns the price of the product selected
  + make: dispenses the product
