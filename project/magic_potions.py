# Step 1: Create the dictionary containing the potions and their ingredients
potions = {
    "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"],
    "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"],
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}

# Step 2: Display the list of potions
print("Welcome to the Magic Potion Shop!")
print("Here are the potions available:")
for i, potion in enumerate(potions.keys(), 1):
    print(f"{i}. {potion}")

# Step 3: Ask the user to choose a potion
choice = int(input("Please choose a potion by entering the corresponding number: ")) - 1
potion_names = list(potions.keys())
chosen_potion = potion_names[choice]

# Step 4: Display the ingredients required for the chosen potion
ingredients = potions[chosen_potion]
print(f"\nYou have chosen the {chosen_potion}.")
print("You need the following ingredients:")
for ingredient in ingredients:
    print(f"- {ingredient}")

# Step 5: Use a loop to "buy" each ingredient one by one
print("\nLet's start buying the ingredients one by one.")
bought_ingredients = []
index = 0

while index < len(ingredients):
    buy = input(f"Do you want to buy {ingredients[index]}? (yes/no): ").strip().lower()
    if buy == "yes":
        bought_ingredients.append(ingredients[index])
        print(f"You have bought {ingredients[index]}.")
        index += 1
    elif buy == "no":
        print("You chose not to buy the ingredient. Stopping the purchase.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Check if all ingredients were bought
if len(bought_ingredients) == len(ingredients):
    print(f"\nCongratulations! You have bought all the ingredients for the {chosen_potion}.")
else:
    print(f"\nYou did not buy all the ingredients for the {chosen_potion}.")
