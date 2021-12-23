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
from enum import Enum, auto
from processor import Processor

class RelationTime(Enum):
	EXIST = auto() # in, at time 
	PAST = auto() # ago (time)
	SINCE = auto() # since (time)
	SOURCE = auto() # from time
	DESTINATION = auto() # till, to time
	DURATION = auto() #  for time
	BEFORE = auto() # before time
	AFTER = auto() # after time
	PROXIMITY = auto() # by time
	BETWEEN = auto() # time
	THROUGH = auto() # time

class Time(Being):
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
	
	def define_relation(self, relation: RelationTime, places: Set[Set['Time']]):
		if not self.type:
			self.relation = relation
			self.places = places 
			self.type = 'relation'
			return True 
		else:
			return False
	
	def process(self, processor: Processor):
		processor.process_time(self)

