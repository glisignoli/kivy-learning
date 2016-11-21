import kivy
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
kivy.require('1.9.1')


class WindowInfo(GridLayout):
    """ Create a window with the labels defined in WindowInfo.kv
    When the window is resized, (via bind on_resize) cause the labels to update with the new height
    """
    def __init__(self, **kwargs):
        super(WindowInfo, self).__init__(**kwargs)
        self.update_window(self, Window.width, Window.height)
        Window.bind(on_resize=self.update_window)

    def update_window(self, instance, width, height):
        win_width = self.ids['win_width']
        win_height = self.ids['win_height']

        win_width.text = str(width)
        win_height.text = str(height)


class WindowInfoApp(App):
    def build(self):
        return WindowInfo()


if __name__ == '__main__':
    WindowInfoApp().run()
