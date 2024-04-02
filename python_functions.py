import math
import random

def addit(num1, num2):
    added = num1 + num2
    print(f"{num1} + {num2} = {added}")

def subtractit(num1, num2):
    subtracted = num1 - num2
    print(f"{num1} - {num2} = {subtracted}")

def multiplyit(num1, num2):
    multiplied = num1 * num2
    print(f"{num1} * {num2} = {multiplied}")

def divideit(num1, num2):
    if num2 == 0:
        print("No answer to give. Cannot divide any number by zero.")
    else:
        divided = num1 / num2
        print(f"{num1} / {num2} = {divided}")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
calc_type = input("Enter the operator to use.  Choices are +, -, *, /")

allow = "yes"

while True:
    if calc_type == "+":
        addit(num1, num2)
    elif calc_type == "-":
        subtractit(num1, num2)
    elif calc_type == "*":
        multiplyit(num1, num2)
    elif calc_type == "/":
        divideit(num1, num2)
    else:
        break

    allow = (input("Do you want to do another calculation? Enter yes or no. ").lower())

    if allow != "yes":
        break
    else:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a second number: "))
        calc_type = input("Enter the operator to use.  Choices are +, -, *, /")

#2: The Shopping List Maker

shoppinglist = []

def list_items(groceries):
    while True:
        grocery_item = input("Enter your grocery item: ")

        if grocery_item == "end":
            break
        else:
            shoppinglist.append(grocery_item)

def grocery_list(shoppinglist):
#    global shoppinglist
    counter = 1
    for i in range(len(shoppinglist)):
        print(f"{counter}) item is: {shoppinglist[i]}")
        counter += 1

print("Time to make the grocery list!")

list_items(shoppinglist)

print("These are your following grocery items: ")

grocery_list(shoppinglist)

answer = input("Do any item(s) need to be removed from the list? Enter yes or no.")
if answer == "yes":
    while True:
        item_to_remove = input("What is the item you want to remove from the grocery list? ")
        index = shoppinglist.index(item_to_remove)
        shoppinglist.pop(index)
        answer1 = input("Any more items to be removed? ")
        if answer1 == "no":
            print("These are your updated grocery items: ")
            grocery_list(shoppinglist)
            break
        else:
            continue
print("This completes your grocery list.")

#3. The Grade Analyzer

grades = [65, 96, 74, 83, 86, 72, 61, 89]
letter_grades = []

def average_grade():
    sum_grade = sum(grades[i] for i in range(len(grades)))
    avg_grade = sum_grade / (len(grades))
    print(f"The average grade is {avg_grade}.")

def min_max_grades():
    min_grade = min(grades)
    max_grade = max(grades)

    print(f"The lowest grade is {min_grade} , and the highest grade is {max_grade}.")

for i in range(len(grades)):
    if grades[i] >= 90:
        letter_grades.append(grades[i])
        letter_grades.append("A")
    if grades[i] >= 80 and grades[i] <= 89:
        letter_grades.append(grades[i])
        letter_grades.append("B")
    if grades[i] >= 70 and grades[i] <= 79:
        letter_grades.append(grades[i])
        letter_grades.append("C")
    if grades[i] >= 60 and grades[i] <= 69:
        letter_grades.append(grades[i])
        letter_grades.append("D")
    if grades[i] < 59:
        letter_grades.append(grades[i])
        letter_grades.append("F")

average_grade()
min_max_grades()

z = 0

while z in range(len(letter_grades)):
    print(letter_grades[z]) 
    z += 1

#4. The Quiz Game

#Popular Household Items

quiz_answers = ["a", "b", "a", "c", "b", "c"]
user_answers = []

def quiz_starter():
    print("Welcome to the Daily Quiz Show!\n")
    print("This week's topic is Popular Household Items!\n")
    print("There are 6 questions being asked of you, with 3 possible answers to choose from.\n")
    print("Let's see if you can guess these popular household items by their uses.\n")

def quiz_questions():
    j = 0
    while j < 6:
        print("Enter either a for vacuum, b for mop, or c for bag.")  
        quest1 = input("1. What electric household item can you use to pick up dirt from the carpet, floor, and the blinds? ")
        user_answers.append(quest1)
        j += 1
        print("Enter either a for vacuum, b for mop, or c for bag.")
        quest2 = input("2. What household item uses water and soap to clean both walls and floors? ") 
        user_answers.append(quest2)
        j += 1
        print("Enter either a for towel, b for bag, or c for duster.")
        quest3 = input("3. What household item is used to dry of both you and your pets? ")          
        user_answers.append(quest3)
        j += 1
        print("Enter a for brillo pad, b or sock, or c for sponge.")
        quest4 = input("4. What household item is used to clean dishes, tubs, sinks, tiles, and even cars with? ") 
        user_answers.append(quest4)
        j += 1
        print("Enter either a for phone, b for keys, or c for bobbie pin.")
        quest5 = input("5. What household item is used to unlock and open doors and/or safes?")
        user_answers.append(quest5)
        j += 1
        print("Enter either a for dryer, b for sink, or c for washing machine.")
        quest6 = input("6. What household item is used to wash clothes, towels, and blankets in bulk?")
        user_answers.append(quest6)
        j += 1
        

def quiz_results():
    score = 0
    for k in range(len(user_answers)):
        if user_answers[k] == quiz_answers[k]:
            score += 16.67
        else:
            continue
    if score >= 99:
        print(f"Your score is {round(score)}%. Congratulations, you have a perfect score!")
    elif score >= 80:
        print(f"Your score is {round(score)}%.  Not bad.  You made some good guesses.")
    else:
        print(f"Your score is {round(score)}%. You can always try again.")

quiz_starter()
quiz_questions()
quiz_results()
    
#5. The Fitness Tracker

""" All MET's are based on general exercise paces.  They do not account for 
more rigorous or lighter exercises. 
"""
"""
bicycling, 7.5, video game activities, 3.8, calesthenics, 3.5, 
weight training, 3.5, home exercises, 3.8, skipping rope, 12.3
stretching, 2.3, pilates, 3.0, water aerobics, 5.3, aerobics, 7.3
"""

activities = []
activities1 = []
duration_of_acts = []
#total_calcs_burned_inacts = []
#total_calcs_burned = 0.0

def fit_acts():
    print("Welcome to Fitbit Online! Let us help you track your calories burned!")
    print("We have a list of activities to choose from.")
    print("They are: bicycling, calesthenics, weight training")
    print("rope skipping, stretching, pilates, and aerobics")

    while True:
        print("Enter letter next to activity performed.")
        print("a-bicycling, b-calesthenics, c-weight training, d-rope skipping")
        print("e-stretching, f-pilates, g-aerobics")
        activity = input("Enter your activity letter: ")
        activities.append(activity)
        for l in range(len(activities)):
            if activities[l] == "a": #for bicycling
                activities1.append("bicycling")
            if activities[l] == "b": #for calesthenics
                activities1.append("calesthenics")
            if activities[l] == "c": #for weight training
                activities1.append("weight training")
            if activities[l] == "d": #for rope skipping
                activities1.append("rope skipping")
            if activities[l] == "e": #for stretching
                activities1.append("stretching")
            if activities[l] == "f": #for pilates
                activities1.append("pilates")
            if activities[l] == "g": #for aerobics
                activities1.append("aerobics")
        duration = input("Enter your duration in minutes: ")
        duration_of_acts.append(duration)
        #body_weight = input("Enter your body weight: ")
        
        print(f"These are your current activities so far: {activities1[l]}")
        redo = input("Do you have anymore activities to log in for today? Enter yes or no. ")
        if redo == "yes":
            continue
        else:
            break

def calc_activity():
    total_calcs_burned = 0.0
    for m in range(len(activities)):
        if activities[m] == "a": #for bicycling
            met = 7.5
        if activities[m] == "b": #for calesthenics
            met = 3.5
        if activities[m] == "c": #for weight training
            met = 3.5
        if activities[m] == "d": #for rope skipping
            met = 12.3
        if activities[m] == "e": #for stretching
            met = 2.3
        if activities[m] == "f": #for pilates
            met = 3.0
        if activities[m] == "g": #for aerobics
            met = 7.3
        
    body_weight = input("Enter your body weight in pounds (lbs): ")
    kbw = 2.2 * float(body_weight)
    met_calc = (met * 3.5 * round(kbw)) / 200
    calcs_burned = met_calc * float(duration_of_acts[m])
    #total_calcs_burned_inacts.append[calcs_burned]
    total_calcs_burned += calcs_burned

    return round(total_calcs_burned)

def activities_summary():
    for n in range(len(activities)):
        print("A summary of today's activities are listed below.")
        print(f"Activity: {activities[n]}, duration: {duration_of_acts[n]}, calories burned: {star}.")
        print(f"Total calories burned in activies are {star}.")

fit_acts()
calc_activity()
star = calc_activity()
print(star)
activities_summary()






    







            















