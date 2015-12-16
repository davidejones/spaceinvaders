import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *
from player import Player
from camera import Camera


class MainGame:
    def __init__(self):
        config = pyglet.gl.Config(major_version=2, minor_version=1)
        self.window = pyglet.window.Window(config=config, width=800, height=600, resizable=True, vsync=True)
        print(self.window.context.get_info().get_renderer())
        print(self.window.context.get_info().get_vendor())
        print('OpenGL Version {}'.format(self.window.context.get_info().get_version()))

        # init objects
        self.camera = Camera()
        self.player = Player()

        # setup function calls
        self.window.on_draw = self.on_draw
        self.window.on_mouse_press = self.on_mouse_press
        self.window.on_key_press = self.on_key_press

    def on_draw(self):
        glViewport(0, 0, 800, 600)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.player.render()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print 'The left mouse button was pressed.'

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT or symbol == key.A:
            print 'The left arrow key was pressed.'
        elif symbol == key.RIGHT or symbol == key.D:
            print 'The left arrow key was pressed.'
        elif symbol == key.SPACE:
            print 'The space key was pressed.'