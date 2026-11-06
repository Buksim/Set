# Different Types of sets in Python 
# Set of Integers
my_set = {1, 2, 3}
print(my_set)

# Set of Mixed Datatypes
my_set = {1.0, "Hello", (1, 2, 3), 8}
print(my_set)

# Set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# We can make set from a List
my_set = set([1, 2, 3, 2])
print(my_set, "\n")

# Remove a Number from the set
num_set = set({0, 1, 2, 3, 4 , 5})
print("Original Set:")
print(num_set)
num_set.pop()
print("After Removing the First Element from the said set:")
print(num_set, "\n")    