print("\n")

intNumber = 123
floatNumber = 12.3
newNumber = intNumber + floatNumber
print("\nnumber:", newNumber, "\ntype:", type(newNumber))
print("\nnumber to float:", float(intNumber), "\ntype:", type(float(intNumber)))
print("\nfloat to number:", int(floatNumber), "\ntype:", type(int(floatNumber)))

print("\n")

stringNumber = '321'
int(stringNumber)
print("string:", stringNumber, "\ntypo:", type(stringNumber))
print("string:", stringNumber, "\ntypo:", type(int(stringNumber)))

print("\n")

number0 = 0
number1 = 1
stringtest = "test"
print("0 to bool:",bool(number0), type(bool(number0)))
print("1 to bool:",bool(number1), type(bool(number1)))
print("string to bool:",bool(stringtest), type(bool(stringtest)))
