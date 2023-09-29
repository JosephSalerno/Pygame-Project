"""

enemy.py
Author: Joseph Salerno

    
"""



import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
from modules.gameObjects.enemyBullet import enemyBullet
from modules.soundManager import SoundManager

class Enemy(Drawable):
   """Creates enemy object one, small guys"""
   def __init__(self, position):
       
      super().__init__("enemy1.png", position)
      
      self._velocity = Vector2(0,-30)
      
      self.deathCounter = 0
      self._shooting = True
      
      self._alive = True
      self._dead = False
      self._count = 0
      
      self._scoreVal = 100
      
   def update(self, ticks, bulletArray, playerPos):
            
       
        #removes explosion image
       if self._dead:
            self.deathCounter+=1
            if self.deathCounter == 3:
                self.setImage("ded.png")
                
                
        #update newPosition=
       newPos = self.getPosition() + self._velocity * ticks
       newPosition = Vector2(newPos[0], newPos[1])
       
       self.setPosition(newPosition)
       
       #dont shoot unless player is close and shoot at a specific frequency
       if newPosition[1] - playerPos[1] < 400 and self._dead == False:
           if(self._count % 60 == 0):
               self.shoot(newPosition, bulletArray)
           self._count+=1

    #enemy shoots bullets
   def shoot(self, pos, bulletArray):
       bulletArray.append(enemyBullet(Vector2(pos[0]+15, pos[1] - 25)))
       
       #enemy explodes and plays a sound effect
   def explode(self):
       self._dead = True
       self.setImage("explosion.png")
       SoundManager.getInstance().playSound("Explosion.wav")
       self._scoreVal = 0
       
       #return score value
   def getScoreVal(self):
       return self._scoreVal
   
    #return whether or not it is dead
   def isDead(self):
       return self._dead
       