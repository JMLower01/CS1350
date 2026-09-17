# Contact records: name -> dictionary of details
contact_book = {
 "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
        "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
"Sister": {"phone": "555-7777", "category": "Family", "city":
"Chicago"},
"Best Friend": {"phone": "555-8888", "category": "Friend", "city":
"Indianapolis"},
"Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
"Boss": {"phone": "555-0000", "category": "Work", "city":
"Chicago"},
"Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
"Dentist": {"phone": "555-2222", "category": "Business", "city":
"Indianapolis"},
}
# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
"Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
"Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
"Sister": {"Jan": 80, "Mar": 70},
"Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
"Roommate": {"Feb": 15, "Mar": 25},
"Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
"Professor": {"Feb": 20, "Mar": 35},
"Dentist": {"Jan": 10},
}
#Created an empty dictionary quick_contacts and add five entries (name → phone string):
quick_contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Best Friend": "555-8888",
    "Pizza Place": "555-9999",
    "Work": "555-0000",
}
print("=== Phase 1: Quick Contacts ===")
#Printed Quick Contacts
print(quick_contacts,"\n")
print("--- Access and Modify ---")
#Printed Mom's number using bracket notation.
print("Mom's number is:", quick_contacts["Mom"])
#Updated Dad's number to "555-4321".
contact_book["Dad"]["phone"] = "555-4321"
#Added "Dentist": "555-2222".
quick_contacts["Dentist"] = "555-2222"
#Look up "Grandma" with get(), printing Contact not found when the key is missing. Do not let the program crash.
print("Grandma's number is:", quick_contacts.get("Grandma", "Not found"))
#Printed the updated dictionary.
print("The updated quick contact dictionary is:", quick_contacts,"\n")

print("--- Delete and Analyze ---")
#Removed "Pizza Place" with del
del quick_contacts["Pizza Place"]
#Remove "Work" with pop(), saving the old number in old_work, and print it.
old_work = quick_contacts.pop("Work")
print("Your old work number was:", old_work)
#Print the number of contacts left with len(), then the names with keys() and the numbers with values(), each wrapped in list().
print("The number of quick contacts left is:", len(quick_contacts))
#We lost the pizza place 🙁 and replaced the work number
print("The names of those contacts are:", list(quick_contacts.keys()))
print("The numbers of those contacts are:", list(quick_contacts.values()))
total_minutes = {}
for contact, calltime in call_log.items():
    months_called = 0
    total_time = 0
    busiest_month, busiest_time = max(calltime.items(), key = lambda x: x[1])
    average = sum(calltime.values())/ len(calltime.values())
    for month, time in calltime.items():
        months_called+=1
        total_time = total_time + time
    print(f"{contact}: {months_called} month(s), {total_time} min total, avg: {average:.2f}, busiest: {busiest_month} ({busiest_time})")
    total_minutes[contact] = total_time
    
month_stats = {"Jan": {"minutes": [], "total": 0, "avg": 0, "contacts": 0 }, "Feb": {"minutes": [], "total": 0, "avg": 0, "contacts": 0}, "Mar": {"minutes": [], "total": 0, "avg": 0, "contacts": 0}}

for contact, calltime in call_log.items():
    for month, time in calltime.items():
        month_stats[month]["minutes"].append(time)
        month_stats[month]["total"]+= time
        month_stats[month]["contacts"]+= 1
for month, index in month_stats.items():
    month_stats[month]["avg"] = month_stats[month]["total"]/ len(month_stats[month]["minutes"])
print(month_stats)
for month in sorted(month_stats, key = lambda x: month_stats[x]["avg"], reverse = True):
    print(f"{month}: {month_stats[month]["total"]} min total, {month_stats[month]["avg"]:.2f} avg {month_stats[month]["contacts"]} contacts")
    
minutes_by_category = {"Family": 0, "Friend": 0, "Work": 0, "Business": 0}
minutes_by_city = {"Fort Wayne": 0, "Chicago": 0, "Indianapolis": 0}
contacts_per_city = {"Fort Wayne": 0, "Chicago": 0, "Indianapolis": 0}
for contact, value in contact_book.items():
    for key, item in value.items():
        if key == "category":
            minutes_by_category[item] += total_minutes[contact] 

for contact, value in contact_book.items():
    for key, item in value.items():
        if key == "city":
            contacts_per_city[item] += 1
            minutes_by_city[item] += total_minutes[contact]

phone_book = {key: value["phone"] for key, value in contact_book.items()}
local_contacts = {key: value["phone"] for key, value in contact_book.items() if value["city"] == "Fort Wayne"}
activity_level = {key: "Frequent"  if  value >= 200 else "Occasional" for key, value in total_minutes.items()}
print(f"Phone book: {phone_book}")
print(f"Local contacts: {local_contacts}")
print(f"Activity level: {activity_level}")

print("\nPhone Book")
for key, value in phone_book.items():
    print(f"{key}: {value}")
print("\nLocal Contacts")
for key, value in local_contacts.items():
    print(f"{key}: {value}")
print("\nActivity Level")
for key, value in activity_level.items():
    print(f"{key}: {value}")
print()
def get_tier(minutes):
    if total_minutes.get(minutes, 0) >= 400:
        return "Platinum"
    elif total_minutes.get(minutes, 0) >= 200:
        return "Gold"
    elif total_minutes.get(minutes, 0) >= 100:
        return "Silver"
    elif total_minutes.get(minutes, 0) >= 50:
        return "Bronze"
    else:
        return "Inactive"
for contact in total_minutes:
    print(f"{contact}: {total_minutes[contact]} min ({get_tier(contact)})")
tier_counts = {"Platinum": 0, "Gold": 0, "Silver": 0, "Bronze": 0, "Inactive": 0}
for contact in total_minutes:
    if get_tier(contact) == "Platinum":
        tier_counts["Platinum"] +=1 
    elif get_tier(contact) == "Gold":
        tier_counts["Gold"] +=1
    elif get_tier(contact) == "Silver":
        tier_counts["Silver"] +=1
    elif get_tier(contact) == "Bronze":
        tier_counts["Bronze"] +=1
    else: 
         tier_counts["Inactive"] +=1
for tier, count in tier_counts.items():
    print(f"{tier}: {count}")
top_minutes = 0
bottom_minutes = 999   
for contact, minutes in total_minutes.items():
    if minutes > top_minutes:
        top_minutes = minutes
    elif minutes < bottom_minutes:
        bottom_minutes = minutes
for contact, minutes in total_minutes.items():
    if minutes == top_minutes:
        print(f"Most contacted: {contact} ({minutes} min)")
    if minutes == bottom_minutes:
            print(f"Least contacted: {contact} ({minutes} min)")
grand_total = 0
for contact, minutes in total_minutes.items():
    grand_total += minutes
average = grand_total / len(total_minutes.values())
print(f"Total minutes: {grand_total}")
print(f"Average per contact: {average:.2f}")
for contact, minutes in total_minutes.items():
    if minutes > average:
        print(f"{contact}: {minutes}")

for contact in sorted(total_minutes, key = lambda x: total_minutes[x], reverse = True):
    print(f"{contact}  {contact_book[contact]["category"]}  {contact_book[contact]["city"]}  {total_minutes[contact]}  {get_tier(contact)}")
print(f"{len(contact_book)} contacts | {grand_total} minutes | {average} average")
  

    
