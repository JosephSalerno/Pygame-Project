 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Init drawing object, most other modules inherit from here
@author: joesalerno
"""

import pygame
import os
from .vector2D import Vector2

WINDOW_OFFSET = Vector2(0,0)

class Drawable(object):
    
    def __init__(self, imageName, position, rect=None, transparent=True, parallax = 0):
        
        self._position = position
        
        self._imageName = imageName
        
        self._image = pygame.image.load(os.path.join("images", self._imageName)).convert()
        
        if (transparent):
            self._image.set_colorkey(self._image.get_at((0,0)))


    def setImage(self, newImageName):
         self._image = pygame.image.load(os.path.join("images", newImageName)).convert()
         self._image.set_colorkey(self._image.get_at((0,0)))
        
    def getPosition(self):
        return self._position
    
    def getX(self):
        return self._position.x
    
    def getY(self):
        return self._position.y

    def setPosition(self, newPosition):
        self._position = newPosition
        
    def getWidth(self):
        return self._image.get_width()
    
    def getHeight(self):
        return self._image.get_height()
       
    def getSize(self):
        return self._image.get_size()

    def getCollisionRect(self):
        newRect =  self._position + self._image.get_rect()
        return newRect
    
   
    def draw(self, surface):
        surface.blit(self._image, list(Vector2(self._position[0], 
                                               self._position[1]) - Drawable.WINDOW_OFFSET))     
      
    @classmethod
    def updateOffset(cls, trackingObject, screenSize, worldSize):
        cls.WINDOW_OFFSET = Vector2(max(0, min(trackingObject.getX() + (trackingObject.getWidth() // 2) - screenSize.x // 2,
                                    worldSize.x - screenSize.x)),
                    max(0, min(trackingObject.getY()+ (trackingObject.getHeight() // 2) - screenSize.y // 2 
                                     ,worldSize.y - screenSize.y)))
    @classmethod
    def adjustMousePos(cls, mousePos):
        newPos = Vector2(mousePos[0], mousePos[1]) + cls.WINDOW_OFFSET
        return Vector2(newPos[0], newPos[1])
    
    