list_of_letter = ["a", "b", "c", "a", "y", "d", "d", "f"]
list_of_vowels = ["a", "i", "o", "u", "y"] 
counter_of_vowels = 0

for char in list_of_letter:
    for vowel in list_of_vowels:
        if char == vowel:
            counter_of_vowels += 1
print(counter_of_vowels)


arr = [1,2,3,4,5,6,7,]