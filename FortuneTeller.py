name = input("What is your name?")
print("Welcome , " + name + ", to the Fortune Teller! I will ask you a few questions and tell your fortune.")
print("You can quit at any time by typing QUIT")

age = input("What is your age?")
if age == "QUIT":
    print("Nobody likes a quitter...")
    raise SystemExit
remainder = int(age) % 2
birth_month = input("Please enter your birth month as a number.  For example, January would be 1.")
if birth_month == "QUIT":
    print("Nobody likes a quitter...")
    raise SystemExit
int(birth_month)
siblings = input("How many siblings do you have?")
if siblings == "QUIT":
    print("Nobody likes a quitter...")
    raise SystemExit
color = input("Please enter your favorite ROYGBIV color. Type help if you don't know what ROYGBIV is. ")
if color == "QUIT":
    print("Nobody likes a quitter...")
    raise SystemExit
lowercase_color = color.lower()
list_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
if lowercase_color == "help":
    print("These are the ROYGBIV colors:")
    for color in list_colors:
        print(color)
    lowercase_color = input("What is your favorite color?")
    if lowercase_color == "QUIT":
        print("Nobody likes a quitter...")
        raise SystemExit
if remainder == 1:
    retire_age = "10"
else:
    retire_age = "20"
if int(birth_month) <= 0:
    money = "$0.00"
elif 1 >= int(birth_month) <= 4:
    money = "$25,000"
elif 5 >= int(birth_month) <= 8:
    money = "$250,000"
elif 9 >= int(birth_month) <= 12:
    money = "$1 million"
else:
    money = "$0.00"
if siblings == "0":
    vacation_home = "Aspen"
elif siblings == "1":
    vacation_home = "Montana"
elif siblings == "2":
    vacation_home = "Naples, FL"
elif siblings == "3":
    vacation_home = "Paris"
elif siblings > 3:
    vacation_home = "Rehobeth Beach"
else:
    vacation_home = "Detroit"
if lowercase_color == "red.":
    car = "Bentley"
elif lowercase_color == "orange.":
    car = "yacht"
elif lowercase_color == "yellow.":
    car = "helicopter"
elif lowercase_color == "green.":
    car = "Lear jet"
elif lowercase_color == "blue.":
    car = "dinghy"
elif lowercase_color == "indigo.":
    car = "truck"
else:
    car = "limousine."
print(name + ", you will retire in " + retire_age + " years with " + money + " in the bank and a vacation home in " + vacation_home + " and a " + car)








#fprint(lowercase_color)