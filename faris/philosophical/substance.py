from being import Being
from linguistic.nouns import Noun
from quality import Quality
from relative import Relative, RelativeType
from typing import Set

class Substance(Being):
	def __init__(self, noun: Noun) -> None:
		super().__init__()
		self.noun = noun
		self.qualities = set()
		# An action can have relatives: He works harder than his brother
		self.relatives: Set[Relative] = set()

	def add_quality(self, quality: Quality):
		self.qualities.add(quality)
	
	def assign_relative(self, reltype: RelativeType, relative) -> Relative:
		relative = Relative(self, reltype, relative)
		self.relatives.add(relative)
		return relative

