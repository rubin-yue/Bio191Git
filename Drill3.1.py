N = int(input('Enter No. '))
print(N)

for i in range(1, N + 1): #loop for rows
   for j in range(1, i + 1): #loop for collumns
      print("*",end='') 
   print()

