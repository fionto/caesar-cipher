# 🔐 Caesar Cipher in Python

Un piccolo progetto, semplice ma fondamentale: implementare il **cifrario di Cesare** in Python per esercitarmi con stringhe, cicli, funzioni e logica modulare.

Questo repository non nasce per creare un sistema sicuro, ma per documentare il mio percorso di apprendimento e costruire basi solide attraverso un problema classico, elegante nella sua semplicità.

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

## 🛠 Scelte implementative

In questa versione (v1.0):

Il cifrario viene applicato solo alle lettere dell’alfabeto.
Numeri, spazi e simboli vengono lasciati invariati, in linea con l’approccio storico.

Il codice permette sia cifratura che decifratura, usando uno shift positivo o negativo.
La logica di base è:

* convertire il carattere in numero
* applicare lo shift
* usare il modulo 26 per rimanere nell’alfabeto
* riconvertire in carattere

La struttura è volutamente semplice, per mantenere chiara la trasformazione.

---

## 📚 Perché documentare questo progetto?

Perché imparare a programmare non significa solo scrivere codice, ma anche spiegare cosa si è fatto, perché lo si è fatto e cosa si è capito nel processo.

Questo repository è parte del mio percorso di crescita in Python.
Ogni progetto è un passo. Anche quelli “semplici”.

