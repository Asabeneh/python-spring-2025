"""
.txt
.md
.csv
.tsc
.json
.yaml

read texts from file
create files
write on files

"""

""" words = []
f = open('notes.txt')
lines = f.read().splitlines()
for line in lines:
    words.extend(line.lower().split())
print(words) """



words = []
with open('notes.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        words.extend(line.lower().split())
print(words)

