#Driving licence checker
#This program uses conditionals if, elif and else
age = int(input("Please enter your age: "))

#the syntax is important, the conditional line ends with a ":"
#the next line is indented, it will run if the condition is TRUE
if age > 17:
    print("you are eligible to apply for a Driving Licence")

elif age ==17:
    print("you can apply for a provisional driving licence")
    
else:
    print("you are not eligible for a driving licence")