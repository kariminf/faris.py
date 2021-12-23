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

from abc import ABC
from enum import Enum, auto


class POS(ABC):
	"""
	
	"""

	def __init__(self, synset:int) -> None:
		super().__init__()
		self.synset: int = synset

	def __eq__(self, other: 'POS') -> bool:
		return self.synset == other.synset

	def __repr__(self) -> str:
		return str(self.synset)

	def __hash__(self) -> int:
		return hash(self.__repr__)
	
	def get_synset(self) -> int:
		return self.synSet

	def has_synset(self, synSet: int) -> bool:
		return (self.synSet == synSet)


class Gender(Enum):
	COMMON = auto()
	FEMININE = auto()
	MASCULINE = auto()
	NEUTER = auto()


class Animacy(Enum):
	ANIMATE = auto()
	INANIMATE = auto()

class Definiteness(Enum):
	INDEFINITE = auto()
	DEFINITE = auto()
	
class Tense(Enum):
	PAST = auto()
	PRESENT = auto()
	FUTURE = auto()

class Polarity(Enum):
	POSITIVE = auto()
	NEGATIVE = auto()

class Aspect(Enum):
	IMPERFECT = auto()
	PERFECT = auto()
	PROSPECTIVE = auto()
	PROGRESSIVE = auto()
	HABITUAL = auto()
	ITERATIVE = auto()
