# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.


def question2():
    answerDiscount = 0.9
    # The agent will always end up in the intended successor state.
    # This will encourage the optimal policy to attempt to cross the bridge.
    answerNoise = 0.0
    return answerDiscount, answerNoise


def question3a():
    # The agent values immediate rewards more than future rewards as preferencing for the close exit.
    answerDiscount = 0.9
    # The agent wants to make more deliberate moves.
    answerNoise = 0.1
    # The agent wants to reach a terminal state quickly.
    answerLivingReward = -5.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3b():
    # The agent values future rewards less compared to immediate rewards.
    # as it is more cautious and less willing to risk negative payoffs from the cliff.
    answerDiscount = 0.1
    # The agent wants to make more deliberate moves.
    answerNoise = 0.1
    # The agent wants to reach a terminal state quickly but is not too strong
    # because it wants to balance reaching the close exit while avoiding the cliff.
    answerLivingReward = -0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3c():
    # The agent values future rewards as it is willing to take the risk of the cliff
    # in order to reach the higher payoff of the distant exit.
    answerDiscount = 0.9
    # The agent wants to make more deliberate moves.
    answerNoise = 0.1
    # The agent wants to balance reaching the distant exit while accepting some negative rewards along the way.
    answerLivingReward = -0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3d():
    # The agent values future rewards more compared to immediate rewards.
    # as it is willing to take the longer path to maximize the higher payoff while avoiding the cliff.
    answerDiscount = 0.9
    # The agent wants to make more deliberate moves.
    answerNoise = 0.1
    # The agent wants to take the longer path to the distant exit while avoiding the cliff.
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3e():
    # The agent wants to avoid the exits and the cliff to maximize long-term rewards.
    answerDiscount = 0.9
    # The agent wants to make more deliberate moves.
    answerNoise = 0.1
    # The agent continuously receives high rewards for remaining in non-terminal states.
    answerLivingReward = 500
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question8():
    answerEpsilon = None
    answerLearningRate = None
    return "NOT POSSIBLE"
    # If not possible, return 'NOT POSSIBLE'


if __name__ == "__main__":
    print("Answers to analysis questions:")
    import analysis

    for q in [q for q in dir(analysis) if q.startswith("question")]:
        response = getattr(analysis, q)()
        print("  Question %s:\t%s" % (q, str(response)))
