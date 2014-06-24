

from game.Background import Background
from game.Grid import Grid
from game.Player import Player
from game.Selectangle import Selectangle
from game.Vector2D import Vector2D
from game.MouseButtons import MouseButtons
from game.globals import SCREEN_SIZE
from game.Colors import Colors
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
        self.drawables.append (self.selectangle)
       
        for n in range (1):
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
        #keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == MouseButtons.LEFT:
                    self.selectangle.position = e.pos
                    self.selectangle.release = e.pos
                    
                if e.button == MouseButtons.MIDDLE:
                    pass
                if e.button == MouseButtons.RIGHT:
                    self.mouseRight (e)
  
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
                p.isSelected = True
            else:
                p.isSelected = False
        pass

    def mouseRight (self, e):
        for p in self.players:
            if p.isSelected:
                clickPosition = Vector2D (e.pos [0], e.pos [1])

                source = self.grid.getNodeAt (p.currentDestination)
                dest = self.grid.getNodeAt (clickPosition)
                
                finishNode = self.grid.shortestPath(source, dest)
                
                # make a line between start node and finish node
                # while lines are intersecting:
                #    Add a new destination right before the final node
                #        while the first line segment is still intersecting:
                #            move the new destination back one space on the path
                #        set the start node to the new node
                
                # Usage
                currentNode = finishNode.previousNode
                while currentNode != Grid.NIL:
                    currentNode.color = Colors.BLUE
                    currentNode = currentNode.previousNode
                    
                #
                p.addDestination(self.grid.getClosestNodePosition (clickPosition))
                     
    
    
if __name__ == '__main__': 
    game = Game ()
    game.run()  