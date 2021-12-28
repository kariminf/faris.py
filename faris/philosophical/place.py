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
from .being import Being

from typing import Set, List, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from ..processor import Processor
	from ..linguistic.adverbs import Adverb
	from .substance import Substance


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
	id = 0
	def __init__(self, relation: RelationPlace = RelationPlace.EXIST) -> None:
		super().__init__()
		self.id = Place.id 
		Place.id += 1
		self.relation = relation
		# TODO: just and relation
		self.relatives: List[Tuple[Adverb, Substance]] = []
	
	def __repr__(self) -> str:
		return 'PLACE(' + repr(self.relation) + ')'
	
	def add_relative(self, relative: Tuple[Adverb, Substance]):
		self.relatives.append(relative)
	
	def process(self, p: Processor):
		p.process_place(self)
