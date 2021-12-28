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
if TYPE_CHECKING:
    # from .knowledge import Mind
    # from .linguistic import Noun
    from .processor import Processor

from .philosophical import Action, Substance, State
from .knowledge import Mind
from .linguistic import Noun

class Faris:
    def __init__(self) -> None:
        self.substances: Mapping[int, Set[Substance]]= {}
        self.actions: Set[Action] = set()
        self.states: Set[State] = set()
        
        self.minds: Mapping[Substance, Mind] = {}

        # Common sense mind (no owner)
        common_mind_owner = Substance(Noun(0))
        self.substances[0] = set([common_mind_owner])
        self.mind = Mind('$', common_mind_owner)
        self.minds[common_mind_owner] = self.mind
        
    def get_mind(self, owner: Substance) -> Mind:
        if owner not in self.minds:
            name = owner.hash_name()
            self.minds[owner] = Mind(name, owner) 
        return self.minds[owner]
    
    def get_substance(self, substance: Substance) -> Substance:
        result = substance
        if substance.noun.synset in self.substances:
            substances = self.substances.get(substance.noun.synset)
            for sub in substances:
                if sub == substance:
                    result = sub 
                    break 
            if result == substance:
                result.update(substance)
            else:
                substances.add(result)
        else: 
            self.substances[substance.noun.synset] = set([substance])

        return result
    
    def process(self, processor: Processor):
        processor.process_faris(self)

