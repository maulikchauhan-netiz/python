print("enter date in given format: DD/MM/YYYY")
date = input("enter date:")
date = date.split("/")
print("date formate is MM/DD/YYYY is :", (date[1],date[0],date[2]))