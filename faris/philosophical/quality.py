from being import Being
from linguistic.adjectives import Adjective
from linguistic.adverbs import Adverb
from typing import List

class Quality(Being):
	def __init__(self, adjective: Adjective) -> None:
		super().__init__()
		self.adjective = adjective
		self.adverbs = set()
	
	def add_adverbs(self, adverbs: List[Adverb]):
		for adverb in adverbs:
			self.adverbs.add(adverb)
