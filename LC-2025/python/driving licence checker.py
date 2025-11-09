#Driving licence checker
age = int(input("Please enter your age: "))

if age > 17:
    print("you are eligible to apply for a Driving Licence")

elif age ==17:
    print("you can apply for a provisional driving licence")
    
else:
    print("you are not eligible for a driving licence")