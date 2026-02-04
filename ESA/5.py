
#Palindrome For string
n=input("Enter the number to check palindrome:")

if n==n[::-1]:
    print("palindrome")
else:
    print("Not Palindrome")


#PAlindrome For numbers
n=int(input("ENter the num"))
temp=n
rev=0

while n>0:
    rev=rev*10+n%10
    n//=10

if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")