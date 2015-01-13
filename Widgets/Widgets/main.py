# Nombre Fila: Widget.py

from kivy.app import App
from kivy.uix.widget import Widget

class MyWiget(Widget):
    pass

class WidgetApp(App):
    def build(self):
        return MyWiget()

if __name__ == '__main__':
    WidgetApp().run()
