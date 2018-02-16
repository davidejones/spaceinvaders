from gameobject import GameObject
from enemy import Enemy
from config import *
from euclid3 import Vector2
import pyglet
from projectile import Projectile
import time
from random import randrange


class Swarm(GameObject):

    def __init__(self):
        self.buffer = SWARM_SPACE
        self.enemy_width = (BLOCK_SIZE * 10) + self.buffer
        self.enemy_height = (BLOCK_SIZE * 10) + self.buffer
        GameObject.__init__(self, (self.enemy_width * 11) - self.buffer, (self.enemy_height * 5) - self.buffer)
        self.enemies = [
            [
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
                Enemy(parent=self, shape=enemy1, color=0xF404D8),
            ],
            [
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
                Enemy(parent=self, shape=enemy1, color=0x8601FE),
            ],
            [
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
                Enemy(parent=self, shape=enemy2, color=0x12EBF7),
            ],
            [
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
                Enemy(parent=self, shape=enemy2, color=0x00FF00),
            ],
            [
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
                Enemy(parent=self, shape=enemy3, color=0xEEF328),
            ],
            [
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
                Enemy(parent=self, shape=enemy3, color=0xFA1904),
            ],
        ]
        for row in self.enemies:
            for enemy in row:
                self.children.append(enemy)

        self.direction = Vector2(1, 0)
        self.interval = 4.5
        for row_index, row in enumerate(self.enemies):
            for col_index, enemy in enumerate(row):
                enemy.Translate(col_index * self.enemy_width, row_index * self.enemy_height, 0.0)
        pyglet.clock.schedule_interval(self.fire, 0.5)
        self.time_elapsed_since_last_action = 0
        self.swarm_projectile_pool = [
            Projectile(Vector2(0, 1)),
            Projectile(Vector2(0, 1)),
            Projectile(Vector2(0, 1)),
            Projectile(Vector2(0, 1)),
            Projectile(Vector2(0, 1)),
            Projectile(Vector2(0, 1)),
        ]

    def faster(self):
        if self.interval > 0.1:
            self.interval -= 0.2

    def render(self):
        super().render()
        for row in self.enemies:
            for enemy in row:
                if enemy:
                    enemy.render()

    def update(self, dt):
        super().update(dt)
        for row in self.enemies:
            for enemy in row:
                if enemy:
                    enemy.update(dt)
        self.time_elapsed_since_last_action += pyglet.clock.tick()
        if self.time_elapsed_since_last_action > self.interval / 1000:
            self.move()
            self.time_elapsed_since_last_action = 0

    def get_firing_enemy(self):
        transpose = list(map(list, zip(*self.enemies)))
        last_of_each_col = []
        for row in transpose:
            for enemy in reversed(row):
                if enemy:
                    last_of_each_col.append(enemy)
                    break
        col = randrange(len(last_of_each_col))
        if last_of_each_col[col]:
            return last_of_each_col[col]

    def fire(self, dt):
        # pick a random space invader to fire
        enemy = self.get_firing_enemy()
        if enemy:
            usable = list(filter(lambda x: not x.in_use, self.swarm_projectile_pool))
            if len(usable):
                #sound = pyglet.resource.media('assets/shoot.wav', streaming=False)
                #sound.play()
                p = usable[0]
                #p.Translate((self.position.x + self.width * 0.5) - (p.width * 0.5), self.position.y, 0)
                p.Translate((self.position.x + enemy.position.x + enemy.width * 0.5) - (p.width * 0.5), self.position.y + enemy.position.y + enemy.height + self.buffer, 0)
                p.in_use = True

    def move(self, dt=0):
        move_amount = (10 * self.direction.x)

        if self.direction.y == 1:
            self.translate(0.0, 10, 0.0)
            self.direction.y = 0
            if self.position.x <= 0:
                self.direction.x = 1
            else:
                self.direction.x = -1

        if self.direction.x == 1:
            if self.position.x + self.width + move_amount >= WIDTH:
                self.Translate(WIDTH - self.width, self.position.y, self.position.z)
                self.direction.y = 1
                self.direction.x = 0
                self.faster()
            else:
                self.translate(move_amount, 0.0, 0.0)
        elif self.direction.x == -1:
            if self.position.x + move_amount <= 0:
                self.Translate(0, self.position.y, self.position.z)
                self.direction.y = 1
                self.direction.x = 0
                self.faster()
            else:
                self.translate(move_amount, 0.0, 0.0)
        #pyglet.clock.schedule_once(self.move, self.interval)

    def check_collide(self, bounds):
        item = []
        collided = False
        for row_index, row in enumerate(self.enemies):
            for col_index, enemy in enumerate(row):
                if enemy:
                    if enemy.bounds.check_intersect(bounds):
                        item = [row_index, col_index]
        if item:
            #del self.enemies[item[0]][item[1]]
            self.enemies[item[0]][item[1]] = None
            collided = True
        return collided
