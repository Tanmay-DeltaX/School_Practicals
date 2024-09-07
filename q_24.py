num  = int(input("Enter your number"))
a = 0
for i in range(2,num):
    if num%i==0:
        a+=1

if a>0:
    print('It is not a prime number')

else:
    print("It is a prime number")