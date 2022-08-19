from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy import platform
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line


class MainWidget(Widget):
    from transforms import transform, transform_2D, transform_perspective
    from user_actions import keyboard_closed, on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    #line = None
    V_NB_LINES = 4 #10
    V_LINES_SPACING = .1 #.25 # percentage in screen width
    vertical_lines = []
    
    H_NB_LINES = 15
    H_LINES_SPACING = .1 # percentage in screen height
    horizontal_lines = []

    current_offset_y = 0
    SPEED = 2

    SPEED_X = 12 #3
    current_speed_x = 0
    current_offset_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        #self.bind(pos=self.update_perspective_point) #creato da copilot
        print("INIT W:" + str(self.width)+ " H:" + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
        
        if self.is_desktop():
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.on_keyboard_down)
            self.keyboard.bind(on_key_up=self.on_keyboard_up)
        
        Clock.schedule_interval(self.update, 1.0 / 60.0)
    
    def is_desktop(self):
        #print("Platform: ",platform)
        if platform in ('linux', 'win', 'macosx'):
            print("Platform: ",platform)
            return True
        return False

    #def on_parent(self, widget, parent):
    #    print("PARENT W:" + str(self.width)+ " H:" + str(self.height))

    #def on_size(self, *args):
        #print("SIZE W:" + str(self.width)+ " H:" + str(self.height))
        #self.perspective_point_x = self.width/2
        #self.perspective_point_y = self.height * 0.75
    #    pass 
        #self.update_vertical_lines()
        #self.update_horizontal_lines()

    #def on_perspective_point_x(self, widget, value):
        #print("PX:" + str(value))
    #    pass

    #def on_perspective_point_y(self, widget, value):
        #print("PY:" + str(value))
    #    pass
    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            #self.line = Line(points=[100, 0, 100, 100]) #[self.width/2, 0, self.width/2, self.height]))
            for i in range(0,self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def get_line_x_from_index(self, index):
        central_line_x = self.perspective_point_x
        spacing = self.V_LINES_SPACING * self.width
        offset = index - 0.5
        line_x = central_line_x + offset * spacing + self.current_offset_x

        return line_x

    def update_vertical_lines(self):
        #central_line_x = int(self.width / 2)
        #spacing = self.V_LINES_SPACING * self.width
        ##self.line.points = [central_line_x, 0, central_line_x, 100]
        #offset = -int(self.V_NB_LINES / 2) + 0.5

        start_index = -int(self.V_NB_LINES/2)+1 # half number of lines
        for i in range(start_index, start_index + self.V_NB_LINES): #(0,self.V_NB_LINES):
            #line_x = int(central_line_x + offset * spacing + self.current_offset_x)
            line_x = self.get_line_x_from_index(i)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            #self.vertical_lines[i].points = [line_x, 0, line_x, self.height]
            self.vertical_lines[i].points = [x1, y1, x2, y2]

            #offset += 1 

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0,self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        #central_line_x = int(self.width / 2)
        #spacing = self.V_LINES_SPACING * self.width
        #offset = -int(self.V_NB_LINES / 2) + 0.5

        #xmin = central_line_x + offset * spacing + self.current_offset_x
        #xmax = central_line_x - offset * spacing + self.current_offset_x

        start_index = -int(self.H_NB_LINES/2)+1 # half number of lines
        end_index = start_index + self.V_NB_LINES -1
        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index)
        spacing_y = self.H_LINES_SPACING * self.height

        for i in range(0,self.H_NB_LINES):
            line_y = i * spacing_y - self.current_offset_y
        
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            #self.vertical_lines[i].points = [line_x, 0, line_x, self.height]
            self.horizontal_lines[i].points = [x1, y1, x2, y2] 

        
    def update(self, dt):
        #print("update")
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        #self.current_offset_y += self.SPEED * time_factor
        spacing_y = self.H_LINES_SPACING * self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y = 0

        # self.current_offset_x += self.SPEED_X * time_factor
        #self.current_offset_x += self.current_speed_x * time_factor
            

class GalaxyApp(App):
    pass

GalaxyApp().run()
