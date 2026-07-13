#expense traker
from datetime import datetime

# Get current hour
hour = datetime.now().hour

if 5 <= hour < 12:
    print("----------🌅 Good Morning! MAULIK----------")
elif 12 <= hour < 17:
    print("----------☀️ Good Afternoon! MAULIK----------")
elif 17 <= hour < 21:
    print("----------🌇 Good Evening! MAULIK----------")
else:
    print("🌙 Good Night! MAULIK")
expenses=[]
print("Welcome to expenses traker Maulik")


while True:
        print("----------MENU----------")
        print("1.Add expense")
        print("2.view expense")
        print("3.view total spending")
        print("4.exit")

if choice==1:
     print        
