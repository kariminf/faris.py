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
from typing import Union

from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .action import Action
	from .substance import Substance
	from ..processor import Processor

from .being import Being

class RelativeType(Enum):
	OF = auto()
	MORE = auto()
	LESS = auto()
	MOST = auto()
	LEAST = auto()
	EQUAL = auto()


class Relative(Being):

	def __init__(self, owner: Union[Action, Substance], reltype: RelativeType, relative: Union[Action, Substance]) -> None:
		super().__init__()
		# The owner can be a substance: the man is taller than the boy
		# The owner can be an action: Karim worked harder than his colleague.
		self.owner = owner 
		self.reltype = reltype
		self.relative = relative

	def __repr__(self) -> str:
		return repr(self.reltype)

	def process(self, p: Processor):
		p.process_relative(self)
