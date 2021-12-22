from being import Being
from action import Action
from typing import Set

from philosophical.substance import Substance

class State(Being):
	def __init__(self, owners: Set[Set[Substance]]) -> None:
		super().__init__()
		self.owners = owners
		self.main_actions = set()
		self.state_action = set()

	def add_main_action_conjunctions(self, main_action: Set(Action)):
		"""A main action is the action where a substance has this state. 
		For example: "The man who was there drives this car"; the action "drives" is 
		one of the main actions for the state "who was there"."""
		self.main_actions.add(main_action)
	
	def add_state_conjunctions(self, state_actions: Set[Action]):
		"""
		This action must not have subjects or objects.<br/>
		Example: a car which is stopped on the road and have an old engine. 
		The car have two states: "stopped" and "having old engine".
		"""
		self.state_action.add(state_actions)