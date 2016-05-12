from random import randint, random

class chromosome:
	def __init__(self,length, ran,fit_fun):
		self.fit = 0
		self.len = length
		self.fit_fun = fit_fun
		self.genes = []
		for x in range(length):
			self.genes.append(ran())

	def fitness(self):
		self.fit = self.fit_fun(self)
		return self.fit

	def show(self):
		for x in self.genes:
			print(x, end=" ")
		print("fit : ", self.fit)


