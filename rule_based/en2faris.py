import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faris.faris2dot import Faris2Dot
from faris.linguistic import *
from faris.philosophical import *
from faris.knowledge.mind import MentalState

from pattern.en import parsetree, wordnet, mood, INDICATIVE
from faris import Faris

# class En2Faris(Processor):
#     def __init__(self) -> None:
#         super().__init__()
#         self.faris = Faris()

text = 'The ugly cats sat on the mat.'

tree = parsetree(text, relations=True, lemmata=True)

# en2faris = En2Faris()
faris = Faris()

main_mind = faris.mind

for sentence in tree:

    doers = []
    receivers = []
    actions = []
    places = []

    prep = None
    subs_prep = {}
    substances = []

    for chunk in sentence.chunks:
        synset = 0
        defined = False
        nbr = 1
        adj = []

        for word in chunk.words:
            lemma = word.lemma
            type = word.type
            print(type)
            if type == 'DT':
                if lemma == 'the':
                    defined = True
            elif type == 'JJ':
                synset = wordnet.synsets(word, pos=wordnet.ADJECTIVE)[0]
                quality = Quality(Adjective(synset.id))
                adj.append(quality)

            elif type in ['NNS', 'NN']:
                synset = wordnet.synsets(word, pos=wordnet.NOUN)[0]
                noun = Noun(synset.id)
                if defined:
                    noun.set_defined()
                    defined = False
                if 'female' in synset.gloss:
                    noun.set_gender(Gender.FEMININE)
                elif 'male' in synset.gloss:
                    noun.set_gender(Gender.MASCULINE)
                substance = Substance(noun)
                if type == 'NNS':
                    plural_quant = Quantity()
                    plural_quant.set_plural()
                    substance.set_quantity(plural_quant)
                for quality in adj:
                    substance.add_quality(quality)
                adj = []

                if prep:
                    subs_prep[prep].append(faris.get_substance(substance))
                else:
                    substances.append(faris.get_substance(substance))
                
            elif type in ['VBD']:
                synset = wordnet.synsets(word, pos=wordnet.VERB)[0]
                verb = Verb(synset.id)
                if type == 'VBD':
                    verb.set_tense(Tense.PAST)
                action = Action(verb)
                actions.append(action)
            
            elif type in ['IN']:
                prep = lemma
                if prep not in subs_prep:
                    subs_prep[prep] = []

        if chunk.type == 'NP':
            if 'on' in subs_prep:
                for substance in subs_prep['on']:
                    place = Place(relation=RelationPlace.ABOVE)
                    place.add_relative(substance)
                    places.append(place)
                prep = None
                subs_prep = []
            if len(substances):
                substance = substances.pop()
                if chunk.role == 'SBJ':
                    doers.append(substance)
                elif chunk.role == 'OBJ':
                    receivers.append(substance)
    
    the_mood = mood(sentence)

    if the_mood == INDICATIVE:
        for action in actions: 
            if len(doers):
                action.add_conjuncted_doers(set(doers))
            if len(receivers):
                action.add_conjuncted_receivers(set(doers))
            for place in places:
                action.add_place(place)

            main_mind.add_thought(MentalState.FACT, action)



faris2dot = Faris2Dot()

faris.process(faris2dot)


with open('d.dot', 'w') as f:
    f.write(faris2dot.graphviz)
