"""Tuple data type."""


eggs = ('hello', 42, 0.5)
print(eggs[0])

print(eggs[1:3])

print(len(eggs))

# Tuples somewhat resemble lists, but they are immutable.
# You can't perform something like that eggs[1] = 99.

# There are functions like list() and tuple() to convert
# in either data type, which are handy at moments.
