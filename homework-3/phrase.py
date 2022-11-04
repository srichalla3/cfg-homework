from collections import Counter


def generate_phrase(characters, phrase):
    new_characters = characters.lower()
    new_phrase = phrase.lower()
    char_counts = Counter(new_characters)
    phrase_counts = Counter(new_phrase)
    return all(char_counts.get(char, 0) >= count for char, count in phrase_counts.items())

characters = "stchllaejaria!"
phrase = "sritejachalla"

print(generate_phrase(characters, phras
