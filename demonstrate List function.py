numbers = [10, 20, 30, 40, 50]
print("\n--- List Function Demonstration ---")
print("Original List :", numbers)
# Length of list
print("Length :", len(numbers))
# Append an element
numbers.append(60)
print("After Append (60) :", numbers)
# Insert at index
numbers.insert(2, 25)
print("After Insert (25 at index 2):", numbers)
# Remove element by value
numbers.remove(40)
print("After Remove (40) :", numbers)
# Pop last element
popped = numbers.pop()
print("After Pop :", numbers)
print("Popped Element :", popped)
# Index of an element
print("Index of 30 :", numbers.index(30))
# Count occurrences
print("Count of 20 :", numbers.count(20))
# Reverse the list
numbers.reverse()
print("After Reverse :", numbers)
# Sort the list
numbers.sort()
print("After Sort :", numbers)
# Copy list
copy_list = numbers.copy()
print("Copied List :", copy_list)
# Clear list
numbers.clear()
print("After Clear :", numbers)
