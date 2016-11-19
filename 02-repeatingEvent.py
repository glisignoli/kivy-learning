import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
kivy.require('1.9.1')


class MyLabel(Label):
    """ A custom label that will update itself every second and stop when it reaches 10
    """
    counter = 0

    def __init__(self, **kwargs):
        """ Initalise the label to update twice ever second
        """
        super(MyLabel, self).__init__(**kwargs)

        # Schedule an event
        Clock.schedule_interval(self.change_text, 1/2)

    def change_text(self, dt):
        """ All 'callbacks' need to have the dt (delta time) argument
        in order to be able to be called from the scheduler
        """
        self.counter += 1
        self.text = 'The counter is now: ' + str(self.counter)

        # If the counter is 10, then unschedule the event by returning false
        if self.counter == 10:
            self.text = 'The counter stopped at ' + str(self.counter)
            return False


class RepeatingEventApp(App):
    """ Main class that will build
    """
    def build(self):
        return MyLabel()


if __name__ == '__main__':
    RepeatingEvent().run()
