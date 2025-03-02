#Default Arguments: Define a function that 
#takes a name as input and prints a greeting. 
#If no name is provided, it should use "Guest" 
#as the default.

def greet(name="Guest"):
    print("welcome", name)
greet()
greet("marta")