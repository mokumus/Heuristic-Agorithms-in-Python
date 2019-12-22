import utilities
import math
import random


def reduceToRadius(p):
	radiuses = []
	for pair in p:
		radiuses.append(pair[1])
	return radiuses


def greedy(p):
	greedyList = []
	radiuses = reduceToRadius(p)

	size = len(radiuses)

	while len(radiuses) > 0:
		if len(radiuses) > 0:
			greedyList.append([0, (max(radiuses))])
			radiuses.remove(max(radiuses))
		if len(radiuses) > 0:
			greedyList.append([0, (min(radiuses))])
			radiuses.remove(min(radiuses))
		if len(radiuses) > 0:
			greedyList.append([0, (min(radiuses))])
			radiuses.remove(min(radiuses))
	return greedyList


def constructInitialSolution(p):
	return greedy(p)


def localSearch(bestSolution, maxIterations=50):
	i = 0
	while i <= maxIterations:
		candidate = perturbation(bestSolution)
		candidateCost = utilities.calculateOffsets(candidate)
		bestSolutionCost = utilities.calculateOffsets(bestSolution)
		if candidateCost < bestSolutionCost:
			bestSolution = candidate
		i += 1

	return bestSolution


def perturbation(bestSolution):
	# swap 2 random neighbours
	candidate = list(bestSolution)
	ri1 = random.randint(0, len(bestSolution) - 1)
	ri2 = random.randint(0, len(bestSolution) - 1)
	candidate[ri1], candidate[ri2] = candidate[ri2], candidate[ri1]
	return candidate


def iteratedLocalSearch(solutionSpace, maxIterations=100):
	bestSolution = constructInitialSolution(solutionSpace)
	globalMinimum = list(bestSolution)
	bestSolution = localSearch(bestSolution)

	print("Initial score: {}".format(utilities.calculateOffsets(solutionSpace)))
	print("#Iterations: {}".format(maxIterations * 50))

	i = 0
	while i <= maxIterations:
		candidate = localSearch(bestSolution)
		myUtils.clearOffsets(candidate)
		candidateCost = myUtils.calculateOffsets(candidate)
		bestSolutionCost = myUtils.calculateOffsets(bestSolution)
		if candidateCost < bestSolutionCost:
			bestSolution = candidate
			myUtils.clearOffsets(globalMinimum)
			myUtils.clearOffsets(bestSolution)
			if myUtils.calculateOffsets(bestSolution) < myUtils.calculateOffsets(globalMinimum):
				globalMinimum = list(bestSolution)
				myUtils.clearOffsets(globalMinimum)
				myUtils.clearOffsets(bestSolution)
		i += 1
	myUtils.clearOffsets(globalMinimum)
	myUtils.calculateOffsets(globalMinimum)
	print("Final score: {}".format(globalMinimum[-1][0]))
	myUtils.calculateOffsets(greedy(solutionSpace))
	if globalMinimum[-1][0] < solutionSpace[-1][0]:
		return globalMinimum
	else:
		return solutionSpace


if __name__ == "__main__":
	myUtils.start = myUtils.time()
	myUtils.atexit.register(myUtils.endlog)
	myUtils.log("Start Program")

	# test1 = [[0,90],[0,16],[0,30]]
	# test1 = [[0,50],[0,2],[0,30],[0,5],[0,5],[0,120],[0,5]]
	# test1 = [[0,16],[0,128],[0,16],[0,4],[0,2],[0,2],[0,2],[0,128]]
	# test1 = [[0,90],[0,16],[0,30],[0,20],[0,44],[0,4],[0,4],[0,16],[0,30],[0,30]]
	test1 = [[0, 90], [0, 90], [0, 16], [0, 30], [0, 20], [0, 44], [0, 4], [0, 4], [0, 16], [0, 30]]

	# print("input: ", end= "")
	# print(test1)

	result = iteratedLocalSearch(test1)

	# print("output: ", end= "")
	# myUtils.printPairedList(result)

	for pair in result:
		print("offset: {:>7.2f}, radius: {:>7.2f}".format(pair[0], pair[1]))




