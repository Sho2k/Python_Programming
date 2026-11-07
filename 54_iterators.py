"""Program 54: Iterators"""

colours = ["Red", "Green", "Blue"]
colour_iterator = iter(colours)

print(next(colour_iterator))
print(next(colour_iterator))
print(next(colour_iterator))

print("Using a for loop:")
for colour in iter(colours):
    print(colour)
