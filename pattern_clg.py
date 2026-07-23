#1

for i in range(7):
    for j in range(1,i):
        print(j,end = " ")
    print()  
print("=====================")

#2

print()
for i in range(1,7):
    for j in range(i,6):
         print(j,end=" ")
    print()    
print("=====================")

#3

for i in range(6):
    for j in range(i):
        print("*",end = " ")
    print()  
print("=====================")

#4

print()
for i in range(5):
    for j in range(i,5):
         print("*",end=" ")
    print()    
print("=====================")

#5

rows = 3

for i in range(1, rows + 1):

    # Print spaces  
    for j in range(rows - i):
        print(" ", end=" ")

    # Print numbers
    for j in range(1, i + 1):
        print(j, end="   ")
    print()
   
print("===========================")

#6

row=3
for i in range(1, rows + 1):

    # Print spaces  
    for j in range(rows - i):
        print(" ", end=" ")

    # Print numbers
    for j in range(1, i + 1):
        print("*", end="   ")

    print()
   
print("===========================")
#7

row=5
for i in range(1, row + 1):

    # Print spaces  
    for j in range(row - i):
        print(" ", end=" ")

    # Print numbers
    for j in range(1, i + 1):
        print("*", end="   ")

    print()

    
    