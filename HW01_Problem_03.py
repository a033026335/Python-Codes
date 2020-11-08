#Name: Alex Su (G01090136)
#Class: SYST 230_001
#Assignment_01 (Due 9/13/20)
#Prof. Raza Hashim
#Problem 3 [25 Points]: Wind chill. Given the temperature T (in degrees Fahrenheit) and the wind speed v (in miles per hour), the National Weather Service defines the effective temperature (the wind chill) to be:w = 35.74 + 0.6215 T + (0.4275 T – 35.75) v**(0.16). Compose a program that takes two floats t and v from the command line and writes out the wind chill. Note: This formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3 (you may assume that the values you get are in that range).
import math

#Have user imput the temperature
T = int(input("Input the temperature (F): "))

#Not valid if t is larger than 50 in absolute value, then print invalid temperature
if abs(T) > 50:
    print("Invalid temperature.")
else:

    #Have user imput the wind speed
    v = int(input("Input the wind speed (m/h): ")) #Have user imput the wind speed
if v not in range (3, 120):
    print("Invalid wind speed (m/h).")
else:
    w = 35.74 + (0.6215*T) + (((0.4275*T)-35.75)*(v**(0.16)))
    print("The wind chill is", w,"F") #Print out the wind chill
