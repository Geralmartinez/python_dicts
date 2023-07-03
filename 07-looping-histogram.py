word = input("dame una pinche palabra!: ")

letter_counter = {}

for letter in word:
   if letter in letter_counter:
    letter_counter[letter] += 1
   else:
    letter_counter[letter] = 1

print(f"tu palabra tiene {len(word)} letras")  
for letter in letter_counter:
   print(letter, letter_counter[letter])