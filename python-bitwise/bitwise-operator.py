# bitwise operator

number1 = 15
number2 = 14

# and (&)
and_operator = number1 & number2
print(f"{number1} & {number2} = {and_operator}")

# or (|)
or_operator = number1 | number2
print(f"{number1} | {number2} = {or_operator}")

# xor (^)
xor_operator = number1 ^ number2
print(f"{number1} ^ {number2} = {xor_operator}")

# not (~)
not_operator = ~number1
print(f"~{number1} = {not_operator}")

# bitwise rightshift (>>)
right_shift_operator = number1 >> 1
print(f"{number1} >> 1 = {right_shift_operator}")

# bitwise rightshift (<<)
left_shift_operator = number1 << 1
print(f"{number1} << 1 = {left_shift_operator}")