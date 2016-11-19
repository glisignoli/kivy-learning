import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
kivy.require('1.9.1')

class MyGrid(GridLayout):
    """ Create a gridlayout that contains a button and a label
    When the button is pressed, use it to schedule an event (trigger)
    that will update the label's counter by 1
    """
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        label1 = MyLabel()

        # Create the trigger
        trigger = Clock.create_trigger(label1.update_counter, 1)

        # Create the button, and on press call the trigger
        button1 = Button(text="Press me!")
        button1.bind(on_press=trigger)

        # Add the widgets to the gridlayout
        self.add_widget(button1)
        self.add_widget(label1)

class MyLabel(Label):
    """ This label contains an internal counter that can be updated by calling update_counter
    """
    counter = 0

    def __init__(self, **kwargs):
        """ Initalise the label with the counter with text
        """
        super(MyLabel, self).__init__(**kwargs)
        self.text = 'The counter is now: ' + str(self.counter)

    def update_counter(self, dt):
        """ Update counter function that can be called via a trigger or schedule
        """
        self.counter += 1
        self.text = 'The counter is now: ' + str(self.counter)


class TriggerEventApp(App):
    """ Main class that will build
    """
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    TriggerEventApp().run()
