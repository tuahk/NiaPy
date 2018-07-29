# encoding=utf8
# pylint: disable=mixed-indentation, line-too-long, multiple-statements
from unittest import TestCase
import NiaPy

class MyBenchmark:
	def __init__(self):
		self.Lower = -11
		self.Upper = 11

	@classmethod
	def function(cls):
		def evaluate(D, sol):
			val = 0.0
			for i in range(D): val = val + sol[i] * sol[i]
			return val
		return evaluate

class RunnerTestCase(TestCase):
	def setUp(self):
		self.algorithms = ['DifferentialEvolutionAlgorithm', 'GreyWolfOptimizer', 'GeneticAlgorithm', 'ParticleSwarmAlgorithm', 'HybridBatAlgorithm', 'SelfAdaptiveDifferentialEvolutionAlgorithm', 'CamelAlgorithm', 'BareBonesFireworksAlgorithm', 'MonkeyKingEvolutionV1', 'MonkeyKingEvolutionV2', 'MonkeyKingEvolutionV3', 'EvolutionStrategy', 'SineCosineAlgorithm']
		self.benchmarks = ['griewank', MyBenchmark()]

	def test_runner_works_fine(self):
		self.assertTrue(NiaPy.Runner(4, 10, 10, 3, self.algorithms, self.benchmarks).run())

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
