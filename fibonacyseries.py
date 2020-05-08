#A phython program to print Fibonacci number.

a=int(input("How many terms required to print Fibonacci series? "))

# first two terms
num1, num2 = 0, 1
c = 0

# check if the number of terms is valid
if a <= 0:
   print("Please enter a positive integer")
elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while c < a:
       print(num1)
       num = num1 + num2
       # update values
       num1 = num2
       num2 = num
       c += 1
