
with open("input.txt", "r") as file:
    content = file.read()

print("Using read():")
print(content)


with open("input.txt", "r") as file:
    lines = file.readlines()

print("\nUsing readlines():")
print(lines)

with open("output.txt", "w") as new_file:
    new_file.write(content)

print("\Content copied to output.txt")