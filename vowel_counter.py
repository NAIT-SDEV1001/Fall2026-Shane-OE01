word = input("Enter a word to count the vowels: ")

vowel_count = 0

for character in word:
    if character in "aeiou":
        vowel_count += 1

print (f"There are {vowel_count} vowels in {word}")

    


