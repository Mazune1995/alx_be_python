#!/usr/bin/python3
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
elif priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a medium priority task. Plan to finish it within the week.")
elif priority == "low":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
else:
    print("Invalid priority. Please enter high, medium, or low.")
#
