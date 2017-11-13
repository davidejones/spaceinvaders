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
        if self.bounds.position.x <= 0:
            # if we reach left side move down and then start moving right
            self.direction.x = 1
            self.direction.y = 1
        elif self.bounds.position.x + self.width >= WIDTH:
            # if we reach right side move down and then start moving left
            self.direction.x = -1
            self.direction.y = 1
        else:
            self.direction.y = 0
        # make the x movement
        self.translate(10 * self.direction.x, 0.0, 0.0)
