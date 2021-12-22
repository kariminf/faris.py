from enum import Enum, auto
from philosophical.action import Action
from philosophical.substance import Substance
from collections.abc import Mapping
from typing import Set
from thought import Thought
from opinion import Opinion
from conditional import Conditional
from idea import Idea


class MentalState(Enum):
	THINK = auto()
	BELIEVE = auto()
	HOPE = auto()
	FEAR = auto()
	FACT = auto()

class Mind:
	def __init__(self, name: str, owner: Substance) -> None:
		self.name = name 
		self.owner = owner 
		self.thoughts: Mapping[MentalState, Set[Thought]] = {}
		self.opinions: Mapping[MentalState, Mapping[Substance, Opinion]] = {}
		self.conditions: Mapping[MentalState, Set[Conditional]] = {}
	
	def add_thought(self, mental_state: MentalState, action: Action):
		if mental_state not in self.thoughts:
			self.thoughts[mental_state] = set()
		
		self.thoughts.get(mental_state).add(Thought(action))

	# To add an opinion about what someone else think, we recover their mind
	# then, we add the ideas
	def get_opinion_other(self, mental_state: MentalState, other: Substance) -> 'Mind':
		if mental_state not in self.opinions:
			self.opinions[mental_state] = {}

		if other not in self.opinions.get(mental_state):
			name = self.name + '.' + other.hash_name()
			self.opinions.get(mental_state)[other] = Opinion(self, Mind(name, other))
		
		return self.opinions.get(mental_state).get(other).other_mind


	def add_conditional(self, mental_state: MentalState, condition: Idea, predicate: Idea):
		if mental_state not in self.conditions:
			self.conditions[mental_state] = set()
		
		self.conditions.get(mental_state).add(Conditional(condition, predicate))

