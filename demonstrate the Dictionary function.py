student = {
"name": "Aadarsh",
"roll_no": 101,
"marks": 85,
"subject": "Math"
}
print("\n--- Dictionary Function Demonstration ---")
print("Original Dictionary :", student)
# Access values
print("Name :", student["name"])
print("Roll Number :", student.get("roll_no"))
# Add new key-value pair
student["grade"] = "A"
print("After Adding Grade :", student)
# Update value
student["marks"] = 90
print("After Updating Marks :", student)
# Remove a key-value pair
student.pop("subject")
print("After Removing 'subject':", student)
# Get keys, values, and items
print("Keys :", student.keys())
print("Values :", student.values())
print("Items :", student.items())
# Check if key exists
print("Is 'marks' in dictionary?:", "marks" in student)
# Loop through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
print(key, ":", value)
# Clear dictionary
student.clear()
print("After Clear :            :", student)