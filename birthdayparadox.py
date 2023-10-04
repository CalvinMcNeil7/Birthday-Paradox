import random

#making list of months of the year and list of the number of days in each month. These will be used to create random days of the year.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

# 2 counters are made for looping through the birthday paradox process 100,000 times and to track how many times there were duplicate birthdays
completed_sim_counter = 0
birthday_paradox_success = 0

# Prompting user to input how many birthdays they want per simulation. Also creating those random birthdays by grabbing a month at random and using its index number to get a random day of the month. both pieces are concatenated and appended to a list called "birthdays"
no_of_birthdays = int(input("How many birthdays shall I generate? (Max 100): "))
birthdays = []
for num in range(no_of_birthdays):
    random_month = random.choice(months)
    random_day = random.randint(1, month_days[months.index(random_month)])
    birthdays.append(random_month + " " + str(random_day))

# showing a visual test run of the simulation on screen to user
print(f"Here are {str(no_of_birthdays)} birthdays: ")
for birthday in birthdays:
    print(birthday)
    
# using dictionary comprehension to determine if there were duplicates
dupe_check = [x for x in birthdays if birthdays.count(x) > 1]
if len(dupe_check) > 0:
    print(f"In this simulation, multiple people have a birthday on {dupe_check[0]}")
else:
    print("In this simulation, nobody had the same birthday.")
    
print(f"\nGenerating {no_of_birthdays} birthdays 100,000 times...")
input("Press Enter to begin...")

#simulation is ran 100,000 times. each iteration increases the sim counter by one to ensure it is run 100,000 times. the success counter it incremented if there were duplicates
while completed_sim_counter <= 100000:
    birthdays = []
    for num in range(no_of_birthdays):
        random_month = random.choice(months)
        random_day = random.randint(1, month_days[months.index(random_month)])
        birthdays.append(random_month + " " + str(random_day))
    
    dupe_check = [x for x in birthdays if birthdays.count(x) > 1]
    
    if len(dupe_check) > 0:
        birthday_paradox_success += 1
    completed_sim_counter += 1
    
#results of the 100,000 simulations are printed out with additional info. The success rate is calculated by dividing the number of successful simulations by 100,000 and that percentage is printed.
print(f"Out of 100,000 simulations of {no_of_birthdays} people, there was a matching birthday in that group {birthday_paradox_success} times. This means that {no_of_birthdays} people have a {100 * round(birthday_paradox_success/100000,2)}% chance of having a matching birthday in their group.")
print("That's probably more than you would think!")