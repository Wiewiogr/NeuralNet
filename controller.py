from neural_net import *
from ga import *
from random import randint


size_x = 1280
size_y = 800
speed = 3
def nnrand():
	return (random()*2)-1

def nnfit(chromo):
	return chromo.fit
r = 6
class Eater:
	def __init__(self):
		self.x = randint(0,size_x)
		self.y = randint(0,size_y)
		self.r = r
		self.tx = (random()*2)-1
		self.ty = (random()*2)-1
		self.fit = 1


class Controller():
	def __init__(self,num,nin,nout,nhlayers,nperhlayer):
		self.num = num
		self.generation = 1
		self.chromo_len = nperhlayer*(nin+1)
		for x in range(1,nhlayers):
			self.chromo_len += nperhlayer**2 + nperhlayer
		self.chromo_len += nperhlayer*nout + nout
		self.ga = Evolution(num,nnrand,nnfit,self.chromo_len,0.7,0.1)
		#print(len(self.ga.chromo[0].genes))
		self.objects = [] ##neural net
		self.draw = [] ##draw
		for x in range(num):
			self.objects.append(Neural_net(nin,nout,nhlayers,nperhlayer))	
			self.objects[x].put_weights(self.ga.chromo[x].genes)
			self.draw.append(Eater())

	def tick(self):
		for x in self.draw:
			x.x += int(x.tx*speed)
			x.y += int(x.ty*speed)
			#print(int(x.tx*speed),x.tx*speed,int(x.ty*speed),x.ty*speed)
			x.x %= size_x
			x.y %= size_y

	def next(self):
		self.generation += 1
		for x in range(self.num):
			self.ga.chromo[x].fit = self.draw[x].fit
		self.ga.update()
		self.draw.clear()
		for x in range(self.num):
			self.objects[x].put_weights(self.ga.chromo[x].genes)
			self.draw.append(Eater())
		




