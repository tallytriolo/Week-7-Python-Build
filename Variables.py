# this is a comment
# this is a print method. Print will wcho out anything inside the 
# () round brackets to the terminal, when we the file
print("This is my very first python script!!!")

# variables are placeholders, with dynamic values -> things that can change
# they get stored in memory and referenced later
name = "Tallyta"
age = 31
eyecolor = "brown"
haircolor = "blond"

# Arrays are variables on steriods. They let us store many values in one
# variable -> to help us group data.
# This makes our scripting files easier to understand and work it.
#car1 = "Volvo"
#car2 = "Toyota"
#car3 = "Fiesta"
cars = ["Volvo", "Toyota", "Fiesta"]

print("My name is " + name)

# input is another Python "thing" - it waits with a flashing cursor
# until you type something and hite enter
alternateName = input("What is YOUR name?")

print("My name is now " + alternateName)

print("My age is " + str(age))