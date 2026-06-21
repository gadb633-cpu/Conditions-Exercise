# Part 1
# 1
age = int(input("what your age? "))
if age >= 18:
    print("can enter")
else:
    print("cannot enter")
# 2
temperature = 38.2
if temperature > 37.5:
    print("high temperature")
else:
    print("normal temperature")
# 3
number = int(input("what your number? "))
if number % 2 == 0:
    print("even number") 
else:
    print("odd number")
# 4
battery = 15
is_charging = True
if battery > 20:
    print("battery ok")
elif battery < 20 and is_charging:
    print("low battery, charging now")
elif battery < 20 and is_charging == False:
    print("low battery, connect charger")
# 5
password = input("what your password? ")
if password == "python123":
    print("access approve")
else:
    print("access denied")
# 6
score = 72
if score >= 90:
    print("excellent")
elif score >= 75:
    print("good")
elif score >= 60:
    print("pass")
else:
    print("fail")
# 7
first_number = int(input("give me first number "))
second_number = int(input("give me second number "))
if first_number > second_number:
    print("first is bigger")
elif first_number < second_number:
    print("second is bigger")
else:
    print("equal")
# 8
fuel = 40
distance = 30
if fuel - distance >= 10:
    print("enough fuel with reserve")
elif fuel - distance < 10:
    print("enough fuel low reserve")
else:
    print("not enough fuel")
# 9
username = input("what your username? ")
if username == False:
    print("guest user")
else:
    print(f"hello {username}")
# 10
hour = 21
if hour < 0 or hour > 23:
    print("invalid hour")
elif hour < 12:
    print("morning")
elif hour < 18:
    print("afternoon")
else:
    print("evening")


# Part 2
place_to_game = input("where you want to go? ")
match place_to_game:
    case "forest":
        at_the_forest =(input( "they want to hide or walk? ")) 
        if in_the_forest == "hide":
            print("You hide behind a tree")
        elif in_the_forest == "walk":
            print("You find a sleeping wolf")
        else:
            print("Invalid forest action")
    case "cave":
        have_a_torch = "yes"
        at_the_cave = input(" they have a torch? ")
        if have_a_torch != at_the_cave:
            print("It is too dark to enter")
        elif have_a_torch == at_the_cave:
            where_want_to_go = (input("they want to go left or right? "))
            if where_want_to_go == "left":
                print("You find gold")
            elif where_want_to_go == "right":
                print("You find bats")
            else:
                print("Invalid cave path")
    case "river":
         print("You find a boat")
    case _:
        print("Unknown place")
# 2
first_number = float(input("give me first number "))
second_number = float(input("give me second number "))
for_an_action = input("what you choose add, subtract or multiply? ")
if for_an_action == "add":
    print(first_number + second_number)
elif for_an_action == "subtract":
    print(first_number - second_number)
elif for_an_action == "multiply":
    print(first_number * second_number)
else:
    print("Unknown action")
                       


            




     



