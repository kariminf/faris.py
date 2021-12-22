from being import Being
from linguistic.adverbs import Adverb
from enum import Enum, auto

class RelationTime(Enum):
	EXIST = auto() # in, at time 
	PAST = auto() # ago (time)
	SINCE = auto() # since (time)
	SOURCE = auto() # from time
	DESTINATION = auto() # till, to time
	DURATION = auto() #  for time
	BEFORE = auto() # before time
	AFTER = auto() # after time
	PROXIMITY = auto() # by time
	BETWEEN = auto() # time
	THROUGH = auto() # time

class Time(Being):
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
	
	def define_relation(self, relation: RelationTime, places: Set[Set['Time']]):
		if not self.type:
			self.relation = relation
			self.places = places 
			self.type = 'relation'
			return True 
		else:
			return False

