age = int(input("Please enter your age: "))
born = input("Are you a natural born citizen of the U.S. (yes/no)? ").lower()
resided = int(input("How many years have you resided in the U.S.? "))

eligible = age >= 35 and born == "yes" and resided >= 14
if eligible:
    print("You are eligible to run for president of the United States!")
else:
    print("You do not meet the eligibility criteria to run for president.")