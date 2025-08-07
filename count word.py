sentence = "this is a test this is only a test"

words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequencies:")
for word, count in word_count.items():
    print(word, ":", count)