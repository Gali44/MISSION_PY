# enumerate() we can

my_l = {"first": "q", "second": "r", "third": "t"}
for number, (key, value) in enumerate(my_l.items(), start=1):
    print(number, key, value)

chemical_elements = {
    "Hydrogen": "H",
    "Helium": "He",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne"
}

print(list(chemical_elements.items()))

for elem, symbol in chemical_elements.items():
    print(f"Element: {elem}, {symbol}")

# Alternative in tuple format

for pair in chemical_elements.items():
    print(pair)
    print(pair[0], pair[1])
