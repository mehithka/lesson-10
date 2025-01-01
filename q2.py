upper = int(input("enter an upper range: "))
lower = int(input("enter a lower range: "))

print("the prime numbers between ",upper,'and ',lower,' are: ')
for num in range(lower, upper+1)
if num > 1 :
    for i in range(2,num):
        if (num % i)==0 :
            break
else:
    print(num)