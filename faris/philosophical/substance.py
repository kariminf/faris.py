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
from linguistic.nouns import Noun
from quality import Quality
from relative import Relative, RelativeType
from typing import Set
from processor import Processor

class Substance(Being):
	def __init__(self, noun: Noun) -> None:
		super().__init__()
		self.noun = noun
		self.qualities = set()
		# An action can have relatives: He works harder than his brother
		self.relatives: Set[Relative] = set()

	def add_quality(self, quality: Quality):
		self.qualities.add(quality)
	
	def assign_relative(self, reltype: RelativeType, relative) -> Relative:
		relative = Relative(self, reltype, relative)
		self.relatives.add(relative)
		return relative

	def process(self, processor: Processor):
		processor.process_substance(self)

