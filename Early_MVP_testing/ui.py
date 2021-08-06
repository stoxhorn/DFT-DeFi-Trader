import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from tools import Tools

    
class My_app(App):
    
    def build(self):
        t = Tools()
        return Login_screen(t)

class MMGridLayout(Widget):
    

class CustomBtn(Widget):

    pressed = ListProperty([0,0])

class Login_screen(GridLayout):

    def __init__(self, tools, **kwargs):
        super(Login_screen, self).__init__(**kwargs)
        print(kwargs.get('val1'))
        self.cols = 3
        self.tools = tools
        btn = Button(text = 'Check Balance', on_press = self.btn_pressed)
        
        self.add_widget(Label(text='Address'))
        self.Address = TextInput(multiline=False)
        self.add_widget(self.Address)
        self.add_widget(btn)

    def btn_pressed(self, instance):
        self.tools.set_address(self.Address.text)
        print(self.tools.get_total_token_balances())
        

'''class MyEventDispatcher(EventDispatcher):

    def __init__(self, **kwargs):
        self.register_event_type('on_test')
        super(MyEventDispatcher, self).__init__(**kwargs)

    # def add_address(self, address):
'''

if __name__=='__main__':
    
    My_app().run()
    