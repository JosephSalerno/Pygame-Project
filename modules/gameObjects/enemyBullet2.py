"""

enemyBullet2.py
Author: Joseph Salerno

    
"""

import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable

class enemyBullet2(Drawable):
   """creates enemy bullet object for bigger enemy"""
   def __init__(self, position):
       
      super().__init__("playerBullet.png", position)
      
      self._velocity = Vector2(0,-150)

      
   def update(self, ticks):

       
     
            
        #update newPosition
       newPos = self.getPosition() + self._velocity * ticks
       newPosition = Vector2(newPos[0], newPos[1])
       
       self.setPosition(newPosition)
       
       
     
