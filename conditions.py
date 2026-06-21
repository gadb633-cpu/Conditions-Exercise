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
