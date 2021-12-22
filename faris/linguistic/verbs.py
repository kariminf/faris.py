from pos import POS
from pos import Tense, Aspect

class Verb(POS):
	def __init__(self, synSet: int) -> None:
		super().__init__(synSet)
		self.tense = Tense.PRESENT
		self.aspect = Aspect.HABITUAL
	

	def set_tense(self, tense: Tense):
		self.tense = tense

	def set_aspect(self, aspect: Aspect):
		self.aspect = aspect
