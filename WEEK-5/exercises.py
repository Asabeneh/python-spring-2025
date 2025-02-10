sentences = [
    "  Python is amazing!  ",
    "I love coding in Python.",
    "Loops, strings, and lists are powerful in Python.",
    "Python is fun!"
]

all_words = []
for sentence in sentences:
    words = sentence.strip().lower().replace('!', '').replace('', '').replace(',', '').replace('.', ('')).split()
    all_words.extend(words)

total_words = len(all_words)
unique_words = set(all_words)
unique_number_words = len(unique_words)
print(f'total words: {total_words}', f'unique words:{unique_number_words}')

lexical_variety = (unique_number_words / total_words) * 100 
print(round(lexical_variety, 1))

vowels = 'aeiou'


text = "Python is fun!"
count = 0
for vowel in vowels:
    if vowel in text:
        count = count + 1
print(count)

total_characters = len(text.replace(' ', '').replace('!', ''))
print(total_characters - count)

text = "Python is fun!"

vowels = 0
consonants = 0
for char in text:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
