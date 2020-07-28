import re
string = raw_input('Enter a string: ')
print "This page was last modified on 16 November 2016, at 12:09."
string = "This page was last modified on 16 November 2016, at 12:09."

pattern = re.compile('\w')
result = pattern.findall(string)

result2 =result.sort()

print result2
