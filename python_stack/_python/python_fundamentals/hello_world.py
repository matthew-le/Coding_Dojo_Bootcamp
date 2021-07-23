#write string to print "Hello World"
print("Hello World")

#create variable for name, print hello "name" using comma
name = "Matt"
print("Hello", name)

#create variable for name, print hello "name" using +
name = "Alex"
print("Hello " + name)

#create variable for favorite number, print hello "number" using comma
num = 2
print("Hello", num)

#create variable for favorite number, print hello "number" using +; error should occur
#print("Hello" + num)

#to resolve above error 
num = "2"
print("Hello " + num)

#create (2) variables and use .format method
food_one = "Crawfish"
food_two = "Noodles"
print("I love to eat {} and {}." .format(food_one, food_two))

#create (2) variables and use f-string method
food_one = "Crawfish"
food_two = "Noodles"
print(f"I love to eat {food_one} and {food_two}.")

