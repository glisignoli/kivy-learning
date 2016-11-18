from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock


class MyLabel(Label):
    """ A custom label that will update itself every second
    """
    counter = 0

    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        self.text = "Test"

    def changetext(self, dt):
        """ All 'callbacks' need to have the dt (delta time) argument
        in order to be able to be called from the scheduler
        """
        self.counter += 1
        self.text = 'The counter is now: ' + str(self.counter)

        if self.counter == 10:
            return False

class repetingEvent(App):

    def build(self):
        countingLabel = MyLabel()
        Clock.schedule_interval(countingLabel.changetext, 1 / 1)
        return MyLabel()


if __name__ == '__main__':
    repetingEvent().run()
