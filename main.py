from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ObjectProperty, StringProperty, Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

class CanvasExample1(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    #rect
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2) #with tuples of points
            Color(0,1,0)
            Line(circle= (400,200,80), width=2)
            Line(rectangle= (700,500,150, 100), width=5)
            self.rect = Rectangle(pos=(700,200), size=(150,100))
    
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
        

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(9) #3
        self.vy = dp(12) #4
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size,self.ball_size)) # pos=(100,100)
        Clock.schedule_interval(self.update, 0.5) # 1second

    def on_size(self, *args):
        #print("on size: " +str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)
    
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

class CanvasExample6(Widget):
    pass

class CanvasExample7(BoxLayout):
    pass

class WidgetsExample(GridLayout):
    my_text = StringProperty("") #"Hello!") #Default value
    text_input_str = StringProperty("foo") 
    my_slider_text = StringProperty("") 
    i = 0
    cEnable = BooleanProperty(False)
    def on_button_click(self):
        print("Button clicked "+str(self.i)+" times")
        if (self.i==0 and self.cEnable):
            self.my_text = "Hello!"
            self.i = self.i +1
        elif (self.i == 1 and self.cEnable):
            self.my_text = "Button clicked "+str(self.i)+" times"
            self.i = self.i +1
        elif (self.i == 2 and self.cEnable):
            self.my_text = "Button clicked "+str(self.i)+" times"
            self.i = 0
    
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

    def on_switch_active(self, widget):
        print("Switch"+ str(widget.active))

    def on_slider_value(self, widget):
        #print("Slider:"+str(int(widget.value)))
        self.my_slider_text = str(int(widget.value))
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text

#class ScrollViewLayoutExample(ScrollView):
#    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="lr-tb"
        for i in range (0,100):
            b = Button(text=str(i+1),size_hint=(None,None), size=(dp(100),dp(100))) #(.2,.2)) #(None,None), size=(dp(100),dp(100)))
            self.add_widget(b)


class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout): #AnchourLayout example code
    pass

class BoxLayoutExample(BoxLayout):
    pass  #se il contenuto viene creato da codice python non occorre il file .kv 
    '''
    #rappresentazione grafica con codice python
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #se volessi cambiare l'orientazione del mio boxlayout
        self.orientation = "vertical" #standard e' orizontal
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
