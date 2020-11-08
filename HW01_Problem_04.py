#Name: Alex Su (G01090136)
#Class: SYST 230_001
#Assignment_01 (Due 9/13/20)
#Prof. Raza Hashim
#Problem 4 [25 Points]:  Order check. Compose a program that accepts three floats x, y, and z as command-line arguments and writes True if the values are strictly ascending or descending (x < y < z or x > y > z), and False otherwise.
  
# creating an empty array
array = []
  
# Given number of elemetns as input for x, y and z
n = int(3)
  
# iterating till the range
for i in range(0, n):
    ele = int(input("Enter 3 numbers:"))
    
    # adding the element
    array.append(ele)

#Print true when ascending
if array[0] < array[1] < array[2]:
    print("True")
    
#Print true when descending
elif array[0] > array[1] > array[2]:
    print("True")
    
#Print fales when otherwise
else:
    print("Fales")
