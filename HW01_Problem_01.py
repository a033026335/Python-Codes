#Name: Alex Su (G01090136)
#Class: SYST 230_001
#Assignment_01 (Due 9/13/20)
#Prof. Raza Hashim
#Problem 1 [25  Points]:  Compose a program that takes two integers m and d from the command line and writes True if day d of month m is between March 20 and June 20, and False otherwise. (Interpret m with 1 for January, 2 for February, and Februaryso forth.)

#Have user imput the month
m = int(input("Input the month: "))

#If the user's input is not in the range of Jan to Dec (1-12). It will ask to enter a valide month (1-12)
if m not in range (1, 13):
    print("Please enter valid month!")
    
#If user enter corret range of month contine to entering the day
else:

    #Have user imput the day
    d = int(input("Input the day: "))
    
    #If the user's input is not in the maximun range of day (1-31). It will ask to enter a valide day (1-31)
    if d not in range (1, 32):
        print("Please enter valid day!")
        
    #If user enter corret range of month and day contine to validate T and F
    else:
    
        #If dates is in between March 20 to June 20, print True.
        if(m == 3) and d in range (20, 32):
            print("True")
        elif (m == 4) and d in range (1, 31):
            print("True")
        elif (m == 5) and d in range (1, 32):
            print("True")
        elif (m == 6) and d in range (1, 21):
            print("True")
            
        #If dates is outside of March 20 to June 20, print Fales.
        else:
            print("Fales")
