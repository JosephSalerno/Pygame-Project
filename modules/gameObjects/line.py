"""

line.py
Author: Joseph Salerno

    
"""



import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
import random

class Line(Drawable):
   """Creates powerup object with random powerup"""
   def __init__(self, position):
       
      super().__init__("line.png", position)
