import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *
from player import Player
from enemy import Enemy
from block import Block, BLOCK_SIZE
from camera import Camera
from euclid import Matrix4


class MainGame:
    def __init__(self):
        config = pyglet.gl.Config(major_version=2, minor_version=1)
        self.window = pyglet.window.Window(config=config, width=800, height=600, resizable=True, vsync=True)
        print(self.window.context.get_info().get_renderer())
        print(self.window.context.get_info().get_vendor())
        print('OpenGL Version {}'.format(self.window.context.get_info().get_version()))

        # start the background music
        #music = pyglet.resource.media('music.mp3')
        #music.play()

        # manage keys
        self.keys = key.KeyStateHandler()
        self.window.push_handlers(self.keys)

        # init objects
        self.camera = Camera()

        self.player = Player()
        self.player.matrix = Matrix4.new_translate(400 - (BLOCK_SIZE * 10)/2, 600 - (BLOCK_SIZE * 10), 0.0)

        self.enemy = Enemy()
        self.enemy.matrix = Matrix4.new_translate(400 - (BLOCK_SIZE * 10)/2, 300 - (BLOCK_SIZE * 10), 0.0)

        # setup function calls
        self.window.on_draw = self.on_draw
        self.window.on_mouse_press = self.on_mouse_press
        self.window.on_key_press = self.on_key_press
        self.window.on_key_release = self.on_key_release

    def on_draw(self):
        glViewport(0, 0, 800, 600)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.player.render()
        self.enemy.render()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print 'The left mouse button was pressed.'

    def trigger_movement(self):
        if self.keys[key.LEFT]:
            self.player.move_left()
        elif self.keys[key.RIGHT]:
            self.player.move_right()
        elif self.keys[key.SPACE]:
            self.player.fire()

    def on_key_press(self, symbol, modifiers):
        pass
        #print('press')

    def on_key_release(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.player.move_right()
        if symbol == key.LEFT:
            self.player.move_left()
        if symbol == key.SPACE:
            self.player.fire()
