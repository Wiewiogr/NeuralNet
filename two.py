import pygame
import math
from controller import *


def Collision():
	for x in carni.draw:
		for e in evo.draw:
			if math.sqrt((x.x - e.x)**2 + (x.y- e.y)**2) <= x.r+e.r:
				e.x = randint(0,size_x)
				e.y = randint(0,size_y)
				e.fit /= 2
				x.fit += 1

def get_input(t):
	best = carni.draw[0]
	for x in carni.draw:
		if math.sqrt((x.x - t.x)**2 + (x.y- t.y)**2) < math.sqrt((best.x - t.x)**2 + (best.y- t.y)**2):
			best = x
	#best.color =(100,100,100)
	tmp = [t.tx,t.ty,t.x-best.x,t.y-best.y]
	return tmp

def carni_get_input(t):
	best = evo.draw[0]
	for x in evo.draw:
		if math.sqrt((x.x - t.x)**2 + (x.y- t.y)**2) < math.sqrt((best.x - t.x)**2 + (best.y- t.y)**2):
			best = x
	#best.color =(100,100,100)
	tmp = [t.tx,t.ty,t.x-best.x,t.y-best.y]
	return tmp
			
def update(t,out):
	t.tx = (out[0]*2)-1
	t.ty = (out[1]*2)-1

evo = Controller(30,4,2,1,6)
carni = Controller(30,4,2,1,6)
pygame.init()
screen = pygame.display.set_mode((size_x,size_y))
done = False
fast = True
font = pygame.font.Font(None,30)
generation = font.render("Generation : "+str(evo.generation), 1,(255,255,255))

clock = pygame.time.Clock()


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
	Collision()
	for x in range(len(evo.draw)):
		tmp = get_input(evo.draw[x])
		update(evo.draw[x],evo.objects[x].get_output(tmp))
		#print(t.objects[x].get_output(tmp))

	for x in range(len(carni.draw)):
		tmp = carni_get_input(carni.draw[x])
		update(carni.draw[x],carni.objects[x].get_output(tmp))
	


	evo.tick()
	carni.tick()
	for x in evo.draw:
		pygame.draw.circle(screen,(255,100,5),(x.x,x.y),x.r)
		#pygame.draw.line(screen,(150,150,10),(x.x,x.y),(int(x.x+x.tx*100),int(x.y+x.ty*100)))

	for x in carni.draw:
		pygame.draw.circle(screen,(5,100,255),(x.x,x.y),x.r)
		#pygame.draw.line(screen,(150,150,10),(x.x,x.y),(int(x.x+x.tx*100),int(x.y+x.ty*100)))
		

	pygame.display.flip()
	if fast :
		clock.tick(60)
	else : 
		clock.tick(20)