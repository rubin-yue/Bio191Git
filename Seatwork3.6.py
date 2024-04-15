n = int(input("Input side lenght "))
for i in range(n):
        print("*" * n, end="  ")
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")      