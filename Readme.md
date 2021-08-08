

# Learning kivy

Studio della librearia Python **kivi** tramite video di freecodecamp: https://youtu.be/l8Imtec4ReQ?t=3445

Sarà necessario installare la libreria kivi tramite la console e se si usa **vscode** vi sarà anche la possibilità di aggiungere la libreria **Kivy** che ci aiuterà nel riconoscimento degli oggetti grafici inseriti.

NOTE: Questo Readme è realizzato con la finalità di una raccolta di appunti personali del corso, non vuole sostituirsi al contenuto del video o fornire un tutorial.

## My first Button


La dimensione _**size**_ si riferisce a Width, Height

La posizione _**pos**_ si riferisce ad x,y

Considerando la densità dei pixel, dovuta a caratteristiche costruttive, potremo vedere pulsanti più grandi o più piccoli a seconda del dispositivo su cui eseguiamo il codice. 
Usando dp la dimensione sarà la stessa indifferente dal dispositivo.


I colori per le Label è definito da **color**: _r_, _g_, _b_, _a_

Per regolare la dimensione statica dei pulsanti utilizzeremo la proprietà **size_hint** con valori relativi alla percentuale della width e dell'height.
Con la descrizione None : _size\_hint: None, None_ si fa in modo di utilizzare la dimensione indicata in **size** che resterà poi fissa e non subirà la dimensione automatica della finestra dove si trova.

La dimenzione del pulsante _size_ può essere anche definita come singole proprietà come **width** e **height**. Con questa definizione delle dimensioni è possibile integrare anche la scalatura tramite _size\_hint_. 

Con **pos\_hint** possiamo definire la posizione dei pulsanti, nel caso di BoxLayout era definita a partire da in alto a sinistra. Ciò che viene passato a questa proprietà è un _dizionario_ : {x, center_x, right} per orizzontale e {y,center_y,top}. Attenzione che è possibile usare solo una fra le coppie {x,right} e {y,top}. I valori di X,y sono in _%_. Il ridimensionamento della finestra grafica, ridurrà anche le dimensioni degli spazi lasciati da x,y. La proprietà **right** identifica la posizione del bordo destro dell'elemento e la sua posizione nella finestra in % in riferimento alla finestra.

```python
pos_hint: {"right":.5}
```

**center_x** invece identifica la posizione del centro dell'elemento grafico (valore in %)

## Come integrare un layout in un altro layout

Per inserire un layout all'interno di un altro è necessario definire il nuovo oggetto come Box,... Verrà così creato un layout annidato.

E' anche possibile aggiungere uno **spacing** fra gli elementi del layout:

```python
spacing: "10dp"
```

## AnchorLayout

Passiamo ora alla creazione di un **AnchorLayout**.
Nel codice principale del programma basta definire:
```python
class AnchorLayoutExample(AnchorLayout):
    pass
```

Come abbiamo fatto in precedenza, definiamo solo lo spazio/il contenitore grafico per l'elemento layout scelto. Andremo poi a popolare i suoi elementi esistenti all'interno del _.kv_ file associato.

L'ancoraggio degli oggetti grafici, se non definito, è pari a _center_ e _center_ per 

```python
    anchor_x: "right"  # possibili valori right, left, center
    anchor_y: "center" # possibili valori bottom, top, center
```

## GridLayout
Ora verrà valutato il **GridLayout**.  
Sarà necessario creare la classe, ovviamente nel main.py ed il relativo layout nel file thelab.kv.

Se si volesse commentare la definizione nel _main.py_ della classe _GridLayoutExample_ (serve solo a definire il tipo di tale oggetto), è possibile commentare tale codice ed implementare la tipologia del LayoutExample direttamente nel file _thelab.kv_ :
```python
    <GridLayoutExample@GridLayout>:
```

Questo stesso processo può essere utilizzato anche per il _BoxLayout_ e _AnchorLayout_ definiti in precedenza.

Il _GridLayout_ ha bisogno anche del numero di righe e colonne. Gli oggetti creati in questo Layout andranno a riempire i riquadri che si formano intersecando le righe e le colonne:
```python
    rows: 2
    cols: 2
```

Potremo usare il _size\_hint_ per il singolo elemento della riga, rispettivamente colonna, solo se tutti gli elementi avranno la stessa definizione per riga, rispettivamente colonna. Potremo usare anche la definizione della dimensione precisa per _width_ o _height_ andando a definire il numero preciso di pixel per gli elementi presenti sulla riga, rispettivamente colonna, di interesse.

Sarà anche possibile richiamare uno dei layout creati in precedenza, semplicemente richiamandone il nome

```python
 <GridLayoutExample>:
    cols:2
    Button:
        text: "A"
        size_hint: .5,1
    BoxLayoutExample:
    Button:
        text: "B"
        size_hint: .5,1
```

## StackLayout
(min 50:22)






