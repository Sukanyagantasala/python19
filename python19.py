1
22
333
4444
55555
n=int(input("enter a number"))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(i,end=" ")
  print()
  
#palindrome number
num=int(input("enter a number"))
temp=num
rev=0
while num>0:
  rem=num%10
  rev=rev*10+rem
  num=int(num/10)
if rev==temp:
  print(temp"is a palindrome")
else:
  print(temp "is Not a palindrome")
  
#Armstrong number
num=int(input("enter a number"))
temp=num
sum=0
l=len(num)
while num>0:
  rem=num%10
  sum=sum+(rem**l)
  num=num//10
if temp==num:
  print("armstrong)
else:
  print("Not an armstrong)
#calculate the area of triangle,square and rectangle
b=int(input("enter a number"))
h=int(input("enter a number"))
s=int(input("enter a number"))
l=int(input("enter a number")
area_t=0.5*b*h
area_sq=s*s
area_r=l*b
print(area_t)
print(area_sq)
print(area_r)
#swap three numbers
#Fibonacci series
n=int(input())
a=0
b=1
if n==0:
      print("not possible")
elif n==1:
      print("not possible")
else:
  for i in range(n):
      c=a+b
      print(c,end=" ")
      a=b
      b=c
      
 
  
  
