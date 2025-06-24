int_input = int(input("Enter an integer"))
float_input = float(input("Enter float"))
string_input = (input("Enter a string"))

print(f"\nInteger value: {int_input} (type: {type(int_input).__name__})" )
print(f"\nFloat value: {float_input} (type: {type(float_input).__name__})" )
print(f"\nString value: {string_input} (type: {type(string_input).__name__})" )