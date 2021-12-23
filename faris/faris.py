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

from typing import Set 
from collections.abc import Mapping
from linguistic.nouns import Noun
from philosophical import Substance, Action, State
from knowledge import Mind
from processor import Processor


class Faris:
    def __init__(self) -> None:
        self.substances: Set[Substance] = set()
        self.actions: Set[Action] = set()
        self.states: Set[State] = set()

        self.minds: Mapping[Substance, Mind] = set()

        # Common sense mind (no owner)
        common_mind_owner = Substance(Noun(0))
        self.substances.add(common_mind_owner)
        self.minds[common_mind_owner] = Mind('$', common_mind_owner)
        
    def get_mind(self, owner: Substance) -> Mind:
        if owner not in self.minds:
            name = owner.hash_name()
            self.minds[owner] = Mind(name, owner) 
        return self.minds[owner]
    
    def get_substance(self, substance: Substance) -> Substance:
        if substance in self.substances:
            pass
        else:
            pass 
    
    def process(self, processor: Processor):
        processor.process_faris(self)

