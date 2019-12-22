import math, random, utilities, greedy

class Particle:
	position = list()		# particle position
	cost = float()			# particle cost
	bestPosition = list()	# best particles position
	bestCost = float()		# best particles cost

	def __init__(self, solutionSpace):
		self.position = utilities.randomPermutaion(solutionSpace)
		self.cost = self.evaluate()
		self.bestPosition = self.position
		self.bestCost = self.cost

	def __str__(self):
		str = "position: ["
		for g in self.position:
			str += "{}, ".format(g)
		str = str[:-2]
		str += "] cost: {:.1f} ".format(self.cost)
		return str

	def evaluate(self):
		tmpPosition = []
		for p in self.position:
			tmpPosition.append(p)
		tmpPosition = utilities.writeOffsets(tmpPosition)
		self.cost = utilities.cost(tmpPosition)
		return self.cost

	def update(self, globalBest, globalBestCost, w= 0.5, c1 = 1.5, c2 = 1.5):
		r1 = random.random()
		r2 = random.random()

		diversify = math.fabs(w * self.cost)
		cognitive = math.fabs(c1 * r1 * (self.bestCost - self.cost))
		social = math.fabs(c2 * r2 * (globalBestCost - self.cost))

		countDiverse = 0
		countCognitive = 0
		countSocial = 0

		if diversify > social and diversify > cognitive:
			self.position = utilities.randomPermutaion(self.position)
			self.cost = self.evaluate()
			countDiverse += 1
			#print("diversify")
		elif cognitive > social:
			self.position = self.bestPosition
			self.cost = self.bestCost
			countCognitive +=1
			#print("cognitive")
		else:
			self.position = globalBest
			self.cost = globalBestCost
			countSocial += 1
			#print("social")

		return countDiverse,countCognitive,countSocial

def cost(positions):
	tmpPosition = []
	for p in positions:
		tmpPosition.append(p)
	tmpPosition = utilities.writeOffsets(tmpPosition)
	return utilities.cost(tmpPosition)


def pso(solutionSpace, swarmSize = 10, w = 0.1, c1 = 1.9, c2 = 1.1, maxIters = 100, stopAfterNoImprovement = 75):
	swarm = [None] * swarmSize
	globalBest = greedy.greedy(solutionSpace)	# Construct initial greedy solution
	globalBestCost = cost(globalBest) # Calculate cost of the initial solution

	iterNoImprovement = 0

	countDiverse = 0
	countCognitive = 0
	countSocial = 0

	# Populate the swarm
	for i in range(0,swarmSize):
		swarm[i] = Particle(solutionSpace)
		#print(swarm[i])

	for i in range(0, maxIters):

		for particle in swarm:
			particle.evaluate()
			# Check if current particle is global best, if so, update global best
			if particle.cost < globalBestCost:
				globalBest = particle.position
				globalBestCost = particle.cost
				iterNoImprovement = 0

		iterNoImprovement += 1

		for particle in swarm:
			tmpDiverse, tmpCognitive, tmpSocial = particle.update(globalBest, globalBestCost, w, c1, c2)
			countDiverse += tmpDiverse
			countCognitive += tmpCognitive
			countSocial += tmpSocial

		if iterNoImprovement >= stopAfterNoImprovement:
			break
	#print("#diversification: {}\n#cognition: {}\n#socialization: {}".format(countDiverse,countCognitive,countSocial))


	return globalBest


if __name__ == "__main__":
	#result = pso(test3, swarmSize = 10, w = 0.1, c1 = 1.9, c2 = 1.1, maxIters = 100, stopAfterNoImprovement = 50)

	for i, test in enumerate(utilities.tests):
		print("#Test{}".format(i+1))
		time = utilities.chronometer(pso, test)










