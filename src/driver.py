import json

from tabulate import tabulate
from os import sys, path

from utils import print_data, print_population_schedules, print_schedule_as_table

POPULATION_SIZE           = 9
MUTATION_RATE             = 0.1
CROSSOVER_RATE            = 0.9
TOURNAMENT_SELECTION_SIZE = 3
NUMB_OF_ELITE_SCHEDULES   = 1

def run():
  global SCHEDULE_NUMBER, CLASS_NO

  from data import Data
  from genetic_algorithm import GeneticAlgorithm
  from population import Population

  generation_number = 0
  data = Data()
  _genetic_algorithm = GeneticAlgorithm(data=data)
  _population = Population(size=POPULATION_SIZE, data=data).sort_by_fitness()

  print_data(data=data)
  print
  print

  print_population_schedules(population=_population, generation_number=generation_number)
  print_schedule_as_table(data=data, schedule=_population.schedules[0], generation=generation_number)

  while _population.schedules[0].fitness != 1.0:
    generation_number += 1
    _population = _genetic_algorithm.evolve(population=_population).sort_by_fitness()

    print_population_schedules(population=_population, generation_number=generation_number)
    print_schedule_as_table(data=data, schedule=_population.schedules[0], generation=generation_number)

if __name__ == '__main__' and __package__ is None:
  sys.path.insert(0, path.dirname(path.abspath(__file__)))
  run()