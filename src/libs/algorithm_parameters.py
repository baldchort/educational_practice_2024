from objects import *


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
