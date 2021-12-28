# FARIS : Factual Arrangement and Representation of Ideas in Sentences
# FAris : Farabi & Aristotle
# Faris : A knight (in Arabic)
# --------------------------------------------------------------------
# Copyright (C) 2015, 2021 Abdelkrime Aries (kariminfo0@gmail.com)
# 
# Autors: 
#        - 2021 Abdelkrime Aries (kariminfo0@gmail.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import Set, List
from collections.abc import Mapping

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .action import Action
	from .substance import Substance
	from ..processor import Processor

from .being import Being

from enum import Enum, auto

class StateType(Enum):
	SUBJECT = auto()
	OBJECT = auto()
	IOBJECT = auto()

class State(Being):
	id = 0
	def __init__(self, state_type: StateType, owners: List[Set[Substance]]) -> None:
		super().__init__()
		self.id = State.id 
		State.id += 1
		self.type = state_type
		self.owners: List[Set[Substance]] = owners
		for owners_lst in owners:
			for owner in owners_lst:
				owner.states.add(self)
		self.main_actions: List[Set[Substance]] = []
		self.state_actions: List[Set[Substance]] = []
	
	def __repr__(self) -> str:
		return 'STATE(' + str(self.type) + ')'

	def add_main_action_conjunctions(self, main_action: Set(Action)):
		"""A main action is the action where a substance has this state. 
		For example: "The man who was there drives this car"; the action "drives" is 
		one of the main actions for the state "who was there"."""
		self.main_actions.append(main_action)
	
	def add_state_conjunctions(self, state_actions: Set[Action]):
		"""
		This action must not have subjects or objects.<br/>
		Example: a car which is stopped on the road and have an old engine. 
		The car have two states: "stopped" and "having old engine".
		"""
		self.state_actions.append(state_actions)
	
	def process(self, p: Processor):
		p.process_state(self)
