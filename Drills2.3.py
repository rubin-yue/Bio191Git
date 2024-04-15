f = int(input("Please enter 1st odd integer: "))
s = int(input("Please enter 2nd odd integer: "))
t = int(input("Please enter 3rd odd integer: "))

odd =  f%2 == 1 and s%2 == 1 and t%2 == 1
if odd:
    if f>s: 
        largest = f
    elif s>t :
        largest = s
    else: largest = t
    print(largest, "is the largest integer")
else: print("Entered a not odd integer")
    