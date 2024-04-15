age = int(input("What is your age?  "))
if age > 15:
    ulicense = input("Do you have a fishing license (yes/no)?  ").lower()
    if age > 15 and ulicense == "yes":
        print("You are legal to fish in MN.")
    else: print("You are not legal to fish in MN")
elif age <= 15: 
    plicense = input("Does your parent have a fishing license (yes/no)?  ").lower()
    if age <= 15 and plicense == "yes":
        print("You are legal to fish in MN.")
    else: print("You are not legal to fish in MN")