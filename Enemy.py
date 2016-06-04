import os, sys, pygame
sys.path.append(os.getcwd())
from pygame.locals import KEYDOWN
from random import randrange, uniform
class Enemy(pygame.sprite.Sprite):
	x = 0
	y=0
	dx = 0
	dy=0
	screen=None
	image=None
	image_w=0
	image_h=0
	rect=None
	active=True
	
	def __init__(self,x,y,screenArg):
		super(Enemy, self).__init__()
		self.x=x
		self.y=y
		self.screen=screenArg
		try:
			self.image = pygame.image.load("mutalisk.gif").convert()
			self.rect  = self.image.get_rect()
		except IOError:
			print "error: can not open mutalisk.gif"
		self.image_h=self.rect.height
		self.image_w=self.rect.width
		self.rect.topleft = (self.x, self.y)

	def draw(self):
		self.screen.blit(self.image, self.rect)
	def bouncing(self):
		if self.x<0 or self.x>730:
			self.dx=-self.dx
		if self.y>560 or self.y<0:
			self.dy=-self.dy
	def outOfWall(self):
		if self.y>580:
			self.active=False
	def randomBouncing(self):
		self.x=self.x+self.dx
		self.y=self.y+self.dy
	def explosion(self):
		try:
			self.image = pygame.image.load("laser_explosion.gif").convert()
			self.rect    = self.image.get_rect()
		except IOError:
			print "An error occured trying to read the file."
		self.image_w   = self.rect.width
		self.image_h   = self.rect.height
		self.active=False

	def update(self):
		self.rect.topleft = (self.x, self.y)
		if self.active==False:
			self.delete()
	def topToDown(self):
		self.y=self.y+10
	def hitTest(self,Lasers):
		for laser in Lasers:
			if laser.x>self.rect.left and laser.x<self.rect.right and laser.y>self.rect.top and laser.y<self.rect.bottom:
				#self.active=False
				return True 
				break
		return False

	def  delete(self):
		del self
if __name__ == "__main__":

	pygame.init()
	screen_size = (800, 600)
	screen = pygame.display.set_mode(screen_size)
	enemies=[]

	for i in range(0,5) :
		enemy=Enemy(randrange(100,600),randrange(200,500),screen)
		enemy.dx=randrange(1,6)
		enemy.dy=randrange(1,5)
		enemies.append(enemy)
	for i in range(0,5) :
		enemy=Enemy(randrange(100,600),randrange(200,500),screen)
		enemy.dx=randrange(-6,-1)
		enemy.dy=randrange(-5,-1)
		enemies.append(enemy)
	black=(0,0,0)
	fpsClock = pygame.time.Clock()
	while True:
		fpsClock.tick(50)
		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				pygame.quit()
				sys.exit()
		for e in enemies:   
			e.draw()
			e.randomBouncing()
			e.bouncing()
			e.update()
		pygame.display.flip() 