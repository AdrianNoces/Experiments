from kivy.metrics import dp
from kivy.uix.button import  Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import  AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import  Clock


class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    slider_value_txt = StringProperty("value")
    Text_input_str = StringProperty(" ")    
    
    def ClickOnButton(self):
        if self.count_enabled:
            print("Button clicked")
            self.count += 1
            self.my_text = str(self.count)
                
    def toggle_button_states(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True    
                                          
    def on_active_switch(self, widget):
        pass

    def on_slider_value(self,widget):
       # self.slider_value_txt = str(int(widget.value))
       pass
    
    def on_text_validate(self, widget):
        self.Text_input_str = widget.text
        
        
class  Stacklayoutexample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range (0,100):
            #size  = dp(100) + i*10
            size = dp(100)
            b = Button(text = str(i+1), size_hint = (None, None), size=(size, size))
            self.add_widget(b)

class Gridlayoutexample (GridLayout):
    pass

class Anchorlayoutexample (AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
	pass

class MainWidget(Widget):
	pass

class TheLabApp(App):
	pass
	

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0, )
            Line(points=(0, 0,100,200), width=(2))
            Line (circle=(600, 600, 50), width=(2))
            Line (rectangle=(500, 200, 160, 100), width=(2))
            self.rect = Rectangle (pos=(200, 100), size=(160, 100))
            
    def on_button_click(self):
            print ("clicked")
            inc = dp(10)
            x, y = self.rect.pos
            w, h = self.rect.size
            
            diff = self.width - (x+w)
            if diff < inc:
                inc = diff

            x += inc
            self.rect.pos = (x, y)
            
            
    def on_button_click_x(self):
            print("okay no problem")
            inc = dp(10)
            x,y = self.rect.pos
            w, h = self.rect.size
            
            diff = self.height - (y+h)
            if diff < inc:
                inc = diff
            
            y += inc
            self.rect.pos = (x,y)
            
    def on_button_click_y(self):
            print("okay no problem")
            x,y = self.rect.pos
            inc = dp(10)
            w, h = self.rect.size

            
            diff = self.width - (x-w)
            if diff < inc:
                inc = diff
            
            
            x -= dp(10)
            self.rect.pos = (x,y)
            
    def on_button_click_x2(self):
            print("okay no problem")
            x,y = self.rect.pos
            y -= dp(10)
            self.rect.pos = (x,y)
            
class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.vx = dp(3)
            self.vy = dp(3)
            self.ball_size = dp(50)
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)
    def on_size (self, *args):
        self.ball.pos = (self.center_x- self.ball_size/2, self.center_y- self.ball_size/2)
    def update(self, dt):
        print("updated")
        x, y = self.ball.pos
        y += self.vy
        x += self.vx
        
        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = - self.vy
        if x + self.ball_size > self.width:
            x = self.width-self.ball_size
            self.vx = - self.vx
        if y < 0:
            y = 0
            self.vy = - self.vy
        if x < 0:
            x = 0
            self.vx = self.vx
            
        self.ball.pos = (x, y)
        
class CanvasExample6(Widget):
        pass        
        
        
class CanvasExample7(BoxLayout):
        pass               
       
 
TheLabApp().run()