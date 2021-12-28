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

from typing import Set
from collections.abc import Mapping

from typing import TYPE_CHECKING

from faris.philosophical.state import State

if TYPE_CHECKING:
	from .quality import Quality
	from .relative import Relative, RelativeType
	from .quantity import Quantity
	from ..processor import Processor
	from ..linguistic.nouns import Noun

from .being import Being

class Substance(Being):
	id = 0
	def __init__(self, noun: Noun) -> None:
		super().__init__()
		self.id = Substance.id 
		Substance.id += 1
		self.noun = noun
		self.quantity = None
		self.qualities = set()
		# An action can have relatives: He works harder than his brother
		self.relatives: Set[Relative] = set()
		self.states: Set[State] = set()

	def __repr__(self) -> str:
		return 'SUBST(' + repr(self.noun) + ')'

	def __hash__(self) -> int:
		return hash(self.__repr__)
	
	def __eq__(self, other: 'Substance') -> bool:
		result = super().__eq__(other)
		result = result and (self.noun == other.noun)
		return result

	def add_quality(self, quality: Quality):
		self.qualities.add(quality)
	
	def set_quantity(self, quantity: Quantity):
		self.quantity = quantity
	
	def assign_relative(self, reltype: RelativeType, relative) -> Relative:
		relative = Relative(self, reltype, relative)
		self.relatives.add(relative)
		return relative
	
	def update(self, substance: 'Substance'):
		self.qualities.difference_update(substance.qualities)
		self.relatives.difference_update(substance.relatives)

	def process(self, p: Processor):
		p.process_substance(self)

