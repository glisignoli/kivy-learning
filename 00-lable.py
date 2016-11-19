import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require('1.9.1')


class MyApp(App):
    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
