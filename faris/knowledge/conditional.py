from idea import Idea

class Conditional(Idea):
	def __init__(self, condition: Idea, predicate: Idea) -> None:
		super().__init__()
		self.condition = condition 
		self.predicate = predicate
