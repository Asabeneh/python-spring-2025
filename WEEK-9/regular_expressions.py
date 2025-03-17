'''
It allows to detect pattern

'''
import re

"""



To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
"""

txt = 'I love to teach python and javaScript. Another love here again. Here is the dragon. Here are some vegs. The first is potatoes and the second would be tomatoes. I love potatoes'
pattern = 'potatoes|tomatoes'
match = re.findall(pattern, txt, re.I)
print(match)
print()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

txt = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(txt)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

pattern = r'[^a-zA-Z0-9. ]'

print(re.sub(pattern, '', sentence))

txt = 'I love to teach python and javaScript but love Golang more than anything'

print(re.split(r'and|but', txt))