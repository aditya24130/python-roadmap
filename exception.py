try:

    num = int(input("Enter a number: "))


    if num < 0:
        raise ValueError("Negative numbers are not allowed")


    with open("input.txt", "r") as file:
        content = file.read()

    print("File Content:")
    print(content)

except ValueError as e:
    print("Value Error:", e)

except FileNotFoundError:
    print("Error: input.txt file not found")

finally:
    print("Program finished")