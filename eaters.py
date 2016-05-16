import pygame
import math
from controller import *


def Collision(tmp):
	for i in tmp.draw:
		for j in tmp.draw:
			if i != j:
				if math.sqrt((i.x - j.x)**2 + (i.y- j.y)**2) <= i.r+j.r:
					j.x = randint(0,800)
					j.y = randint(0,600)
					i.fit += 1
					if j.fit > 1:
						j.fit -= 1

class Food:
	def __init__(self):
		self.x = randint(0,800)
		self.y = randint(0,600)
		self.color = (0,100,255)
		self.r = 5
		

food = []

def addFood():
	for x in range(100):
		food.append(Food())


def get_input(t):
	if evo.draw[0] != t:	
		best = evo.draw[0]
	else:
		best = evo.draw[1]
	for x in evo.draw:
		if t != x:
			if math.sqrt((x.x - t.x)**2 + (x.y- t.y)**2) < math.sqrt((best.x - t.x)**2 + (best.y- t.y)**2):
				best = x
	#best.color =(100,100,100)
	tmp = [t.tx,t.ty,t.x-best.x,t.y-best.y]
	return tmp
			
def update(t,out):
	t.tx = (out[0]*2)-1
	t.ty = (out[1]*2)-1
	#print(out[0],out[1])
	#print(int(t.tx*speed),t.tx*speed,int(t.ty*speed),t.ty*speed)
	

evo = Controller(30,4,2,1,6)
pygame.init()
screen = pygame.display.set_mode((size_x,size_y))
done = False
fast = True
font = pygame.font.Font(None,30)
generation = font.render("Generation : "+str(evo.generation), 1,(255,255,255))

clock = pygame.time.Clock()
addFood()

num = 0


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			fast = not fast
	num += 1
	if num >= 360:
		num = 0
		evo.next()
		generation = font.render("Generation : "+str(evo.generation), 1,(255,255,255))		
	screen.fill((0, 0, 0))
	screen.blit(generation, (10, 10))      
	Collision(evo)
	for x in range(len(evo.draw)):
		tmp = get_input(evo.draw[x])
		update(evo.draw[x],evo.objects[x].get_output(tmp))
		#print(t.objects[x].get_output(tmp))


	evo.tick()
	for x in evo.draw:
		pygame.draw.circle(screen,(255,100,5),(x.x,x.y),x.r)
		pygame.draw.line(screen,(150,150,10),(x.x,x.y),(int(x.x+x.tx*100),int(x.y+x.ty*100)))
	#for x in food:
	#		pygame.draw.circle(screen,x.color,(x.x,x.y),x.r)
	

	pygame.display.flip()
	if fast :
		clock.tick(60)
	else : 
		clock.tick(20)