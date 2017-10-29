import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *
from player import Player
from enemy import Enemy
from swarm import Swarm
from block import Block, BLOCK_SIZE
from camera import Camera
from euclid3 import Matrix4

WIDTH = 800
HEIGHT = 600


class MainGame:
    def __init__(self):
        config = pyglet.gl.Config(major_version=2, minor_version=1)
        self.window = pyglet.window.Window(config=config, width=WIDTH, height=HEIGHT, resizable=False, vsync=True)
        #print(self.window.context.get_info().get_renderer())
        #print(self.window.context.get_info().get_vendor())
        #print('OpenGL Version {}'.format(self.window.context.get_info().get_version()))

        # start the background music
        #music = pyglet.resource.media('music.mp3')
        #music.play()

        # manage keys
        self.keys = key.KeyStateHandler()
        self.window.push_handlers(self.keys)

        # init objects
        self.camera = Camera(WIDTH, HEIGHT)

        self.player = Player()
        self.player.Translate(WIDTH/2 - (BLOCK_SIZE * 10)/2, HEIGHT - (BLOCK_SIZE * 10), 0.0)

        #self.enemy = Enemy()
        #self.enemy.Translate(WIDTH/2 - (BLOCK_SIZE * 10)/2, HEIGHT/2 - (BLOCK_SIZE * 10), 0.0)

        self.swarm = Swarm()

        # setup function calls
        self.window.on_draw = self.on_draw
        self.window.on_mouse_press = self.on_mouse_press
        self.window.on_mouse_motion = self.on_mouse_motion
        pyglet.clock.schedule_interval(self.update, 1/60.0) # update at 60Hz

    def on_draw(self):
        glViewport(0, 0, WIDTH, HEIGHT)
        glClearColor(0.114, 0.114, 0.114, 1.0) #1d1d1d
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.player.render()
        self.swarm.render()

    def update(self, dt):
        self.player.update(dt)
        self.swarm.update(dt)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.player.fire()

    def on_mouse_motion(self, x, y, dx, dy):
        # their x and y is from bottom left
        # my x and y is from top left
        increment_x = x - self.player.position.x
        self.player.translate(increment_x, 0.0, 0.0)
