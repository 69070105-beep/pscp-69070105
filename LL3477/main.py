"""Pad Thai"""

required_ingredients = {
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts",
}
required_flavors = {"Sweet", "Sour", "Salty"}

used_ingredients = set()
while True:
    item = input().strip()
    if item == "Cook":
        break
    used_ingredients.add(item)

used_flavors = set()
while True:
    flavor = input().strip()
    if flavor == "End":
        break
    used_flavors.add(flavor)

if not used_ingredients.issubset(required_ingredients):
    print("This is not Pad Thai!!!")
elif used_ingredients != required_ingredients:
    print("This is bad!")
elif used_flavors == required_flavors:
    print("Delicious!")
else:
    print("Not Bad...")
