# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
import logging
from NiaPy.algorithms.basic import SineCosineAlgorithm
from NiaPy.benchmarks.utility import TaskConvPrint, TaskConvPlot

logging.basicConfig()
logger = logging.getLogger('examples')
logger.setLevel('INFO')

# For reproducive results
random.seed(1234)

class MyBenchmark(object):
	def __init__(self):
		self.Lower = -11
		self.Upper = 11

	def function(self):
		def evaluate(D, sol):
			val = 0.0
			for i in range(D): val += sol[i] ** 2
			return val
		return evaluate

def simple_example(runs=10):
	for i in range(runs):
		algo = SineCosineAlgorithm(D=50, nFES=1000, NP=50, a=7, Rmin=0.1, Rmax=3, benchmark=MyBenchmark())
		best = algo.run()
		logger.info('%s %s' % (best[0], best[1]))

def logging_example():
	task = TaskConvPrint(D=50, nFES=50000, nGEN=10000, benchmark=MyBenchmark())
	algo = SineCosineAlgorithm(NP=35, a=3, Rmin=0.1, Rmax=1.1, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))

def plot_example():
	task = TaskConvPlot(D=50, nFES=50000, nGEN=10000, benchmark=MyBenchmark())
	algo = SineCosineAlgorithm(NP=35, a=7, Rmin=0.1, Rmax=3, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))
	input('Press [enter] to continue')

if __name__ == '__main__':
	if len(sys.argv) <= 1: simple_example(1)
	elif sys.argv[1] == 'plot': plot_example()
	elif sys.argv[1] == 'log': logging_example()
	else: simple_example(10)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
