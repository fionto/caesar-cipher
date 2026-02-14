# 📔 LOGBOOK - 14/02/2026

## 🚀 Funzionalità Implementate (v1.0)
- **Cifratura a Scorrimento**: Implementazione del core engine per il Cifrario di Cesare.
- **Case Sensitivity**: Gestione automatica di maiuscole e minuscole senza perdita di formattazione.
- **Preservazione Caratteri Speciali**: Logica di filtraggio per mantenere invariati spazi e punteggiatura.
- **Normalizzazione Alfabeto**: Algoritmo per la deduplicazione e la costruzione dinamica del set di caratteri.

## ⚙️ Competenze Tecniche Utilizzate
- **Data Structures**:
    - `tuple`: Scelta per garantire l'immutabilità dei dati di riferimento (alfabeto).
    - `set`: Utilizzato per l'ottimizzazione del lookup ($O(1)$) dei caratteri nel messaggio.
    - `dict`: Mappatura degli indici per evitare ricerche lineari ripetitive.
- **Control Flow & Logic**:
    - **Operatore Modulo (`%`)**: Calcolo matematico della circolarità dell'indice per lo shift.
    - **Enumerate**: Utilizzato per la costruzione efficiente delle mappe di indicizzazione.
- **Python Best Practices**:
    - **Type Hinting**: Applicazione di tipizzazione statica per la chiarezza del codice.
    - **Docstrings**: Documentazione tecnica dettagliata delle funzioni.
    - **Modularità**: Separazione tra funzioni di utilità e logica di esecuzione principale.