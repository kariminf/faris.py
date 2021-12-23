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
from linguistic.verbs import Verb, verb 
from collections.abc import Mapping
from action import Action
from substance import Substance
from typing import Set
from processor import Processor

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
	
	def process(self, processor: Processor):
		processor.process_attitude(self)
