fruits = ("apple", "banana", "cherry", "banana", "apple")
print("\n--- Tuple Function Demonstration ---")
print("Original Tuple :", fruits)
# Length of tuple
print("Length :", len(fruits))
# Count occurrences
print("Count of 'banana' :", fruits.count("banana"))
print("Count of 'apple' :", fruits.count("apple"))
# Index of an element
print("Index of 'cherry' :", fruits.index("cherry"))
# Accessing elements
print("First Element :", fruits[0])
print("Last Element :", fruits[-1])
# Slicing
print("Slice [1:4] :", fruits[1:4])
# Loop through tuple
print("Loop through tuple :")
for item in fruits:
print("-", item)
# Check membership
print("Is 'mango' in tuple? :", "mango" in fruits)
print("Is 'banana' in tuple?:", "banana" in fruits)
mixed = ("John", 25, True)
print("Mixed Tuple :", mixed)