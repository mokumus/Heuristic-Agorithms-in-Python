import utilities, random, greedy
from copy import deepcopy
#import matplotlib.pyplot as plt
#import numpy as np

def cost(positions):
	tmpPosition = []
	for p in positions:
		tmpPosition.append(p)
	tmpPosition = utilities.writeOffsets(tmpPosition)
	return utilities.cost(tmpPosition)

def constructInitialSolution(p):
	return greedy(p)

def twoOpt(circles):
	perm = deepcopy(circles)
	c1 = random.randint(0, len(perm) - 1)
	c2 = random.randint(0, len(perm) - 1)
	if c2 > c1:
		c1, c2 = c2, c1

	perm[c1:], perm[:c2] = perm[:c2], perm[c1:]
	return perm


def is_a_in_x(A, X):
	for i in range(len(X) - len(A) + 1):
		if A == X[i:i+len(A)]: return True
	return False

def isTabu(permutaion, tabuList):
	for i in range(len(permutaion)):
		if is_a_in_x(permutaion[i], tabuList):
			return True
	return False

def generateCandidate(best, tabuList):
	perm = []
	while True: #Until non-tabu candidate is found
		perm = twoOpt(twoOpt(best))
		if not isTabu(perm, tabuList):
			break
	return perm


def tabuSearch(circles, tabuSize = 5, maxIterations=25):

	current = greedy.greedy(circles)
	currentCost = cost(current)
	best = current

	tabuList = [None] * tabuSize
	iters = 0
	while(iters <= maxIterations):
		candidates = []
		for i in range(0,3):
			candidates.append(generateCandidate(best,tabuList))

		#Find lowest cost candidate
		candidates.sort(key=lambda x: cost(x), reverse=False)
		best_candidate = candidates[0]

		if cost(best_candidate) < currentCost:
			current = best_candidate
			if cost(best) > cost(best_candidate):
				best = best_candidate
				tabuList.append(best_candidate)
				if len(tabuList) > tabuSize:
					tabuList.pop(0)
		iters += 1

	return best

if __name__ == "__main__":
	t = []
	s = []
	for i, test in enumerate(utilities.tests):
		print("#Test{}".format(i+1))
		time = utilities.chronometer(tabuSearch, test)
		t.append(time)
		s.append(len(test))

"""
	plt.plot(s, t, label='First Line')
	plt.xlabel('Input Size')
	plt.ylabel('Time(s)')
	plt.title('TabuSize: 5, MaxIters: 100 ')
	plt.show()
"""










