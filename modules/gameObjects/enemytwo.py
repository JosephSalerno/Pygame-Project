"""

enemyTwo.py
Author: Joseph Salerno

    
"""




import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
from modules.gameObjects.enemyBullet2 import enemyBullet2
from modules.soundManager import SoundManager

class EnemyTwo(Drawable):

   def __init__(self, position):
      """creates enemy two object"""
       
      super().__init__("enemy2.png", position)
      
      self._velocity = Vector2(0,-30)
      
      self._shootingSpeed = -35
      
      self._count = 0
      
      self.deathCounter = 0
      
      self._alive = True
      self._dead = False
      
      self._scoreVal = 250
      
   def update(self, ticks, bulletArray, playerPos):

       
        #removes explosion image
       if self._dead:
            self.deathCounter+=1
            if self.deathCounter == 3:
                self.setImage("ded.png")
     
            
        #update newPosition again in case an edge was reached
       newPos = self.getPosition() + self._velocity * ticks
       newPosition = Vector2(newPos[0], newPos[1])
       
       self.setPosition(newPosition)
       
       #dont shoot unless player is close and shoot at a set frequency
       if newPosition[1] - playerPos[1] < 400 and self._dead == False:
           if(self._count % 60 == 0):
               self.shoot(newPosition, bulletArray)
           self._count+=1

        #enemy shoots a bullet
   def shoot(self, pos, bulletArray):
       bulletArray.append(enemyBullet2(Vector2(pos[0]+12.5, pos[1] - 25)))
       
       #returns score of killing this enemy
   def getScoreVal(self):
       return self._scoreVal
          #enemy explodes and plays a sound effect
   def explode(self):
       self._dead = True
       self.setImage("explosion.png")
       SoundManager.getInstance().playSound("Explosion.wav")
       
       #return whether or not it is dead
   def isDead(self):
       return self._dead