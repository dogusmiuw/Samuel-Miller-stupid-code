
file = open("test.py", "w")

file.write("print('THE NUMBER IS ODD OR EVEN?')\n")

file.write("number = input('Enter a number: ')\n")

file.write("if number == 1: print('number is odd')\n")

for i in range(2, 100000):
    if i % 2 == 0:
        file.write("elif number == " + str(i) + ": print('number is even')\n")
    else:
        file.write("elif number == " + str(i) + ": print('number is odd')\n")
