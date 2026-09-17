#Unit 3.1
#Beginner

inventory = {"apples": 50, "bananas": 30, "oranges": 25}

for item, quantity in inventory.items():
    print(item)
print(sum(inventory.values()))
for item, quantity in inventory.items():
    print(item, quantity)
    
#Intermediate

prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
for key in sorted(prices):
    print(key)
for key in sorted(prices, key=prices.get):
    print(key)
for key, value in sorted(prices.items(), key = lambda x: x[1]):
    print(key, value)

#Advanced

temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}
print(sum(temps.values()) / len(temps.values()))
for key, value in temps.items():
    if value == max(temps.values()):
        print(key, value)
    elif value == min(temps.values()):
        print(key, value)
above_average = 0
for key, value in temps.items():
    if value > sum(temps.values()) / len(temps.values()):
        above_average += 1
print(above_average)

#Unit 3.2

#Beginner

products = {
"laptop": {"price": 999, "stock": 15},
"phone": {"price": 699, "stock": 50}
}
print(products["laptop"]["price"])
for item in products:
    print(item, products[item]["stock"])
    
#Intermediate

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
countries_dict = {}
for country, capital in zip(countries, capitals):
    countries_dict[country] = capital

products["tablet"] = {"price": 449, "stock": 30}
for item in list(products):
    if products[item]["stock"] < 20:
        del products[item]


#Advanced
company = {
"Engineering": {"Alice": 95000, "Bob": 85000},
"Marketing": {"Carol": 75000, "Dave": 70000}
}
highest_salary = 0
highest_paid = ""
for department, employees in company.items():
    print(employees)
    average = sum(employees.values()) / len (employees.values())
    print(f" The average salary for {department} is {average:.0f}")
    for employee, salary in employees.items():
        if salary > highest_salary:
            highest_salary = salary
            highest_paid = employee
print(f"The highest paid employee is {highest_paid}")

#Unit 3.3

#Beginner

cubes = {x: x**3 for x in range(1, 6)}
print(cubes)
    
temps = {"Mon": 72, "Tue": 68, "Wed": 75} 
celsius_temps = {}
for day, temp in temps.items():
    celsius_temps[day] = (temp-32) / 1.8  
print(celsius_temps)

#Intermediate

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
passing = {}
letter_grades = {}
for student, grade in scores.items():
    if grade >= 90:
        letter_grades[student] = "A"
    elif grade >= 80:
        letter_grades[student] = "B"
    elif grade >= 70:
        letter_grades[student] = "C"
    elif grade >= 60:
        letter_grades[student] = "D"
    else:
        letter_grades[student] = "F"
    if grade >= 70:
        passing[student] = grade

print(passing)
print(letter_grades)
student_ids = {"Alice": 101, "Bob": 102}
by_id = {number:student for student, number in student_ids.items()}
print(by_id)

#Advanced

sales = [
("North", "Alice", 5000), ("South", "Bob", 4500),
("North", "Carol", 6000), ("South", "Alice", 3500)
]
by_region = {}
by_salesperson = {}
for item in sales:
    by_salesperson[item[1]] = by_salesperson.get(item[1], 0) + item[2]
for item in sales:
    by_region[item[0]] = by_region.get(item[0], 0) + item[2]

print(by_region)
print(by_salesperson)
nested_dict = {}
for item in sales:
    if nested_dict.get(item[0], 0) == 0:
        nested_dict[item[0]] = {}
    nested_dict[item[0]][item[1]] = nested_dict[item[0]].get(item[1], 0) + item[2]
print(nested_dict)

# Unit 4.1

#Beginner

vowels = set(["a", "e", "i", "o", "u"])
numbers = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(numbers)
print(len(numbers))
#empty = {}
#This creates a dictionary

#Intermediate

text = "mississippi"
unique_text = set(text)
print(unique_text)
print(len(unique_text))
emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = set(emails)
emails = list(unique_emails)
print(emails)
#s = {[1, 2], [3, 4]}
#Lists are not hashable and cannot be used in sets

#Advanced

import time
long_list = list(range(10000000))
list_start = time.time()
999999 in long_list
list_end = time.time() - list_start
print(f"List time: {list_end:.10f} seconds")

long_set = set(range(10000000))
set_start = time.time()
999999 in long_set
set_end = time.time() - set_start
print(f"Set time {set_end:.10f} seconds")

fs = frozenset([1, 2, 3])
fs_dict = {fs: 0}
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
edge_set = set(sum(edges, ()))
print(edge_set)


#Unit 4.2

#Beginner

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)
#Intermediate

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}


print(morning_shift & evening_shift & weekend_shift)
print(morning_shift | evening_shift | weekend_shift)
print(morning_shift - evening_shift - weekend_shift)
print(morning_shift ^ evening_shift ^ weekend_shift)

#Advanced

prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

print(prereqs_met & has_space & paid_tuition)
print(prereqs_met - paid_tuition)
print(prereqs_met ^ paid_tuition)


#Unit 4.3

#Beginner

numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(1)
even_numbers = {x for x in range(20) if x % 2 == 0}
print(even_numbers)
#numbers.remove(5)
numbers.discard(5)


#Intermediate

numbers_list = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
def unique_ordered(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(unique_ordered(numbers_list))

sentence = "To be or not to be that is the question"
sentence = sentence.lower()
unique_sentence = {x for x in sentence.split()}
print(unique_sentence)

expected = set(range(1, 11)) # 1 through 10
actual = {1, 2, 4, 5, 7, 8, 10}
# What numbers are missing?
missing = expected - actual
print(missing)


#Advanced

def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates    

print(find_duplicates([1, 2, 2, 3, 3, 3, 4])) # {2, 3}

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

print(alice & bob & carol)
print(alice - bob - carol)
print((alice ^ bob ^ carol) - (alice & bob & carol))

def common_chars(string1, string2):
    all_characters = [char.lower() for char in string1 + string2 if char.isalpha()]
    seen = set()
    common = set()
    for char in all_characters:
        if char in seen:
            common.add(char)
        else:
            seen.add(char)
    return common

print(common_chars("hello", "world")) # {'l', 'o'}

