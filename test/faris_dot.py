import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faris.philosophical.place import Place
from faris.philosophical.state import State, StateType
from faris.faris2dot import Faris2Dot
from faris.knowledge.mind import MentalState
from faris.linguistic.adjectives import Adjective
from faris.linguistic.adverbs import Adverb
from faris.linguistic.nouns import Noun
from faris.linguistic.pos import Gender, Tense
from faris.linguistic.verbs import Verb
from faris.philosophical.action import Action
from faris.philosophical.quality import Quality
from faris.philosophical.quantity import Quantity

from faris.philosophical.substance import Substance
from faris.philosophical.time import Time

from faris import Faris

faris = Faris()

# substance + quantity
men_noun = Noun(10306910)
men_noun.set_defined()
men_noun.set_gender(Gender.MASCULINE)
the_5_men = Substance(men_noun)
quantity_5 = Quantity()
quantity_5.set_number(5)
the_5_men.set_quantity(quantity_5)

the_5_men = faris.get_substance(the_5_men)

# substance + quality
car_noun = Noun(2961779)
red_car = Substance(car_noun)
red_adjective = Adjective(382159)
red_quality = Quality(red_adjective)
red_car.add_quality(red_quality)

red_car = faris.get_substance(red_car)

# action + time
rent_verb = Verb(2213319)
rent_action = Action(rent_verb)
yesterday_adverb = Adverb(510249)
yesterday_time = Time()
yesterday_time.add_relative(yesterday_adverb)
rent_action.add_conjuncted_doers(set([the_5_men]))
rent_action.add_conjuncted_receivers(set([red_car]))
rent_action.add_time(yesterday_time)

faris.mind.add_thought(MentalState.FACT, rent_action)


# 
# state
engine_noun = Noun(3292644)
old_adjective = Adjective(1642580)
old_quality = Quality(old_adjective)
old_engine = Substance(engine_noun)
old_engine.add_quality(old_quality)
have_verb = Verb(2208144)
have_verb.set_tense(Tense.PRESENT)
have_action = Action(have_verb)
have_action.add_conjuncted_receivers(set([old_engine]))


road_noun = Noun(4103160)
road = Substance(road_noun)
stop_verb = Verb(1863207)
stop_action = Action(stop_verb)
on_road = Place()
on_road.add_relative(road)
stop_action.add_place(on_road)

state = State(StateType.SUBJECT, [set([red_car])])
state.add_main_action_conjunctions(set([rent_action]))
state.add_state_conjunctions(set([have_action, stop_action]))



faris2dot = Faris2Dot()

faris.process(faris2dot)


with open('test.dot', 'w') as f:
    f.write(faris2dot.graphviz)




