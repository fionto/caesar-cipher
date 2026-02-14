################################################################################
# PROGETTO: Caesar Cipher Evolution
# OBIETTIVI DEL MODULO:
# - Implementare un sistema di cifratura a scorrimento (Cifrario di Cesare).
# - Gestire un set di caratteri estensibile (lettere, poi accentate, poi altre).
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
messaggio = "Si vis pacem, para bellum"

# Anche se la lista è "hardcoded" voglio una funzione che pulisca i doppioni
# e crei la versione maiuscola appended.
def build_case_alphabet(letters: tuple[str, ...]) -> tuple[str, ...]:
    """
    Costruisce una tupla contenente le versioni minuscole e maiuscole
    delle lettere uniche fornite in input.

    La funzione itera sulla sequenza in ingresso, rimuove eventuali duplicati
    preservando l'ordine originale e genera due liste ordinate:
    una con le lettere in minuscolo e una con le lettere in maiuscolo.
    La tupla restituita contiene prima tutte le lettere minuscole,
    seguite dalle corrispondenti lettere maiuscole.

    Args:
        letters (tuple[str, ...]): Tupla di stringhe rappresentanti lettere.

    Returns:
        tuple[str, ...]: Tupla contenente le lettere uniche in minuscolo,
        seguite dalle rispettive versioni maiuscole.
    """
    seen = set()
    lower_case = []
    upper_case = []

    for letter in letters:
        
        if not letter.isalpha():
            continue

        key = letter.lower()
        if key not in seen:
            seen.add(key)
            lower_case.append(key)
            upper_case.append(key.upper())

    return tuple(lower_case + upper_case)

# Per rendere più efficiente la ricerca dell'indice assegnato ad ogni lettera
# creo un dizionario 
def build_index_map(letters: tuple[str, ...]) -> dict[str, int]:
    """
    Costruisce un dizionario che associa ogni lettera al suo primo indice di occorrenza.

    La funzione itera sulla tupla di lettere fornita in input e crea
    una mappatura tra ciascun elemento e l'indice della sua prima
    apparizione nella sequenza. Eventuali duplicati successivi
    vengono ignorati.

    Args:
        letters (tuple[str, ...]): Tupla di stringhe rappresentanti lettere
            o simboli da indicizzare.

    Returns:
        dict[str, int]: Dizionario in cui:
            - la chiave è la lettera
            - il valore è l'indice della prima occorrenza nella tupla
    """
    index_map = {}
    
    for i, letter in enumerate(letters):
        if letter not in index_map.keys():
            index_map[letter] = i

    return index_map

def shift_character(
        letter: str, 
        shift: int, 
        letters: tuple[str, ...],
        index_map: dict[str, int],
        ) -> str:
    """Applica uno shift ciclico a una lettera all'interno di un alfabeto definito.

    La funzione prende una lettera e la trasla di un certo numero di posizioni
    (positivo) all'interno della tupla `letters`. L'indice della
    lettera viene recuperato da `index_map` e il risultato viene calcolato
    ciclicamente usando l'operatore modulo, in modo che lo shift "giri" 
    all'inizio della tupla se necessario.

    Args:
        letter (str): La lettera da traslare.
        shift (int): Il numero di posizioni da spostare. Può essere positivo
            (verso destra) o negativo (verso sinistra).
        letters (tuple[str, ...]): Tupla contenente tutte le lettere
            valide in ordine.
        index_map (dict[str, int]): Dizionario che mappa ciascuna lettera
            al suo indice nella tupla `letters`.

    Returns:
        str: La lettera risultante dopo l'applicazione dello shift ciclico.    
    """
    char_index = index_map[letter]
    shifted_index = (char_index + shift) % len(letters)
    return letters[shifted_index]

def main():
    alphabet = build_case_alphabet(LETTERS)
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