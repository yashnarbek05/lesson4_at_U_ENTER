

tuple = (1, 4, "7", 12, "129")

print(tuple)
print(type(tuple))

print("first element:", tuple[0])
print("last element:", tuple[-1])

#tuple[0] = 1  #can't modify any element of tuple

one,two,*three = tuple

print("one:", one)
print("two:", two)
print("three:", three)

tuple = three

print(tuple)