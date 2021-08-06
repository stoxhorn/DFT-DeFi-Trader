import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# atm wallet is a seperate screen, but in the future this should be a gridlayout on the side of the app, preferrably left side. 

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from tools import Tools

t = Tools()
#define screens

class MM(Screen):

    def get_balance(self):
        global t
        t.get_total_token_balances()

def convert_data(data):
    l = []
    for key in data:
        l.append({'text': key, 'value': data[key]})
    return l

class Wallet(Screen):
    def get_balances(self):
        #fetching from database
        global t
        arr = t.get_balances()
        print(arr)
        self.rv.data = convert_data(arr)

class Options(Screen):
    
    def add_token(self):
        token_name = self.token_name.text
        token_address = self.token_address.text
        global t
        t.add_token(token_name, token_address)

    def add_address(self):
        address = self.address.text
        global t
        t.set_address(address)
        print("address set to " + address)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('ui.kv')
    
    
class MyApp(App):
    
    def build(self):
        return kv



if __name__=='__main__':
    MyApp().run()
    