from being import Being 
from linguistic.verbs import Verb, verb 
from collections.abc import Mapping
from action import Action
from substance import Substance
from typing import Set

class Attitude(Being):

	def __init__(self, ing_verb: Verb) -> None:
		super().__init__()
		self.posture = ing_verb
		self.owners: Mapping[Substance, Set[Action]] = {}

	def add_owner(self, player: Substance, in_action: Action):
		if player in self.owners:
			self.owners.get(player).add(in_action)
		else:
			self.owners[player] = set([in_action])
		
