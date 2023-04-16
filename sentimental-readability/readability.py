from cs50 import get_string


# initial data
text = get_string("Text: ")
letters = 0
words = 1
sentences = 0

# count letters in the text
for i in range(len(text)):
    if (text[i].isalpha()):
        letters += 1


# count words in the text
    if (text[i].isspace()):
        words += 1


# count sentences in the text
    if (text[i] == '.' or text[i] == '!' or text[i] == '?'):
        sentences += 1


L = 100 * (letters / words)  # letters per 100 words
S = 100 * (sentences / words)  # sentences per 100 words
index_fl = 0.0588 * L - 0.296 * S - 15.8
grade = round(index_fl)
if grade >= 16:
    print('Grade 16+')
elif grade < 1:
    print('Before Grade 1')
else:
    print('Grade', grade)