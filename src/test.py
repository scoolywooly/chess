def update_dictionary(dictionary, key, updates):
    dictionary |= {key : updates}
    return dictionary

my_dict = {
    "White": ["rook","knight"]
}

new_update = ["canaray", "pawn", "queen"]

my_dict = update_dictionary(my_dict, "White", new_update)

print(my_dict)