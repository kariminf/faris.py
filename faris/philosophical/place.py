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
from linguistic.adverbs import Adverb
from typing import Set
from enum import Enum, auto
from processor import Processor

class RelationPlace(Enum):
	EXIST = auto() # in, at  a place
	SOURCE = auto() # starting place
	DESTINATION = auto() # destination place
	BEFORE = auto() 
	AFTER = auto() 
	FRONT = auto() 
	BEHIND = auto() 
	RIGHT = auto() 
	LEFT = auto() 
	PROXIMITY = auto() 
	BELOW = auto() 
	ABOVE = auto() 
	INSIDE = auto() 
	OUTSIDE = auto() 
	BETWEEN = auto() 
	THROUGH = auto() 


class Place(Being):
	def __init__(self) -> None:
		super().__init__()
		self.type = None
	
	def define_adverb(self, adverb: Adverb) -> bool:
		if not self.type:
			self.adverb = adverb
			self.type = 'adverb'
			return True 
		else:
			return False
	
	def define_relation(self, relation: RelationPlace, places: Set[Set['Place']]):
		if not self.type:
			self.relation = relation
			self.places = places 
			self.type = 'relation'
			return True 
		else:
			return False
	
	def process(self, processor: Processor):
		processor.process_place(self)
	