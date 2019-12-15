print "How old are you?",
age = raw_input()
print "How tall are you (inches)?",
height = raw_input()
print "How much do you weigh (lbs)?",
weight = raw_input()

print "Hello, you're %r old, %r inches tall, and %r lbs heavy." % (
    age, height, weight
)