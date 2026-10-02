a = [2, 3, 34, 5, 5, 2, 2, 2, 3]

print(len(a))
print(a.index(34))

# Modify the list in-place first, then print
a.insert(2, "lamo kha")
print(a)

# Remove the string so Python can sort the numbers
a.remove("lamo kha")

# sort() works in-place (returns None), sorted() returns a new sorted list
i = sorted(a)
print(i)
