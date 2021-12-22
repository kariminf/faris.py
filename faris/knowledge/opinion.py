from idea import Idea


class Opinion(Idea):
	def __init__(self, super_mind: Mind, other_mind: Mind) -> None:
		super().__init__()
		self.super_mind = super_mind
		self.other_mind = other_mind

