# Caratteri base. Aggiungo un solo simbolo '-' per testare casi limite
CHARACTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-'
            )

messaggio = "Ave, Cesare!"

def build_alphabet_lower(characters: tuple[str, ...]) -> dict[str, int]:
    alphabet_lower = {}
    
    for i, character in enumerate(characters):
        character = character.lower() if character.isalpha() else character
        alphabet_lower[character] = i

    return alphabet_lower

def build_alphabet_upper(characters: tuple[str, ...]) -> dict[str, int]:
    alphabet_upper = {}
    
    for i, character in enumerate(characters):
        character = character.upper() if character.isalpha() else character
        alphabet_upper[character] = i

    return alphabet_upper


def shift_character(
        letter: str, 
        shift: int, 
        alphabet: tuple[str, ...],
        index_map: dict[str, int],
        ) -> str:
    
    char_index = index_map[letter]
    shifted_index = (char_index + shift) % len(alphabet)
    return alphabet[shifted_index]

print(shift_character('z', 3, CHARACTERS, build_alphabet_lower(CHARACTERS)))