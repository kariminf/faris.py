
from pos import POS
from pos import Gender

class Noun(POS):

	def __init__(self, synSet: int) -> None:
		super().__init__(synSet)
		self.gender = Gender.COMMON
		self.defined = False

	def set_defined(self):
		self.defined = True
	
	def set_gender(self, gender):
		self.gender = gender

class ProperNoun(Noun):
	def __init__(self, synSet: int, name: str) -> None:
		super().__init__(synSet)
		self.name = name