x = 5
y = 10
z = x + y

def animals(x):
    if x == "dog":
      return "Woof!"
    elif x == "cat":
      return "Meow!" 
      
    return "Unknown animal"
    

x = user_input = input("Enter an animal (dog/cat): ")

print(animals(x))