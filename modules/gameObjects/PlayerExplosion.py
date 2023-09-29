"""

PlayerExplosion.py
Author: Joseph Salerno

    
"""

import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
import random

class playerExplosion(Drawable):
    """creates mini explosion object that dies quickly"""
    def __init__(self, position):
       
      super().__init__("miniExp.png", position)
      
      self._timer = 2
      
      self._count = 0
      
      self._dead = False
      
    def update(self):
       #lasts for two updates, then disappears
       if self._count == self._timer:
           self._dead = True
       self._count += 1
       
       
    def isDead(self):
       return self._dead