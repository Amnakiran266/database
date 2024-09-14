name= input("enter your name: ")
num1= int(input("enter your first favorite number:"))
num2= int(input("enter your second favorite number:"))
num3= int(input("enter your third favorite number:"))
print(f"hello {name}! lets explore your favorite numbers:")
numbers= [num1, num2, num3]
for number in numbers:

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd") 
tup=(num1, num2, num3)
print(f"the number {tup[0]} and its square {tup[0]**2}")       
print(f"the number {tup[1]} and its square {tup[1]**2}")   
print(f"the number {tup[2]} and its square {tup[2]**2}")   
print(f"amazing! the sum of your favorite numbers is: {tup[0]+tup[1]+tup[2]}")
print("wow 12 is not a prime number!")
