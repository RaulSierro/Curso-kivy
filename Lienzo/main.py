__author__ = 'Raul'
# Nombre de la Fila: drawing.py

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
    pass

class Drawing1App(App):
    def build(self):
        return DrawingSpace()

if __name__ == '__main__':
   Drawing1App().run()