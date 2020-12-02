#1
import re
def char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
print(char("SAyuz07) 
print(char("Sayuz@2k"))


#2
import re
def match(text):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match("I went to abroad last week."))
print(match("Python Internship."))


#3
import re
def match(text):
        patterns = '\w+\S *4'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(match("Sayuz54"))
print(match("Sayuz00"))
print(match("54Sayuz"))


#4
import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 34995 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))


#5
import re
def text_match(text):
        patterns = '^[A-Z]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("SAYUZ"))
print(text_match("Sayuz_19"))
