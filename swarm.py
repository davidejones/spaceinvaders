from gameobject import GameObject
from enemy import Enemy
from config import *
from euclid3 import Vector2
import pyglet
import time


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
        #pyglet.clock.schedule_once(self.move, self.interval)
        self.time_elapsed_since_last_action = 0

    def faster(self):
        if self.interval > 0.1:
            self.interval -= 0.2

    def render(self):
        super().render()
        for row in self.enemies:
            for enemy in row:
                enemy.render()

    def update(self, dt):
        super().update(dt)
        for row in self.enemies:
            for enemy in row:
                enemy.update(dt)
        self.time_elapsed_since_last_action += pyglet.clock.tick()
        if self.time_elapsed_since_last_action > self.interval / 1000:
            self.move()
            self.time_elapsed_since_last_action = 0

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
                if enemy.bounds.check_intersect(bounds):
                    item = [row_index, col_index]
        if item:
            del self.enemies[item[0]][item[1]]
            collided = True
        return collided
