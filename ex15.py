from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "I'll also ask you to type it again:"
file_again = open(file_again)