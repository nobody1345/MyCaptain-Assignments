# Python Program for fibonacci sequence

a = int(input ("Number of terms: "))  
 
b = 0  
c = 1  
d = 0  
if a <= 0:  
    print ("Invalid Input")   
elif a == 1:  
    print ("The Fibonacci sequence of the numbers up to 1:")  
    print(b)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while d < a:  
        print(b)  
        nth = b + c   
        b = c  
        c = nth  
        d += 1 
