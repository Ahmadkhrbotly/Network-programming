binary = input('Enter 8 bits in binary system: ')
list = list(binary)
ans = 0
for i in range(len(list)):
    digit = list.pop()
    if digit =='1':
        ans = ans + pow(2,i)
print('The decimal value of the number is: ',ans)
