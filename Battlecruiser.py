import os, sys, pygame
sys.path.append(os.getcwd())
from pygame.locals import KEYDOWN
import Laser as myLaser
class Battlecruiser(pygame.sprite.Sprite):
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
	lasers=[]
	def __init__(self,x,y,screenArg):
		super(Battlecruiser, self).__init__()
		self.x=x
		self.y=y
		self.screen=screenArg
		try:
			self.image = pygame.image.load("battlecruiser.gif").convert()
			self.rect           = self.image.get_rect()
		except IOError:
			print "error: can not open battlecruiser.gif"
		self.image_h=self.rect.height
		self.image_w=self.rect.width
		self.rect.topleft = (self.x, self.y)

	def draw(self):
		if self.active:
			self.screen.blit(self.image, self.rect)
			for laser in self.lasers:
				laser.draw()

	def  pressKeyOnce(self,event):
		if event.type == pygame.KEYDOWN :
			if event.key==pygame.K_SPACE:
				laser=myLaser.Laser(self.x+self.image_w/2,self.y,self.screen)
				self.lasers.append(laser)
				laser.laserSound()
	def gameover(self):
		myfont = pygame.font.SysFont("monospace", 40)
		myfont.set_bold(True)
		label = myfont.render("Gome Over", 10, (255, 0, 0))
		self.screen.blit(label, (250, 300))

		
	def crash(self,enemies):
		for e in enemies:
			if e.x>self.rect.left and e.x<self.rect.right and e.y<self.rect.bottom and e.y>self.rect.top and e.active==True:
				pygame.mixer.music.load('death_explode.wav')
				pygame.mixer.music.play()
				return True;break
		return False
	def holdingOnKeys(self):
		keys_pressed = pygame.key.get_pressed()

		if self.x in range(0 , 800 - self.image_w / 2) :
			if keys_pressed[pygame.K_LEFT]:
				self.x -= 5

		if self.x in range(0 - self.image_w / 2, 800 - self.image_w ) :
			if keys_pressed[pygame.K_RIGHT]:
				self.x += 5
		if self.y in range(0 , 600 - self.image_h / 2) :
			if keys_pressed[pygame.K_UP]:
				self.y -= 5
		if self.y in range(0 - self.image_h / 2, 600 - self.image_h ) :
			if keys_pressed[pygame.K_DOWN]:
				self.y += 5

			

			
	def update(self):
		self.rect.topleft = (self.x, self.y)
		for laser in self.lasers:
			laser.downtotop()
			laser.update()
	def  delete(self):
		del self
if __name__ == "__main__":
	pygame.init()
	screen_size = (800, 600)
	screen = pygame.display.set_mode(screen_size)
	black=(0,0,0)
	fpsClock = pygame.time.Clock()
	battlecruiser = Battlecruiser(350,450,screen)
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
			battlecruiser.pressKeyOnce(event)
		battlecruiser.holdingOnKeys()
		battlecruiser.draw()
		battlecruiser.update()
		pygame.display.flip() 
	