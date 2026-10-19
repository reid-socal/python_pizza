cost = 0
del_cost = 0


order = input("what do you want? Large or Small Pizza")
distance = int(input("what is the distance? "))
toppings = int(input("How many additional toppings? "))

if order.lower() == "small":
    cost = 8
elif order.lower() == "large":
    cost = 12
else:
    print("I do not understand")
    exit()

cost = cost + toppings

if distance <= 5:
    del_cost = 2
else:
    del_cost = 2 + (distance - 5)

total_cost = cost + del_cost


print(f'your cost is {total_cost}')