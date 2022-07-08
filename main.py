import pygame
from sys import exit

white = [255, 255, 255]
digits = 3
fps = 10000**digits * 2

class Square( object ):
	def __init__(self, screen: any, x: int, v: int, width: int, mass: int):
		self.width = width
		self.screen = screen
		self.x = x
		self.mass = mass
		self.v = v
		self.rebounds = 0
	
	def draw(self):
		pygame.draw.rect(self.screen, (255,0,0), (self.x, 420-self.width ,self.width,self.width))

	def next_position(self):
		if self.x - self.v < 0: 
			self.v *= -1
			self.rebounds += 1
		else:
			self.x -= self.v
	
	def collide(other, self):
		if other.x + other.width >= self.x:
			self.v = (self.mass - other.mass)/(self.mass + other.mass) * self.v + (2*other.mass)/(self.mass + other.mass) * other.v
			other.v = (2*self.mass)/(self.mass + other.mass) * self.v + (other.mass - self.mass)/(self.mass + other.mass) * other.v
			self.rebounds += 1
			other.rebounds += 1


pygame.font.init()
pygame.init()


screen = pygame.display.set_mode((1280,720))
screen.fill([255,255,255])
pygame.display.set_caption('Pi-Collide')

square1 = Square(screen, 300, 0, 30, 1)
square2 = Square(screen, 600, 0.07, 100, 100**digits)

myfont = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()

def redraw():
	screen.fill(white)
	text = myfont.render(str(square1.rebounds),False,(0,0,0))
	screen.blit(text,(900,50))
	square1.collide(square2)
	square1.next_position()
	square2.next_position()
	square2.draw()
	square1.draw()
	pygame.display.update()

while True:
	clock.tick(fps)
	redraw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()