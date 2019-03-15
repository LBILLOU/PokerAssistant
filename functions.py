import math
from classes import *
from collections import Counter

def chenFormula(cardA, cardB):
    # http://www.thepokerbank.com/strategy/basic/starting-hand-selection/chen-formula/
    # Initializing score
    chenScore = 0
    # Sorting cards
    if cardA.value > cardB.value:
        highCard = cardA
        lowCard = cardB
    else:
        highCard = cardB
        lowCard = cardA
    # High Card Bonus
    if highCard.value == 14:
        chenScore += 10
    elif highCard.value == 13:
        chenScore += 8
    elif highCard.value == 12:
        chenScore += 7
    elif highCard.value == 11:
        chenScore += 6
    else:
        chenScore += highCard.value / 2
    # Pair Bonus
    if highCard.value == lowCard.value:
        chenScore *= 2
    # Same Suit Bonus
    if highCard.suit == lowCard.suit:
        chenScore += 2
    # Cards Gap Malus
    if highCard.value - lowCard.value - 1 <= 0:
        chenScore = chenScore
    elif highCard.value - lowCard.value - 1 <= 1:
        chenScore -= 1
    elif highCard.value - lowCard.value - 1 <= 2:
        chenScore -= 2
    elif highCard.value - lowCard.value - 1 <= 3:
        chenScore -= 4
    else:
        chenScore -= 5
    # Possible Straight Bonus
    if highCard.value < 12:
        if highCard.value - lowCard.value - 1 <= 1:
            chenScore += 1
    # Round Score Up
    chenScore = math.ceil(chenScore)
    # Return Score
    return chenScore

def chen2rank(chenScore):
    # Function to convert chen score to a rank from 0 to 7
    if chenScore >= 12:
        return 7
    elif chenScore >= 10:
        return 6
    elif chenScore == 9:
        return 5
    elif chenScore == 8:
        return 4
    elif chenScore == 7:
        return 3
    elif chenScore == 6:
        return 2
    elif chenScore == 5:
        return 1
    else:
        return 0

def checkPlayersHandRanking(player):
    if player.hand1 and player.hand2:
        player.handRank = chen2rank(chenFormula(player.hand1[0], player.hand2[0]))
    else:
        player.handRank = int()
    return True

def btn2card(btn):
    # Generate card from Button
    if len(btn['text']) == 2:
        value = btn['text'][0]
    elif len(btn['text']) == 3:
        value = btn['text'][0:2]
    else:
        return ''
    # Managing transcodification
    if value == 'A':
        value = 14
    elif value == 'K':
        value = 13
    elif value == 'Q':
        value = 12
    elif value == 'J':
        value = 11
    else:
        value = int(value)
    suit = btn['text'][-1]
    # Managing transcodification
    if suit == '♥':
        suit = 'H'
    elif suit == '♣':
        suit = 'C'
    elif suit == '♦':
        suit = 'D'
    elif suit == '♠':
        suit = 'S'
    return Card(value, suit)

def createCardsToCheck(player,board):
    allSlots = [player.hand1, player.hand2, board.flop1, board.flop2, board.flop3, board.turn, board.river]
    # Remove empty slot
    cardSlots = [elem for elem in allSlots if elem != []]
    # Turn list of list into list
    cardsInPlay = [card for cardList in cardSlots for card in cardList]
    return cardsInPlay

def checkPokerCombination(player, board, deck):
    twoPairs, twoPairsOs = check2Pairs(player, board, deck)
    pair, pairOs = checkPair(player, board, deck)
    hc, hcOs = checkHighCard(player, board, deck)
    return twoPairs, twoPairsOs, pair, pairOs, hc, hcOs

def checkHighCard(player, board, deck):
    cardsInPlay = createCardsToCheck(player,board)
    if cardsInPlay == []:
        print('>>> checkHighCard : False')
        return False, False
    else:
        # Sorting cards from high to low
        cardsInPlay.sort(key=lambda card: card.value, reverse=True)
        highCard = cardsInPlay[0]
        outs = checkHighCardOuts(deck, highCard)
        print('>>> checkHighCard : ', end = '')
        print(highCard)
        print('>>> checkHighCardOuts : ', end = '')
        print(outs)
    return highCard, outs

def checkHighCardOuts(deck, highCard):
    outs = []
    for i in range(len(deck.cards)):
        if deck.cards[i].value >= highCard.value:
            outs.append(deck.cards[i])
    return outs

def checkPair(player, board, deck):
    cardsInPlay = createCardsToCheck(player,board)
    if len(cardsInPlay) < 2:
        print('>>> checkPair : False')
        return False, False
    else:
        cardsInPlay.sort(key=lambda card: card.value, reverse=True)
        for i in range(len(cardsInPlay)-1):
            if cardsInPlay[i].value == cardsInPlay[i+1].value:
                pair = [cardsInPlay[i], cardsInPlay[i+1]]
                outs = checkPairOuts(player, board, deck, pair)
                print('>>> checkPair : ', end = '')
                print(pair)
                print('>>> checkPairOuts : ', end = '')
                print(outs)
                return pair, outs
        print('>>> checkPair : False')
        return False, False

def checkPairOuts(player, board, deck, pair):
    outs = []
    cardsInPlay = createCardsToCheck(player,board)
    # Seeking three of a kind
    for card in deck.cards:
        if card.value == pair[0].value:
            outs.append(card)
        # Seeking second pair
        for kard in cardsInPlay:
            if card.value == kard.value:
                outs.append(card)
    # Removing duplicates in outs
    outs = list(set(outs))
    # Sorting outs
    outs.sort(key=lambda card: card.value, reverse=True)
    return outs

def check2Pairs(player, board, deck):
    cardsInPlay = createCardsToCheck(player,board)
    if len(cardsInPlay) < 4:
        print('>>> check2Pairs : False')
        return False, False
    else:
        twoPairs = []
        cardsInPlay.sort(key=lambda card: card.value, reverse=True)
        for i in range(len(cardsInPlay)-1):
            if cardsInPlay[i].value == cardsInPlay[i+1].value:
                twoPairs.append(cardsInPlay[i])
                twoPairs.append(cardsInPlay[i+1])
        # Removing duplicate pairs when 3 of a kind available for instance
        twoPairs = list(set([i for i in twoPairs if twoPairs.count(i)==1]))
        # All available pairs sorted
        twoPairs.sort(key=lambda card: card.value, reverse=True)
        # Return False if only one pair
        if len(twoPairs) < 4:
            print('>>> check2Pairs : False')
            return False, False
        # Else keep the 2 best pairs
        else:
            twoPairs = twoPairs[:4]
            outs = check2PairsOuts(twoPairs, deck)
            print('>>> check2Pairs : ', end = '')
            print(twoPairs)
            print('>>> check2PairsOuts : ', end = '')
            print(outs)
        return twoPairs, outs

def check2PairsOuts(twoPairs, deck):
    outs = []
    # Seeking "Full" combination -> cards with same value as any of the pairs
    for card in deck.cards:
        if card.value == twoPairs[0].value or card.value == twoPairs[2].value:
            outs.append(card)
    return outs


#
##
###
####
#####
