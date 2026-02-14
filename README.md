# 🔐 Caesar Cipher in Python

Questo repository ospita un'implementazione del Cifrario di Cesare, uno dei più antichi e semplici algoritmi di cifratura per sostituzione. Il progetto non nasce solo come strumento crittografico, ma come diario di apprendimento per esplorare le potenzialità delle strutture dati di Python e l'organizzazione del codice in ottica modulare.

L'obiettivo principale è documentare l'evoluzione da uno script procedurale di base a una soluzione ottimizzata, sicura e tipizzata.

---

## 📜 Cos’è il Cifrario di Cesare

Il cifrario di Cesare è uno dei metodi di crittografia più antichi. Il principio è elementare: ogni lettera del testo viene spostata in avanti di un numero fisso di posizioni nell’alfabeto.

Se lo spostamento è 3:

```
A → D  
B → E  
C → F  
...
```

E così via, tornando all’inizio dell’alfabeto quando si supera la Z.

Storicamente, veniva applicato solo alle lettere dell’alfabeto latino. Numeri, spazi e simboli non venivano cifrati.

---

## 🛠️ Scelte implementative

Il cuore del progetto risiede nella gestione efficiente dell'alfabeto e nella separazione delle responsabilità. Invece di limitarsi a una stringa statica, il sistema costruisce dinamicamente i set di caratteri per garantire flessibilità.

### 📂 v1.0 - Fondamenta e Logica di Base

Questa prima iterazione del progetto è in grado di processare stringhe alfanumeriche applicando una traslazione ciclica personalizzabile alle sole lettere, preservando al contempo la formattazione originale (spazi, simboli e distinzione tra maiuscole e minuscole).

* **Preservazione dei Simboli**: Il cifrario viene applicato esclusivamente alle lettere dell'alfabeto. Numeri, spazi e punteggiatura vengono lasciati invariati per mantenere la leggibilità della struttura del messaggio originale, in linea con l'approccio storico.
* **Case Sensitivity**: Il sistema riconosce e mappa separatamente caratteri minuscoli e maiuscoli, evitando la perdita di informazioni stilistiche durante la cifratura.

---

## 🚀 Prossimi Passi (Roadmap)

L'evoluzione del progetto si articolerà su due binari paralleli: l'espansione delle capacità crittografiche e il raffinamento dell'architettura del codice.

### 🧩 Ampliamento Funzionalità

L'obiettivo è trasformare lo script v1.0 in un tool completo di manipolazione testuale, mantenendo l'approccio basato su mappature custom:

1. **Modulo Bi-direzionale (Encode/Decode)**: Implementazione della logica di decifratura permettendo all'utente di scegliere la direzione dello shift, trasformando il sistema in uno strumento di comunicazione completo.
2. **Offuscamento degli Spazi**: Evoluzione della versione storica per includere lo spazio nel set di caratteri mappati. Questo impedirà a un analista esterno di identificare la lunghezza delle parole, aumentando la sicurezza del messaggio.
3. **Supporto Simboli e Punteggiatura**: Estensione dell'alfabeto a caratteri speciali (es. `-`, `!`, `?`) mantenendo il vincolo di **non utilizzare** `ord()` o `chr()`. La gestione avverrà esclusivamente tramite l'espansione delle tuple e dei dizionari di mappatura.
4. **Keyword-based Caesar**: Introduzione di una "chiave" alfabetica per rimescolare l'alfabeto di partenza prima dello shift, rendendo la crittoanalisi per forza bruta molto più complessa rispetto al metodo tradizionale.

### ⚙️ Miglioramento Tecnico

Per gestire la crescente complessità, il codice evolverà verso standard industriali più elevati:

* **Programmazione a Oggetti (OOP)**: Transizione verso una classe `CaesarCipher`. Questo permetterà di incapsulare l'alfabeto e la logica di shift all'interno di un oggetto, facilitando la gestione di stati diversi (es. due cifrari con alfabeti diversi che lavorano contemporaneamente).
* **Gestione degli Errori (Exception Handling)**: Introduzione di blocchi `try-except` per gestire input non validi o shift non numerici, garantendo che il programma non si interrompa bruscamente.
* **Interfaccia CLI (Command Line Interface)**: Utilizzo del modulo `argparse` per permettere l'utilizzo dello script direttamente dal terminale, passando messaggio e shift come parametri di lancio.
* **Unit Testing**: Scrittura di test automatizzati per verificare che ogni modifica al codice non rompa le funzionalità preesistenti (regression testing).