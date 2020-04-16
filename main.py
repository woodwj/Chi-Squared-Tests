import pygame as pg
import pathlib
import math
import settings
import textWidgets
import utils
pg.init()
vec = pg.math.Vector2

# master class that hold objects and settings #
class programScene:
    def __init__(self):
        # activates program loop
        self.programLoop = True
        # create the game clock to track time
        self.clock = pg.time.Clock()
        # create the state to hold constants
        self.state = programState()
        # create object to hold sprites
        self.objects = programObjects()
        # start the scene
        self.initScene()
        
    # start/restart a scene #  
    def initScene(self):
        self.state.mousePos = vec(pg.mouse.get_pos())
        self.state.mousePressed = pg.mouse.get_pressed()
        textWidgets.textbox(self, (10,10),(200,100), "hello world")
        textWidgets.button(self, (400,300),(200,100), "press me")
        textWidgets.inputbox(self, (200,450),(200,100), q= "Table Width?: ")

    # events each gameloop #
    def events(self):
        for event in pg.event.get():
        # input events #
            # quit event #
            if event.type == pg.QUIT:
                self.programLoop = False
            # key events #
            if event.type == pg.KEYUP:
                # Esc ~> quit #
                if event.key == pg.K_ESCAPE:
                    self.programLoop = False
            # mouseclick #
            if event.type == pg.MOUSEBUTTONDOWN:
                #double click #
                if self.state.dcClock.tick() < self.state.dcTime:
                    for sprite in self.objects.groupTextBoxes:
                        if sprite.textRect.collidepoint(event.pos) and not sprite.textLocked:
                            sprite.editText = True
                            sprite.text = ""
                    for sprite in self.objects.groupInputBoxes:
                        if sprite.textRect.collidepoint(event.pos) and not sprite.textLocked:
                            sprite.editText = True
                            sprite.answer = ""

                # single click #
                if event.button == 1:
                    for sprite in self.objects.groupButtons:
                        if sprite.hover:
                            sprite.buttonFunc()
            

            if event.type == pg.KEYDOWN:
                for sprite in self.objects.groupTextBoxes:
                    if sprite.editText:
                        if event.key == pg.K_RETURN:
                            sprite.editText = False
                        elif event.key == pg.K_BACKSPACE:
                            sprite.text = sprite.text[:-1]
                        elif event.key == pg.K_DELETE:
                            sprite.kill()
                        else:
                            sprite.text += event.unicode
                
                for sprite in self.objects.groupInputBoxes:
                    if sprite.editText:
                        if event.key == pg.K_RETURN:
                            sprite.editText = False
                        elif event.key == pg.K_BACKSPACE:
                            sprite.answer = sprite.answer[:-1]
                        else:
                            sprite.answer += event.unicode
                

    # draw backround -> sprites -> text #
    def draw(self):
        # backround #
        pg.display.set_caption(settings.s_title)
        self.state.screen.fill(settings.bgColour)
        for sprite in self.objects.groupAll:
            self.state.screen.blit(sprite.image, sprite.rect)
            self.state.screen.blit(sprite.textSurf, sprite.textRect)
        #self.objects.groupAll.draw(self.state.screen)        
        # render display #
        pg.display.flip()
        
    # updates controls + sprite update methods #    
    def update(self):
        self.state.mousePos = vec(pg.mouse.get_pos())
        self.state.mousePressed = pg.mouse.get_pressed()
        self.objects.groupAll.update()
        
# structure to hold sprites #
class programObjects:
    def __init__(self):
        self.groupButtons = pg.sprite.Group()
        self.groupTextBoxes = pg.sprite.Group()
        self.groupInputBoxes = pg.sprite.Group()
        self.groupAll = pg.sprite.Group()
        
        
# structure to hold constants #
class programState:
    def __init__(self):
        # time #
        self.del_t = 0
        self.dcClock = pg.time.Clock()
        self.dcTime = 500
        # screen #
        self.screenWidth = settings.s_screenWidth
        self.screenHeight = settings.s_screenHeight
        self.tileSize = settings.s_tileSize
        self.FPS = settings.s_FPS
        self.size = (self.screenWidth,self.screenHeight)
        #self.screen = pg.display.set_mode( (0,0) , pg.FULLSCREEN)
        self.screen = pg.display.set_mode(self.size)
        # text #
        self.font = settings.s_font
        

#~~MAIN~~#
# instatiate #
chiSquare = programScene()

# gameLoop #
while chiSquare.programLoop:
    chiSquare.state.del_t = chiSquare.clock.tick(chiSquare.state.FPS) / 1000
    chiSquare.events()
    chiSquare.update()
    chiSquare.draw()
# Close the window and quit.
pg.quit()