from idea import Idea 
from philosophical.action import Action

class Thought(Idea):
	def __init__(self, action: Action) -> None:
		super().__init__()
		self.thought = action
		