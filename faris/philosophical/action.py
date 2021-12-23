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

from being import Being
from enum import Enum
from linguistic.verbs import Verb
from linguistic.adverbs import Adverb
from substance import Substance
from relative import Relative, RelativeType
from place import Place
from time import Time
from collections import Set
from typing import Union
from processor import Processor

class ActionRelation(Enum):
	IMPLY = 0
	CAUSE = 1
	AFTER = 2
	BEFORE = 3

class Action(Being):

	def __init__(self, verb: Verb) -> None:
		super().__init__()
		self.verb =  verb # An action is defined by a verb
		self.adverbs : Set[Adverb] = set()
		# Here, we use disjunctions of conjunctions 
		# An Action can have many doers (we can't duplicate a doer)
		self.doers : Set[Set[Substance]] = set()
		# An Action can affect many predicates 
		self.receivers : Set[Set[Substance]] = set()

		# An action can have relatives: He works harder than his brother
		self.relatives: Set[Relative] = set()
		# An action can have locations
		self.locations: Set[Place] = set()
		# An action can have times
		self.times: Set[Time] = set()
		
	def add_conjuncted_doers(self, conj_doers: Set[Substance]):
		self.doers.add(conj_doers)

	def add_conjuncted_receivers(self, conj_receivers: Set[Substance]):
		self.receivers.add(conj_receivers)
	
	def add_adverbs(self, adverb: Adverb):
		self.adverbs.add(adverb)

	def add_location(self, location: Place):
		self.locations.add(location)
	
	def add_time(self, time: Time):
		self.times.add(time)

	def assign_relative(self, reltype: RelativeType, relative) -> Relative:
		relative = Relative(self, reltype, relative)
		self.relatives.add(relative)
		return relative

	def process(self, processor: Processor):
		processor.process_action(self)
