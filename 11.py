str3="maulik"
print(str3[0])
print(str3[5])
print(len(str3))

#slicing
str1="gulabjamun"
print(str1[0:5])
print(str1[:10])
print(str1[:9])
print(str1[9])

firsthalf=str1[0:5]
print(firsthalf)

str2="pizzaa"
print(str2[2:5])
print(str2[4:6])

#slicing practice question
food=input("enter the food item")
mid=len(food)//2
output1=food[mid-1:mid+2]
print(output1)

output2=food[-2:]
print(output2)