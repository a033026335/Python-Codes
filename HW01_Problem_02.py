#Name: Alex Su (G01090136)
#Class: SYST 230_001
#Assignment_01 (Due 9/13/20)
#Prof. Raza Hashim
#Problem 2[25 Points]: Continuously compounded interest. Compose a program that calculates and writes the amount of money you would have if you invested it at a given interest rate compounded continuously, taking the number of years t, the principal P, and the annual interest rate r as command-line arguments. The desired value is given by the formula Pe^(rt) e=math.e.
import math

#Have user imput the year(s)
t = int(input("Input the year(s): "))

#Have user imput the principal
P = int(input("Input the principal:$ "))

#Have user imput the annual interest rate
r = int(input("Input the annual interest rate (%): "))

#Apply user's input to continuously compounded interest formula Pe^(rt)
C = P*(math.e**((r/100)*t))

#Print out continuously compounded interest
print("The continuously compounded interest is: $", C)
