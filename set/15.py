# Working with immutable sets
normal_set = {1, 2, 3}
frozen = frozenset([3, 4, 5])

print("Frozenset:", frozen)
# Useful as dictionary keys or set elements
dict_with_frozen = {frozen: "Immutable Key"}
print(dict_with_frozen)