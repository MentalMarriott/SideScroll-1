"""SideScroll game"""

from pyglet import clock
from pyglet.sprite import Sprite
from pyglet.image import load
from pyglet.gl import *
from pyglet.window import Window, key, mouse

tilde_bullet = load('tilde.png')
#ship_x and ship_y are location of ship currently
#test
bullet = Sprite(tilde_bullet, x=-50, y=-50)

arch_image = load('arch1.png')
arch = Sprite(arch_image, x=50, y=50)


########################## Controls ################################
def update(dt):
    # Move 100 pixels per second
    if keyboard[key.RIGHT]: arch.x += dt * 200

    #move 100px per started
    if keyboard[key.LEFT]: arch.x -= dt * 200

    #move up 100px/s
    if keyboard[key.UP]: arch.y += dt * 200

    #down 100px/s
    if keyboard[key.DOWN]: arch.y -= dt * 200

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
