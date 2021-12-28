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

from enum import Enum, auto
from collections.abc import Mapping
from typing import Set
from .thought import Thought
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .opinion import Opinion
	from .conditional import Conditional
	from .idea import Idea
	from ..processor import Processor
	from ..philosophical.action import Action
	from ..philosophical.substance import Substance


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

	def process(self, p: Processor):
		p.process_mind(self)
