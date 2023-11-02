"""Mutable and immutable data types."""


name = 'Zophie a cat'


# This won't work because you can't mutate strings like that
# name[7] = 'the'


# The proper way is to slice the string and concat, building a new string.
# It is that way because strings are immutable objects.
new_name = name[0:7] + 'the' + name[8:12]
print(new_name)  # This will print the altered string


eggs = [1, 2, 3]
eggs = [4, 5, 6]

# This prints the [4, 5, 6] list, but not because
# the `eggs` list has been changed. Instead a completely
# different `eggs` list values have overwritten the initial list.
print(eggs)
