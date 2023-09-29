"""

tracking.py
Author: Joseph Salerno

    
"""
import pygame
import os
import random
from modules.vector2D import Vector2
from modules.drawable import Drawable

class Tracking(Drawable):
    """creates an invisible orb that the screen follows"""
    def __init__(self, position, speed = 0):
        
        super().__init__("Tracking Obj.png", position)
        #75
        self._velocity = Vector2(0,75 + speed)
    
    
    #update orbs position and its velocity
    def update(self, worldinfo, ticks):
        
        velocity = self._velocity * ticks
        newPosition = self.getPosition() + Vector2(velocity[0], velocity[1])
        
        self._position = newPosition
        
        
        
        
        
        