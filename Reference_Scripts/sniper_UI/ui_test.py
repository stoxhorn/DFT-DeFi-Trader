import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from test1 import test


# first goal is to read a naddress and it's tokens

class My_app(App):
    
    
    def build(self):
        return Login_screen()

class Login_screen(GridLayout):

    def __init__(self, **kwargs):
        super(Login_screen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Address'))
        self.Address = TextInput(multiline=False)
        self.add_widget(self.username)
        #self.add_widget(Label(text='API key'))
        #self.key = TextInput(password=True, multiline=False)
        #self.add_widget(self.password)


if __name__=='__main__':
    print(test("0x9c8619590014D54AD9B6121dec82fF0EC949F47c"))
    #My_app().run()
    