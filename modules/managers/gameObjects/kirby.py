from .mobile import Mobile
from ..FSMs.kirbyFSM import KirbyState
from ..managers.itemManager import BasicItemManager
from .items import *

import pygame

class Kirby(Mobile):
   def __init__(self, position):
      super().__init__("kirby.png", position)
      
      self._stats = BasicItemManager()
      self._stats.addItem("lives", TextItem((10,10), "Lives: ", 5, font="default8"))
      
      
      self._jumpTime = 0.5
      self._vSpeed = 100
      self._jSpeed = 100
      
      self._stats.addItem("jump",
                          RectBarItem(pygame.Rect(10,50,100,10),
                                      initialValue=self._jumpTime * 200,
                                      maxValue=self._jumpTime * 200,
                                      backgroundColor=(0,0,0)))

      
      self._nFrames = 2
      self._framesPerSecond = 2
      
      self._nFramesList = {
         "moving" : 4,
         "swimming" : 4,
         "falling" : 4,
         "jumping" : 1,
         "standing" : 2
      }
      
      self._rowList = {
         "moving" : 1,
         "jumping" : 2,
         "swimming" : 3,
         "falling" : 4,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "swimming" : 8,
         "standing" : 2,
         "jumping" : 1,
         "falling" : 8
      }
      
      self._state = KirbyState()      
      
      self.transitionState("falling")
   
   def update(self, ticks, worldSize):
      
      if self._stats.getItemValue("lives") == 0:
         return "dead"
         
      super().update(ticks, worldSize)
      
      if self._state.getState() == "jumping":
         self._stats.decreaseItem("jump", ticks * 200)
      elif self._state.getState() == "standing":
         self._stats.updateItem("jump", self._jumpTime * 200)
   
   def handleEvent(self, event):      
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_1:
            self._stats.decreaseItem("lives")
         elif event.key == pygame.K_2:
            self._stats.increaseItem("lives")
         
               
         elif event.key == pygame.K_UP:
            self._state.manageState("jump", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("left", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("right", self)
      
      elif event.type == pygame.KEYUP:
            
         if event.key == pygame.K_UP:
            self._state.manageState("fall", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("stopleft", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("stopright", self)
   
   def collideGround(self, yClip):
      self._state.manageState("ground", self)
      self._position.y -= yClip
   
   def updateMovement(self):
      pressed = pygame.key.get_pressed()
      
      if not pressed[pygame.K_UP] and self._state == "jumping":
         self._state.manageState("fall", self)
      if not pressed[pygame.K_LEFT]:
         self._state.manageState("stopleft", self)
      if not pressed[pygame.K_RIGHT]:
         self._state.manageState("stopright", self)
   
   def drawStats(self, drawSurf):
      self._stats.draw(drawSurf)
   