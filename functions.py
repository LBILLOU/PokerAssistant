import math
from classes import *
from collections import Counter

# Function to transcode a cardButton clicked into a card using btn text
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

# Chen formula used to set plyer's hand ranking
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

# Function to convert Chen score (-1 to 20) to rank (0 to 10)
def chen2rank(chenScore):
    # Function to convert chen score to a rank from 0 to 7
    if chenScore >= 12:
        return 10
    elif chenScore >= 10:
        return 9
    elif chenScore == 9:
        return 8
    elif chenScore == 8:
        return 7
    elif chenScore == 7:
        return 6
    elif chenScore == 6:
        return 5
    elif chenScore == 5:
        return 4
    elif chenScore == 4:
        return 3
    elif chenScore == 3:
        return 2
    elif chenScore == 2:
        return 1
    else:
        return 0

# Function to define player's hand rankind
def definePlayersHandRanking(player):
    if player.hand1 and player.hand2:
        player.handRank = chen2rank(chenFormula(player.hand1[0], player.hand2[0]))
    else:
        player.handRank = int()
    return True

# Function that generate a list of cards to evaluate (removing empty slots)
def createCardsToCheck(player,board):
    allSlots = [player.hand1, player.hand2, board.flop1, board.flop2, board.flop3, board.turn, board.river]
    # Remove empty slot
    cardSlots = [elem for elem in allSlots if elem != []]
    # Turn list of list into list
    cardsInPlay = [card for cardList in cardSlots for card in cardList]
    return cardsInPlay

# Function that return a dict in order to store outs for all combinations
def createOutsList():
    outsList = [ [], # 0 -> outs to get a Royal flush
            [],  # 1 -> outs to get a Straight Flush (or higher)
            [],  # 2 -> outs to get a 4 of a Kind
            [],  # 3 -> outs to get a Full house (or higher)
            [],  # 4 -> outs to get a Flush (or higher)
            [],  # 5 -> outs to get a Straight (or higher)
            [],  # 6 -> outs to get a 3 of a Kind (or higher)
            [],  # 7 -> outs to get 2 pairs (or higher)
            [],  # 8 -> outs to get a Pair (or higher)
            []  # 9 -> outs to get a Higher Card
            ]
    return outsList

# Function which returns highest combination and outs
def checkPokerCombination(player, board, deck):
    bestCombination = []
    combinationsFunctionsList = [isRoyalFlush, isStraightFlush, is4ofaKind, isFullHouse, isFlush, isStraight, is3ofaKind, is2Pairs, isPair, isHighCard]
    outsFunctionsList = [royalFlushOuts, straightFlushOuts, fourOfAKindOuts, fullHouseOuts, flushOuts, straightOuts, threeOfAKindOuts, twoPairsOuts, pairOuts, highCardOuts]
    # outsFunctionsList = [outs for royal flush, ..., outs for high card]
    for i in range(len(combinationsFunctionsList)):
        functionResult = combinationsFunctionsList[i](player, board, deck)
        if functionResult is False:
            bestCombination.append(False)
        else:
            bestCombination.append(functionResult)
            outs = outsFunctionsList[i](player, board, deck, bestCombination[-1])
            #print(bestCombination)
            #print(outs)
            return bestCombination, outs
    print('ERROR : No poker combination found (no cards given)')
    return False

# Functions that return generic cards combinations
def searchForPairs(cardslist):
    # Funtion that returns all pairs from a given cardsList
    # If no pair possible return false
    if len(cardslist) < 2:
        return False
    else:
        pairs = list()
        # Sorting cards from high to low
        cardslist.sort(key=lambda card: card.value, reverse=True)
        # Adding all pairs to the return variable
        for i in range(len(cardslist)-1):
            if cardslist[i].value == cardslist[i+1].value:
                pairs.append(cardslist[i])
                pairs.append(cardslist[i+1])
        # If no pair return false
        if len(pairs) < 2:
            return False
        else:
            # Removing "false" pairs in case of 3/4 of a kind
            pairs2 = pairs.copy()
            # Creating dict w/ card value and count
            counter = Counter(card.value for card in pairs)
            # Remove cards with same value appearing more than twice in list
            for key, value in counter.items():
                if value > 2:
                    for card in pairs:
                        if card.value == key:
                            pairs2.remove(card)
            return pairs2

def searchFor3ofaKind(cardslist):
    # Funtion that returns all "3 of a kind" from a given cardsList
    # If no "3 of a kind" possible return false
    if len(cardslist) < 3:
        return False
    else:
        threeofakind = list()
        # Sorting cards from high to low
        cardslist.sort(key=lambda card: card.value, reverse=True)
        # Adding all "3 of a kind" to the return variable
        for i in range(len(cardslist)-2):
            if cardslist[i].value == cardslist[i+1].value == cardslist[i+2].value:
                threeofakind.append(cardslist[i])
                threeofakind.append(cardslist[i+1])
                threeofakind.append(cardslist[i+2])
        # If no "3 of a kind" return false
        if len(threeofakind) < 3:
            return False
        else:
            # Removing "false" pairs in case of 3/4 of a kind
            threeofakind2 = threeofakind.copy()
            # Creating dict w/ card value and count
            counter = Counter(card.value for card in threeofakind)
            # Remove cards with same value appearing more than twice in list
            for key, value in counter.items():
                if value > 3:
                    for card in threeofakind:
                        if card.value == key:
                            threeofakind2.remove(card)
            return threeofakind2

def searchFor4ofaKind(cardslist):
    # Funtion that returns all "4 of a kind" from a given cardsList
    # If no "4 of a kind" possible return false
    if len(cardslist) < 4:
        return False
    else:
        fourofakind = list()
        # Sorting cards from high to low
        cardslist.sort(key=lambda card: card.value, reverse=True)
        # Adding all "4 of a kind" to the return variable
        for i in range(len(cardslist)-3):
            if cardslist[i].value == cardslist[i+1].value == cardslist[i+2].value == cardslist[i+3].value:
                fourofakind.append(cardslist[i])
                fourofakind.append(cardslist[i+1])
                fourofakind.append(cardslist[i+2])
                fourofakind.append(cardslist[i+3])
        # If no "4 of a kind" return false
        if len(fourofakind) < 4:
            return False
        else:
            return fourofakind

def searchForStraight(cardslist):
    # Function that returns all (can be more than 5) straight cards from a given cardsList
    # If no straight possible return false
    if len(cardslist) < 5:
        return False
    else:
        straight = list()
        # Issue with pairs/3ofakind, keeping card with most common suit the cardsList
        #for later combination of straight and flush comparaison to evaluate straight flush
        # Creating dict w/ card suit and count to manage pairs/3ofaKind
        counter = Counter(card.suit for card in cardslist)
        mostSuit = '' # Setting default value to Hearts
        # Defining most common suit in case of a flush still possible
        for key, value in counter.items():
            if len(cardslist) == 5 and value >= 3:
                mostSuit = key
            elif len(cardslist) == 6 and value >= 4:
                mostSuit = key
            elif len(cardslist) == 7 and value >= 5:
                mostSuit = key
            else:
                pass
        cardslist.sort(key=lambda card: card.value, reverse=True)
        cardslist2 = cardslist.copy()
        # Removing duplicate cards (with same value), keeping most common suit of card if possible
        for i in range(len(cardslist)-1):
            if cardslist[i].value == cardslist[i+1].value:
                if mostSuit and cardslist[i+1].suit == mostSuit:
                    cardslist2.remove(cardslist[i])
                else:
                    cardslist2.remove(cardslist[i+1])
        # Sorting cards from high to low
        cardslist2.sort(key=lambda card: card.value, reverse=True)
        # Looking for straight
        for i in range(len(cardslist2)-4):
            if cardslist2[i].value == cardslist2[i+1].value+1 == cardslist2[i+2].value+2 == cardslist2[i+3].value+3 == cardslist2[i+4].value+4:
                temp = [cardslist2[i], cardslist2[i+1], cardslist2[i+2], cardslist2[i+3], cardslist2[i+4]]
                for card in temp:
                    if card not in straight:
                        straight.append(card)
                return straight
        return False

def searchForFlush(cardslist):
    # Function that returns all (can be more than 5) Flush cards from a given cardsList
    # If no Flush possible return false
    if len(cardslist) < 5:
        return False
    else:
        flush = list()
        # Creating dict w/ card suit and count
        counter = Counter(card.suit for card in cardslist)
        flushSuit = ''
        for key, value in counter.items():
            if value >= 5:
                flushSuit = key
                for card in cardslist:
                    if card.suit == flushSuit:
                        flush.append(card)
                # Sorting cards from high to low
                flush.sort(key=lambda card: card.value, reverse=True)
                return flush
        return False

# Functions that return outs in order to hit a specific cards combination
def checkOutsForHighCard(cardslist, deck):
    # Used for High card --> higher cards
    #
    # higher straight (straightCards)
    # higher flush straight (straightCards + flush suit)
    # higher flush (flushCards + flush suit)
    outs = list()
    cardslist.sort(key=lambda card: card.value, reverse=True)
    highCard = cardslist[0]
    for i in range(len(deck.cards)):
        if deck.cards[i].value > highCard.value:
            outs.append(deck.cards[i])
    outs.sort(key=lambda card: card.value, reverse=True)
    return outs

def checkOutsForPair(cardslist, deck):
    outs = list()
    cardslist.sort(key=lambda card: card.value, reverse=True)
    for card in deck.cards:
        for kard in cardslist:
            if card.value == kard.value:
                outs.append(card)
    outs.sort(key=lambda card: card.value, reverse=True)
    return outs

def checkOutsFor3or4ofaKind(cardslist, deck):
    if len(cardslist) < 2:
        return False
    outs = list()
    cardslist.sort(key=lambda card: card.value, reverse=True)
    for card in deck.cards:
        for kard in cardslist:
            if card.value == kard.value:
                outs.append(card)
    outs = list(set(outs))
    outs.sort(key=lambda card: card.value, reverse=True)
    return outs

def checkOutsForStraight(cardslist, deck):
    outs = list()
    cardslist.sort(key=lambda card: card.value, reverse=True)
    cardslist2 = cardslist.copy()
    # Removing eventual pair/3ofakind
    for i in range(len(cardslist)-1):
        if cardslist[i].value == cardslist[i+1].value:
            cardslist2.remove(cardslist[i+1])
    # Need 4 cards at least to create a straight with an out.
    if len(cardslist2) < 4:
        return [] # Equivalent to false
    # Case of a continuous 4 cards straight
    for i in range(len(cardslist2)-3):
        if cardslist2[i].value == cardslist2[i+1].value+1 == cardslist2[i+2].value+2 == cardslist2[i+3].value+3:
            high = cardslist2[i]
            low = cardslist2[i+3]
            for card in deck.cards:
                if card.value == high.value + 1 or card.value == low.value - 1:
                    outs.append(card)
            return outs
    # Case of straight with a missing card
    aboveMissing = Card(2, 'H') # Setting default value to aboveMissing
    for i in range(len(cardslist2)-3):
        # Case 1.111
        if cardslist2[i].value  == cardslist2[i+1].value+2 == cardslist2[i+2].value+3 == cardslist2[i+3].value+4:
            aboveMissing = cardslist2[i]
        # Case 11.11
        elif cardslist2[i].value == cardslist2[i+1].value+1 == cardslist2[i+2].value+3 == cardslist2[i+3].value+4:
            aboveMissing = cardslist2[i+1]
        # Case 111.1
        elif cardslist2[i].value == cardslist2[i+1].value+1 == cardslist2[i+2].value+2 == cardslist2[i+3].value+4:
            aboveMissing = cardslist2[i+2]

        for card in deck.cards:
            if card.value == aboveMissing.value - 1:
                outs.append(card)
        return outs

def checkOutsForFlush(cardslist, deck):
    # high, pair, 2pairs, 3ofakind, straight -> flush ?
    if len(cardslist) < 4:
        return [] # Equivalent to False
    outs = list()
    # Searching for 4 cards of same suit
    flushSuit = ''
    counter = Counter(card.suit for card in cardslist)
    for key, value in counter.items():
        if value == 4:
            flushSuit = key
    # Adding same suit cards to outs
    if flushSuit:
        for card in deck.cards:
            if card.suit == flushSuit:
                outs.append(card)
    # Sorting cards from high to low
    outs.sort(key=lambda card: card.value, reverse=True)
    return outs

# Functions that check if a specific poker combination is found
# (using the above searchForXxx generic functions)
def isHighCard(player, board, deck):
    cardsInPlay = createCardsToCheck(player,board)
    if cardsInPlay == []:
        return False
    else:
        # Sorting cards from high to low
        cardsInPlay.sort(key=lambda card: card.value, reverse=True)
        highCard = cardsInPlay[0]
        return highCard

def isPair(player, board, deck):
    allPairs = searchForPairs(createCardsToCheck(player,board))
    if allPairs != False:
        if len(allPairs) >= 2:
            bestPair = allPairs[:2]
            return bestPair
    return False

def is2Pairs(player, board, deck):
    allPairs = searchForPairs(createCardsToCheck(player,board))
    if allPairs != False:
        if len(allPairs) >= 4:
            best2Pairs = allPairs[:4]
            return best2Pairs
    return False

def is3ofaKind(player, board, deck):
    all3ofaKind = searchFor3ofaKind(createCardsToCheck(player,board))
    if all3ofaKind != False:
        if len(all3ofaKind) >= 3:
            best3ofaKind = all3ofaKind[:3]
            return best3ofaKind
    return False

def isStraight(player, board, deck):
    allStraight = searchForStraight(createCardsToCheck(player,board))
    if allStraight != False:
        straight = allStraight[:5]
        return straight
    return False

def isFlush(player, board, deck):
    allFlush = searchForFlush(createCardsToCheck(player,board))
    if allFlush !=False:
        flush = allFlush[:5]
        return flush
    return False

def isFullHouse(player, board, deck):
    pair = isPair(player, board, deck)
    threeOfAKind = searchFor3ofaKind(createCardsToCheck(player,board))
    if pair and threeOfAKind:
        fullHouse = []
        fullHouse += threeOfAKind
        fullHouse += pair
        return fullHouse
    # Case of multiple 3 of a kind on board
    elif threeOfAKind:
        if len(threeOfAKind) >= 6:
            fullHouse2 = []
            fullHouse2 = threeOfAKind[:5]
            return fullHouse2
        else:
            return False
    else:
        return False

def is4ofaKind(player, board, deck):
    all4ofaKind = searchFor4ofaKind(createCardsToCheck(player,board))
    if all4ofaKind != False:
        return all4ofaKind
    return False

def isStraightFlush(player, board, deck):
    allStraight = searchForStraight(createCardsToCheck(player,board))
    allFlush = searchForFlush(createCardsToCheck(player,board))
    if allStraight != False and allFlush !=False:
        # Case len(allFlush) == 7
        if len(allFlush) == 7:
            straightFlush = allStraight[:5]
            return straightFlush
        # Case len(allFlush) == 5 or 6
        elif len(allFlush) == 6 or len(allFlush) == 5:
            for i in [5, 6]: # 5 ou 6
                for j in [5, 6, 7]: # 5 6 ou 7
                    if allFlush[i-5:i] == allStraight[j-5:j]:
                        straightFlush = allStraight[j-5:j]
                        return straightFlush
        return False
    else:
        return False

def isRoyalFlush(player, board, deck):
    straightFlush = isStraightFlush(player, board, deck)
    if straightFlush != False:
        if straightFlush[0].value == 14:
            return straightFlush
    return False

# Functions that return outs for a given poker combination
# (using the above searchOutsForXxx generic functions)
def highCardOuts(player, board, deck, currentHC):
    outs = createOutsList()
    # Seeking higher card
    highCard = list()
    highCard.append(currentHC)
    outs[9] = checkOutsForHighCard(highCard, deck)
    # Seeking pair
    cardsInPlay = createCardsToCheck(player,board)
    outs[8] = checkOutsForPair(cardsInPlay, deck)
    # Seeking straight
    outs[5] = checkOutsForStraight(cardsInPlay, deck)
    return outs

def pairOuts(player, board, deck, currentP):
    outs = createOutsList()
    cardsInPlay = createCardsToCheck(player,board)
    cardsLeft = [card for card in cardsInPlay if card not in currentP]
    higherCardsLeft = [card for card in cardsLeft if card.value > currentP[0].value]
    # Seeking a higher pair
    outs[8] = checkOutsForPair(higherCardsLeft, deck)
    # Seeking a second pair
    outs[7] = checkOutsForPair(cardsLeft, deck)
    # Seeking 3 of a kind
    outs[6] = checkOutsFor3or4ofaKind(currentP, deck)
    # Seeking straight
    outs[5] = checkOutsForStraight(cardsInPlay, deck)
    # Seeking flush
    outs[4] = checkOutsForFlush(cardsInPlay, deck)
    return outs

def twoPairsOuts(player, board, deck, current2P):
    outs = createOutsList()
    cardsInPlay = createCardsToCheck(player,board)
    cardsLeft = [card for card in cardsInPlay if card not in current2P]
    higherCardsLeft = [card for card in cardsLeft if card.value > current2P[-1].value]
    # Seeking higher second pair
    outs[7] = checkOutsForPair(higherCardsLeft, deck)
    # Seeking straight
    outs[5] = checkOutsForStraight(cardsInPlay, deck)
    # Seeking flush
    outs[4] = checkOutsForFlush(cardsInPlay, deck)
    # Seeking full house
    outs[3] = checkOutsFor3or4ofaKind(current2P, deck)
    return outs

def threeOfAKindOuts(player, board, deck, current3K):
    outs = createOutsList()
    cardsInPlay = createCardsToCheck(player,board)
    cardsLeft = [card for card in cardsInPlay if card not in current3K]
    # Seeking straight
    outs[5] = checkOutsForStraight(cardsInPlay, deck)
    # Seeking flush
    outs[4] = checkOutsForFlush(cardsInPlay, deck)
    # Seeking full house
    outs[3] = checkOutsForPair(cardsLeft, deck)
    # Seeking 4 of a kind
    outs[2] = checkOutsFor3or4ofaKind(current3K, deck)
    return outs

def straightOuts(player, board, deck, currentS):
    outs = createOutsList()
    cardsInPlay = createCardsToCheck(player,board)
    # Seeking higher straight
    outs[5] = checkOutsForHighCard(currentS, deck)[-4:]
    # Seeking flush
    outs[4] = checkOutsForFlush(cardsInPlay, deck)
    # Seeking straight flush
    outs[1] = checkOutsForFlush(currentS, deck)
    outs[1] = [card for card in outs[1] if card.value <= currentS[0].value]
    outs[1] = [card for card in outs[1] if card.value >= currentS[-1].value]
    # Seeking royal flush
    if currentS[0].value == 13 and outs[4]:
        outs[0] = [card for card in deck.cards if card.value > currentS[0].value and card.suit == currentS[0].suit]
    return outs

def flushOuts(player, board, deck, currentF):
    outs = createOutsList()
    # Seeking higher  flush
    outs[4] = checkOutsForHighCard(currentF, deck)[-4:]
    # Seeking straight flush
    outs[1] = checkOutsForStraight(currentF, deck)
    outs[1] = [card for card in outs[1] if card.suit == currentF[0].suit]
    # Seeking royal flush
    if currentF[0].value == 13 and outs[1]:
        outs[0] = [card for card in deck.cards if card.value > currentF[0].value and card.suit == currentF[0].suit]
    return outs

def fullHouseOuts(player, board, deck, currentFH):
    outs = createOutsList()
    cardsInPlay = createCardsToCheck(player,board)
    cardsWithout3oaK = [card for card in cardsInPlay if card not in currentFH[:3]]
    # Seeking higher full house
    outs[3] = checkOutsFor3or4ofaKind(cardsWithout3oaK, deck)
    # Seeking 4 of a kind
    outs[2] = checkOutsFor3or4ofaKind(currentFH[:3], deck)
    return outs

def fourOfAKindOuts(player, board, deck, current4K):
    outs = createOutsList()
    # No outs when having 4 of a kind
    return outs

def straightFlushOuts(player, board, deck, currentSF):
    outs = createOutsList()
    # Seeking higher straight flush
    outs[1] = checkOutsForHighCard(currentSF, deck)[-4:]
    # Seeking royal flush
    if currentSF[0].value == 13:
        outs[0] = [card for card in deck.cards if card.value > currentSF[0].value and card.suit == currentSF[0].suit]
    return outs

def royalFlushOuts(player, board, deck, currentRF):
    outs = createOutsList()
    # No outs for the best combination in the game
    return outs

#########################
#########################

# WARNING couleur
# WARNING suite

#outs = list(set(outs))
#outs.sort(key=lambda card: card.value, reverse=True)
#
##
###
####
#####
