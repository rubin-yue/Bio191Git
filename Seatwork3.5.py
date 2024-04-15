n= int(input("Get multiplication table: "));print('\n')
print('\t\t\t\tMutliplication table of', n, end='\n')
print('\t')
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end='\t')
    print('                                                        \n')
print()

