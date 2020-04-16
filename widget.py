import pygame as pg
import settings
import utils
vec = pg.math.Vector2

class widget(pg.sprite.Sprite):
    def __init__(self, programScene, tl, dimensions, groups = [], txt = ""):
        pg.sprite.Sprite.__init__(self,groups)
        self.scene = programScene
        self.dimensions = dimensions
        self.pos = vec(tl)
        self.text = str(txt)
        self.padding = 10
        self.image = pg.Surface(dimensions)
        self.rect = self.image.get_rect(topleft=tl)
        self.bgColor, self.bdrColor, self.fColour = settings.bgColour, settings.bdrColour, settings.fColour
        self.editText, self.mFollow = False, False
        self.posLocked, self.textLocked, self.widthLocked = True, True, True
        self.update()


    def draw(self, tl = None, c = None):
        if tl != None:
            self.pos = tl
        elif c != None:
            self.rect.center = c
            self.pos = self.rect.topleft

        self.image = pg.Surface(self.dimensions)
        self.image.fill(self.bgColor)
        self.rect = self.image.get_rect(topleft=self.pos)
        pg.draw.rect(self.image, self.fColour, pg.Rect((0,0),self.dimensions), 1)
        self.textSurf = self.scene.state.font.render(self.text, True, self.fColour)
        self.textRect = self.textSurf.get_rect(center = self.rect.center)
        if not self.widthLocked:
            self.dimensions = (self.textRect.width,self.dimensions[1])
            if self.dimensions[0] <= self.textRect.width: self.dimensions = (self.dimensions[0]+ 2*self.padding, self.dimensions[1])
            if self.dimensions[1] <= self.textRect.height: self.dimensions = (self.dimensions[0], self.dimensions[1] + 2*self.padding)
        elif self.dimensions[0] <= self.textRect.width:
            self.text = self.text[0:-1]
            self.editText = False
        if self.textRect.width < 50: self.textRect.width = 50
        

      
    def move(self):
        if self.mFollow:
            self.pos = self.scene.state.mousePos
            self.draw(c=self.pos)
        else: self.draw(tl=self.pos)

    def update(self):
        
        # mouse hover #
        if self.rect.collidepoint(self.scene.state.mousePos):
            self.hover = True
            # mouse click #
            if self.scene.state.mousePressed[2] and not self.posLocked: self.mFollow = True
            else: self.mFollow = False
        else:
            self.hover = False
            self.editText = False
        
        if self.hover: self.bgColor = settings.GREY
        else: self.bgColor = settings.LGREY

        
        self.move()
        
        



        
        
        
