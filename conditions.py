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
                
     



