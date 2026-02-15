"""
Day 1 - Python Basics
Topic: Conditional Statements & Exception Handling
Author: Madhavan
"""

try:
    salary = float(input("Enter your monthly salary: "))

    if salary >= 70000:
        print("You are eligible 👍 for a loan 💸 of 10 Lakhs with 11.5% interest.")
        print("Please click this link to apply for loan 👉 <<<loan link>>>")
    elif salary >= 40000:
        print("You are eligible 👍 for a loan 💸 of 5 Lakhs with 12.75% interest.")
        print("Please click this link to apply for loan 👉 <<<loan link>>>")
    else:
        print("You are not eligible for a loan.")

except ValueError:
    print("Invalid input! Please enter numbers only.")
