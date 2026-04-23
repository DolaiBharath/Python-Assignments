num=int(input("enter a number:"))
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print(num,"is a not prime number")
            break
        else:
            print("is a prime number")
else:
    print("is a not prime number")