n1 = 5
n2 = 10
n3 = 15
n4 = 20

  

mx = (n1 if (n1 > n2 and n1 > n2 and n1 > n4)  

         else (n2 if (n2 > n3 and n3 > n4)  

         else (n3 if n3 > n4 else n4))) 

  
# str() function is used to convert integer to string, it is required as we are concatenating integers with string 

print("Largest number among " + str(n1) + ", " + 

            str(n2) + ", " + str(n3) + " and " + 

            str(n4) + " is " + str(mx))
