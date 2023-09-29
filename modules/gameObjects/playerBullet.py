"""

playerBullet.py
Author: Joseph Salerno

    
"""








import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
from modules.soundManager import SoundManager

class playerBullet(Drawable):
   """Creates bullet object for player"""
   def __init__(self, position, powerUp):
       
      if powerUp == "laser":
          super().__init__("laser.png", position)
      elif powerUp == "boom":
          super().__init__("bomb.png", position)
      else:
          super().__init__("playerBullet.png", position)
          
      self._velocity = Vector2(0,300)
      
      self._powerUp = powerUp
      self._bulletLife = 28
      
      #if laser powerup
      if self._powerUp == 'laser':
          self._bulletLife = 4
          self._velocity = Vector2(0,500)
          
          #if bomb powerup
      elif self._powerUp == "boom":
          self._bulletLife = 30
          self._velocity = Vector2(0,400)
          
          
      self._count = 0
      self._alive = True
      self._dead = False

      
   def update(self, ticks):

       
       self._count+=1
       
       #if bullet is alive too long
       if self._count == self._bulletLife:
            self._dead = True
            
            #update bullet position
       newPos = self.getPosition() + self._velocity * ticks
       newPosition = Vector2(newPos[0], newPos[1])
       
       self.setPosition(newPosition)
       
      #check if bullet is dead 
   def isDead(self):
       return self._dead
   
    
   def hit(self):
       #remove bullet if its a regular bullet and it hit something
       if self._powerUp != 'laser' and self._powerUp != 'boom':
           self.setImage("ded.png")
           self._count = 27
           
           #if the bullet is a bomb and it hits something, blow up
       elif self._powerUp == 'boom':
           self.setImage("bigbomb.png")
           SoundManager.getInstance().playSound("bombExplosion.wav")
           self._count = 28
           self._velocity = Vector2(0,0)
           
       #return current powerup    
   def getPower(self):
       return self._powerUp