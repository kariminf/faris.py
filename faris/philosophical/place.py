from being import Being
from linguistic.adverbs import Adverb
from typing import Set
from enum import Enum, auto

class RelationPlace(Enum):
	EXIST = auto() # in, at  a place
	SOURCE = auto() # starting place
	DESTINATION = auto() # destination place
	BEFORE = auto() 
	AFTER = auto() 
	FRONT = auto() 
	BEHIND = auto() 
	RIGHT = auto() 
	LEFT = auto() 
	PROXIMITY = auto() 
	BELOW = auto() 
	ABOVE = auto() 
	INSIDE = auto() 
	OUTSIDE = auto() 
	BETWEEN = auto() 
	THROUGH = auto() 


class Place(Being):
	def __init__(self) -> None:
		super().__init__()
		self.type = None
	
	def define_adverb(self, adverb: Adverb) -> bool:
		if not self.type:
			self.adverb = adverb
			self.type = 'adverb'
			return True 
		else:
			return False
	
	def define_relation(self, relation: RelationPlace, places: Set[Set['Place']]):
		if not self.type:
			self.relation = relation
			self.places = places 
			self.type = 'relation'
			return True 
		else:
			return False
	