import pygame as pg
import settings
import utils
vec = pg.math.Vector2

class widget(pg.sprite.Sprite):
    def __init__(self, programScene, tl, dimensions, groups = [], txt = "test"):
        pg.sprite.Sprite.__init__(self,groups)
        self.scene = programScene
        self.dimensions = dimensions
        self.pos = vec(tl)
        self.text = str(txt)
        self.image = pg.Surface(dimensions)
        self.rect = self.image.get_rect(topleft=tl)
        self.move(self.pos)

    def move(self, pos):
        self.pos = pos
        
        self.image.fill(settings.bgText)
        self.rect = self.image.get_rect(topleft=self.pos)
        pg.draw.rect(self.image, settings.fColour, pg.Rect((0,0),self.dimensions), 1)
        self.textSurf = self.scene.state.font.render(self.text, True, settings.fColour)
        self.textRect = self.textSurf.get_rect(center = self.rect.center)
    
    def update(self):
        self.pos.x +=10
        self.move(self.pos)
        
        
