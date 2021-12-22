# FARIS : Factual Arrangement and Representation of Ideas in Sentences
# FAris : Farabi & Aristotle
# Faris : A knight (in Arabic)
# --------------------------------------------------------------------
# Copyright (C) 2021 Abdelkrime Aries (kariminfo0@gmail.com)
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




# /**
#  * 
#  * @author Abdelkrime Aries (kariminfo0@gmail.com)
#  *         <br>
#  *         Copyright (c) 2015-2016 Abdelkrime Aries
#  *         <br><br>
#  *         Licensed under the Apache License, Version 2.0 (the "License");
#  *         you may not use this file except in compliance with the License.
#  *         You may obtain a copy of the License at
#  *         <br><br>
#  *         http://www.apache.org/licenses/LICENSE-2.0
#  *         <br><br>
#  *         Unless required by applicable law or agreed to in writing, software
#  *         distributed under the License is distributed on an "AS IS" BASIS,
#  *         WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  *         See the License for the specific language governing permissions and
#  *         limitations under the License.
#  */

from abc import ABC
from enum import Enum


class POS(ABC):
	"""
	
	"""

	def __init__(self, synSet:int) -> None:
		super().__init__()
		self.synSet = synSet
	
	def getSynset(self) -> int:
		return synSet

	def hasSynset(self, synSet: int) -> bool:
		return (this.synSet == synSet)


class Gender(Enum):
	COMMON = 0
	FEMININE = 1
	MASCULINE = 2
	NEUTER = 3


class Animacy(Enum):
	ANIMATE = 0
	INANIMATE = 1

class Definiteness(Enum):
	INDEFINITE = 0
	DEFINITE = 1
	
class Tense(Enum):
	PAST = 0
	PRESENT = 1
	FUTURE = 2

class Polarity(Enum):
	POSITIVE = 0
	NEGATIVE = 1

class Aspect(Enum):
	IMPERFECT = 0
	PERFECT = 1
	PROSPECTIVE = 2
	PROGRESSIVE = 3
	HABITUAL = 4
	ITERATIVE = 5
