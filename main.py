from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class AnchorLayoutExample(AnchorLayout): #AnchourLayout example code
    pass

class BoxLayoutExample(BoxLayout):
    pass  #se il contenuto viene creato da codice python non occorre il file .kv 
    '''
    #rappresentazione grafica con codice python
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #se volessi cambiare l'orientazione del mio boxlayout
        self.orientation = "vertical" #standard è orizontal
        b1 = Button(text="A")  
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    '''
    # min 30:54
    
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


TheLabApp().run()
