"""SideScroll game"""

from pyglet import clock
from pyglet.sprite import Sprite
from pyglet.image import load
from pyglet.gl import *
from pyglet.window import Window, key, mouse
from pyglet.window.key import KeyStateHandler

# The images used for sprites
images = {
    'arch':   load('sprites/arch-rotated.png'),
    'bullet': load('sprites/tilde.png'),
    'star':   load('sprites/star.png'),
}

# The sprites

class Game(Window):
    def __init__(self):
        """This is run when the game is created"""
        super(Game, self).__init__()

        # Create the sprites
        self.arch = Sprite(images['arch'], x=50, y=50)
        self.bullet = Sprite(images['bullet'], x=-50, y=-50)

        # A handler that watches the keyboard state
        self.keyboard = KeyStateHandler()
        self.set_handlers(self.keyboard)

        # Call update() 60 times a second
        clock.schedule_interval(self.update, 1/60.0)

    def on_draw(self):
        """Clear the window and draw the sprites"""
        self.clear()
        self.arch.draw()
        self.bullet.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """This is run when a mouse button is pressed"""
        if button == mouse.LEFT:
            print "The left mouse button was pressed."
        elif button == mouse.RIGHT:
            print "The right mouse button was pressed."

    def update(self, dt):
        """This is called on every update

        It uses the keyboard input to move the player
        at around 200 pixels per second"""

        if self.keyboard[key.RIGHT]:
            self.arch.x += dt * 200

        if self.keyboard[key.LEFT]:
            self.arch.x -= dt * 200

        if self.keyboard[key.UP]:
            self.arch.y += dt * 200

        if self.keyboard[key.DOWN]:
            self.arch.y -= dt * 200

        # Fire if spce bar pressed
        if self.keyboard[key.SPACE]:
            self.fire()

    def fire(self):
        print "Fire!"

window = Game()
pyglet.app.run()
