#this program is for a pizza restaurant to calculate the cost of a pizza order 
#the user will input the size of the pizza, the number of toppings, and whether they want a stuffed crust
#the program will then calculate the total cost of the pizza order and print it out 
#using all conditional statements

print("*** Welcome to python pizza delevery ***")
size = input("what size pizza do you want? S,M or L : ")
pepperoni = input("do you want pepperoni on your pizza? Y or N : ")
cheese = input("do you want extra cheese? Y or N : ")

final_bill = 0

if size == "S":
    final_bill += 15
    if pepperoni == "Y":
        final_bill += 2
elif size == "M":
    final_bill += 20
elif size == "L":
    final_bill += 25
    

if size == "M" or size == "L":
    if pepperoni == "Y":
        final_bill += 3

if cheese == "Y":
    final_bill += 1

print(f"Your total bill is ${final_bill}")





            
