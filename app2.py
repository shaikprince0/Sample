a = int(input("Enter an integer: "))
if a % 2 == 0:
    print("even")
else:
    print("odd")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
