import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#kivy.require('1.11.1')

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))
        # Add input Box
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))
        # Add input Box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))
        # Add input Box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        # Create a Submit Button
        self.submit = Button(text="Submit", font_size=32)
        #Binf the Button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza =  self.pizza.text
        color =  self.color.text

        #print(f'Hello {name}, you like {pizza} pizza, and your favorite color es {color}')

        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color es {color}'))

        # Clear the input boxes
        self.name.text= ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()