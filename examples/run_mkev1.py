# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
import logging
from NiaPy.algorithms.basic import MonkeyKingEvolutionV1
from NiaPy.benchmarks.utility import TaskConvPrint, TaskConvPlot, OptimizationType
from margparser import getDictArgs

logging.basicConfig()
logger = logging.getLogger('examples')
logger.setLevel('INFO')

# For reproducive results
random.seed(1234)

class MinMB(object):
	def __init__(self):
		self.Lower = -11
		self.Upper = 11

	def function(self):
		def evaluate(D, sol):
			val = 0.0
			for i in range(D): val = val + sol[i] * sol[i]
			return val
		return evaluate

class MaxMB(MinMB):
	def function(self):
		f = MinMB.function(self)
		def e(D, sol): return -f(D, sol)
		return e

def simple_example(runs=10, D=10, nFES=50000, nGEN=100000, seed=None, optType=OptimizationType.MINIMIZATION, optFunc=MinMB, **kn):
	for i in range(10):
		Algorithm = MonkeyKingEvolutionV1(D=D, nFES=nFES, NP=25, C=3, F=0.5, FC=0.5, R=0.4, optType=optType, benchmark=optFunc())
		Best = Algorithm.run()
		logger.info('%s %s' % (Best[0], Best[1]))

def logging_example(D=10, nFES=50000, nGEN=100000, seed=None, optType=OptimizationType.MINIMIZATION, optFunc=MinMB, **kn):
	task = TaskConvPrint(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc())
	algo = MonkeyKingEvolutionV1(NP=25, C=3, F=0.5, FC=0.5, R=0.4, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))

def plot_example(D=10, nFES=50000, nGEN=100000, seed=None, optType=OptimizationType.MINIMIZATION, optFunc=MinMB, **kn):
	task = TaskConvPlot(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc())
	algo = MonkeyKingEvolutionV1(NP=25, C=3, F=0.5, FC=0.5, R=0.4, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))
	input('Press [enter] to continue')

def getOptType(strtype):
	if strtype == 'min': return OptimizationType.MINIMIZATION, MinMB
	elif strtype == 'max': return OptimizationType.MAXIMIZATION, MaxMB
	else: return None

if __name__ == '__main__':
	pargs = getDictArgs(sys.argv[1:])
	optType, optFunc = getOptType(pargs.pop('optType', 'min'))
	if not pargs['runType']: simple_example(optType=optType, optFunc=optFunc, **pargs)
	elif pargs['runType'] == 'log': logging_example(optType=optType, optFunc=optFunc, **pargs)
	elif pargs['runType'] == 'plot': plot_example(optType=optType, optFunc=optFunc, **pargs)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
