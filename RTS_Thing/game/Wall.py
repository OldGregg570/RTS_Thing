from game.globals import CENTER_X, CENTER_Y, SCREEN_H, SCREEN_W
from game.Entity import Entity
from game.Vector2D import Vector2D
from game.Colors import Colors
import pygame

GAP_SIZE = 50

WALL_LENGTH = SCREEN_H - (6 * (GAP_SIZE))

WALL_A1 = [(CENTER_X - GAP_SIZE, CENTER_Y - (WALL_LENGTH / 2)),
           (CENTER_X - GAP_SIZE, CENTER_Y + (WALL_LENGTH / 2))]
WALL_A2 = [(CENTER_X + GAP_SIZE, CENTER_Y - (WALL_LENGTH / 2)),
           (CENTER_X + GAP_SIZE, CENTER_Y + (WALL_LENGTH / 2))]
WALL_A3 = [(CENTER_X, CENTER_Y - (GAP_SIZE / 2)),
           (CENTER_X, GAP_SIZE),
           (CENTER_X + WALL_LENGTH, GAP_SIZE)]
WALL_A4 = [(CENTER_X, CENTER_Y + (GAP_SIZE / 2)),
           (CENTER_X, SCREEN_H - GAP_SIZE),
           (CENTER_X - WALL_LENGTH, SCREEN_H - GAP_SIZE)]

MAP_A = [WALL_A1, WALL_A2, WALL_A3, WALL_A4]


class Wall (Entity):
    '''
    wall entity
    '''
    def __init__ (self, points):
        position = Vector2D (points [0][0], points [0][1])
        self.points = points
        
        self.bottomPoints = self._getWallBase ()
        
        super (Wall, self).__init__ (position)
    def _getWallBase (self):
        retVal = []
        for p in self.points:
            x, y = p[0], p[1]
            xOffset = (x - CENTER_X) / 12
            yOffset = (y - CENTER_Y) / 12
            retVal.append ((x - xOffset, y - yOffset)) 
        return retVal
        
        
    def draw (self, g):
        '''
        draw a line connecting all points of this wall
        '''
        super (Wall, self).draw (g)
        pygame.draw.lines (g, Colors.GREEN, False, self.points, 2)
        #pygame.draw.lines (g, COLOR_GREEN, False, self.bottomPoints)
        i = 0
        for p in self.points:
            pygame.draw.line (g, Colors.GREEN, p, self.bottomPoints [i])
            i += 1   