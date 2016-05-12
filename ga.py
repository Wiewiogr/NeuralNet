from chromo import *
import copy
target = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def randfun():
	return randint(0,1)
def fit(chromo):
	score = 0
	for x in range(len(chromo.genes)):
		if chromo.genes[x] == target[x]:
			score += 1
	return score
"""
def nnrand():
	return random()
"""



class Evolution:
	def __init__(self,num,ran,fit,length,cross,mut):
		self.mutation_rate = mut
		self.generation = 0
		self.num = num
		self.chromo = []
		self.cross_rate = cross
		for x in range(num):
			self.chromo.append(chromosome(length,ran,fit))
	
	def roulette(self,total):
		choice = random() * total
		tmp = 0.
		for x in self.chromo:
			tmp += x.fit
			if tmp >= choice:
				return x

	def crossover(self,x1,x2):
		if random() < self.cross_rate:
			
			tmp = randint(1,x1.len-1)
			t = x1.genes[tmp:]
			del x1.genes[tmp:]
			for x in x2.genes[tmp:]:
				x1.genes.append(x)
			del x2.genes[tmp:]
			for x in t:
				x2.genes.append(x)
			
	def mutation(self,x1):
		if random() < self.mutation_rate:
			
			t = randint(0,x1.len-1)
			"""
			x1.genes[t] += 1
			x1.genes[t] %= 2  
			"""
			x1.genes[t] = (random()*2)+1
	def best(self):
		best = self.chromo[0]
		for x in self.chromo:
			if x.fit > best.fit:
				best = x
		return best

	def update(self):
		self.generation += 1
		total = 0
		for x in self.chromo:
			total += x.fitness()

		best = self.best()
		print("Generacja : ",self.generation," - best score : ",best.fit)

		
		for x in self.chromo:
			x.show()


		new_list = []
		for x in range(int(self.num/2)):
			a = copy.deepcopy(self.roulette(total))
			b = copy.deepcopy(self.roulette(total))
			self.crossover(a,b)

			self.mutation(a)
			self.mutation(b)

			new_list.append(a)
			new_list.append(b)

		self.chromo = new_list



"""
t = Evolution(50,randfun,fit,len(target),0.7,0.01)

for x in range(100):
	t.update()
"""