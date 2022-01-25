from random import choice
from click import Choice


print("welcome to recipe Generator.")
print("press 1 For FRENCH FRIES , press 2 for NOODLES , press 3 for PASTA, press 4 for GARLIC BREAD")

Choice = int(input("choose which recipe do you want?"))

if Choice == 1:
   a = open("frenchfries.txt", "r")
   print(a.read())
elif Choice == 2:
    b = open("noodles.txt", "r")
    print(b.read())
elif Choice == 3:
    c = open("pasta.txt", "r")
    print(c.read())
elif Choice == 4:
   d = open("garlicBread.txt", "r")
   print(d.read())