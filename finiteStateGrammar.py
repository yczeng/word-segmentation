''' Goal: to create a visual of mother's speech's finite state grammar'''


from pygraphviz import *
from transitions import Machine
import random
from helpers import *
from transitions.extensions import GraphMachine as Machine


def finiteStateGrammar(utteranceArray):
    '''
    Scans every syllable against syllable in memory. If the same, add to lexicon with weight.

    Args:
        utteranceArray: an array of String utterances
    Returns:
        a set of syllables with sets of syllables with frequencies.
        maps transitional counts for every syllable

    '''

    probabilities = {}
    for count, eachUtterance in enumerate(utteranceArray):
        utterance = list(filter(None, eachUtterance.split("S")))
        probabilities = processUtterance(utterance, probabilities)

    return probabilities

def processUtterance(utterance, probabilities):

    for i in range(2, len(utterance)):

        previousSyllable = utterance[i-1]
        currentSyllable = utterance[i]

        if previousSyllable in probabilities:
            # check if syllable already given

            if currentSyllable in probabilities[previousSyllable]:
                probabilities[previousSyllable][currentSyllable] += 1
            else:
                probabilities[previousSyllable][currentSyllable] = 1
        else:
            probabilities[previousSyllable] = {currentSyllable: 1}

    return probabilities

# # This doesn't work yet. Also is it worth visualizing?
# class finiteStateMachine():

#     utterances = getArrayFromTextFile('data/splitByUtterance.txt', 0)
#     processedData = finiteStateGrammar(utterances)
#     states = [i for i in processedData]
#     print(states)

#     def __init__(self):
#         # Initialize the state machine
#         self.machine = Machine(self, finiteStateMachine.states, initial='solid')

#         for firstSyllable in processedData:
#             print(firstSyllable)
#             for secondSyllable in processedData[firstSyllable]:
#                 count = 0
#                 print("doing a syllable")
#                 while count < processedData[firstSyllable][secondSyllable]:
#                     self.machine.add_transition(firstSyllable, secondSyllable)
#                     count += 1

#         self.get_graph().draw('my_state_diagram.png', prog='dot')