from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file("calculator.kv")

Window.size = (720, 1250)


class calculatorwidget(Widget):
    
    def clear(self):
        
        self.ids.input_box.text = "0"
           
        
    def number_value (self, number):
        
        prev_number = self.ids.input_box.text
        
        if "wrong equation" in prev_number:
            
            prev_number = ""
        
        if prev_number == "0":
            
            self.ids.input_box.text = ""
            
            self.ids.input_box.text = f"{number}"

        else:
            self.ids.input_box.text = f"{prev_number}{number}"
            
            
    def signs(self, sing):
        
        prev_number = self.ids.input_box.text
        
        self.ids.input_box.text = f"{prev_number}{sing}"
        
        
    def r_l(self):
        
        prev_number = self.ids.input_box.text
        
        prev_number = prev_number[:-1]
        
        self.ids.input_box.text = prev_number
        
        
    def result(self):
        
        prev_number =   self.ids.input_box.text
        
        try:
            result = eval(prev_number)
        
            self.ids.input_box.text = str(result)
            
        except:
            
            self.ids.input_box.text = "wrong equation"
            
            
    def positive_n(self):
            
            prev_number = self.ids.input_box.text
            
            if "-" in prev_number:
                
                self.ids.input_box.text = f"{prev_number.replace('-', '')}"
                
            else:
                
                self.ids.input_box.text = f"-{prev_number}"
                
                
    def dot(self):
        
        prev_number = self.ids.input_box.text
        numb_list = re.split("\+ | \* | - | / | % ", prev_number)
        
        
        
        

        
        
        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number) and "." not in numb_list[-1]:
            
            prev_number = f"{prev_number}."
            
            self.ids.input_box.text = prev_number
            
                             
        
        elif "." in prev_number:
            pass

        else:
            
            prev_number = f"{prev_number}."
            
            self.ids.input_box.text = prev_number

    

class calculator (App):
    
    def build (self):
        
        return calculatorwidget()
        
if __name__ == "__main__":
    calculator().run()