import pygame as pg
import math, sys, random

from player import *
from world import *
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.FPS = 60
        self.DT = 1/self.FPS
        self.clock = pg.time.Clock()

    # initialization
    def new_game(self):
        self.world = World(self)
        self.player = Player(self)

    def load_game(self, savedata):
        pass

    # tickables
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.player.call_key_event(event)

    def update(self):
        self.world.update()
        self.player.update()
        pg.display.update()

    def draw(self):
        self.world.draw()
        self.player.draw()
        if self.player.show_inventory:
            self.inventory.draw(self.screen)

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)
