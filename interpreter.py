expression = str(input("expression:"))
x, y, z = expression.split(" ")

num_x = float(x)
num_z = float(z)

if y == "+":
    result = num_x + num_z

elif y == "-":
    result = num_x - num_z

elif y == "*":
    result = num_x * num_z

elif y == "/":
    result = num_x / num_z

print(f"{result:.1f}")