word = input("dame una pinche palabra wey!: ")

letter_counter = {}

for letter in word:
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] = 1
print(letter_counter)            