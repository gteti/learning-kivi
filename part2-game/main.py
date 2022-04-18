from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

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
        print("SIZE W:" + str(self.width)+ " H:" + str(self.height))
        #self.perspective_point_x = self.width/2
        #self.perspective_point_y = self.height * 0.75
        pass 

    def on_perspective_point_x(self, widget, value):
        print("PX:" + str(value))
    
    def on_perspective_point_y(self, widget, value):
        print("PY:" + str(value))

class GalaxyApp(App):
    pass

GalaxyApp().run()
