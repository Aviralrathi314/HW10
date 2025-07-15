number = int(input("Enter the number: "))
multiplier = int(input("Enter the multiplier: "))

result = 1
for i in range(multiplier):
    result = result * number  

print("Result:", result)