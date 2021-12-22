from being import Being 

class Quantity(Being):

	def __init__(self) -> None:
		super().__init__()
		self.cardinal = True
		self.plural = False
		self.unit = None
		self.nbr = 1
	
	def set_ordinal(self):
		if not self.plural:
			self.cardinal = False
	
	def set_plural(self):
		self.plural = True
	
	def set_unit(self, unit):
		self.unit = unit

	def set_number(self, nbr):
		self.nbr = nbr
