import os, sys, pygame
sys.path.append(os.getcwd())
from pygame.locals import KEYDOWN
from random import randrange, uniform
class Laser(pygame.sprite.Sprite):
	x = 0
	y=0
	dx = None
	dy=None
	screen=None
	image=None
	image_w=0
	image_h=0
	rect=None
	active=True
	def __init__(self,x,y,screenArg):
			super(Laser, self).__init__()
			self.x=x
			self.y=y
			self.screen=screenArg
			try:
				self.image = pygame.image.load("laser.gif").convert()
				self.rect  = self.image.get_rect()
			except IOError:
				print "error: can not open laser.gif"
			self.image_h=self.rect.height
			self.image_w=self.rect.width
			self.rect.topleft = (self.x, self.y)
	def draw(self):
			self.screen.blit(self.image, self.rect)
	def downtotop(self):
			self.y-=10
	def update(self):
			self.rect.topleft = (self.x, self.y)
			if(self.y<-10):
				self.active=False
				del self
	def laserSound(self):
			pygame.mixer.music.load('laser.wav')
			pygame.mixer.music.play()
if __name__ == "__main__":
	pygame.init()
	screen_size = (800, 600)
	screen = pygame.display.set_mode(screen_size)
	black=(0,0,0)
	lasers=[]
	fpsClock = pygame.time.Clock()
	while True:
		fpsClock.tick(50)
		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
		laser=Laser(randrange(0, 800),550,screen)
		laser.laserSound()
		lasers.append(laser)
		for  laser in lasers:
			laser.downtotop()
			laser.draw()
			laser.update()
		pygame.display.flip() 