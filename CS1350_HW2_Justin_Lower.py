#Unit 1.1

#Beginner

my_info = {"name": "Justin", "age": 19, "major": "cybersecurity"}

#Intermediate

menu = {"pie": 4.50, "cake": 6.00, "cookie": 2.50, "brownie": 3.00}
course_credits = {"CS1350": 3, "IS2180": 3, "NET2300": 3}

#Advanced

weekly_temps = dict(Monday=77, Tuesday=85, Wednesday=83, Thursday=72, Friday=68, Saturday=91, Sunday=88)


#Unit 1.2

#Beginner

pet = {"name": "Buddy", "type": "dog", "age": 3}
print(pet["name"])
print(pet["age"])

#Intermediate

print(pet.get("color", "unknown"))

#Advanced

products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}

price = products.get("laptop", "Product not available")
print(price)
price = products.get("phone", "Product not available")
print(price)

#Unit 1.3

#Beginner

inventory = {}
inventory["apples"] = 10
inventory["oranges"] = 5
inventory["bananas"] = 15

#Intermediate

scores = {"Team A": 45, "Team B": 38}
scores["Team B"] = 52
scores["Team C"] = 41
score = scores.pop("Team A")
print(score)

#Advanced

cart = {}
cart["bread"] = 3.50
cart["milk"] = 5.00
cart["eggs"] = 2.50
cart["bread"] = 4.00
removed = cart.pop("eggs")
print(removed)
print(cart)

#Unit 2.1

#Beginner 

"student_name" # Valid (reason: it is a string)
[1, 2, 3] # Invalid (reason: it is a list)
100 # Valid(reason: it is a number)
("x", "y") # Valid (reason: it is a tuple)
{"a": 1} # Invalid (reason: it is a dictionary)
frozenset({1,2}) # Invalid (reason: it is a set)

#Intermediate

locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}

data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data)) 
# it will print {"a": 3, "b": 4} then it will print 2

print(hash("Justin"))
print(hash(100))
#Advanced

high_scores = {("Alice", "Tetris"):50000, ("Bob", "Pac-man"): 100000, ("Carol", "Super Mario Bros"): 250000}
print(high_scores[("Alice", "Tetris")])

long_list = list(range(100000))
long_dict = {i for i in range(100000)}
import time
start = time.time()
result = 99999 in long_list
list_time = time.time() - start

start = time.time()
result = 99999 in long_dict
dict_time = time.time() - start
print(f"List time: {list_time:.6f} seconds")
print(f"Dict time: {dict_time:.6f} seconds")
print(f"Dict is {list_time/dict_time:.0f}x faster")

#Unit 2.2

#Beginner

temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(len(temps.keys()))

#Intermediate

print(max(temps.values()))
print(min(temps.values()))
if "Friday" in temps.keys():
    print("Friday is in the dictionary")
else:
    print("Friday is not in the dictionary")
keys_list = temps.keys()
print(keys_list)
temps.setdefault("Thursday", 70)
print(keys_list)

#Advanced

prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
prices_list = list(prices.values())
print(prices_list)
print(sum(prices_list))
print(f"{sum(prices_list)/len(prices_list):.0f}")
max_product, max_value = max(prices.items(), key=lambda x: x[1])
print(f"{max_product}, {max_value}")
import sys
keys_list = list(prices.keys())
print(f"View: {sys.getsizeof(prices.keys())} bytes")
print(f"List: {sys.getsizeof(list(keys_list))} bytes")
prices.update({"TV": 749, "desktop": 899, "keyboard": 199})
print(prices)


#Unit 2.3

#Beginner

colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
    print(f"The {fruit} is {color}")

#Intermediate

prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
for product, price in prices.items():
    print(f"{product}: {price} + tax = {price * 1.1:.2f}")
count = 0
for price in prices.values():
    if price > 4:
        count+=1
print (f"{count} items cost more than $4.00")
x = 10
y = 20
x, y = (y, x)
print(x)
print(y)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)
print(middle)
print(last)

#Advanced
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
max_name, max_grade = max(scores.items(), key=lambda x: x[1])
print(f"{max_name} had the highest score")
passed = {}
failed = {}
for name, grade in scores.items():
    if grade >= 70:
        passed[name] = grade
    else:
        failed[name] = grade
print(passed)
print(failed)
average = sum(scores.values()) / len(scores)
average = round(average)
print(average)
deviations ={}
for name, grade in scores.items():
    deviation = grade - average
    deviations[name] = deviation
print(deviations)
big_dict = {i: i for i in range(50000)}
items_start = time.time()
for key, value in big_dict.items():
    _ = key + value
items_time = time.time() - items_start
keys_start = time.time()
for key in big_dict.keys():
    value = big_dict[key]
    _ = key + value
keys_time = time.time() - keys_start
print(f"Items is {keys_time - items_time:.3f} seconds faster")