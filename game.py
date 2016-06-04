import os, sys, pygame
sys.path.append(os.getcwd())
from pygame.locals import KEYDOWN
import Laser as myLaser
import Enemy as myEnemy
import Battlecruiser as myBattlecruiser
from random import randrange, uniform
def removeEnemies(ens):
	for en in ens :
		if en.y>600:
			ens.remove(en)
			del en
	pass
if __name__ == '__main__':
	score=0
	pygame.init()
	enemies=[]
	screen_size = (800, 600)
	screen = pygame.display.set_mode(screen_size)
	black=(0,0,0)
	fpsClock = pygame.time.Clock()
	battlecruiser = myBattlecruiser.Battlecruiser(350,450,screen)
	gaming=True
	while True:
		removeEnemies(enemies)
		fpsClock.tick(50)
		screen.fill(black)
		i=randrange(1,100)
		if gaming:
			if i>95:
				enemy=myEnemy.Enemy(randrange(100,500),20,screen)
				enemies.append(enemy)

		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			battlecruiser.pressKeyOnce(event)
		battlecruiser.holdingOnKeys()
		for e in enemies:
			e.draw()
			e.topToDown()
			e.outOfWall()
			if e.hitTest(battlecruiser.lasers):
				if e.active==True:
					score+=100 
				e.explosion()
				e.update()
				e.active=False
			e.update()
		if battlecruiser.crash(enemies):
			gaming=False
			battlecruiser.active=False
		if not(gaming):
			myfont = pygame.font.SysFont("monospace", 40)
			myfont.set_bold(True)
			gameoverdisplay = myfont.render("Gome Over", 10, (255, 0, 0))
			screen.blit(gameoverdisplay, (300, 200))
		myfont = pygame.font.SysFont("monospace", 40)
		scoredisplay = myfont.render("score: "+str(score), 10, (255, 255, 0))
		screen.blit(scoredisplay, (20, 20))
		battlecruiser.draw()
		battlecruiser.update()
		pygame.display.flip() 