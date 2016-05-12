from ga import *
import math

sigm = lambda x: 1 / (1 + math.exp(-x))
class Neuron():
	def __init__(self, num_inputs):
		self.num_inputs = num_inputs
		self.weights = []

class Neuron_layer():
	def __init__(self,num,num_inputs):
		self.neurons = []
		for x in range(num):
			self.neurons.append(Neuron(num_inputs))


class Neural_net():
	#nhlayers - number of hidden layers nperhlayer - number of neurons per hidden layer
	def __init__(self,nin,nout,nhlayers,nperhlayer):
		self.nin = nin
		self.nout = nout
		self.n_hlayers = nhlayers
		self.n_per_hlayer = nperhlayer
		self.layers = []
		self.layers.append(Neuron_layer(nperhlayer,nin))
		for x in range(1,self.n_hlayers):
			self.layers.append(Neuron_layer(nperhlayer,nperhlayer))
		self.layers.append(Neuron_layer(nout,nperhlayer))
	
	def put_weights(self,genes):
		tmp = 0
		for l in self.layers:
			for n in l.neurons:
				n.weights.clear()
				n.weights += genes[tmp:tmp+n.num_inputs+1]
				tmp += n.num_inputs+1
		#		print(n.weights)
		#print(tmp)

	def get_output(self,_in):
		output = []
		inputs = _in
		for l in self.layers:
			output.clear()
			for n in l.neurons:
				val = 0
				for w in range(len(n.weights)-1):
					val += inputs[w] * n.weights[w]
				val -= n.weights[-1]
				output.append(sigm(val))

			inputs = list(output)

		return output



#t = Neural_net(4,4,1,5)
			







