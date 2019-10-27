formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) #outputs "1 2 3 4"
print formatter % ("one", "two", "three", "four") #outputs "'one' 'two' 'three' 'four'"
print formatter % (True, False, False, True) #outputs "True False False True"
printer formatter % (formatter)