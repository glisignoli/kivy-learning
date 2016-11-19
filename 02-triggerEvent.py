from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock

class MyWidget(App):
    """Simple widget that will trigger a popup after pressing a button
    """
    def build(self):
        # Create the button
        launch_button = Button(text = 'Open Popup')
        launch_button.bind(on_press=create_popup)

        return launch_button

    def create_popup(self, dt):
        #foo = MyPopup()
        #foo.open()

        # Create the trigger
        my_trigger = Clock.create_trigger(MyPopup())
        my_trigger()


class MyPopup(Popup):
    """Popup with a single button that will close itself
    """

    def __init__(self, **kwargs):
        """ Initalise the label to update twice ever second
        """
        super(MyPopup, self).__init__(**kwargs)

        self.title = 'Hello'

        content = Button(text='Close me!')
        content.bind(on_press=self.dismiss)

        self.add_widget(content)


class TriggerEvent(App):
    """ Main class that will build
    """
    def build(self):
        return MyWidget


if __name__ == '__main__':
    MyWidget().run()
