
number = int(input("Enter number: "))

if number % 2 == 0:
    if number > 0:
        print(f"{number} is a positive")
        print(f"{number} is a even")
    elif number < 0:
        print(f"{number} is a negative")
        print(f"{number} is a even")
elif number % 2 != 0:
    if number > 0:
        print(f"{number} is a positive")
        print(f"{number} is a odd")
    elif number < 0:
        print(f"{number} is a negative")
        print(f"{number} is a odd")
else:
    print(f"{number} is a zero")