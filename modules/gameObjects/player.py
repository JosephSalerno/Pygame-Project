"""

player.py
Author: Joseph Salerno

    
"""



import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
from modules.gameObjects.playerBullet import playerBullet
from modules.soundManager import SoundManager

class Player(Drawable):
   """Creates Player Object"""
   def __init__(self, position):
       
      self._constantVelocity = Vector2(0,50)
      super().__init__("plane.png", position)
      self._velocity = self._constantVelocity
      
      #150, 200
      self._maxVelocity = 150.0
      self._acceleration = 200
      
      self._score = 0
      
      self._movement = {pygame.K_UP: False,
                        pygame.K_LEFT: False,
                        pygame.K_RIGHT: False,
                        pygame.K_DOWN: False}
      
      self._powerup = {'laser': False,
                       'speed': False,
                       'boom': False}
          
      self._powerUpCount = 0
      self._shooting = False
      
      #returns current score
   def getScore(self):
       return self._score
   
        #updates score
   def setScore(self, newScore):
       self._score = newScore
      
   def update(self, worldinfo, screeninfo, trackingObjPos, ticks, bulletArray):

       
      #If down or up button pressed, update velocity in that direction
       if self._movement[pygame.K_DOWN] == True:
              self._velocity.y += (2 * self._acceleration * ticks)
       elif self._movement[pygame.K_UP] == True:
              self._velocity.y -= (2 * self._acceleration * ticks)
           
      #if right and left pressed, update velocity in that direction
       if self._movement[pygame.K_RIGHT] == True:
              self._velocity.x += (3 * self._acceleration * ticks)
           
       elif self._movement[pygame.K_LEFT] == True:
              self._velocity.x -= (3 * self._acceleration * ticks)
              
           
              
       #if max velocity reached, update
       if(self._velocity.magnitude() > self._maxVelocity):
          self._velocity.scale(self._maxVelocity)
           
       newPos = self.getPosition() + self._velocity * ticks
       newPosition = Vector2(newPos[0], newPos[1])
              
       #wall behavior
      
       if newPosition[0] < 0:
            self._velocity[0] = 0
       elif newPosition[1] < trackingObjPos.y + self.getHeight()//2 - screeninfo.y//2:
            self._velocity[1] = self._maxVelocity
       elif newPosition[0] + self.getWidth() > worldinfo[0]:
            self._velocity[0] = 0
       elif newPosition[1] + self.getHeight()//2 > trackingObjPos.y  + screeninfo.y//2:
            self._velocity[1] = 0
            
        #update newPosition again in case an edge was reached
       newPos = self.getPosition() + self._velocity * ticks
       newPosition = Vector2(newPos[0], newPos[1])
       
       self.setPosition(newPosition)
       
       #if player pressed space bar
       if self._shooting:
           self.shoot(newPosition, bulletArray)
           self._shooting = False
       
       
   def handleEvent(self, event):
       
       #depending on which key is pressed/unpressed, movement is updated
       if event.type == pygame.KEYDOWN:
           
          if event.key == pygame.K_DOWN:
              self._movement[pygame.K_DOWN] = True
          elif event.key == pygame.K_UP:
              self._movement[pygame.K_UP] = True
          if event.key == pygame.K_LEFT:
              self._movement[pygame.K_LEFT] = True
          elif event.key == pygame.K_RIGHT:
              self._movement[pygame.K_RIGHT] = True
              
          if event.key == pygame.K_SPACE:
              self._shooting = True
              
         
            
       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_DOWN:
               self._movement[pygame.K_DOWN] = False
               self._velocity[1] = self._constantVelocity[1]
           elif event.key == pygame.K_UP:
               self._movement[pygame.K_UP] = False
               self._velocity[1] = self._constantVelocity[1]
           if event.key == pygame.K_LEFT:
               self._movement[pygame.K_LEFT] = False
               self._velocity[0] = self._constantVelocity[0]
           elif event.key == pygame.K_RIGHT:
               self._movement[pygame.K_RIGHT] = False
               self._velocity[0] = self._constantVelocity[0]
               
   def shoot(self, pos, bulletArray):
       powerUp = None
       #if you've shot a powerup 15 times remove it
       if self._powerUpCount == 15:
           self._powerUpCount = 0
           self._powerup['laser'] = False
           self._powerup['boom'] = False
           
           #if laser
       if self._powerup['laser']:
           powerUp = 'laser'
           SoundManager.getInstance().playSound("laser.wav")
           self._powerUpCount+=1
           
           #if bomb
       elif self._powerup['boom']:
           powerUp = 'boom'
           SoundManager.getInstance().playSound("bomb.wav")
           self._powerUpCount+=1
       else:
           SoundManager.getInstance().playSound("player-shot.wav")
       bulletArray.append(playerBullet(Vector2(pos[0]+7.5, pos[1] + 10), powerUp))
       
   def setPowerUp(self, powerUp):
       #nullify existing powerup
       self._powerup['boom'] = False
       self._powerup['laser'] = False
       
       #set new powerup
       if powerUp == 1:
           self._powerup['boom'] = True
           self._powerUpCount = 0
       elif powerUp == 2:
           self._powerup['laser'] = True
           self._powerUpCount = 0