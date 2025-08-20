number = 50

# Check if the number is even. This conditions uses the modulo operator (%) which checks for any remainders!
# if a number is a multiple of another number, it's remainder is 0 (zero)
if number % 2 == 0:
    print(f"{number} is an even number.")
    # Now, inside this if statement, check if it's also a multiple of 10. Replace "True" with the correct condition
    if True:
        print("It is also a multiple of 10!")
    else:
        print("But it is not a multiple of 10.")
else:
    print(f"{number} is an odd number.")
