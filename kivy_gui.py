from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window


Builder.load_file('kv/chat.kv')


class ChatLayout(BoxLayout):
    pass


class MainWindow(Widget):
    '''Основное окно чата'''
    def sender(self, msg=None):
        '''Отправка сообщения в персперктиве $)
            А пока это только заполнение окна чата
        '''
        if msg != '':
            chat_str = "[b][color=008080]Вы[/color][/b]: {}\n".format(msg)
            self.ids.chat_message.text += chat_str
        self.ids.text_msg.text=''


class ChatApp(App):
    '''Класс приложения'''
    title = 'Finger balabolka'

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    Window.size = (400, 600)

    chat = ChatApp()
    chat.run()
