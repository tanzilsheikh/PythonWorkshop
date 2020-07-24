def compound_interest(principle, rate, n): 

  

    # Calculates compound interest  

    Amount = principle * (pow((1 +(n * rate) / 100), n)) 

    CI = Amount - principle 

    print("Compound interest is", CI) 

  
# Driver Code  

compound_interest(10000, 10.25, 5)
