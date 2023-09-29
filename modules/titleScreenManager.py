"""

TitleScreen.py
Author: Joseph Salerno + (mostly)Liz Matthews

    
"""
from modules.FSMs.screenFSM import ScreenState #
from modules.UI.entries import Text #
from modules.UI.displays import * #
from modules.vector2D import Vector2 #
import pygame #

class titleScreenManager(object):
      
   def __init__(self, SCREEN_SIZE):
      '''The screen displayed before game starts'''
      self._state = ScreenState()
      self._pausedText = Text(Vector2(0,0),"Paused")
      
      size = self._pausedText.getSize()
      midPointX = SCREEN_SIZE.x // 2 - size[0] // 2
      midPointY = SCREEN_SIZE.y // 2 - size[1] // 2
      
      self._pausedText.setPosition(Vector2(midPointX, midPointY))
      
      
      self._mainMenu = HoverClickMenu("background.jpg", fontName="default8")
      self._mainMenu.addText("First Pursuit", Vector2(SCREEN_SIZE.x//2 - 50.5, 
                                                              SCREEN_SIZE.y//2 - 150))
      self._mainMenu.addOption("start", "Start Game", Vector2(SCREEN_SIZE.x//2, 
                                                              SCREEN_SIZE.y//2 - 50),
                               center="both")
      self._mainMenu.addOption("exit", "Exit Game",
                               Vector2(SCREEN_SIZE.x//2, 
                                      SCREEN_SIZE.y//2 + 50),
                               center="both")
   
   def setMainMenu(self, menuType):
      if menuType == "event":
         self._mainMenu = self._eventMenu
      elif menuType == "cursor":
         self._mainMenu = self._cursorMenu      
      elif menuType == "hoverclick":
         self._mainMenu = self._hoverClickMenu
   
   def draw(self, drawSurf):
      if self._state == "game":
         self._game.draw(drawSurf)
      
         if self._state.isPaused():
            self._pausedText.draw(drawSurf)
      
      elif self._state == "mainMenu":
         self._mainMenu.draw(drawSurf)
      
      elif self._state == "gameOver":
         self._gameOver.draw(drawSurf)
   
   def handleEvent(self, event):
      # Handle screen-changing events first
      if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
         self._state.manageState("pause", self)
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
         self._state.manageState("mainMenu", self)
      else:
         if self._state == "game" and not self._state.isPaused():
            self._game.handleEvent(event)
         elif self._state == "mainMenu":
            choice = self._mainMenu.handleEvent(event)
            
            if choice == "start":
               #self._state.manageState("startGame", self)
               return "start"
            elif choice == "exit":
               return "exit"
         elif self._state == "gameOver":
            choice = self._gameOver.handleEvent(event)
            
            if choice == "exit":
               return "exit"
   
   
   def update(self, ticks):      
      if self._state == "game" and not self._state.isPaused():
         status = self._game.update(ticks, SCREEN_SIZE)
         
         
      elif self._state == "mainMenu":
         self._mainMenu.update(ticks)
      
      elif self._state == "gameOver":
         self._gameOver.update(ticks)