

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

Canvas permette di poter disegnare nella finestra del programma con figure che si adattino al ridimensionamento. 

## Instructions KV (Rectangle, Ellipse, Line, Color ...)
Potremmo anche aggiungere una proprietà **canvas** anche all'interno di un pulsante poiché è anch'esso un widget.

```python
main.py
class CanvasExample1(Widget):
    pass

thelab.kv
<CanvasExample1>:
    canvas:
        Rectangle:
        
```

Questo visualizzerà un rettangolo bianco in basso a sinistra della nostra finestra.
Per gestire la posizione e la dimensione del rettangolo disegnato occorre utilizzare **pos** e **size**.
Se volessimo posizionarlo al centro della finestra, potremo usare _self.center_ ma dovremo sottrarre la lunghezza e la larghezza. 

```python
thelab.kv
<CanvasExample1>:
    canvas:
        Rectangle:
            pos: self.center #dp(100), dp(200) #width, height from bottom left
            size: dp(150), dp(100)  #width, height 


```

Per disegnare correttamente il rettangolo, utilizzeremo la definizione di variabili all'interno del _.kv_ file. 
Aggiungiamo anche un ellisse.
```python
thelab.kv
<CanvasExample1>:
    canvas:
        Rectangle:
            pos: self.center_x-s/2,self.center_y-s/2 #dp(100), dp(200) #width, height from bottom left
            size: s, s #dp(150), dp(100)  #width, height 
        Ellipse:
            pos: 200, 500
            size: s, s/2

```
Per i rettangoli abbiamo come dimensioni _posX_, _posY_, _lunghezza_ e _larghezza_.

### Line
Disegnando una linea che abbia come punto _self.width_ si crea una linea che si adatta al ridimensionamento della finestra stessa.
Per creare un segnale a dente invece utilizziamo 

```python
thelab.kv
Line:
    #points: (0,0, 100, 100, 200, 0, self.width, 100) # couple of x,y
    points: (0,0, self.width/4, 100, self.width/2, 0, self.width *3/4, 100, self.width, 0) # couple of x,y
    width: 2
```

Con _width: 2_ aumentiamo la dimensione della linea appena creata. 

## Circle
Proviamo a disegnare ora un cerchio. I parametri del **circle** sono definiti da _center\_x_, _center\_y_ e _raggio_:

```python
thelab.kv
<CanvasExample3>:
    canvas:
        Line:
            circle: (200,200,100) # center_x, center_y, radius
            width: 2


```

Un ellisse invece ha bisogno di _center\_x_, _center\_y_, _raggio\_x_ e _raggio\_y_:

Possiamo aggiungere un colore alle figure disegnate nella finestra utilizzando la proprietà del _canvas_ chiamata **Color** ed al cui interno **rgb**.

```python
<CanvasExample3>:
    canvas:
        Color:
            rgb: 1,0,0
        Line:
            circle: (200,200,100) # center_x, center_y, radius
            width: 2
        Line:
            ellipse: (500,300,100, 200) # center_x, center_y, radius
            width: 4
        Line:
            rectangle: (800, 100, 300, 100 ) # x, y, w, h
            width: 4
```

Se la parte relativa al colore, venisse spostata dopo una delle figure, allora solo le successive verranno modificate ed avranno il colore definito.

La proprietà **rgba** tiene conto anche del canale _Alpha_. 
Queste non sono proprietà delle singole figure, ma proprietà globali del _Canvas_.

## Drawing by Code
Per provare a definire degli oggetti grafici tramite il codice python, creiamo un _CanvasExample4_ e cercheremo di disegnare le stesse cose che visualizzavamo prima nel _canvas_ del _thelab.kv_ file. 

Proviamo a disegnare una linea:
```python
thelab.kv
CanvasExample4:  #per richiamare il codice di <CanvasExample4>

main.py
from kivy.graphics.vertex_instructions import Line
class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500)) #with tuples of points

```
I punti andranno indicati come tuple di valori X,Y. 
Aggiungiamo la dimensione della riga con _width_ ed inoltre cambiamo il colore delle figure disegnate da quel punto in poi (come prima per _Color_):

```python
main.py
class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2) #with tuples of points
            Color(0,1,0)
            Line(circle= (400,200,80), width=2)
            
```
Aggiungiamo ora un rettangolo ed uno che abbia un colore di sfondo.

```python
main.py
class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2) #with tuples of points
            Color(0,1,0)
            Line(circle= (400,200,80), width=2)
            Line(rectangle= (700,500,150, 100), width=5)
            Rectangle(pos=(700,200), size=(150,100))
```

## Movements
Vediamo come aggiornare le X,Y di una figura disegnata affinché si sposti nello spazio della finestra.

## Move the Rectangle
Aggiungiamo un pulsante e tramite il suo click, sposteremo il rettangolo verso destra. Il pulsante lo inseriremo nel _.kv_ file.

```python
thelab.kv
<CanvasExample4>:
    Button:
        pos: 100, 400
        text: "A"
        on_press: root.on_btn_click()
        width: "100dp"
        height: "40dp"

main.py
def on_btn_click(self):
        #print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size #rectangle size
        inc = dp(10)

        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x,y)
```
Quando aggiorniamo la posizione viene anche richiamato il comando di _redraw_. La gestione dell'incremento con una variabile, in funzione anche della dimensione della finestra, permette inoltre la corretta visualizzazione del rettangolo al bordo quando cambiamo la dimensione della finestra: se ci sarà ulteriore spazio, continuerà a spostarsi; se lo spazio diminuisce allora verrà ridisegnato per farlo entrare nella finestra.

## Ball and animation

(2:13:30)
Realizziamo CanvasExample5 per questa parte del codice dove realizzeremo una sfera che si muoverà nello spazio. 
Non avendo le dimensioni della finestra non riusciamo a disegnare il cerchio, al centro del riquadro. La posizione inoltre non si aggiornerà in quanto il codice è presente nel main, nel CanvasExample5 nella funzione init, quindi verrà eseguito una volta sola e non si aggiornaerà con la dimensione effettiva della finestra.
Aggiungendo la funzione 
```python
def on_size(self, *args):
```
possiamo accedere alle dimensioni della finestra e da questa aggiornare la posizione del cerchio. Siccome la posizione indicata è il punto inferiore a sinistra bisogna compensare questi. 

Per spostare la palla avremo bisogno di utilizzare una funzione che richiamata periodicamente, modifichi la sua posizione.

```python
# main
Clock.schedule_interval(self.update, 1) # 1second
def update(self, dt): #each update function requires a DT which is delta time
    x,y = self.ball.pos 
    self.ball.pos = (x+10,y)
```

Giusto per verificare il funzionamento facciamo in modo che il cerchio si sposti autonomamente verso destra con un movimento di 10 pixels.

(2:19:22)

### Exercise

Ora voglia che la pallina, dopo essere arrivata al bordo della finestra, quindi muovendosi su X,Y, rimbalzi indietro quando incontra il bordo.
Pertanto definiamo una **vx** e **vy** rispettivamente per velocità di X e Y in *main.py*.

```python
#main.py
class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
```

Ed aggiorniamo anche il metodo *update*:
```python
def update(self, dt): #each update function requires a DT which is delta time
        #print("update")
        x,y = self.ball.pos 
        x += self.vx
        y += self.vy
        #self.ball.pos = (x+10,y)
        self.ball.pos = (x,y)
```

Rilanciando il programma, *main.py* possiamo vedere di come la pallina ora si muova lunga X e Y.
La pallina però può uscire dalla finestra, quindi aggiungiamo delle condizioni alla funzione *update*:

```python
def update(self, dt): #each update function requires a DT which is delta time
        #print("update")
        x,y = self.ball.pos 
        x += self.vx
        y += self.vy
        #self.ball.pos = (x+10,y)

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if y<0:
            y = 0
            self.vy = -self.vy
        if x<0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x,y)
```

## Coordinates (RelativeLayout)
Creiamo un CanvasExample6, come classe nel *main.py* e come richiamo nel *thelab.kv*. Aggiungiamo però al canvas un pulsante per iniziare.

```python
#thelab.kv
<CanvasExample6>:
    Button:
        text: "A"
```

Avviando il programma vedremo un semplice pulsante posto nell'angolo in basso a sinistra della finestra.
Il pulsante è un *Widget* quindi posso aggiungere un canvas al suo interno:

```python
#thelab.kv
<CanvasExample6>:
    Button:
        canvas:
            Rectangle:
        text: "A"
```

Lanciando il programma possiamo quindi vedere che il *Rettangolo* viene visualizzato sopra il pulsante.
Siccome il rettangolo viene creato dopo la realizzazione del pulsante, apparirà sopra. L'ordine è quindi importante e per cambiarlo dobbiamo usare *canvas.before*:

```python
#thelab.kv
<CanvasExample6>:
    Button:
        canvas.before:
            Rectangle:
        text: "A"
```

Esiste anche *canvas.after*.
Se definissimo una posizione X,Y per il pulsante:

```python
#thelab.kv
<CanvasExample6>:
    Button:
        canvas.before:
            Rectangle:
        text: "A"
        pos: 100,100
```

Potremmo vedere come solo il pulsante venga sposta alle coordinate 100,100 e non il rettangolo. 

- Il canvas viene sempre disegnato a partire dalla posizione 0,0. L'unica eccezione è utilizzare il *RelativeLayout*.

Cambiamo il Pulsante con un **RelativeLayout**:

```python
#thelab.kv
<CanvasExample6>:
    RelativeLayout:
        canvas:
            Rectangle:
        #text: "A"
        pos: 100,100
```

Così vediamo che il rettangolo disegnato all'interno del canvas, viene spostato del valore indicato nella posizione. 
Il *RelativeLayout* è l'unico componente grafico a comportarsi così.

Proviamo ancora il comportamento appena descritto. Cambiamo il codice utilizzando un *BoxLayout* al cui interno inseriamo 2 pulsanti.

```python
#thelab.kv
<CanvasExample6>:
    BoxLayout:
        Button:
            text: "A"
        Button:
            text: "B"
```

Questo è dovuto al fatto che la classe CanvasExample6 del *main* non tiene conto della posizione. Quindi al *BoxLayout* darà una dimensione standard che è 100x100. Se volessimo dare al *BoxLayout* l'intera dimensione della finestra, dovremmo specificare la dimensione con il comando *size*.

```python
#thelab.kv
<CanvasExample6>:
    BoxLayout:
    size: root.size
        Button:
            text: "A"
        Button:
            text: "B"
```

Negli esempi precedenti non abbiamo dovuto fare questo perché non partivamo da un Canvas per istanziare i componenti grafici, ma partivamo direttamente dal *BoxLayout* e quindi occupava tutta la finestra. 

Sostituendo ad uno dei pulsante, un **Widget** posso creare al suo interno un *canvas*. 

```python
#thelab.kv
BoxLayout:
        size: root.size
        Widget:
            canvas:
                Rectangle:
                
        Button:
            text: "B"
```

Il rettangolo occuperà parte della parte sinistra della finestra. Posso invece usare i parametri size affinché il rettangolo creato occupi tutta la sua parte di schermo, cioè la dimensione del *widget*. Ne cambiamo anche il color utilizzando la proprietà *Color* del *canvas*.

```python
#thelab.kv
 BoxLayout:
        size: root.size
        Widget:
            canvas:
                Color:
                    rgb: 0, 1, 0
                Rectangle:
                    size: self.size
        Button:
            text: "B"
```

Decidiamo di cambiare il pulsante creato in precedenza, "B", con un widget rettangolo di colore blu. 

```python
#thelab.kv
#part 3 with widget modification
    BoxLayout:
        size: root.size
        Widget:
            canvas:
                Color:
                    rgb: 0, 1, 0
                Rectangle:
                    size: self.size
        Widget:
            canvas:
                Color:
                    rgb: 0, 0, 1
                Rectangle:
                    size: self.size
```

Il rettangolo appena creato viene sovrapposto al precedente. Dobbiamo definire la sua posizione per poterlo vedere a fianco a quello creato in precedenza. 

```python
#thelab.kv
#part 3 with widget modification
    BoxLayout:
        size: root.size
        Widget:
            canvas:
                Color:
                    rgb: 0, 1, 0
                Rectangle:
                    size: self.size
        Widget:
            canvas:
                Color:
                    rgb: 0, 0, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
```

Se cambiassimo il secondo widget con un *RelativeLayout* possiamo evitare di inserire la posizione come attributo.

```python
#thelab.kv
#part 3 with widget modification
    BoxLayout:
        size: root.size
        Widget:
            canvas:
                Color:
                    rgb: 0, 1, 0
                Rectangle:
                    size: self.size
        RelativeLayout:
            canvas:
                Color:
                    rgb: 0, 0, 1
                Rectangle:
                    size: self.size
```

(2:29:00)

### Esercizio
Creare *CanvasExample7* per disegnare la finestra la bandiera francese. 

```python
#thelab.kv
# in testa aggiungere:
CanvasExample7:  #per richiamare il codice di <CanvasExample7> oppure la funzione del main con lo stesso nome


    <CanvasExample7>:
    RelativeLayout:
        canvas:
            Color:
                rgb: 0, 0, 1
            Rectangle:
                size: self.size
    
    RelativeLayout:
        canvas:
            Color:
                rgb: 1, 1, 1
            Rectangle:
                size: self.size
    
    RelativeLayout:
        canvas:
            Color:
                rgb: 1, 0, 0
            Rectangle:
                size: self.size
```

```python
#main.py

class CanvasExample7(BoxLayout):
    pass
```

## Learning kivi - part 2 - Galaxy V1

Iniziamo ora la seconda parte del videocorso.
Galaxy è un gioco in cui il giocatore deve muovere la sua astronave(cursore) lungo un percorso bianco.

Gli scopi del progetto sono:
- Creare un gioco Desktop/mobile, IOS e Android, da A a Z
- Allenarsi nello sviluppo di app con Kivy (specialmente con i canvas)
- Imparare a strutturare e organizzare il codice
- Migliorare le capacità di debug (errori, comportamento sbagliato)
- Sviluppo di algoritmi (generazione di sfondi, visualizzazione in prospettiva)
- Creare ed implementare tutti gli elementi del gioco (sfondo, l'astronave, ...)
- Codificare la logica del gioco (le azioni dell'utente, fine del gioco, il punteggio, i suoni, ...)

Step 1 -> disegnare la griglia, prospettiva ed aggiungere il movimento

Step 2 -> Generare il percorso bianco. Visualizzare l'astronave e gestire le collisioni

Step 3 -> Finalizzare il gioco (menu, suoni, sfondo, punteggio, ...) 

## V1

(2:39:23)
Realizziamo il *main.py* pulito insieme al relativo *galaxy.kv*:

```python
#main.py
from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass


class GalaxyApp(App):
    pass

GalaxyApp().run()
```

    
```python
#galaxy.kv
MainWidget: #per richiamare il codice di <MainWidget> oppure la funzione del main con lo stesso nome

```

Aggiungiamo delle variabili nel *main.py* sia per la prospettiva che per la dimensione della finestra:

```python
#main.py
class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        #self.bind(pos=self.update_perspective_point) #creato da copilot
        print("INIT W:" + str(self.width)+ " H:" + str(self.height))
```

Come risultato otteniamo:
    
```bash
INIT W:100 H:100
```

Che è il valore standard e non si rifa alla dimensione corrente della finestra in quel particolare momento. Funzionerebbe se fosse lanciato dal *parent* sulla dimensione della finestra. Per gestire meglio la dimensione della finestra ed il riadattamento, oltre ad assegnare i valori della finestra, opportunamente scalati a X e Y (prospettiva) definiamo le due funzioni che gestiscono questi valori:

    
```python
#main.py
class MainWidget(Widget):
perspective_point_x = NumericProperty(0)
perspective_point_y = NumericProperty(0)

def __init__(self, **kwargs):
    super(MainWidget, self).__init__(**kwargs)
    #self.bind(pos=self.update_perspective_point) #creato da copilot
    print("INIT W:" + str(self.width)+ " H:" + str(self.height))

def on_parent(self, widget, parent):
    print("PARENT W:" + str(self.width)+ " H:" + str(self.height))

def on_size(self, *args):
    #print("SIZE W:" + str(self.width)+ " H:" + str(self.height))
    self.perspective_point_x = self.width/2
    self.perspective_point_y = self.height * 0.75

def on_perspective_point_x(self, widget, value):
    print("PX:" + str(value))

def on_perspective_point_y(self, widget, value):
    print("PY:" + str(value))
```

Possiamo farlo anche dal *.kv* file quindi commentiamo le righe nel main e scriviamo nel galaxy.kv:

```python
#galaxy.kv
MainWidget: #per richiamare il codice di <MainWidget> oppure la funzione del main con lo stesso nome


<MainWidget>:
    perspective_point_x : self.width/2
    perspective_point_y : self.height*0.75
```

(2:44:36)
### Vertical lines

Vogliamo ora visualizzare le linee verticali che costituiranno la nostra griglia. Poi useremo il *transform* per trasformare le linee verticali in prospettiva. Aggiungiamo al *main.py* la funzione che gestisce le linee verticali:

```python
#main.py
def init_vertical_lines(self):
    with self.canvas:
        Color(1, 1, 1)
        Line(points=[100, 0, 100, 100])
```

Vediamo di come la linea disegnata si sposa bene con la finestra ed il suo ridimensionamento. Vogliamo ora disegnare la linea al centro della finestra. 
Aggiungiamo una variabile alla classed *MainWidget* che contiene la linea:

```python
#main.py

line = None

def init_vertical_lines(self):
    with self.canvas:
        Color(1, 1, 1)
        self.line = Line(points=[100, 0, 100, 100]) 
```

Creiamo una funzione che assegni nuovi punti alla linea verticale. Utilizzare la funzione di *init_vertical_lines* nell'init ci crea delle problematiche sul disegno della linea usando le dimensioni della finestra: lì *self.width* sarà uguale a 100. Se usassimo la funzione di init in *on_size* il disegno verrebbe richiamato ogni volta che la finestra si ridimensiona e questo provecherebbe disegni orribili. Lasciamo la chiamata in *init* ed aggiorniamo le coordinate che chiameremo invece nel *on_size*.

```python
#main.py
def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("INIT W:" + str(self.width)+ " H:" + str(self.height))
        self.init_vertical_lines()

 def on_size(self, *args):
        self.update_vertical_lines()

 def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            self.line = Line(points=[100, 0, 100, 100]) 

    def update_vertical_lines(self):
        center_x = int(self.width / 2)

        self.line.points = [center_x, 0, center_x, 100]

```

Vediamo che la linea è posizionata al centro della finestra e quando la ridimensiono, resta sempre al posto giusto.

Adesso disegniamo le linee verticali ed orizzontali. Cambiamo la variabile *line* in *vertical_lines* come lista. Nel *init_vertical_lines* inizializzeremo le lista di linee, solo creandole. Nell' *update_vertical_lines* le definiremo per essere visualizzate correttamente.

```python
#main.py
class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    #line = None
    V_NB_LINES = 7
    V_LINES_SPACING = .1 # percentage in screen width
    vertical_lines = []

     def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0,self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2)

        for i in range(0,self.V_NB_LINES):
            line_x = int(central_line_x + offset * spacing)
            self.vertical_lines[i].points = [line_x, 0, line_x, self.height]

            offset += 1

```

Usiamo un numero dispari per *V_NB_LINES* perché altrimenti la visualizzazione non sarebbe bilanciata dal centro della finestra.

(2:55:13)

### Principle: Perspective transformation

Abbiamo utilizzato *V_SPACING* per definire la distanza fra le linee verticali affinché fosse uguale per tutte ed abbiamo disegnato le linee affinché avessero la dimensione della finestra.
Come aggiungiamo la prospettiva? Useremo *(perspective_x, perspective_y)* per definire il punto di prospettiva. Per fare questo useremo una funzione **transform_perspective()** versione 1. Dobbiamo considerare che il delta di x dipende da y. 

### Prespective Transformation: Applcation Version 1

Utilizziamo queste funzioni perché possiamo facilmente cambiare la riga del return affinché usi una o l'altra funzione implementata (*transform_2D* da/verso *transform_perspective*). Chiameremo la funzione *trasform* subito prima dell'assegnazione dei punti in *update_vertical_lines*.

```python
# main.py
class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    #line = None
    V_NB_LINES = 7
    V_LINES_SPACING = .1 # percentage in screen width
    vertical_lines = []

## ...

def update_vertical_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2)

        for i in range(0,self.V_NB_LINES):
            line_x = int(central_line_x + offset * spacing)

            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]

            offset += 1 

    def transform(self, x, y):

        #return self.transform_2D(x, y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        tr_y = y * self.perspective_point_y / self.height
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y
        
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        proportion_y = diff_y / self.perspective_point_y # 1 when diff_y == self.perspective_point_y or 0 when diff_y == 0 

        tr_x = self.perspective_point_x + diff_x * proportion_y
        return int(tr_x), int(tr_y)
```

(3:11:38)

### Exercise

Vogliamo evitare la linea centrale in modo da lasciare libera l' "intera" strada al centro.  
Riduciamo *V_NB_LINES* a 4 e vogliamo shiftare il disegno a destra. Lavoreremo in *update_vertical_lines* e possiamo o aumentare la *central_line_x* di metà dello *spacing* oppure cambiare l'*offset* aggiungendo metà di una riga (0.5).

```python
# main.py
def update_vertical_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NB_LINES / 2) + 0.5

        for i in range(0,self.V_NB_LINES):
            line_x = int(central_line_x + offset * spacing)

            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]

            offset += 1 

```

(3:14:40)

### Horizontal lines

Vogliamo ora aggiungere le linee orizzontali. Aggiungiamo le variabili necessarie alla classe e il codice necessario nell' *init*. Definiamo **init_horizontal_lines** e **update_horizontal_lines** e in quest'ultima, utilizziamo xmin e xman per capire i punti di partenza e fine delle linee verticali. Ricordiamo che l'offset è negativo e pertanto andrà sommato o sottratto nei punti necessari. 

    
```python
# main.py
H_NB_LINES = 4
H_LINES_SPACING = .2 # percentage in screen height
horizontal_lines = []

def init_horizontal_lines(self):
    with self.canvas:
        Color(1, 1, 1)
        for i in range(0,self.H_NB_LINES):
            self.horizontal_lines.append(Line())

def update_horizontal_lines(self):
    central_line_x = int(self.width / 2)
    spacing = self.V_LINES_SPACING * self.width
    offset = -int(self.V_NB_LINES / 2) + 0.5

    xmin = central_line_x + offset * spacing
    xmax = central_line_x - offset * spacing

    spacing_y = self.H_LINES_SPACING * self.height

    for i in range(0,self.H_NB_LINES):
        line_y = i * spacing_y
    
        x1, y1 = self.transform(xmin, line_y)
        x2, y2 = self.transform(xmax, line_y)
        #self.vertical_lines[i].points = [line_x, 0, line_x, self.height]
        self.horizontal_lines[i].points = [x1, y1, x2, y2] 
```

Dato che lo spacing è costante fra le linee, alcune di quelle orizzontali ci possono apparire più sottili di altre. Dobbiamo quindi aggiornare la funzione *transform*.

(3:21:55)

### Horizontal lines perspective

Le linee orizzontali sono via via più corte man mano che ci avviciniamo al vertice della prospettiva. Vogliamo trasformarlo in qualcosa che venga "*attratto*" dalla prospettiva, lo spacing anche diventa sempre più piccolo man mano che ci si avvicina. 

*factor_y* dovrà diminuire più velocemente della prospettiva, useremo *factor_y*^2. 

Modificheremo il codice della *transform_perspective*. Qui cambieremo prima *tr_y* in *lin_y*, *proportion_y* in *factor_y* e poi calcoleremo il factor_y al quadrato.


```python
# main.py
V_LINES_SPACING = .25 # percentage in screen width
V_NB_LINES = 10

H_LINES_SPACING = .1

def transform_perspective(self, x, y):
        lin_y = y * self.perspective_point_y / self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y
        
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - lin_y
        factor_y = diff_y / self.perspective_point_y # 1 when diff_y == self.perspective_point_y or 0 when diff_y == 0 

        factor_y = factor_y * factor_y

        tr_x = self.perspective_point_x + diff_x * factor_y
        tr_y = self.perspective_point_y - factor_y * self.perspective_point_y # perspective_point_y is the maximum height
        
        return int(tr_x), int(tr_y)
```

Potremmo accentuare ancora l' *attrazione* della prospettiva, aggiungiamo *factor_y* ^ N  con la funzione **pow** di python.

### Forward movement

Adesso vogliamo l'animazione del movimento in avanti. Lo faremo, come abbiamo detto, shiftando le linee orizzontali in avanti. Sottrarremo sulla linea y facendo andare le linee fuori dallo schermo. Dobbiamo implementare un meccanismo di *loop* in modo che quando shiftiamo più del vertical spacing, torniamo alla posizione iniziale. Per fare questo creeremo **current_offset_y** e lo assegneremo alle posizioni di y, 60 FPS. Definiremo inoltre la velocità di aggiornamento. Non abbiamo più la necessità di richiamare le funzioni in *on_size* lo faremo nell' **update** che stiamo definendo. 

```python
# main.py
current_offset_y = 0
SPEED = 2

def __init__(self, **kwargs):
    super(MainWidget, self).__init__(**kwargs)
    print("INIT W:" + str(self.width)+ " H:" + str(self.height))
    self.init_vertical_lines()
    self.init_horizontal_lines()
    Clock.schedule_interval(self.update, 1.0 / 60.0)

def on_size(self, *args):
    #print("SIZE W:" + str(self.width)+ " H:" + str(self.height))
    #self.perspective_point_x = self.width/2
    #self.perspective_point_y = self.height * 0.75
    pass 
    #self.update_vertical_lines()
    #self.update_horizontal_lines()

def update(self, dt):
    self.update_vertical_lines()
    self.update_horizontal_lines()
    self.current_offset_y += self.SPEED
    spacing_y = self.H_LINES_SPACING * self.height
    if self.current_offset_y >= spacing_y:
        self.current_offset_y = 0
```

Controllando se il *current_offset_y* supera lo *spacing_y* possiamo dare un senso di ciclicità alle linee. 

### Delta Time

https://youtu.be/l8Imtec4ReQ?t=12971