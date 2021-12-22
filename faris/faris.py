from typing import Set 
from collections.abc import Mapping
from linguistic.nouns import Noun
from philosophical import Substance, Action, State
from knowledge import Mind


class Faris:
    def __init__(self) -> None:
        self.substances: Set[Substance] = set()
        self.actions: Set[Action] = set()
        self.states: Set[State] = set()

        self.minds: Mapping[str, Mind] = set()

        # Common sense mind (no owner)
        self.minds['$'] = Mind('$', Substance(Noun(0)))
        