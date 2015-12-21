from gameobject import GameObject
from enemy import Enemy
from block import BLOCK_SIZE
import pyglet


class Swarm(GameObject):

    def __init__(self):
        GameObject.__init__(self)
        self.enemies = []
        self.enemies.append([
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
        ])
        self.enemies.append([
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
        ])
        self.enemies.append([
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
            Enemy(),
        ])
        self.buffer = 20
        self.enemy_width = (BLOCK_SIZE * 10) + self.buffer
        self.enemy_height = (BLOCK_SIZE * 10) + self.buffer
        for row_index, row in enumerate(self.enemies):
            for col_index, enemy in enumerate(row):
                enemy.Translate(col_index * self.enemy_width, row_index * self.enemy_height, 0.0)
        pyglet.clock.schedule_interval(self.move, 1)

    def render(self):
        GameObject.render(self)
        for row in self.enemies:
            for enemy in row:
                enemy.render()

    def update(self, dt):
        GameObject.update(self, dt)

    def move(self, dt):
        self.translate(10.0, 0.0, 0.0)
