# WAP to check if a list contain a palindrome of elements.

P = []
P.append(int(input("Enter 1st number : ")))
P.append(int(input("Enter 2nd number : ")))
P.append(int(input("Enter 3rd number : ")))
q = P.copy()
q.reverse()
if(P == q):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# OR

P = []
P.append(int(input("Enter 1st number : ")))
P.append(int(input("Enter 2nd number : ")))
P.append(int(input("Enter 3rd number : ")))
q = P[::-1]
if(P == q):
    print("It is a palindrome")
else:
    print("It is not a palindrome")