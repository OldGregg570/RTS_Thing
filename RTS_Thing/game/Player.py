from game.Entity import Entity
from game.Colors import Colors
from game.globals import CENTER_X, CENTER_Y
import math
import pygame

class Player (Entity):
    '''
    player entity
    '''
    def __init__ (self, position):
        super (Player, self).__init__ (position)
        self.selected = False
    def draw (self, g): 
        if self.selected:
            color = Colors.GREEN
        else:
            color = Colors.RED
            
        p = (self.position.x, self.position.y)
        d = (self.destination.x, self.destination.y)
        x, y = p[0], p[1]
        if self.velocity.length() > 0:
            pygame.draw.line(g, Colors.GREEN, p, d)

        for n in range (4):
            xOffset = (x - CENTER_X) / (41 - (8 * n))
            yOffset = (y - CENTER_Y) / (41 - (8 * n))
            p = (int (self.position.x + xOffset), 
                int (self.position.y + yOffset))
            pygame.draw.circle(g, color, p, 4)
            
    def move (self):
        if self.selected:
            super (Player, self).move ()
            
    def checkCollision (self, other):
        if self.position.displacement (other.position) < 20:
            v = other.position - self.position
            d = v.getDirection ()
            self.nudge(d + math.pi)
            other.nudge (d) 