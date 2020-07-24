def odd_even(num):
  if num%2==0:
    print("The number is even")
  else:
    print("The number is odd")

def fact(num):
  fact=1
  if num==0:
    print("Factorial of 0 is 1")
  else:
    for i in range(1,num+1):
      fact=fact*i
    print("The factorial of",num,"is",fact)

def odd(num):
  for i in range(0,num+1):
    if (i%2)!=0:
      print(i)

def prime(num):
  for num in range(1, num+1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

loop=1
choice=0
while loop == 1:
  print ("Welcome to menu")
  print ("your options are:")
  print (" ")
  print("1) Find odd or even number")
  print("2) find factorial")
  print("3) find all odd number")
  print("4) find prime number")
    
  print(" ")
  try:
    choice = int(input("Choose your option: "))
  except:
    print('please enter a valid number for option')
    print(" ")
    print(" ")

  if choice==1:
    number=int(input("enter the number:"))
    print("Result:",odd_even(number))
  elif choice==2:
    number=int(input("enter the number:"))
    print("Result:",fact(number))
  elif choice==3:
    number=int(input("enter the number:"))
    print("Result:",odd(number))
  elif choice==4:
    number=int(input("enter the number:"))
    print("Result:",prime(number))
  elif choice == 5:
    loop = 0
     
  else:
    print("please choice a valid option from 1 to 5")
    choice=0
