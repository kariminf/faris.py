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
from action import Action
from typing import Set

from philosophical.substance import Substance
from processor import Processor

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
	
	def process(self, processor: Processor):
		processor.process_state(self)