from kivy.app import App
from kivy.uix.button import Button

class MyKivyApp(App):
    def build(self):
        # Create a button with a callback function
        button = Button(text='Press me!', on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        print("Button pressed!")

# Run the app
if __name__ == '__main__':
    MyKivyApp().run()
