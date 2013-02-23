"""Menu for sidescroll game"""

from pyglet.gl import *
from pyglet.window import Window, key, mouse
from pyglet import clock
from pyglet.window.key import KeyStateHandler

label = pyglet.text.Label('Menu', font_size=24,
			    x=window.width//2)

#window = pyglet.window.Window()
#Displays a menu title at half x width and from top of size 24

class main_menu(Window):
	def __init__(self):
	        """This is run when the game is created"""
		super(main_menu, self).__init__()

		self.keyboard = KeyStateHandler()
		self.set_handlers(self.keyboard)

		# Call update() 60 times a second
	        clock.schedule_interval(self.update, 1/60.0)

	def on_draw(self):
	    window.clear()
	    label.draw();

	def update(self, dt):	
		"""Called on each update"""
		if self.keyboard[key.RIGHT]:
			pass
	

window = main_menu()
pyglet.app.run()



