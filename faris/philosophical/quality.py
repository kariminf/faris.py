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

from typing import List

from .being import Being

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from ..processor import Processor
	from ..linguistic.adjectives import Adjective
	from ..linguistic.adverbs import Adverb


class Quality(Being):

	id = 0

	def __init__(self, adjective: Adjective) -> None:
		super().__init__()
		self.id = Quality.id 
		Quality.id += 1
		self.adjective = adjective
		self.adverbs = set()
	
	def __repr__(self) -> str:
		return repr(self.adjective)
	
	def add_adverbs(self, adverbs: List[Adverb]):
		for adverb in adverbs:
			self.adverbs.add(adverb)

	def process(self, p: Processor):
		p.process_quality(self)
