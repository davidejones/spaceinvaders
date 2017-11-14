from gameobject import GameObject
from enemy import Enemy
from config import *
from euclid3 import Vector2
import pyglet


class Swarm(GameObject):

    def __init__(self):
        self.buffer = SWARM_SPACE
        self.enemy_width = (BLOCK_SIZE * 10) + self.buffer
        self.enemy_height = (BLOCK_SIZE * 10) + self.buffer
        GameObject.__init__(self, (self.enemy_width * 11) - self.buffer, (self.enemy_height * 5) - self.buffer)
        self.enemies = [
            [
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
            ],
            [
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
            ],
            [
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
            ],
            [
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
            ],
            [
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
                Enemy(parent=self),
            ]
        ]
        for row in self.enemies:
            for enemy in row:
                self.children.append(enemy)

        self.direction = Vector2(1, 0)
        for row_index, row in enumerate(self.enemies):
            for col_index, enemy in enumerate(row):
                enemy.Translate(col_index * self.enemy_width, row_index * self.enemy_height, 0.0)
        pyglet.clock.schedule_interval(self.move, 1)

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

    def move(self, dt):
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
            else:
                self.translate(move_amount, 0.0, 0.0)
        elif self.direction.x == -1:
            if self.position.x + move_amount <= 0:
                self.Translate(0, self.position.y, self.position.z)
                self.direction.y = 1
                self.direction.x = 0
            else:
                self.translate(move_amount, 0.0, 0.0)
