formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) #outputs "1 2 3 4"
print formatter % ("one", "two", "three", "four") #outputs "'one' 'two' 'three' 'four'"
print formatter % (True, False, False, True) #outputs "True False False True"
print formatter % (formatter, formatter, formatter, formatter) #outputs "'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'"
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) #end print
#Weirdest output:
#"'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'"
# 
#Note to self: why is the third string in double quotes??