from copy import deepcopy
from utils import get_random_number

from population import Population
from schedule import Schedule

from driver import NUMB_OF_ELITE_SCHEDULES, CROSSOVER_RATE, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE

class GeneticAlgorithm(object):
  def __init__(self, data):
    self.data = data
  
  def evolve(self, population):
    return self.mutate_population(self.crossover_population(population))

  def crossover_population(self, population):
    _cross_over_popluation = Population(size=len(population.schedules), data=self.data)
    for idx in range(NUMB_OF_ELITE_SCHEDULES):
      _cross_over_popluation.schedules[idx] = deepcopy(population.schedules[idx])
    
    for idx in range(NUMB_OF_ELITE_SCHEDULES, len(population.schedules)):
      if CROSSOVER_RATE > get_random_number():
        schedule1 = self.select_tournament_population(population).sort_by_fitness().schedules[0]
        schedule2 = self.select_tournament_population(population).sort_by_fitness().schedules[1]
        _cross_over_popluation.schedules[idx] = self.crossover_schedule(schedule1, schedule2)
      else:
        _cross_over_popluation.schedules[idx] = deepcopy(population.schedules[idx])

    return _cross_over_popluation
  
  def crossover_schedule(self, schedule1, schedule2):
    _crossover_schedule = Schedule(data=self.data).initialize()
    for idx in range(len(_crossover_schedule.classes)):
      if get_random_number() > 0.5:
        _crossover_schedule.classes[idx] = deepcopy(schedule1.classes[idx])
      else:
        _crossover_schedule.classes[idx] = deepcopy(schedule2.classes[idx])
      
    return _crossover_schedule

  def mutate_population(self, population):
    _mutate_population = Population(size=len(population.schedules), data=self.data)
    
    _schedules = list(_mutate_population.schedules)
    for idx in range(NUMB_OF_ELITE_SCHEDULES):
      _schedules[idx] = deepcopy(population.schedules[idx])
    
    for idx in range(NUMB_OF_ELITE_SCHEDULES, len(population.schedules)):
      _schedules[idx] = self.mutate_schedule(population.schedules[idx])

    _mutate_population.schedules = _schedules

    return _mutate_population

  def mutate_schedule(self, _mutate_schedule):
    _mutate_schedule = deepcopy(_mutate_schedule)
    _schedule = Schedule(data=self.data).initialize()

    for idx in range(len(_mutate_schedule.classes)):
      if MUTATION_RATE > get_random_number():
        _mutate_schedule.classes[idx] = deepcopy(_schedule.classes[idx])
    
    return _mutate_schedule

  def select_tournament_population(self, population):
    tournament_population = Population(size=TOURNAMENT_SELECTION_SIZE, data=self.data)
    for idx in range(TOURNAMENT_SELECTION_SIZE):
      tournament_population.schedules[idx] = population.schedules[int(get_random_number() * len(population.schedules))]
    
    return tournament_population