import kivy
from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.uix.widget import Widget
kivy.require('1.9.1')


class BreakoutBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)


class BreakoutPaddle(Widget):
    pass


class BreakoutBrick(Widget):
    pass


class BreakoutGame(Widget):
    """For a game of breakout we need a ball, a paddle, and some bricks
    """
    ball = ObjectProperty(None)


class BreakoutApp(App):
    #TODO Multiple Screens

    def build(self):
        game = BreakoutGame()
        return game

if __name__ == '__main__':
    BreakoutApp().run()