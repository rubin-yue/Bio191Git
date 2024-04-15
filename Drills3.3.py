N = int(input('Enter the number of prime numbers to find: '))
count = 0  # Initialize the count of prime numbers found

# Start checking numbers from 2
num = 2
while count < N:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1

           