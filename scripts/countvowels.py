
#Count vowels in a word
def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

words = ["security", "governance", "risk", "assurance"]

for w in words:
    print(w, count_vowels(w))