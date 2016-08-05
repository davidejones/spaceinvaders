from gameobject import GameObject
from enemy import Enemy
from block import BLOCK_SIZE
from euclid import Vector2
import pyglet


class Swarm(GameObject):

    def __init__(self):
        GameObject.__init__(self)
        self.enemies = []
        self.enemies.append([
            Enemy(self),
            Enemy(self),
            Enemy(self),
            Enemy(self),
            Enemy(self),
            Enemy(self),
            Enemy(self),
            Enemy(self),
        ])
        for row in self.enemies:
            for enemy in row:
                self.children.append(enemy)
        self.buffer = 20
        self.enemy_width = (BLOCK_SIZE * 10) + self.buffer
        self.enemy_height = (BLOCK_SIZE * 10) + self.buffer
        self.direction = Vector2(1, 0)
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
        print('move')
        if self.position.x <= 0:
            # if we reach left side move down and then start moving right
            self.direction.x = 1
            self.direction.y = 1
        elif self.position.x >= self.enemy_width * 8:
            # if we reach right side move down and then start moving left
            self.direction.x = -1
            self.direction.y = 1
        else:
            self.direction.y = 0
        # make the x movement
        self.translate(self.enemy_width * self.direction.x, self.enemy_height * self.direction.y, 0.0)
