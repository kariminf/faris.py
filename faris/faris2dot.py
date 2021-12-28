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

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
from faris.knowledge.conditional import Conditional
from faris.knowledge.opinion import Opinion

from faris.knowledge.thought import Thought
if TYPE_CHECKING:
    from .faris import Faris
    from .knowledge import Mind, Idea
    from .philosophical import Action, Attitude, Place, Quality
    from .philosophical import Quantity, Relative, State, Substance, Time

from .processor import Processor

class Faris2Dot(Processor):
    def __init__(self) -> None:
        super().__init__()
        self.graphviz = 'digraph {\n'
        self.cluster_nbr = 0
        self.substances = []
        self.qualities = []
        self.quantities = []
        self.states = []
        self.times = []
        self.places = []
        self.actions = []

    # Knowledge
    def process_faris(self, faris: Faris) -> None:
        faris.mind.process(self) 
        self.graphviz += '}\n'


    def process_mind(self, mind: Mind) -> None:
        self.graphviz += 'subgraph cluster{0} {{\n'.format(self.cluster_nbr)
        self.cluster_nbr += 1
        self.graphviz += 'node [shape="box"]\n'
        self.graphviz += 'label = "' + mind.name + '";\n'

        # Thoughts 
        self.graphviz += 'subgraph cluster{0} {{\n'.format(self.cluster_nbr)
        self.cluster_nbr += 1
        self.graphviz += 'node [shape="box"]\n'
        self.graphviz += 'label = "Thoughts";\n'
        for mental_state in mind.thoughts:
            self.graphviz += 'subgraph cluster{0} {{\n'.format(self.cluster_nbr)
            self.cluster_nbr += 1
            self.graphviz += 'node [shape="box"]\n'
            self.graphviz += 'label = "{0}";\n'.format(str(mental_state))
            for thought in mind.thoughts.get(mental_state):
                thought.process(self)
            self.graphviz += '}\n'
        self.graphviz += '}\n'

        self.graphviz += '}\n'

    def process_idea(self, idea: Idea) -> None:
        if isinstance(idea, Thought):
            idea.thought.process(self)
        elif isinstance(idea, Opinion):
            idea.other_mind.process(self)
        elif isinstance(idea, Conditional):
            self.graphviz += 'subgraph cluster{0} {{\n'.format(self.cluster_nbr)
            self.cluster_nbr += 1
            self.graphviz += 'node [shape="box"]\n'
            
            self.graphviz += 'subgraph cluster{0} {{\n'.format(self.cluster_nbr)
            self.cluster_nbr += 1
            self.graphviz += 'node [shape="box"]\n'
            self.graphviz += 'label = "Condition";\n'
            idea.condition.process(self)
            self.graphviz += '}\n'

            self.graphviz += 'subgraph cluster{0} {{\n'.format(self.cluster_nbr)
            self.cluster_nbr += 1
            self.graphviz += 'node [shape="box"]\n'
            self.graphviz += 'label = "Predicate";\n'
            idea.predicate.process(self)
            self.graphviz += '}\n'


            self.graphviz += '}\n'


    # Philosophical
    def process_action(self, action: Action) -> None:
        if action in self.actions:
            return 

        self.actions.append(action)
        act_name = 'act' + str(action.id)
        self.graphviz += '{0} [shape=box, style=rounded, label="{1}"]\n'.format(act_name, repr(action.verb))
        for doers_conj in action.doers:
            for doer in doers_conj:
                doer.process(self)
                dname = 'sub' + str(doer.id)
                self.graphviz += '{0} -> {1}\n'.format(dname, act_name)

        for receivers_conj in action.receivers:
            for receiver in receivers_conj:
                receiver.process(self)    
                rname = 'sub' + str(receiver.id)
                self.graphviz += '{0} -> {1}\n'.format(act_name, rname)
            
        for time in action.times:
            time.process(self)
            tname = 'time' + str(time.id)
            self.graphviz += '{0} -> {1}\n'.format(act_name, tname)
        
        for place in action.places:
            place.process(self)
            place_name = 'place' + str(place.id)
            self.graphviz += '{0} -> {1}\n'.format(act_name, place_name)


    def process_attitude(self, attitude: Attitude) -> None:
        pass 

    def process_place(self, place: Place) -> None:
        if place in self.places:
            return
        self.places.append(place)
        place_name = 'place' + str(place.id)
        self.graphviz += '{0} [shape=ellipse, label="{1}"]\n'.format(place_name, str(place.relation))
        self.graphviz += '{0}b [shape=box, label="{1}"]\n'.format(place_name, str(place.relatives))
        self.graphviz += '{0} -> {0}b\n'.format(place_name) 

    def process_quality(self, quality: Quality) -> None:
        if quality in self.qualities:
            return
        self.qualities.append(quality)
        name = 'qual' + str(quality.id)
        self.graphviz += '{0} [shape=pentagon, label="{1}"]\n'.format(name, repr(quality))

    def process_quantity(self, quantity: Quantity) -> None:
        if quantity in self.quantities:
            return
        self.quantities.append(quantity)
        name = 'quan' + str(quantity.id)
        self.graphviz += '{0} [shape=octagon, label="{1}"]\n'.format(name, repr(quantity)) 

    def process_relative(self, relative: Relative) -> None:
        pass 

    def process_state(self, state: State) -> None:
        if state in self.states:
            return 
        
        self.states.append(state)
        state_name = 'state' + str(state.id) 
        self.states.append(state)
        self.graphviz += '{0} [shape=parallelogram, label="{1}"]\n'.format(state_name, repr(state))

        for main_conj in state.main_actions:
            for main_action in main_conj:
                main_action.process(self)
                actname = 'act' + str(main_action.id)
                self.graphviz += '{0} -> {1}\n'.format(actname, state_name)

        for state_conj in state.state_actions:
            for state_action in state_conj:
                state_action.process(self)
                actname = 'act' + str(state_action.id)
                self.graphviz += '{0} -> {1}\n'.format(state_name, actname)

        for owners_conj in state.owners:
            for owner in owners_conj:
                owner.process(self)
                ownername = 'sub' + str(owner.id)
                self.graphviz += '{0} -> {1}\n'.format(ownername, state_name)

    def process_substance(self, substance: Substance) -> None:
        if substance in self.substances:
            return

        self.substances.append(substance)
        name = 'sub' + str(substance.id)
        self.graphviz += '{0} [shape=box, label="{1}"]\n'.format(name, repr(substance.noun))
        for quality in substance.qualities:
            quality.process(self)
            qname = 'qual' + str(quality.id)
            self.graphviz += '{0} -> {1}\n'.format(name, qname) 
        
        quantity = substance.quantity
        if quantity:
            quantity.process(self)
            name = 'sub' + str(substance.id)
            qname = 'quan' + str(quantity.id)
            self.graphviz += '{0} -> {1}\n'.format(name, qname)

        for state in substance.states:
            state.process(self)


    def process_time(self, time: Time) -> None:
        if time in self.times:
            return 
        self.times.append(time)
        time_name = 'time' + str(time.id)
        self.graphviz += '{0} [shape=ellipse, label="{1}"]\n'.format(time_name, str(time.relation))
        self.graphviz += '{0}b [shape=box, label="{1}"]\n'.format(time_name, str(time.relatives))
        self.graphviz += '{0} -> {0}b\n'.format(time_name)

