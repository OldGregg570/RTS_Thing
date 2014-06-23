

from game.Background import Background
from game.Grid import Grid
from game.Player import Player
from game.Selectangle import Selectangle
from game.Vector2D import Vector2D
from game.MouseButtons import MouseButtons
from game.globals import SCREEN_SIZE
import pygame

pygame.init ()



class Game ():
    '''
    Main Game Logic
    '''
    def __init__(self):
        self.drawables = []
        self.window = pygame.display.set_mode (SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        
        self.background = Background ()
        self.players = []
        self.selectangle = Selectangle (None)
        self.grid = Grid (SCREEN_SIZE)
        
        
        # Populate our list of drawables
        self.drawables.append (self.grid)
        self.drawables.append (self.selectan.gle)
       
        for n in range (3):
            self.players.append (Player (Vector2D (40, 20 * (n + 1))))
            
        for p in self.players:
            self.drawables.append (p)
    
    def update (self):
        self.checkInput()
        for p in self.players:
            p.update()
        
        for n in range (3):
            for p1 in self.players:
                for p2 in self.players:
                    if p2 != p1:
                        p1.checkCollision (p2)
                        
        
    def render (self):
        '''
        draw all drawables to the screen
        '''
        self.background.draw (self.window)
        for d in self.drawables:
            d.draw (self.window)
        pygame.display.flip()    
    
    def run (self):
        '''
        run the game
        '''
        # Event loop
        while 1:
            self.clock.tick (60)    
            self.update()
            self.render()

            
    def checkInput (self):
        '''
        check the keyboard and mouse for input
        '''
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == MouseButtons.LEFT:
                    self.selectangle.position = e.pos
                    self.selectangle.release = e.pos
                    
                if e.button == MouseButtons.MIDDLE:
                    pass
                if e.button == MouseButtons.RIGHT:
                    for p in self.players:
                        if p.selected:
                            p.setDestination(self.grid.getClosestNode (Vector2D (e.pos [0], e.pos [1])))
                            
            if e.type == pygame.MOUSEMOTION:
                if mouse [MouseButtons.LEFT - 1]:
                    self.selectangle.release = e.pos
                elif self.selectangle.release:
                    self._releaseSelectangle (pos)
            if e.type == pygame.MOUSEBUTTONUP and e.button == MouseButtons.LEFT:
                self._releaseSelectangle (pos)
    
    def _releaseSelectangle (self, pos):
        self.selectangle.release = pos
        self.select ()
        self.selectangle.release = None  
            
    def select (self):
        for p in self.players:
            if self.selectangle.contains (p.position):
                p.selected = True
            else:
                p.selected = False
        pass

            
if __name__ == '__main__': 
    game = Game ()
    game.run()  