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

from abc import ABC, abstractmethod
from faris import Faris
from knowledge import Mind, Idea
from philosophical import Action, Attitude, Place, Quality
from philosophical import Quantity, Relative, State, Substance, Time


class Processor(ABC):
    # Knowledge
    @abstractmethod
    def process_faris(self, faris: Faris) -> None:
        pass 

    @abstractmethod
    def process_mind(self, mind: Mind) -> None:
        pass

    @abstractmethod
    def process_idea(self, idea: Idea) -> None:
        pass 

    # Philosophical
    @abstractmethod
    def process_action(self, action: Action) -> None:
        pass

    @abstractmethod
    def process_attitude(self, attitude: Attitude) -> None:
        pass 

    @abstractmethod
    def process_place(self, place: Place) -> None:
        pass 

    @abstractmethod
    def process_quality(self, quality: Quality) -> None:
        pass 

    @abstractmethod
    def process_quantity(self, quantity: Quantity) -> None:
        pass 

    @abstractmethod
    def process_relative(self, relative: Relative) -> None:
        pass 

    @abstractmethod
    def process_state(self, state: State) -> None:
        pass 

    @abstractmethod
    def process_substance(self, substance: Substance) -> None:
        pass 

    @abstractmethod
    def process_time(self, time: Time) -> None:
        pass 