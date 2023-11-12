import os
import time
import curses

WELCOME = ("[•] __WELCOME TO IMAGINARY__[•]\n\n")

time.sleep(3)
print(WELCOME)
time.sleep(3)

name = ""
equipment = [
"ODD",
"  [•]__CURRENT EQUIPMENT__[•]\n",
"R-hand: \n",
"L-hand: \n",
"Armor: \n",
"additional-eqiupment: \n",
"rings: \n",
"          --END--"
]

for i in range(1):
    while i < 7:
        i+=1
        print(equipment[i])

freeitems = [
"ODD",
"katana",
"sword",
"two handed sword",
"halberd",
"bow",
"magic rod"
]

for i in range(1):
    while i < 5:
        i+=1
        #print(freeitems[i])