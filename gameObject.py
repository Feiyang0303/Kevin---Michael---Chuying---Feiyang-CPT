import pygame as pg
import math
import sys

from settings import *

class GameObject:
    def __init__(self, game, pos:pg.Vector2, hitbox:pg.Vector2, sprite=None, sprite_rect:pg.Rect=None) -> None:
        self.game = game

        self.pos = pos
        self.hitbox = hitbox

        if sprite_rect == None: self.sprite_rect = pg.Rect((0, 0), (self.hitbox.x*TILE_WIDTH, self.hitbox.y*TILE_HEIGHT))
        else: self.sprite_rect = sprite_rect

        if sprite == None: self.sprite = None
        elif isinstance(sprite, pg.Surface): self.sprite = sprite
        else: self.sprite = pg.transform.scale(pg.image.load(sprite), self.sprite_rect.size)
    
    def update(self):
        pass

    def immuneUpdate(self):
        pass
    
    def draw(self):
        pass
    
    def callEvent(self, event):
        pass

    def delete(self):
        pass
