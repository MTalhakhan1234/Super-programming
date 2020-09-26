print("    SIMPLE CALCULATOR    ")
first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))
print("----List of operations----")
print("For Addition type + ")
print("For Subtraction type - ")
print("For Multiplication type * ")
print("For Division type / ")
operator = input("Enter the operator: ")
if operator == "+":
    ans = first_num + second_num
    print(f"Sum of {first_num} and {second_num} is = {ans}.")
elif operator == "-":
    ans = first_num - second_num
    print(f"subtraction of {second_num} from {first_num} gives = {ans}.")
elif operator == "*":
    ans = first_num * second_num
    print(f"Multiplication of {first_num} and {second_num} gives = {ans}.")
elif operator == "/":
    ans = first_num / second_num
    print(f"Division of {second_num} from {first_num} gives = {ans}.")
else:
    print("Incorrect input!, Please Try again!!!")