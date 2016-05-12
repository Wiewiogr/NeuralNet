import pygame
import math
from random import randint




class Circle:
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r

def Collision():
	for x in circles:
		if math.sqrt((x.x - me.x)**2 + (x.y- me.y)**2) <= x.r+me.r:
			x.x =randint(0,800)
			x.y = randint(0,600)
r = 10
score = 0
circles = []
me = Circle(0,0,r)

for x in range(10):
	circles.append(Circle(randint(0,800),randint(0,600),r))



pygame.init()
screen = pygame.display.set_mode((800,600))
done = False
x = 0
y = 0
clock = pygame.time.Clock()


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		#if event.type == pygame.KEYDOWN:
			
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: me.y -= 3
	if pressed[pygame.K_DOWN]: me.y += 3
	if pressed[pygame.K_LEFT]: me.x -= 3
	if pressed[pygame.K_RIGHT]: me.x += 3
	
	screen.fill((0, 0, 0))
      
	Collision()
	for x in circles:
		pygame.draw.circle(screen,(255,100,5),(x.x,x.y),x.r)
	pygame.draw.circle(screen,(0,100,255),(me.x,me.y),x.r)
	
	pygame.display.flip()
	clock.tick(60)