import utilities
from tabuSearch import tabuSearch
from greedy import greedy
from geneticAlgorithm import geneticAlgorithm
from pso import pso

if __name__ == "__main__":
	algorithms = [greedy, tabuSearch, geneticAlgorithm, pso]

	for i, test in enumerate(utilities.tests):
		print("#Test{}".format(i+1))
		for algorithm in algorithms:
			utilities.chronometer(algorithm, test)


