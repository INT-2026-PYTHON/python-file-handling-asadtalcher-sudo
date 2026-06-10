"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
#ASAD AHMAD 25BCSG20
def has_all_vowels(word):
    vowels = set('aeiou')
    word_vowels = set()
    for ch in word.lower():
        if ch in vowels:
            word_vowels.add(ch)
    return word_vowels == vowels
def words_with_all_vowels(filename):
    result = []
    with open(filename, "r") as f:
        for line in f:
            word = line.strip().lower()
            if not word:
                continue
            if has_all_vowels(word):
                result.append(word)
    return result
if __name__ == "__main__":
    filename = "sowpods.txt"
    words = words_with_all_vowels(filename)
    for w in words:
        print(w)
    print("Total words with all vowels:", len(words))