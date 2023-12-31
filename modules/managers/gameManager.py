
from .basicManager import BasicManager
from ..gameObjects.drawable import Drawable
from ..gameObjects.backgrounds import *
from ..gameObjects.vector2D import Vector2
from .itemManager import BasicItemManager
from ..gameObjects.items import *

class GameManager(BasicManager):
   
   WORLD_SIZE = Vector2(5000, 200)
   _DEBUG = True
   
   def __init__(self, screenSize):
      self._kirby = Kirby(Vector2(0,0))
      self._floor = Floor(GameManager.WORLD_SIZE.x)
      self._bg1 = EfficientBackground(screenSize, "bg1.png", parallax=0.5)
      self._bg2 = EfficientBackground(screenSize, "bg2.png", position=Vector2(50,0), parallax=0.25)
      self._staticBG = EfficientBackground(screenSize, "bg3.png", parallax=0)
      
      self._fog = MovingBackground(screenSize, "fog.png", Vector2(-50,0), parallax=2)
      self._fog.setAlpha(100)
      
      
      
      self._HUD = BasicItemManager()
            
      self._HUD.addItem("time", RoundedItem((130,10), "Time: ", 100, font="default8"))


   
   def draw(self, drawSurf):
      
      drawSurf.fill((255,0,255))
      
      # Draw everything
      self._staticBG.draw(drawSurf)
      self._bg2.draw(drawSurf)
      self._bg1.draw(drawSurf)
         
      self._floor.draw(drawSurf)
      self._kirby.draw(drawSurf)
      
      self._fog.draw(drawSurf)
   
      self._HUD.draw(drawSurf)
      self._kirby.drawStats(drawSurf)
   
   def handleEvent(self, event):
      
      
               
      self._kirby.handleEvent(event)
   
   
   def update(self, ticks, screenSize):
      clipRect = self._kirby.getCollisionRect().clip(self._floor.getCollisionRect())
         
      if clipRect.width > 0:
         self._kirby.collideGround(clipRect.height)
         
      
      # let others update based on the amount of time elapsed
      
      status = self._kirby.update(ticks, GameManager.WORLD_SIZE)
      if status:
         return status
      self._bg2.update()
      self._bg1.update()
      self._fog.update(ticks)
      
      self._HUD.updateItem("time", -ticks)
      
      if self._HUD.getItemValue("time") <= 0:
         return "dead"
      
      Drawable.updateWindowOffset(self._kirby, screenSize, GameManager.WORLD_SIZE)
      
      
   def updateMovement(self):
      self._kirby.updateMovement()