from kivy.app import  App
from  kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import  Color
from kivy.graphics.vertex_instructions import  Line



class MainWidget(Widget):
    pr_p_x = NumericProperty(0)
    pr_p_y = NumericProperty(0)
    v_nb_lines = 4
    vSL = .1
    v_lines = []
    
    h_nb_lines = 4
    hSL = .2
    h_lines = []

    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
#        print("init w:" + (str(self.width)) + " h:" + (str(self.height)))
        self.init_v_Lines()
        
    def on_parent(self, widget,  parent):
#        print("parent w:" + (str(self.width)) + " h:" + (str(self.height)))
        pass   
        
    def on_size(self, *args):
        print("on size w:" + (str(self.width)) + " h:" + (str(self.height)))
        self.up_vr_lines()
        
#        self.pr_p_x = self.width/2
#        self.pr_p_y = self.height * 0.75
        
    def on_pr_p_x(self, widget, value):
        print("value x:" + (str(value)))
        
    def on_pr_p_y(self, widget, value):
        print("value y:" + (str(value)))        
        
    def init_v_Lines(self):
        with self.canvas:
            Color(1, 1, 1,)
            #self.line = Line(points=[100, 0, 100, 100])
            for i in range (0, self.v_nb_lines):
                self.v_lines.append(Line())
            
    def up_vr_lines(self):
        center_x = int(self.width/2)
        #self.line.points = [center_x, 0,center_x, 100 ]
        offset = -int(self.v_nb_lines/2) +0.5
        spacing = self.vSL * self.width
        
        
        for i in range (0, self.v_nb_lines):              
                Line_x = int(center_x + offset * spacing)
                x1, y1 = self.transform(Line_x, 0)
                x2, y2 = self.transform(Line_x, self.height)
                self.v_lines[i].points = [x1 , y1, x2, y2]
                offset += 1
                
    def transform (self, x, y):
        return self.transform_2d(x, y)
   #     return self.transform_perspective(x, y)
        
    def transform_2d(self, x, y):
        return int(x), int(y)
        
    def transform_perspective(self, x, y):
        tr_y = y * self.pr_p_y / self.height
        if tr_y > self.pr_p_y:
            tr_y = self.pr_p_y
            
            
        diff_y = x-self.pr_p_x
        diff_x = self.pr_p_y-tr_y
        proportion_y = diff_y/self.pr_p_y
        
        tr_x = self.pr_p_x + diff_x * proportion_y
        
        return int(tr_x), int(tr_y)





class GalaxyApp(App):
    pass


GalaxyApp().run()