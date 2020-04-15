import pygame as pg
import pathlib
import math
import settings
import textbox
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
        textbox.textbox(self, (10,10),(200,500), "hello world")

    # events each gameloop #
    def events(self):
        for event in pg.event.get():
        # input events #
            # quit event #
            if event.type == pg.QUIT:
                pg.quit()
            # key events #
            if event.type == pg.KEYUP:
                # Esc ~> quit #
                if event.key == pg.K_ESCAPE:
                    self.programLoop = False
            

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
        
    # updates control -> buildmode or camera + sprites #    
    def update(self):       
        self.objects.groupAll.update()
        
# structure to hold sprites #
class programObjects:
    def __init__(self):
        self.groupAll = pg.sprite.Group()
        
# structure to hold constants #
class programState:
    def __init__(self):
        # time #
        self.del_t = 0
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