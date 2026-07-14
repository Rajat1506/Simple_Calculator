num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("Enter your operation:")
print("1: Addition { + }")
print("2: Subtraction { - }")
print("3: Multiplication { * }")
print("4: Divide { / }")

choice = input("Enter your arithmetic operation {1-4}:")

match choice:

    case "1":
        print("Result = ",num1 + num2)

    case "2":
         print("Result = ",num1 - num2)

    case "3":
         print("Result = ",num1 * num2)

    case "4":
        if num2 != 0:
             print("Result = ",num1 / num2)

        else:
              print("Number 2 is not valid:")

    case "_":
          print("Invalid operator:")


         




        



