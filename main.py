
"""

Final Game
Author: Joseph Salerno

Scoring:
    Getting hit: -500
    Killing small enemies: +100
    Killing larger enemies: +250
    
    
Sorry about the messiness of this page, I tried to include a levelManager
but it ended up not coming to be because of how I formatted my code.
It is well commented so it should be easy to follow
    
"""
import pygame
import os
import random
from modules.vector2D import Vector2
from modules.gameObjects.player import Player
from modules.gameObjects.enemy import Enemy
from modules.gameObjects.enemytwo import EnemyTwo
from modules.gameObjects.tracking import Tracking
from modules.drawable import Drawable
from modules.gameObjects.playerBullet import playerBullet
from modules.titleScreenManager import titleScreenManager
from modules.EndScreenManager import endScreenManager
from modules.gameObjects.powerup import Powerup
from modules.gameObjects.PlayerExplosion import playerExplosion
from modules.soundManager import SoundManager
from modules.gameObjects.line import Line

# Two different sizes now! Screen size is the amount we show the player,
#  and world size is the size of the interactable world
SCREEN_SIZE = Vector2(510, 780)
WORLD_SIZE = Vector2(510, 4300)


def main():
    
    
   # initialize the  pygame module
   pygame.init()
   
   UPSCALED = SCREEN_SIZE
   
   # load and set the screen/caption
   pygame.display.set_caption("First Pursuit")
   screen = pygame.display.set_mode(list(UPSCALED))
   
   #create all the variables we will need for both levels
   background = Drawable("level One.png", Vector2(0, 0), None, False)
   backgroundTwo = Drawable("levelTwo.png", Vector2(0, 0), None, False)
   backgroundThree = Drawable("level Three.png", Vector2(0, 0), None, False)
   
   player = Player(Vector2(SCREEN_SIZE.x/2,50))
   playerTwo = Player(Vector2(SCREEN_SIZE.x/2,50))
   playerThree = Player(Vector2(SCREEN_SIZE.x/2,50))
   
   track = Tracking(Vector2(SCREEN_SIZE.x//2, SCREEN_SIZE.y//2))
   trackTwo = Tracking(Vector2(SCREEN_SIZE.x//2, SCREEN_SIZE.y//2), 5)
   trackThree = Tracking(Vector2(SCREEN_SIZE.x//2, SCREEN_SIZE.y//2), -50)
   
   endLine = Line(Vector2(-80, 4200))
   finalEnd = Line(Vector2(-80, 1600))
   
   #init arrays we will need for both levels
   enemies = []
   enemiesTwo = []
   enemiesThree = []
   
   playerBullets = []
   playerBulletsTwo = []
   playerBulletsThree = []
   
   enemyBullets = []
   enemyBulletsTwo = []
   enemyBulletsThree = []
   
   powerUps = []
   powerUpsTwo = []
   powerUpsThree = []
   
   miniExplosions = []
   miniExplosionsTwo = []
   miniExplosionsThree = []
   
   
   #create gameClock
   gameClock = pygame.time.Clock()
   
   #create managers
   SoundManager.getInstance().playMusic("POL-its-a-blast-short.wav")
   titleScreen = titleScreenManager(UPSCALED)
   
   #init initial offset
   Drawable.updateOffset(player, SCREEN_SIZE, WORLD_SIZE)
   
   #init texts
   arial = pygame.font.SysFont('Arial', 40)
   scoreString = "Score: 0" 
   levelString = "Level: 1"
   scoreText = arial.render(scoreString, True, (255,255,255))
   levelText = arial.render(levelString, True, (255,255,255))
   
   #init incremental values
   musicTime = 0
   score = 0
   
   #title screen boolean
   start = False;
   
   #================================================================#
   
   #create enemies for level one
   for i in range(0, 50, 10):
       enemies.append(Enemy(Vector2(10 + 4 * i,1500 + i)))
       
       
   for i in range(0, 50, 10):
       enemies.append(Enemy(Vector2(10 + 4 * i,1600 + i)))
       
   for i in range(0, 50, 10):
       enemies.append(Enemy(Vector2(295 + 4 * i,1700 - i)))
       
       
   for i in range(0, 50, 10):
       enemies.append(Enemy(Vector2(10 + 4 * i,1800 + i)))
   
   for i in range(0, 50, 10):
       if i != 40:
           enemies.append(Enemy(Vector2(10 + 4 * i,2000 + i)))
       else:
           enemies.append(EnemyTwo(Vector2(15 + 4 * i,2000 + i + 5)))
       
   for i in range(0, 50, 10):
       if i != 0:
           enemies.append(Enemy(Vector2(295 + 4 * i,2250 - i)))
       else:
           enemies.append(EnemyTwo(Vector2(280 + 4 * i,2250 - i)))
           
   for i in range(0, 50, 10):
       if i != 10:
           enemies.append(Enemy(Vector2(50 + 8*i,2450)))
        
   for i in range(0, 50, 10):
       if i != 10:
           enemies.append(Enemy(Vector2(95 + 8*i,2550)))
       
   for i in range(0, 50, 10):
       if i != 10:
           enemies.append(Enemy(Vector2(50 + 8*i,2650)))
        
   for i in range(0, 50, 10):
       if i!= 10:
           enemies.append(Enemy(Vector2(95 + 8*i,2750)))
       
   for i in range(0, 40, 10):
       enemies.append(EnemyTwo(Vector2(50 + 12 * i,3100)))
       
   for i in range(0, 90, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,3350)))
       
   for i in range(0, 90, 10):
       enemies.append(Enemy(Vector2(30 + 5.2 * i,3600)))
       
   for i in range(0, 90, 10):
       enemies.append(Enemy(Vector2(30 + 5.2 * i,3700)))
       
   for i in range(0, 90, 10):
       enemies.append(Enemy(Vector2(30 + 5.2 * i,3800)))
       
   for i in range(0, 90, 10):
       enemies.append(Enemy(Vector2(30 + 5.2 * i,3900)))
       
   for i in range(0, 90, 10):
       enemies.append(Enemy(Vector2(30 + 5.2 * i,4000)))
   
   for i in range(0, 90, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,4200)))
 
   for i in range(0, 90, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,4300)))
     
   for i in range(0, 90, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,4400)))
       
       
   for i in range(0, 90, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,4600)))
       
   for i in range(0, 90, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,4700)))
       
   for i in range(0, 50, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,4900 - i)))
       
   for i in range(0, 50, 10):
       enemies.append(EnemyTwo(Vector2(235 + 5.2 * i,4950 - i)))
       
    
   for i in range(0, 50, 10):
       enemies.append(EnemyTwo(Vector2(30 + 5.2 * i,5050 - i)))
       
   for i in range(0, 50, 10):
       enemies.append(EnemyTwo(Vector2(235 + 5.2 * i,5100 - i)))
       
       
#================================================================#   
       
 #create enemies for level two
   for i in range(0, 120, 10):
       enemiesTwo.append(Enemy(Vector2(10 + 4 * i,1500 + i)))
       
   for i in range(0, 120, 10):
       enemiesTwo.append(Enemy(Vector2(10 + 4 * i,1700 + i)))
       
   for i in range(0, 120, 10):
       enemiesTwo.append(Enemy(Vector2(460 - 4 * i,1950 + i)))
       
   for i in range(0, 120, 10):
       enemiesTwo.append(Enemy(Vector2(460 - 4 * i,2200 + i)))
       
   for i in range(0, 60, 10):
       enemiesTwo.append(Enemy(Vector2(460 - 4 * i,2500 + i)))
   for i in range(0, 60, 10):
       enemiesTwo.append(Enemy(Vector2(10 + 4 * i,2500 + i)))
       
       
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(460 - 6 * i,2750 + i)))
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(10 + 6 * i, 2750 + i)))
       
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(460 - 6 * i,2900 + i)))
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(10 + 6 * i, 2900 + i)))
       
       
       
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(460 - 6 * i,3050 + i)))
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(10 + 6 * i, 3050 + i)))
       
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(460 - 6 * i,3200 + i)))
   for i in range(0, 40, 10):
       enemiesTwo.append(EnemyTwo(Vector2(10 + 6 * i, 3200 + i)))
       

       
   for i in range(0, 90, 10):
       enemiesTwo.append(Enemy(Vector2(30 + 5.2 * i,3500)))
       
   for i in range(0, 90, 10):
       enemiesTwo.append(Enemy(Vector2(30 + 5.2 * i,3600)))
       
   for i in range(0, 90, 10):
       enemiesTwo.append(Enemy(Vector2(30 + 5.2 * i,3700)))
       
       
   for i in range(0, 90, 10):
       enemiesTwo.append(EnemyTwo(Vector2(10, 3900 + i*4)))
       enemiesTwo.append(EnemyTwo(Vector2(460 , 3900 + i*4)))
       
   for i in range(0, 100, 10):
       enemiesTwo.append(Enemy(Vector2(150 , 3900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(300 , 3900 + i*4)))
       if i % 4 == 0:
           enemiesTwo.append(Enemy(Vector2(75 , 3900 + i*4)))
           enemiesTwo.append(Enemy(Vector2(375 , 3900 + i*4)))
           
    
   for i in range(0, 90, 10):
       enemiesTwo.append(EnemyTwo(Vector2(30 + 5.2 * i,4550)))
       enemiesTwo.append(Enemy(Vector2(30 + 5.2 * i,4650)))
       enemiesTwo.append(EnemyTwo(Vector2(30 + 5.2 * i,4750)))
    
    
   for i in range(0, 50, 10):
       enemiesTwo.append(Enemy(Vector2(150 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(300 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(175 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(275 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(250 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(200 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(325 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(225 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(350 , 4900 + i*4)))
       enemiesTwo.append(Enemy(Vector2(125 , 4900 + i*4)))


#================================================================#


   #create enemies for level Three
   for i in range(0, 450, 10):
       enemiesThree.append(EnemyTwo(Vector2(10, 500 + i*4)))
       enemiesThree.append(EnemyTwo(Vector2(460 , 500 + i*4)))
       enemiesThree.append(EnemyTwo(Vector2(230 , 500 + i*4)))
       
   for i in range(0, 500, 10):
       enemiesThree.append(Enemy(Vector2(150 , 500 + i*4)))
       enemiesThree.append(Enemy(Vector2(300 , 500 + i*4)))
       if i % 4 == 0:
           enemiesThree.append(Enemy(Vector2(75 , 500 + i*4)))
           enemiesThree.append(Enemy(Vector2(375 , 500 + i*4)))
           
           
#================================================================#        
           
           
   #create powerups for level One
   powerUps.append(Powerup(Vector2(SCREEN_SIZE.x/2, 2500)))
   
   powerUps.append(Powerup(Vector2(SCREEN_SIZE.x/2, 3200)))
   
   
   #create powerups for level two
   powerUpsTwo.append(Powerup(Vector2(100, 2500)))
   
   powerUpsTwo.append(Powerup(Vector2(400, 3200)))
   
   powerUpsTwo.append(Powerup(Vector2(250, 1800)))
   
   
   #create powerups for level three
   for i in range(0, 80, 10):
       powerUpsThree.append(Powerup(Vector2(30 + i*10, 300)))
       powerUpsThree.append(Powerup(Vector2(30 + i*10, 700)))
       powerUpsThree.append(Powerup(Vector2(30 + i*10, 1100)))
   
   
   
   
   #create level arrays
   
   lvlOne = [background, player, track, enemies, playerBullets, enemyBullets,
             powerUps, miniExplosions]
   lvlTwo = [backgroundTwo, playerTwo, trackTwo, enemiesTwo, playerBulletsTwo, 
             enemyBulletsTwo, powerUpsTwo, miniExplosionsTwo]
   lvlThree = [backgroundThree, playerThree, trackThree, enemiesThree, playerBulletsThree, 
             enemyBulletsThree, powerUpsThree, miniExplosionsThree]
   
   #set current level to be the first level
   currLvl = lvlOne
  #run the main loops
   RUNNING = True
   while RUNNING:
      #loop music
      if musicTime == 210:
          SoundManager.getInstance().playMusic("POL-its-a-blast-short.wav")
          musicTime = 0
      musicTime+=1
      
      #draw background
      currLvl[0].draw(screen)
      
      #draw player
      currLvl[1].draw(screen)
      
      #draw tracking
      currLvl[2].draw(screen)
      
      #draw enemies
      for i in currLvl[3]:
          i.draw(screen)
          
      #draw playerBullets
      for i in currLvl[4]:
          i.draw(screen)
          
      #draw enemyBullets
      for i in currLvl[5]:
          i.draw(screen)
          
      #draw powerups
      for i in currLvl[6]:
          i.draw(screen)
          
      #draw mini Explosions
      for i in currLvl[7]:
          i.draw(screen)
          
      #draw ending line
      endLine.draw(screen)
      
      #draw final end line
      if currLvl == lvlThree:
          finalEnd.draw(screen)
          

      #draw score
      screen.blit(scoreText,(10, 0))
      #draw level
      screen.blit(levelText, (400, 0))
      
      #title screen display
      if start == False:
          titleScreen.draw(screen)
      # Flip the display to the monitor
      pygame.display.flip()
      
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
            break;
            
            
            #read title screen player selection
         result = titleScreen.handleEvent(event)
         
         if result == "exit":
            RUNNING = False
            break
         if result == "start":
             start = True;
             
        #read player input for character
         currLvl[1].handleEvent(event)
            
         #if player hit start, start updating everything
      if start == True:
          gameClock.tick()
          ticks = gameClock.get_time() / 1000  
          if ticks > 0.1:
              ticks = 0.07
        
            
      #update tracking object
          currLvl[2].update(WORLD_SIZE, ticks)
          
      #update player (add to bullet aray and based off tracking pos)
          currLvl[1].update(WORLD_SIZE, SCREEN_SIZE,currLvl[2].getPosition(), 
                            ticks, currLvl[4])
          
      #update powerups  
          for i in currLvl[6]:
              #if player collides with powerup
              if currLvl[1].getCollisionRect().colliderect(i.getCollisionRect()):
                  #pick powerup at random for player
                  currLvl[1].setPowerUp(int(random.randint(1,2)))
                  #remove powerup
                  currLvl[6].remove(i)
      
        
        #update enemy bullets
          for i in currLvl[5]:
              i.update(ticks)
              #if hits players
              if currLvl[1].getCollisionRect().colliderect(i.getCollisionRect()):
                  #update score
                  currLvl[1].setScore(currLvl[1].getScore()-500)
                  #play sound
                  SoundManager.getInstance().playSound("Explosion.wav")
                  #explosion SFX
                  currLvl[7].append(playerExplosion(i.getPosition()))
                  #remove bullet
                  currLvl[5].remove(i)
              
              
              ##update enemies (add to bullet array and based off player pos)
          for i in currLvl[3]:
              i.update(ticks, currLvl[5], currLvl[1].getPosition())
          
          ##update player bullets
          for i in currLvl[4]:
              i.update(ticks)
         
              for j in currLvl[5]:
                  #if it hits enemy bullets
                if i.getCollisionRect().colliderect(j.getCollisionRect()):
                    i.hit()
                    #play sound
                    SoundManager.getInstance().playSound("Explosion.wav")
                    #explosion SFX
                    currLvl[7].append(playerExplosion(i.getPosition()))
                    currLvl[5].remove(j)
                    
              for j in currLvl[3]:
                  #if it hits enemies
                  if i.getCollisionRect().colliderect(j.getCollisionRect()):
                      if j.isDead() != True:
                          #update score
                          currLvl[1].setScore(currLvl[1].getScore()+j.getScoreVal())
                          #play sound
                          SoundManager.getInstance().playSound("Explosion.wav")
                          i.hit()
                          #enemy explodes
                          j.explode()
                      
              if i.isDead():
                  currLvl[4].remove(i)
             #mini explosion updates     
          for i in currLvl[7]:
              i.update()
              if i.isDead():
                  currLvl[7].remove(i)
                  
          #update the offset for the tracking
          Drawable.updateOffset(currLvl[2], SCREEN_SIZE, WORLD_SIZE)
          
          #update ScreenManager
          titleScreen.update(min(ticks, 0.1))
          
          #update the score
          scoreString = "Score: " + str(player.getScore() + playerTwo.getScore() +
                                        playerThree.getScore())
          scoreText = arial.render(scoreString, True, (255,255,255))
          
          #switch level if end is reached
          if (currLvl[1].getPosition()[1] >= 4200 and currLvl == lvlOne):
            currLvl = lvlTwo
            levelString = "Level: 2"
            levelText = arial.render(levelString, True, (255,255,255))
            
            
          #switch level if end is reached
          elif (currLvl[1].getPosition()[1] >= 4200 and currLvl == lvlTwo):
            currLvl = lvlThree
            levelString = "Level: 3"
            levelText = arial.render(levelString, True, (255,255,255))
            
            
          #switch to end screen if end of level 3 is reached
          elif (currLvl[1].getPosition()[1] >= 1600 and currLvl == lvlThree):
              
              notExited = True
              endScreen = endScreenManager(UPSCALED, 
                                           str(player.getScore() + 
                                               playerTwo.getScore()+
                                               playerThree.getScore()))
              while notExited:
                  endScreen.draw(screen)
                  pygame.display.flip()
                  for event in pygame.event.get():
                      result = endScreen.handleEvent(event)
         
                      if result == "exit":
                          notExited = False
                          break
              break
          
   

   pygame.quit()
   
   
if __name__ == "__main__":
   main()