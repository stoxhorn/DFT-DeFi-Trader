from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

def convert_data(data):
    l = []
    for item in data:
        for key, value in item.items():
            l.append({'text': key, 'value': value})
    return l

class Invoice(Screen):
    def abc(self):
        #fetching from database
        arr = ({'Item1': 5000},{'Item2': 1000})

        # convert to [{'text': 'Item1', 'value': 5000}, {'text': 'Item2', 'value': 1000}]
        self.rv.data = convert_data(arr)

class MyApp(App):
    def build(self):
        return Builder.load_file('test.kv')

if __name__ == '__main__':
    MyApp().run()