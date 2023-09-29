
"""

powerup.py
Author: Joseph Salerno

    
"""


import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
import random

class Powerup(Drawable):
   """Creates powerup object"""
   def __init__(self, position):
       
      super().__init__("powerUp.png", position)
