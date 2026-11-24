# A program that counts how many times each word appears in a paragraph.

paragraph = "cat dog mouse cat rat cat mouse"

counts = {}
# split() cuts the paragraph into a list of words at the spaces
for word in paragraph.split():
    if word in counts:
        counts[word] += 1  # the word was seen before, so its counter grows
    else:
        counts[word] = 1   # the first appearance of the word

for word, count in counts.items():
    print(f'{word}: {count}')
