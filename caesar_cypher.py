################################################################################
# PROGETTO: Caesar Cipher Evolution
# OBIETTIVI DEL MODULO:
# - Implementare un sistema di cifratura a scorrimento (Cifrario di Cesare).
# - Gestire un set di caratteri estensibile (inclusi simboli speciali come '-').
# - Supportare dinamicamente la distinzione tra alfabeti minuscoli e maiuscoli.
# - Ottimizzare il recupero degli indici tramite mappature (dictionary mapping).
# - Garantire la circolarità dello shift tramite operatore modulo.
################################################################################


# CARATTERI BASE:
# 1) Scelta tupla in quanto il set non mantiene l'ordine e lista è modificabile
LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            )

# INPUT: Per il momento il messaggio da testare è una semplice variabile
messaggio = "Ave, Cesare!"

# Anche se la lista è "hardcoded" voglio una funzione che pulisca i doppioni
# e crei la versione maiuscola appended.
def build_alphabet(letters: tuple[str, ...]) -> tuple[str, ...]:
    seen = set()
    lower_case = []
    upper_case = []

    for letter in letters:
        if letter not in seen:
            seen.add(letter)
            lower_case.append(letter.lower())
            upper_case.append(letter.upper())

    return tuple(lower_case + upper_case)

# Per rendere più efficiente la ricerca dell'indice assegnato ad ogni lettera
# creo un dizionario 
def build_index_map(letters: tuple[str, ...]) -> dict[str, int]:
   
    alphabet = {}
    
    for i, letter in enumerate(letters):
        if letter not in alphabet.keys():
            alphabet[letter] = i

    return alphabet

def shift_character(
        letter: str, 
        shift: int, 
        letters: tuple[str, ...],
        index_map: dict[str, int],
        ) -> str:
    
    char_index = index_map[letter]
    shifted_index = (char_index + shift) % len(letters)
    return letters[shifted_index]

def main():
    alphabet = build_alphabet(LETTERS)
    alphabet_set = set(alphabet)
    index_map = build_index_map(alphabet)
    encrypted_message = ""

    for char in messaggio:      
        if char in alphabet_set:
            encrypted_message += shift_character(char, 3, alphabet, index_map)
        else:
            encrypted_message += char

    print(encrypted_message)

main()