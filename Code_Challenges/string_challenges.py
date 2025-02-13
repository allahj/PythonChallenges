# Vowel Count

def get_count(sentence):
    vowels = 'aeiou'
    vowels_count = 0

    for char in sentence:
        if char in vowels:
            vowels_count += 1

    return vowels_count

# Remove String Spaces

def no_space(string):
    return string.replace(" ", "")

# Convert a Number to a String!

def number_to_string(num):
    return str(num)
