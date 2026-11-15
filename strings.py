def is_palindrome_text(text):
    normalized = "".join(character.lower() for character in text if not character.isspace())
    return normalized == normalized[::-1]


def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""


def are_anagrams(first, second):
    normalize = lambda text: sorted(character.lower() for character in text if character.isalnum())
    return normalize(first) == normalize(second)


def remove_duplicate_characters(text):
    seen = set()
    result = []
    for character in text:
        if character not in seen:
            seen.add(character)
            result.append(character)
    return "".join(result)


def compress_string(text):
    if not text:
        return ""

    compressed = []
    current_character = text[0]
    count = 1
    for character in text[1:]:
        if character == current_character:
            count += 1
        else:
            compressed.append(f"{current_character}{count}")
            current_character = character
            count = 1
    compressed.append(f"{current_character}{count}")
    return "".join(compressed)