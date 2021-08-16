

# Learning kivy

Studio della librearia Python **kivi** tramite video di freecodecamp: https://youtu.be/l8Imtec4ReQ

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

Per questo layout avremo bisogno sia del codice python che della definizione degli oggetti nel _thelab.kv_ poiché sarà necessario per definire delle funzionalità aggiuntive.
Lo _StackLayout_ inserirà gli oggetti "interamente" e quindi bisogna definire, per ognuno, la sua dimensione. 

Definiamo quindi la forma standard del costruttore nel codice python:
```python
    class StackLayoutExample(StackLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            #Per esempio aggiungiamo un pulsante
            b = Button(text="Z",size_hint=(.2,.2))
            self.add_widget(b)
```
Questo nuovo pulsante _Z_ verrà inserito per prima degli ulteriori 6 pulsanti questo perché il costruttore, la funzione __init__ viene eseguita prima dell'interpretazione del _*.kv_ file. 

Creando dei bottoni a runtime è possibile definire la loro dimensione tramite _size\_hint_ in % dell'intera dimensione della finestra. Quando questa verrà ridimensionata a runtime, i pulsanti stessi si rimpiccioliranno di conseguenza.
Se invece definiamo la dimensione come _size_ dopo aver aggiunto l'importazione dalle metriche di **dp** allora possiamo instaziare a runtime i pulsanti come:
```python
b = Button(text=str(i+1),size_hint=(None,None), size=(dp(100),dp(100))) 
```
Con l'uso della dimensione in _dp_ quando la dimensione della finestra cambierà, non cambieranno di conseguenza le dimensione dei pulsanti, ma a scaglioni verranno spostati su righe successive. La dimensione dei pulsanti è quindi fissa e la loro generazione avviene da sinistra verso destra e dall'alto verso il basso. Quest'ultima parte definisce l'**orientazione** che è diversa a quanto visto in precedenza. 
```python
<StackLayoutExample>:   
    orientation: "lr-tb" #left to right and top to bottom
```
Possiamo utilizzare l'orientamento anche direttamente dal codice python:
```python
self.orientation="lr-tb"
```

E' possibile inoltre definire un **padding** e **spacing** 
```python
<StackLayoutExample>:
    #padding Left Top Right Bottom
    padding:("20dp","30dp","40dp","50dp") 
    #Spacing orizontally and vertically
    spacing: "20dp", "20dp"
```

## Scrollview
Se gli elementi nella finestra sono tanti, può essere necessario o ridimensionare la finestra(a volta non è sufficiente) oppure utilizzare il layout **Scrollview**. 
ScrollView può prendere un solo figlio:
```python
<ScrollViewExample@ScrollView>:
    StackLayoutExample:
```
Occore quindi definire la dimensione del layout chiaramente e la tipologia di scroll se verticale o orizzontale.


## PageLayout

Questo layout permette di unire layout diversi. Proviamo a visualizzare alcuni layout già creati direttamente dal _thelab.kv_ file:
```python
<PageLayoutExample@PageLayout>:
    MainWidget:
    BoxLayoutExample:
    AnchorLayoutExample:
    GridLayoutExample:
```

Potremo vedere come la visualizzazione è anomala. I layout vengono creati in sequenza e si trovano tutti a destra del primo layout, il _MainWidget_. Per poter visualizzare gli altri layout dovremo trascinarli da destra verso sinistra e questi nuovi layout andranno a sovrapporsi man mano ai precedenti creando appunto un rendering non proprio bello. Vedremo meglio come sistemare il tutto nel **CanvasLayout**.



# Widgets section

Passiamo ora alla sezione widget dove vedremo i **Toogle button**, **Switch**, **Sliders**, **Progress Bar** e anche **Text input** e infine come visualizzare le immagini e controllarne la visualizzazione.

## Button click
Vediamo come gestire il click di un pulsante. Useremo il **on_press**: Qui passeremo la funzione da eseguire quando viene premuto il pulsante. Il codice python relativo a questa funzione è nel main.py

```python
thelab.kv
<WidgetsExample>:
    cols: 3
    Button:
        text: "click here"
        on_press: root.on_button_click()
    Label:
        text: "hello"

main.py
class WidgetsExample(GridLayout):
    def on_button_click(self):
        print("Button clicked")
```

La funzione richiamata nel _.kv_ file necessata della definizione **root** e non **self** poiché altrimenti farebbe riferimento al _Button_ e non al _WidgetsExample_.


## Custom Font
Utilizzeremo il font **Lcd.ttf** indicato nelle _Resources_ del progetto.
```python
Label:
   text: root.my_text
   font_name: "RESOURCES_KIVY/1_THE_LAB/RESOURCES/fonts/Lcd.ttf"
   font_size: "40dp"
   color: 1, .5, 1, 1
```

## Toggle Button
Per utilizzare un ToggleButton dobbiamo 
```python
thelab.kv
<WidgetsExample>:
    cols: 3
    ToggleButton:
        text: "Toggle"
        on_state: root.on_toggle_button_state(self)
        size_hint: None, 1
        width: "100dp"

main.py
def on_toggle_button_state(self, widget):
    print("toggle state "+widget.state)
    if widget.state == "normal":
        #OFF
        widget.text = "OFF"
        self.cEnable = False
    else:
        #ON
        widget.text = "ON"
        self.cEnable = True
```
Richiameremo una nuova funzione con il pulsante toggle che riceverà il toggle widget stesso. In funzione dello stato di quest'ultimo potremo abilitare o meno l'incremento del contatore.

## Disabled Button
Quando abbiamo disabilitato l'incremento (Toggle Button) rimane ancora possibile premere il pulsante per incrementare il conteggio. Ovviamente il numero non cambia, la funzione non viene eseguita, ma l'animazione del pulsante è ancora attiva.

Per fare questo useremo la proprietà del pulsante **disabled** e trasfromeremo la variabile enable in una **Proprietà booleana** della classe. Il resto del codice rimarrà invariato.

```python
thelab.kv
...
Button:
    text: "click here"
    on_press: root.on_button_click()
    disabled: not(root.cEnable)
...

main.py
...
   cEnable = BooleanProperty(False) 
...
```


## Switch
Oggetto grafico semplicemente instanziato e collegato ad una funzione utilizzando la proprietà **on_active**
```python
thelab.pv
Switch:
    size_hint: None, 1
    width: "100dp"
    on_active: root.on_switch_active(self)

main.py
def on_switch_active(self, widget):
    print("Switch"+ str(widget.active))
```


## Slider
Il valore dello **Slider** è compreso fra 0 e 100.
Utilizzando una funzione per visualizzare il valore dello slider ci rendiamo conto che è un _float_ che dovremo convertire, magari in INT a seconda della necessità.

Per visualizzare il valore dello slider all'interno di una label modifichiamo il codice :
```python
thelab.pv
Slider:
    min: 0
    max: 100
    #value :
    orientation: "vertical"
    on_value: root.on_slider_value(self)

main.py
def on_slider_value(self, widget):
        #print("Slider:"+str(int(widget.value)))
        self.my_slider_text = str(int(widget.value))

```

E' possibile utilizzare una specie di variabile all'interno del _.kv_ file. Ossia definire un **id** per l'oggetto grafico e richiamarlo per ottenere il valore :
```python
thelab.pv
Slider:
        id: my_slider
        min: 0
        max: 100
        #value :
        orientation: "vertical"
        on_value: root.on_slider_value(self)
    Label:
        text: str(my_slider.value) #root.my_slider_text
        font_name: "RESOURCES_KIVY/1_THE_LAB/RESOURCES/fonts/Lcd.ttf"
        font_size: "30dp"
        color: 0, .5, 1, 1

```
Il comportamento è il medesimo che se definissimo una proprietà all'interno della classe, nel _main.py_ che contenga il valore dello slider assegnato alla label.


## Progress Bar

Useremo la **Progress Bar** e la collegheremo allo slider. Il _max_ sarà 100 ed il _min_ invece 0: è sempre 0 e non è modificabile.
Spostiamo la Label all'interno di un _BoxLayout_ :
```python
thelab.pv
BoxLayout:
    orientation: "vertical"
    Label:
        text: str(int(my_slider.value)) #rootmy_slider_text
        font_name: "RESOURCES_KIVY/1_THE_LABRESOURCES/fonts/Lcd.ttf"
        font_size: "30dp"
        color: 0, .5, 1, 1
    ProgressBar:
        max: 100
        #min: 0 è sempre 0 e non è indicabile
        value: my_slider.value
```

## TextInput
https://youtu.be/l8Imtec4ReQ?t=5949

Aggiungiamo ora un TextInput per gestire l'Input di un utente. Per avere del testo di default nel riquadro, usiamo il parametro **text**. Il contenuto inserito è di solito su multilinea, quindi occorre operare sulla propietà **multiline**. Così facendo però, quando premiamo _Invio_ la _TextInput_ abbiamo un comportamento non sempre giusto: si può fare di meglio.

```python
thelab.pv
TextInput:
    id: my_textinput
        size_hint: None, 1 #Gestiamo la lunghezza da width
        width: "100dp"
        text: "Foo" #default text
        multiline: False
Label: 
    text: my_textinput.text

```

Per operare meglio in questa condizione utilizzeremo **on_text_validate** che chiamerà una nuova funzione, propriamente definita.
```python
thelab.pv
TextInput:
    id: my_textinput
        size_hint: None, 1 #Gestiamo la lunghezza da width
        width: "100dp"
        text: "Foo" #default text
        multiline: False
        on_text_validate: root.on_text_validate(self)
Label: 
    text: root.text_input_str        

```


## Images

Vediamo ora come aggiungere le immagini in un progetto.
Partiremo da un interfaccia grafica pulita per questa parte. 

```python
<ImagesExample@GridLayout>:
    cols: 3
    Image: 
        source: "RESOURCES_KIVY/1_THE_LAB/RESOURCES/images/cake.jpg"

```

L'aspetto dell'immagine aggiunta è preservato quando si ridimensiona la finestra, il cosìddetto **ratio**. Quando riallarghiamo la pagina, le dimensioni dell'immagine arriveranno al massimo ai suoi attributi originali. La parte di finestra ulteriore sarà nera.
Per poter consentire ad un immagine di occupare una parte di finestra maggiore delle sue dimensioni originali, occorre utilizzare la proprietà **allow_stretch**.

```python
Image: 
    source: "RESOURCES_KIVY/1_THE_LAB/RESOURCES/images/cake.jpg"
    allow_stretch: True
```

Per far riempire l'intero spazio bisogna combinare *allow_stretch* con un'altra proprietà, **keep_ratio** 

```python
Image: 
    source: "RESOURCES_KIVY/1_THE_LAB/RESOURCES/images/cake.jpg"
    keep_ratio: False
```

Nel corso python, disponibile su _udemy_ per 29.99€, c'è una maggiore gestione della grafica dell'applicazione con i menù, l'apertura di nuove finestre ed il ritorno alle precedenti ecc.


# Canvas















