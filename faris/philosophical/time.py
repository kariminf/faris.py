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
from collections.abc import Set 
from typing import List, Tuple

from typing import TYPE_CHECKING

from faris.philosophical.substance import Substance
if TYPE_CHECKING:
	from ..processor import Processor
	from ..linguistic.adverbs import Adverb

from .being import Being

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
	id = 0
	def __init__(self, relation: RelationTime = RelationTime.EXIST) -> None:
		super().__init__()
		self.id = Time.id 
		Time.id += 1
		self.relation = relation
		# TODO: just and relation
		self.relatives: List[Tuple[Adverb, Substance]] = []
	
	def __repr__(self) -> str:
		return 'TIME(' + repr(self.relation) + ')'
	
	def add_relative(self, relative: Tuple[Adverb, Substance]):
		self.relatives.append(relative)
	
	def process(self, p: Processor):
		p.process_time(self)

