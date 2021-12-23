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

from pos import POS
from pos import Gender, Definiteness

class Noun(POS):

	def __init__(self, synSet: int) -> None:
		super().__init__(synSet)
		self.gender = Gender.COMMON
		self.defined = Definiteness.INDEFINITE
	
	def __eq__(self, other: 'Noun') -> bool:
		result = super().__eq__(other)
		result = result and (self.gender == other.gender)
		result = result and (self.defined == other.defined)
		return result
	
	def __repr__(self) -> str:
		return 'n-' + super().__repr__()

	def set_defined(self):
		self.defined = True
	
	def set_gender(self, gender):
		self.gender = gender

class ProperNoun(Noun):
	def __init__(self, synSet: int, name: str) -> None:
		super().__init__(synSet)
		self.name = name
		# self.set_defined()
	
	def __eq__(self, other: 'ProperNoun') -> bool:
		result = super().__eq__(other)
		result = result and (self.name == other.name)
		return result
	
	def __repr__(self) -> str:
		return super().__repr__() + '@' + self.name

