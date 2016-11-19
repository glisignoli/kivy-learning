import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

kivy.require('1.9.1')


class MyLabel(Label):
    """ A custom label that will update itself every second and start a new event when it reaches 10
    """
    counter = 0

    def __init__(self, **kwargs):
        """ Initalise the label to update twice ever second
        """
        super(MyLabel, self).__init__(**kwargs)

        self.text = 'This text will soon change!'

        # Schedule an event to happen 5 seconds
        update_counter = Clock.schedule_interval(self.change_text, 5)

    def change_text(self, dt):
        """ Change the text of the label to changed!
        """
        self.text = 'Changed!'


class OneTimeEventApp(App):
    """ Main class that will build
    """
    def build(self):
        return MyLabel()


if __name__ == '__main__':
    OneTimeEventApp().run()
