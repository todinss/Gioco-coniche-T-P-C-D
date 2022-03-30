# **Gruppo coniche**
*Il nostro gruppo per la realizzazione di questo progetto è formato da Todino,  Pala, Carotenuto, Di Gennaro.*

## **Ruoli**

- Todino: **Gestione e realizzazione del software, creazione e modifica del diagramma di flusso, creazione e modifica della descrizione del gioco e addetto ad aggiornare il file README.md**
- Pala: **Gestione e realizzazione del software, addetto ad aggiornare il file changelog.md e addetto ai preconcetti matematici.**
- Carotenuto: **Gestione e realizzazione del software, addetto ad aggiornare il file .md, creazione del changhelog e addetto alla modifica delle immagini su Adobe Photoshop**

- Di Gennaro: **Creazione diagramma di flusso e gestione del file README.md**

## **Organizzazione del gruppo:**

*Prima di andare a lavorare effettivamente sul codice abbiamo stabilito dei giorni e degli orari precisi dove ci saremmo
potuti vedere su Google Meet, questo per avere un'organizzazione più efficace e pulita.*

Come si è potuto notare, bene o male tutti quanti abbiamo lo stesso ruolo, ma c'è da dire che, in realtà, durante una riunione Meet ognuno ha un ruolo ben preciso in cui spesso ci si alterna.

- C'è chi, qualora ce ne fosse la necessità, presenta da Youtube un video che potrebbe aiutarci ulteriormente nella realizzazione del codice.
- C'è chi scrive un file ReadMe per spiegare come ci siamo organizzati.
- C'è chi lavora sul codice e lo presenta per rendere tutti partecipi nel lavoro..
***

# Alla conquista di Saturno

## **Descrizione del gioco:**

### *Abstract (descrizione delle caratteristiche del gioco):*

È un gioco arcade 2D ambientato nello spazio, dove l’utente impersonifica degli alieni, a comando di una navicella spaziale, che vogliono conquistare un nuovo pianeta. La loro scelta ricade su Saturno e si dirigono verso di esso. La traiettoria della navicella è decisa dall'utente, il quale seleziona una conica tra la retta e la parabola e successivamente inserisce un’equazione della conica selezionata. La navicella si muoverà lungo la lista dei punti appartenenti alla conica e arriverà nei pressi di Saturno. 
A questo punto la navicella dovrà schivare i detriti che compongono gli anelli di Saturno, affinché possa raggiungere la superficie del pianeta. Le abilità del pilota porteranno alla buona o alla cattiva riuscita della missione aliena. 

### *Interfaccia:*

Nella prima scena del gioco compare sullo schermo l’astronave aliena su uno sfondo spaziale ed un pop up che chiede all’utente di selezionare una conica da un elenco che gli viene mostrato. Una volta selezionata la conica, all’utente viene chiesto di inserire i parametri dell’equazione della conica selezionata, all'interno di una barra di testo che comparirà successivamente sullo schermo. L’astronave comincerà a muoversi lungo la lista di punti che compongono la conica data in input dall’utente, finché essa non uscirà dallo schermo. Successivamente comparirà sullo schermo, un altro pop up che indica all’utente di digitare il tasto spazio per proseguire con la seconda scena del gioco.

Una volta che l’utente avrà digitato il tasto spazio comincerà la seconda scena, nella quale inizia il gioco vero e proprio. L’utente dovrà schivare i meteoriti che si muovono verso l’astronave e nel caso venisse colpita, all’utente verrà sottratta una vita. Nel caso l’astronave venisse colpita tre volte, l’utente perderebbe la partita e gli comparirebbe sullo schermo la scritta “GAME OVER”.
In alto a sinistra sullo schermo, sarà visibile un contatore, che riporterà il punteggio dell’utente, che equivale allo spazio percorso dall’astronave durante la partita, misurato in chilometri.

# ![github-small](https://github.com/renatogallo27/gruppo-coniche/blob/main/images/astro.png)

# ![github-small](https://github.com/renatogallo27/gruppo-coniche/blob/main/images/saturno.png)

### *Requisiti*

#### *Concetti teorici:*

Conoscenza delle caratteristiche delle coniche (in particolare retta e parabola) e della forma delle loro equazioni.

#### *Software:*

Bisogna possedere python e un suo interprete sul proprio computer.

#### *Moduli python:*

Bisogna avere installati sul proprio computer i moduli python: pygame, sys, random,
(possibili altri moduli che probabilmente ci serviranno ma di cui adesso non siamo a conoscenza).

## *Preconcetti matematici:*

### *Tutti i metodi della classe retta:*

#### *eqImplicita:*

	in base ai valori dei parametri (a, b, c) ricava l’equazione implicita del tipo 
	ax + by + c = 0.

#### *eqEsplicita:*

	in base al valore dei parametri (a, b, c) ricava l’equazione esplicita del tipo 
	y = (-a/b)x + (-c/b) dove (-a/b) è il coefficiente angolare e (-c/b) è l’intercetta.

#### *trovaY:*

	presi i valori di a, b, c e x trova il valore di y. Questo metodo è implementato nel
	metodo “punti”.

#### *punti:*

    l’utente inserisce un range di valori di x e il metodo trova i corrispondenti valori di y
    attraverso il metodo “trovaY”. Successivamente inserisce le coordinate dei punti
    trovati in quel range di x all’interno di una lista di tuple

#### *m (coefficiente angolare):*

	dati i valori dei parametri (a, b) ricava il valore del coefficiente angolare (m) tramite 	la formula m = -a/b.

#### *intersezione:*

    se coefficiente angolare (m) e intercetta (q) delle due equazioni sono uguali allora le rette sono coincidenti (hanno tutti i punti in comune).
    Se il coefficiente angolare è uguale mentre l’intercetta è diversa allora non ci sono punti di intersezione in quanto le rette sono parallele.
    Se il coefficiente angolare è diverso metti a sistema le due equazioni ricavando il
    punto d’intersezione tra le due rette.

### *Tutti i metodi della classe parabola*

#### *fuoco:*

    Se l’asse di simmetria della parabola è parallelo all’asse delle ordinate allora le
    coordinate del fuoco saranno (-b/2a ; 1-Δ/4a);
    Se l’asse di simmetria della parabola è parallelo all’asse delle ascisse allora le
    coordinate del fuoco saranno (1-Δ/4a ; -b/2a).

#### *direttrice:*

	Se l’asse di simmetria della parabola è parallelo all’asse delle ordinate allora l’
    equazione della direttrice sarà y = -1-Δ/4a;
    Se l’asse di simmetria della parabola è parallelo all’asse delle ascisse allora l’
    equazione della direttrice sarà x = -1-Δ/4a.

#### *trovaY:*

	presi i valori di a, b, c e x trova il valore/valori (a seconda dell’asse di simmetria) di y.
    Questo metodo è implementato nel metodo “punti”.

#### *trovaX:*

	presi i valori di a, b, c e y trova il valore/valori (a seconda dell’asse di simmetria) di x.
    Questo metodo è implementato nel metodo “punti”.

#### *punti:*

	Se l’asse della parabola è parallelo all’asse delle ordinate:
    l’utente inserisce un range di valori di x e il metodo trova il corrispondente 
    valore di y per ogni x attraverso il metodo “trovaY”. Successivamente inserisce le coordinate dei punti trovati in quel range di x all’interno di una lista di tuple;
	Se l’asse della parabola è parallelo all’asse delle ascisse:
    l’utente inserisce un range di valori di y e il metodo trova il corrispondente 
    valore di x per ogni y attraverso il metodo “trovaX”. Successivamente inserisce le coordinate dei punti trovati in quel range di y all’interno di una lista di tuple.
    
## *Utilizzo dei concetti matematici*

Il gruppo intende utilizzare i concetti della teoria matematica acquisita fino ad ora, per la creazione di una breve animazione prepartita presente all’inizio del gioco. La teoria matematica viene quindi applicata esclusivamente nella prima scena del gioco, descritta accuratamente nella parte iniziale di questo documento. L’animazione prepartita mostrerà l’astronave aliena, che si sposta lungo la lista dei punti dell’equazione della conica digitata dall'utente, prima di procedere con la fase di “gameplay” del gioco.

## *Salvataggio dati*

Il gruppo si propone di creare una parte relativa al salvataggio remoto dei dati per poter implementare un eventuale classifica online o una modalità “multigiocatore”.
I dati che si ipotizzano di salvare, sono quelli relativi ai punteggi di fine partita in modo da creare una classifica online, dove è registrato il punteggio migliore di ogni utente.
Nel caso un utente giocasse più partite, con punteggi differenti, la classifica registrerebbe solo il punteggio più alto, che si aggiornerebbe solo nel caso in cui l'utente totalizzasse un punteggio superiore.
