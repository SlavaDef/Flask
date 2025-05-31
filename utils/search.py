def find(phrase: str, letters: str) -> list:
    return sorted(list(letter for letter in letters.lower() if letter in phrase.lower()))
