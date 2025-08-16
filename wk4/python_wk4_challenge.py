# Part 1: Function to add an item.
# This function should take a list and an item, then add the item to the list.
def add_item_to_list(my_list, item):
    # TODO: Use a list method to add the 'item' to 'my_list'.
    _____________________________

# Part 2: Main program to build the list.
shopping_list = []

print("Enter your shopping list items. Type 'done' when you are finished.")

# TODO: Create a loop that continues to run until the user types 'done'.
while ______________________:
    # Get an item from the user.
    item_to_add = input("Enter an item: ")

    # TODO: Add a condition here.
    # If the user's input is NOT 'done', call the function to add the item to the list.
    if ______________________:
        # TODO: Call the 'add_item_to_list' function here with the correct arguments.
        _____________________________________
    else:
        # TODO: Use a keyword to exit the loop.
        # HINT: What should you do if the input IS 'done'? 🤔🤔
        ____________________

# Print the final shopping list.
print("\nYour final shopping list:")
# TODO: Use a for loop to print each item on a new line.
for ____________________:
    print("_________________")
