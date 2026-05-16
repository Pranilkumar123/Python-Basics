# 4. WAP to find the gretest of 3 numbers enetered by the user

a = int(input("Enter number 1 :"))

b = int(input("Enter number 2 :"))

c = int(input("Enter number 3 :"))

if (a>b and a>c):
    print(a,"is greater")
elif(b>a and b>c):
    print(b,"is greater")
elif(c>a and c>b):
    print(c,"is greater" )