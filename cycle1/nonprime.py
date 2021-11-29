first=int(input("enter the lowerlimit:"))
last=int(input("enter the upperlimit:"))
for num in range(first,last + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i == 0):
                print(num)
                break

