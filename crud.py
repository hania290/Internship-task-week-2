student = {}

# Create
student["name"] = "Ali"
student["age"] = 18
student["grade"] = "A"

# Read
print("Student Record:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])

# Update
student["grade"] = "A+"
print("\nUpdated Grade:", student["grade"])

# Delete
del student["age"]
print("\nAfter deleting age:", student)