from pos import POS


class Adjective(POS):

	def __init__(self, synSet: int) -> None:
		super().__init__(synSet)


# public static enum Graduation {
# 		ABSOLUTE,
# 		COMPARATIVE,
# 		SUPERLATIVE
