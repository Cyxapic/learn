import random
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.modalview import ModalView
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import ListProperty, ObjectProperty, StringProperty


class ToolsLayout(BoxLayout):
    color_picked = ListProperty([])
    shape = StringProperty('')

    def choose_color(self):
        view = ModalView()
        clrpr = ColorPicker()
        view.add_widget(clrpr)
        view.open()
        def on_color(instance, value):
            self.color_picked = value
        clrpr.bind(color=on_color)

    def pick_circle(self):
        self.shape = 'circle'
    
    def pick_line(self):
        self.shape = 'line'

    def pick_clear(self):
        self.shape = 'clear'


class PainLayout(BoxLayout):
    y_old = 0

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color, mode='hsv')
            if self.shape == 'clear':
                self.canvas.clear()
            elif self.shape == 'circle':
                self.y_old = touch.y
                touch.ud['data'] = Ellipse(pos=(touch.x - 30 / 2,
                                                touch.y - 30 / 2),
                                                size=(30, 30))
            else:
                touch.ud['data'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        data = touch.ud.get('data', None)
        if data:
            if self.shape == 'circle':
                try:
                    old_size = touch.ud['data'].size
                    if touch.y > self.y_old:
                        touch.ud['data'].size = (old_size[0]-10, old_size[0]-10)
                    else:
                        touch.ud['data'].size = (old_size[0]+10, old_size[0]+10)
                    self.y_old = touch.y
                except:
                    pass
            elif self.shape == 'line':
                try:
                    touch.ud['data'].points += [touch.x, touch.y]
                except:
                    pass
            else:
                pass


class MainWindow(Widget):
    pass


class MainApp(App):
    '''Класс приложения'''
    title = 'Simple painter'

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    Window.size = (800, 600)

    app = MainApp()
    app.run()