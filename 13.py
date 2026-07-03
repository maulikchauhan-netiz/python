#conditinal statements


#if else

marks=99
if(marks>=90):
    print("grade A")
else:
    print("grade B")


age=18
if(age>=18):
    print("you are eligible")
else:
    print("you are not eligible")


#elif

marks=int(input("enter the marks"))

if(marks>=90):
    print("grade A")
elif(marks>=60):
    print("grade B")
elif(marks>=50):
    print("grade C")
else:
    print("fail")            


#pratice question

num=int(input("enter the number"))
if(num>0):
    print("positive")
elif(num==0):
    print("zero")
elif(num<0):
    print("negative")
else:   
    print("invalid")         