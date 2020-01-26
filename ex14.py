from sys import argv

script, user_name = argv #run using 'python ex14.py Tanjiro"
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)