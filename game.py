"""SideScroll game"""

from pyglet import clock
from pyglet.sprite import Sprite
from pyglet.image import load
from pyglet.gl import *
from pyglet.window import Window, key, mouse

# The images used for sprites
images = {
    'bullet': load('tilde.png'),
    'arch': load('arch1.png'),
}

# The sprites
bullet = Sprite(images['bullet'], x=-50, y=-50)
arch = Sprite(images['arch'], x=50, y=50)

def update(dt):
    """This is called on every update

    It uses the keyboard input to move the player
    at around 200 pixels per second"""
    
    if keyboard[key.RIGHT]:
        arch.x += dt * 200

    if keyboard[key.LEFT]:
        arch.x -= dt * 200

    if keyboard[key.UP]:
        arch.y += dt * 200
        
    if keyboard[key.DOWN]:
        arch.y -= dt * 200

    #fire if spce bar pressed
    #if keyboard[key.SPACE]: fire()

# Call update 60 times a second
clock.schedule_interval(update, 1/60.0)

keyboard = key.KeyStateHandler()

window = Window()
window.push_handlers(keyboard)

@window.event
def on_draw():
	window.clear()
	arch.draw()
	bullet.draw()
   
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed.'
    elif button == mouse.RIGHT:
        print 'The right mouse button was pressed.'

pyglet.app.run()
