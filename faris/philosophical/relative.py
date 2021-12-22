from being import Being
from enum import Enum
from typing import Union
from action import Action
from substance import Substance

class RelativeType(Enum):
	OF = 0
	MORE = 1
	LESS = 2
	MOST = 3
	LEAST = 4
	EQUAL = 5


class Relative(Being):

	def __init__(self, owner: Union[Action, Substance], reltype: RelativeType, relative: Union[Action, Substance]) -> None:
		super().__init__()
		# The owner can be a substance: the man is taller than the boy
		# The owner can be an action: Karim worked harder than his colleague.
		self.owner = owner 
		self.reltype = reltype
		self.relative = relative
	