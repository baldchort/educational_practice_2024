from src.libs.objects import *
from prettytable import PrettyTable


generationNum = 1
mutationNum = 1
discreteRecomb = 1
log = 0


class AlgorithmParameters:
    def __init__(self,
                 maxBackpackWeight: int,
                 crossingProbability: float,
                 mutationProbability: float,
                 amountOfIndividsPerGeneration: int,
                 maxAmountOfGenerations: int,
                 parentsSelectionStrategy: 'ParentSelectionStrategy',
                 crossingStrategy: 'CrossingStrategy',
                 mutationStrategy: 'MutationStrategy',
                 generationSelectionStrategy: 'GenerationSelectionStrategy'):
        self.maxBackpackWeight = maxBackpackWeight
        self.crossingProbability = crossingProbability
        self.mutationProbability = mutationProbability
        self.amountOfIndividsPerGeneration = amountOfIndividsPerGeneration
        self.maxAmountOfGenerations = maxAmountOfGenerations
        self.parentsSelectionStrategy = parentsSelectionStrategy
        self.crossingStrategy = crossingStrategy
        self.mutationStrategy = mutationStrategy
        self.generationSelectionStrategy = generationSelectionStrategy
