import utilities, random
from copy import deepcopy

class Individual:
	gene = list()
	fitness = float()

	def __init__(self, genePool):
		self.gene = utilities.randomPermutaion(genePool)
		self.calculateFitness()

	def __str__(self):
		str = "gene: ["
		for g in self.gene:
			str += "{}, ".format(g)
		str = str[:-2]
		str += "] fitness: {:.1f}".format(self.fitness)
		return str

	def calculateFitness(self):
		tmpGene = []
		for g in self.gene:
			tmpGene.append([0, g])
		tmpGene = utilities.writeOffsets(tmpGene)
		self.fitness = utilities.cost(tmpGene)


class Population:
	individuals = list()
	size = int()

	def __init__(self, genePool, size):
		self.individuals = [None] * size
		#
		# Important to assign this way, other methods of list assignments cause
		# problems with consecutive testing
		#
		for i in range(0,size):
			self.individuals[i] = Individual(genePool)

		self.size = size

	def __str__(self):
		str = ""
		for i in self.individuals:
			str += Individual.__str__(i)
			str += "\n"
		return str

	def sortPopulation(self):
		self.individuals.sort(key=lambda x: x.fitness, reverse=False)

	def getFittestMember(self) -> Individual:
		self.sortPopulation()
		return self.individuals[0]

	def getWeakestMember(self) -> Individual:
		self.sortPopulation()

		return self.individuals[-1]

	def getRandomMember(self):
		return self.individuals[random.randint(0,self.size-1)]

class GeneticFramework:
	population = None
	populationSize = None
	geneSize = None
	fittestIndividualLived = None

	def __init__(self, genePool, popSize):
		self.population = Population(genePool, popSize)
		self.populationSize = popSize
		self.geneSize = len(genePool)
		self.fittestIndividualLived = self.population.getFittestMember()


	#Tournament Selection
	def selection(self):
		tournamentWinners = []
		tournamentWinners.append(self.fittestIndividualLived)

		while len(tournamentWinners) <= self.populationSize:
			#4 way tournament group
			constestants = []
			for i in range (4):
				r = random.randint(0, self.population.size - 1)
				constestants.append(self.population.individuals[r])

			winner = min(constestants, key=lambda x: x.fitness)
			tournamentWinners.append(winner)

		#Update population with winners
		self.population.individuals = tournamentWinners

		#Update fittest individual lived if necessary
		if self.fittestIndividualLived.fitness > self.population.getFittestMember().fitness:
			self.fittestIndividualLived = self.population.getFittestMember()


	#One point crossover modified for permutations with non-unique values
	def crossover(self, i1 , i2):
		offspring = [-1] * len(i1.gene)
		c = random.randint(1, self.geneSize - 1)
		offspring[0:c] = reversed(i1.gene[0:c])

		j = 0
		for g in i2.gene:
			for i in range(0, c):
				if g not in offspring or offspring.count(g) < i2.gene.count(g) and j <= self.geneSize-c:
					offspring[c+j] = g
					j += 1


		newIndividiual = Individual(offspring)
		self.population.sortPopulation()
		self.population.individuals[-1] = newIndividiual
		return newIndividiual

	#Mutation on targeted individual
	def mutation(self, i):

		c = random.randint(1, self.geneSize - 1)
		i.gene[0], i.gene[c] = i.gene[c], i.gene[0]

	def generationRecipe(self):
		self.selection()
		self.crossover(self.population.getRandomMember(), self.population.getRandomMember())
		self.mutation(self.population.getWeakestMember())
		self.crossover(self.population.getRandomMember(), self.population.getRandomMember())
		self.mutation(self.population.getWeakestMember())
		self.crossover(self.population.getRandomMember(), self.population.getRandomMember())


def geneticAlgorithm(circles, populationSize = 10, generations = 50):
	formatedInput = utilities.reduceToRadius(circles)
	ga = GeneticFramework(formatedInput, populationSize)

	for i in range(0,generations):
		ga.generationRecipe()

	output = []

	for r in ga.fittestIndividualLived.gene:
		output.append([0,r])


	return output

if __name__ == "__main__":
	for i, test in enumerate(utilities.tests):
		print("#Test{}".format(i+1))
		time = utilities.chronometer(geneticAlgorithm, test)




