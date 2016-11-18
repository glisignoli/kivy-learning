from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class myLayout(GridLayout):

    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(MyLabel())
        self.add_widget(StartStop())


class StartStop(Button):
    """A button to start/stop the counter
    """
    status = "Started"

    def __init__(self, **kwargs):
        super(StartStop, self).__init__(**kwargs)
        self.text = self.status

    def toggle(self, instance):
        if self.status == "Started":
            self.text = "Stopped"
        else:
            self.text = "Started"


class MyLabel(Label):
    """ A custom label that will update itself every second
    """
    counter = 0

    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)

        # Schedule an event
        updateCounter = Clock.schedule_interval(self.changeText, 1)


    def changeText(self, dt):
        """ All 'callbacks' need to have the dt (delta time) argument
        in order to be able to be called from the scheduler
        """
        self.counter += 1
        self.text = 'The counter is now: ' + str(self.counter)


class repetingEvent(App):

    def build(self):
        return myLayout()


if __name__ == '__main__':
    repetingEvent().run()
