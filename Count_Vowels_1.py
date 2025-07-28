def count_vowels(text):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count



f = open('H:\\Python Programme\\Random Files for python file Handling\\Countvowels.txt', 'r') 
content = f.read()

num_vowels = count_vowels(content)
print("Number of vowels in the file: ",num_vowels)

f.close()
