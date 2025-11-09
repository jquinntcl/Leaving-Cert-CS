#iteration - While loop

#a program to print the numbers from 1 - 10
counter = 0
while counter<10:
    print(counter)
    counter += 1 #incrementing the counter

#we want the program to print/display the numbers between start number and end no.
#so we use inputs and we ask the user to enter integers (whole numbers)
start_number = int(input("Enter your start number: "))
end_number = int(input("Enter your end number: "))

while start_number<end_number:
    print(start_number)
    start_number+=1
'''
#an infinite loop
while True:
    print("To infinity and beyond!")
'''