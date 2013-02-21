import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *
from pyglet import clock

window = pyglet.window.Window()

tilde_bullet = pyglet.image.load('tilde.png')
#ship_x and ship_y are location of ship currently
#test
bullet = pyglet.sprite.Sprite(tilde_bullet, x=-50, y=-50)

arch_image = pyglet.image.load('arch1.png')
arch = pyglet.sprite.Sprite(arch_image, x=50, y=50)


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

#updates
pyglet.clock.schedule_interval(update, 1/60.0)

keyboard = key.KeyStateHandler()
window.push_handlers(keyboard)


############################## loads on start
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
	print 'Right mouse'



pyglet.app.run()
