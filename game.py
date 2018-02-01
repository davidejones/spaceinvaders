import pyglet
pyglet.options['debug_gl'] = True
pyglet.options['shadow_window'] = False # we need this for mac os to be able to grab opengl 3.2
from pyglet.window import key, mouse, FPSDisplay
from pyglet.gl import *
from player import Player
from swarm import Swarm
from config import *
from camera import Camera
from projectile import Projectile


class MainGame:
    def __init__(self):
        config = pyglet.gl.Config(double_buffer=True, major_version=3, minor_version=2, forward_compatible=False)
        self.window = pyglet.window.Window(config=config, width=WIDTH, height=HEIGHT, resizable=False, vsync=True)
        glViewport(0, 0, WIDTH, HEIGHT)

        print('OpenGL version:', self.window.context.get_info().get_version())
        print('OpenGL 3.2 support:', self.window.context.get_info().have_version(3, 2))

        # start the background music
        #music = pyglet.resource.media('assets/music.mp3')
        #music.play()

        # init objects
        self.camera = Camera(WIDTH, HEIGHT)
        self.player = Player()
        self.player.Translate(WIDTH/2 - (BLOCK_SIZE * 10)/2, HEIGHT - (BLOCK_SIZE * 10), 0.0)
        self.swarm = Swarm()
        self.player_projectile_pool = [
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile(),
                Projectile()
        ]

        # setup function calls
        self.window.on_draw = self.render
        self.window.on_mouse_press = self.on_mouse_press
        self.window.on_mouse_motion = self.on_mouse_motion
        self.window.on_key_press = self.on_key_press
        self.window.on_key_release = self.on_key_release
        self.window.on_resize = self.on_resize
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def render(self):
        glClearColor(0.114, 0.114, 0.114, 1.0) #1d1d1d
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.player.render()
        self.swarm.render()
        for p in self.player_projectile_pool:
            if p.in_use:
                p.render()

    def update(self, dt):
        self.player.update(dt)
        self.swarm.update(dt)
        for p in self.player_projectile_pool:
            p.update(dt)
            if p.in_use:
                if self.swarm.check_collide(p.bounds):
                    sound = pyglet.resource.media('assets/invaderkilled.wav', streaming=False)
                    sound.play()
                    p.in_use = False

    def fire(self):
        sound = pyglet.resource.media('assets/shoot.wav', streaming=False)
        sound.play()
        usable = list(filter(lambda x: not x.in_use, self.player_projectile_pool))
        if len(usable):
            p = usable[0]
            p.Translate((self.player.position.x + self.player.width * 0.5) - (p.width * 0.5), self.player.position.y, 0)
            p.in_use = True

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.fire()

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.move_mouse(x, y)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.player.move_left()
        elif symbol == key.RIGHT:
            self.player.move_right()
        elif symbol == key.SPACE:
            self.fire()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.player.move_end()
        elif symbol == key.RIGHT:
            self.player.move_end()

    def on_resize(self, width, height):
        pass
