from sys import argv, raw_input #'sys' module with 'argv' variable passed to the python script.

script, first, second, third = argv
fourth, fifth = raw_input

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third