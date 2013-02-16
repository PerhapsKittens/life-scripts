import random
from datetime import datetime

# Get the current time and hope that the user set their clock correctly.
# h is current hour and m is current minute.
h = datetime.now().hour
m = datetime.now().minute

# n is the (sudo)random number being generated and used for decisions.
n = random.randint(1,7)

print('Your computer has made the decision for you!')
print('Now go to:')

# Lazy options (doesn't require leaving campus, even for the sandwich shop).
if (n==1):
  print('Library Cafe')
elif (n==2):
  print('JCR')
# Meh options (fairly close to campus).
elif (n==3):
  print('Sandwich shop')
elif (n==4):
  print('Chopstix')
elif (n==5):
  print('Tesco')
elif (n==6):
  print('Burger King')
# Adventure options (Prepared to go a long way for food).
elif (n==7):
  print('McDonalds')