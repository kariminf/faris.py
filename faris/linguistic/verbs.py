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

from .pos import POS
from .pos import Tense, Aspect

class Verb(POS):
	def __init__(self, synSet: int) -> None:
		super().__init__(synSet)
		self.tense = Tense.PRESENT
		self.aspect = Aspect.HABITUAL
	
	def __eq__(self, other: 'Verb') -> bool:
		result = super().__eq__(other)
		result = result and (self.tense == other.tense)
		result = result and (self.aspect == other.aspect)
		return result
	
	def __repr__(self) -> str:
		result = 'VRB(' + super().__repr__() + ',' 
		result += str(self.tense) + ', '
		result += str(self.aspect) + ')'
		return result

	def set_tense(self, tense: Tense):
		self.tense = tense

	def set_aspect(self, aspect: Aspect):
		self.aspect = aspect
	
	

