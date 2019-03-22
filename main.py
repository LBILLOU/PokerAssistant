#!/usr/local/bin/python3
from classes import *
from functions import *
from tkinter import *

deck_one = Deck()
player_one = Player('Player 1')
board_one = Board()

window = Tk()
window.title('Poker Assistant')

# Colors
redCard = '#ff0000'
blackCard = '#2d2d2d'
hand = '#03018c'
flop = '#54008c'
turn = '#89008c'
river = '#c100ab'
BLACK = '#000000'

selectionPane = Frame(window)
playerPane = Frame(window)
cardsInPlayPane = Frame(window)
sideBar = Frame(window)
combinationPane = Frame(window)

# SELECTION PANE UI
# Hearts ♥♥♥♥♥♥♥
btn14H = Button(selectionPane,text='A♥',command=lambda:selectionPaneClicked(btn14H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn13H = Button(selectionPane,text='K♥',command=lambda:selectionPaneClicked(btn13H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn12H = Button(selectionPane,text='Q♥',command=lambda:selectionPaneClicked(btn12H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn11H = Button(selectionPane,text='J♥',command=lambda:selectionPaneClicked(btn11H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn10H = Button(selectionPane,text='10♥',command=lambda:selectionPaneClicked(btn10H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn9H = Button(selectionPane,text='9♥',command=lambda:selectionPaneClicked(btn9H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn8H = Button(selectionPane,text='8♥',command=lambda:selectionPaneClicked(btn8H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn7H = Button(selectionPane,text='7♥',command=lambda:selectionPaneClicked(btn7H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn6H = Button(selectionPane,text='6♥',command=lambda:selectionPaneClicked(btn6H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn5H = Button(selectionPane,text='5♥',command=lambda:selectionPaneClicked(btn5H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn4H = Button(selectionPane,text='4♥',command=lambda:selectionPaneClicked(btn4H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn3H = Button(selectionPane,text='3♥',command=lambda:selectionPaneClicked(btn3H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn2H = Button(selectionPane,text='2♥',command=lambda:selectionPaneClicked(btn2H,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn14H.grid(row=0,column=0)
btn13H.grid(row=1,column=0)
btn12H.grid(row=2,column=0)
btn11H.grid(row=3,column=0)
btn10H.grid(row=4,column=0)
btn9H.grid(row=6,column=0)
btn8H.grid(row=7,column=0)
btn7H.grid(row=8,column=0)
btn6H.grid(row=9,column=0)
btn5H.grid(row=10,column=0)
btn4H.grid(row=11,column=0)
btn3H.grid(row=12,column=0)
btn2H.grid(row=13,column=0)
# Clubs ♣♣♣♣♣♣♣
btn14C = Button(selectionPane,text='A♣',command=lambda:selectionPaneClicked(btn14C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn13C = Button(selectionPane,text='K♣',command=lambda:selectionPaneClicked(btn13C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn12C = Button(selectionPane,text='Q♣',command=lambda:selectionPaneClicked(btn12C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn11C = Button(selectionPane,text='J♣',command=lambda:selectionPaneClicked(btn11C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn10C = Button(selectionPane,text='10♣',command=lambda:selectionPaneClicked(btn10C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn9C = Button(selectionPane,text='9♣',command=lambda:selectionPaneClicked(btn9C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn8C = Button(selectionPane,text='8♣',command=lambda:selectionPaneClicked(btn8C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn7C = Button(selectionPane,text='7♣',command=lambda:selectionPaneClicked(btn7C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn6C = Button(selectionPane,text='6♣',command=lambda:selectionPaneClicked(btn6C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn5C = Button(selectionPane,text='5♣',command=lambda:selectionPaneClicked(btn5C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn4C = Button(selectionPane,text='4♣',command=lambda:selectionPaneClicked(btn4C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn3C = Button(selectionPane,text='3♣',command=lambda:selectionPaneClicked(btn3C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn2C = Button(selectionPane,text='2♣',command=lambda:selectionPaneClicked(btn2C,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn14C.grid(row=0,column=1)
btn13C.grid(row=1,column=1)
btn12C.grid(row=2,column=1)
btn11C.grid(row=3,column=1)
btn10C.grid(row=4,column=1)
btn9C.grid(row=6,column=1)
btn8C.grid(row=7,column=1)
btn7C.grid(row=8,column=1)
btn6C.grid(row=9,column=1)
btn5C.grid(row=10,column=1)
btn4C.grid(row=11,column=1)
btn3C.grid(row=12,column=1)
btn2C.grid(row=13,column=1)
# Diamonds ♦♦♦♦♦♦♦
btn14D = Button(selectionPane,text='A♦',command=lambda:selectionPaneClicked(btn14D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn13D = Button(selectionPane,text='K♦',command=lambda:selectionPaneClicked(btn13D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn12D = Button(selectionPane,text='Q♦',command=lambda:selectionPaneClicked(btn12D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn11D = Button(selectionPane,text='J♦',command=lambda:selectionPaneClicked(btn11D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn10D = Button(selectionPane,text='10♦',command=lambda:selectionPaneClicked(btn10D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn9D = Button(selectionPane,text='9♦',command=lambda:selectionPaneClicked(btn9D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn8D = Button(selectionPane,text='8♦',command=lambda:selectionPaneClicked(btn8D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn7D = Button(selectionPane,text='7♦',command=lambda:selectionPaneClicked(btn7D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn6D = Button(selectionPane,text='6♦',command=lambda:selectionPaneClicked(btn6D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn5D = Button(selectionPane,text='5♦',command=lambda:selectionPaneClicked(btn5D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn4D = Button(selectionPane,text='4♦',command=lambda:selectionPaneClicked(btn4D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn3D = Button(selectionPane,text='3♦',command=lambda:selectionPaneClicked(btn3D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn2D = Button(selectionPane,text='2♦',command=lambda:selectionPaneClicked(btn2D,player_one,board_one,deck_one),width=3,highlightbackground=redCard)
btn14D.grid(row=0,column=2)
btn13D.grid(row=1,column=2)
btn12D.grid(row=2,column=2)
btn11D.grid(row=3,column=2)
btn10D.grid(row=4,column=2)
btn9D.grid(row=6,column=2)
btn8D.grid(row=7,column=2)
btn7D.grid(row=8,column=2)
btn6D.grid(row=9,column=2)
btn5D.grid(row=10,column=2)
btn4D.grid(row=11,column=2)
btn3D.grid(row=12,column=2)
btn2D.grid(row=13,column=2)
# Spades ♠♠♠♠♠♠♠
btn14S = Button(selectionPane,text='A♠',command=lambda:selectionPaneClicked(btn14S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn13S = Button(selectionPane,text='K♠',command=lambda:selectionPaneClicked(btn13S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn12S = Button(selectionPane,text='Q♠',command=lambda:selectionPaneClicked(btn12S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn11S = Button(selectionPane,text='J♠',command=lambda:selectionPaneClicked(btn11S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn10S = Button(selectionPane,text='10♠',command=lambda:selectionPaneClicked(btn10S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn9S = Button(selectionPane,text='9♠',command=lambda:selectionPaneClicked(btn9S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn8S = Button(selectionPane,text='8♠',command=lambda:selectionPaneClicked(btn8S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn7S = Button(selectionPane,text='7♠',command=lambda:selectionPaneClicked(btn7S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn6S = Button(selectionPane,text='6♠',command=lambda:selectionPaneClicked(btn6S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn5S = Button(selectionPane,text='5♠',command=lambda:selectionPaneClicked(btn5S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn4S = Button(selectionPane,text='4♠',command=lambda:selectionPaneClicked(btn4S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn3S = Button(selectionPane,text='3♠',command=lambda:selectionPaneClicked(btn3S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn2S = Button(selectionPane,text='2♠',command=lambda:selectionPaneClicked(btn2S,player_one,board_one,deck_one),width=3,highlightbackground=blackCard)
btn14S.grid(row=0,column=3)
btn13S.grid(row=1,column=3)
btn12S.grid(row=2,column=3)
btn11S.grid(row=3,column=3)
btn10S.grid(row=4,column=3)
btn9S.grid(row=6,column=3)
btn8S.grid(row=7,column=3)
btn7S.grid(row=8,column=3)
btn6S.grid(row=9,column=3)
btn5S.grid(row=10,column=3)
btn4S.grid(row=11,column=3)
btn3S.grid(row=12,column=3)
btn2S.grid(row=13,column=3)
# Player Pane UI
btnPH1 = Button(playerPane,text='-',command=lambda:playersCardClicked(btnPH1,player_one,board_one,deck_one),width=3,highlightbackground=hand)
btnPH2 = Button(playerPane,text='-',command=lambda:playersCardClicked(btnPH2,player_one,board_one,deck_one),width=3,highlightbackground=hand)
btnPH1.grid(row=1,column=0)
btnPH2.grid(row=1,column=1)


lblPName = Label(playerPane,text=player_one.name.upper())
lblPHR = Label(playerPane,text='0')
lblPName.grid(row=0,columnspan=2)
lblPHR.grid(row=2,columnspan=2)

# Cards in Play Pane UI
btnBF1 = Button(cardsInPlayPane,text='-',command=lambda:boardCardClicked(btnBF1,player_one,board_one,deck_one),width=3,highlightbackground=flop)
btnBF2 = Button(cardsInPlayPane,text='-',command=lambda:boardCardClicked(btnBF2,player_one,board_one,deck_one),width=3,highlightbackground=flop)
btnBF3 = Button(cardsInPlayPane,text='-',command=lambda:boardCardClicked(btnBF3,player_one,board_one,deck_one),width=3,highlightbackground=flop)
btnBT = Button(cardsInPlayPane,text='-',command=lambda:boardCardClicked(btnBT,player_one,board_one,deck_one),width=3,highlightbackground=turn)
btnBR = Button(cardsInPlayPane,text='-',command=lambda:boardCardClicked(btnBR,player_one,board_one,deck_one),width=3,highlightbackground=river)
btnBF1.grid(row=1,column=0)
btnBF2.grid(row=1,column=1)
btnBF3.grid(row=1,column=2)
btnBT.grid(row=1,column=3)
btnBR.grid(row=1,column=4)

lblBoardName = Label(cardsInPlayPane,text='BOARD')
lblBoardName.grid(row=0,columnspan=5)
lblBFlop = Label(cardsInPlayPane,text='Flop')
lblBFlop.grid(row=2,column=0,columnspan=3)
lblBTurn = Label(cardsInPlayPane,text='Turn')
lblBTurn.grid(row=2,column=3,columnspan=1)
lblBRiver = Label(cardsInPlayPane,text='River')
lblBRiver.grid(row=2,column=4,columnspan=1)

# Side Bar UI
btnReset = Button(sideBar,text='Reset',command=lambda:resetCardsInPlay(player_one,board_one,deck_one),width=5,highlightbackground=BLACK)
btnReset.grid(row=0,column=0)

# Combination Panu UI
lblRoyalFlush = Label(combinationPane,text='Royal Flush',width=14,anchor=W)
lblStrFlush = Label(combinationPane,text='Straight Flush',width=14,anchor=W)
lbl4oaKind = Label(combinationPane,text='Four of a Kind',width=14,anchor=W)
lblFullHouse = Label(combinationPane,text='Full House',width=14,anchor=W)
lblFlush = Label(combinationPane,text='Flush',width=14,anchor=W)
lblStraight = Label(combinationPane,text='Straight',width=14,anchor=W)
lbl3oaKind = Label(combinationPane,text='Three of a Kind',width=14,anchor=W)
lbl2Pairs = Label(combinationPane,text='Two Pairs',width=14,anchor=W)
lblPair = Label(combinationPane,text='Pair',width=14,anchor=W)
lblHighCard = Label(combinationPane,text='High Card',width=14,anchor=W)
lblSpacing = Label(combinationPane,text='',anchor=W)
lblRoyalFlush.grid(row=0,column=0)
lblStrFlush.grid(row=1,column=0)
lbl4oaKind.grid(row=2,column=0)
lblFullHouse.grid(row=3,column=0)
lblFlush.grid(row=4,column=0)
lblStraight.grid(row=5,column=0)
lbl3oaKind.grid(row=6,column=0)
lbl2Pairs.grid(row=7,column=0)
lblPair.grid(row=8,column=0)
lblHighCard.grid(row=9,column=0)
lblSpacing.grid(row=10,column=0)


selectionPane.pack(side=LEFT,fill=X)
playerPane.pack(side=LEFT,fill=X)
cardsInPlayPane.pack(side=LEFT,fill=X)
combinationPane.pack(side=LEFT,fill=X)
sideBar.pack(side=RIGHT,fill=X)


def refreshUI(player, board, deck):
    definePlayersHandRanking(player)
    # Refreshing cards in play pane
    cardElems = [player_one.hand1, player_one.hand2, board_one.flop1, board_one.flop2, board_one.flop3, board_one.turn, board_one.river]
    uiCardElems = [btnPH1, btnPH2, btnBF1, btnBF2, btnBF3, btnBT, btnBR]
    for i in range(len(uiCardElems)):
        if cardElems[i]:
            uiCardElems[i]['text'] = cardElems[i][0].show()
        else:
            uiCardElems[i]['text'] = ''

    # Refreshing player's hand rank
    lblPHR['text'] = str(player_one.handRank)

    # Refreshing combination pane
    uiCombElems = [lblRoyalFlush, lblStrFlush, lbl4oaKind, lblFullHouse, lblFlush, lblStraight, lbl3oaKind, lbl2Pairs, lblPair, lblHighCard]
    if len(createCardsToCheck(player,board)) >= 7:
        bestCombination, outs = checkPokerCombination(player, board, deck)
        bestCombIndex = len(bestCombination)-1
        for elem in uiCombElems:
            elem['fg']='#0000ff' #BLUE
        uiCombElems[bestCombIndex]['fg']='#00ff00' #GREEN

    elif len(createCardsToCheck(player,board)) >= 1:
        bestCombination, outs = checkPokerCombination(player, board, deck)
        for i in range(len(bestCombination)):
            if bestCombination[i] == False:
                uiCombElems[i]['fg']='#ff8800' #ORANGE
            else:
                uiCombElems[i]['fg']='#00ff00' #GREEN
                for j in range(i+1,len(uiCombElems)):
                    uiCombElems[j]['fg']='#707070' #GREY
    else:
        for elem in uiCombElems:
            elem['fg']='#000000' #BLACK


    # Resetting size dur to MacOS Mojave x pyinstaller button refresh issue
    # https://stackoverflow.com/questions/52529403/button-text-of-tkinter-not-works-in-mojave
    window.geometry(window.geometry())
    return True


def playersCardClicked(btn, player, board, deck):
    # Print error if no card in button
    print('> playersCardClicked : ', end = '')
    print(btn2card(btn))
    definePlayersHandRanking(player)
    cardsInPlayClicked(btn, player, board, deck)
    return True

def boardCardClicked(btn, player, board, deck):
    # Print error if no card in button
    print('> boardCardClicked : ', end = '')
    print(btn2card(btn))
    cardsInPlayClicked(btn, player, board, deck)
    return True

def cardsInPlayClicked(btn, player, board, deck):
    cardsInPlay = [player.hand1, player.hand2, board.flop1, board.flop2, board.flop3, board.turn, board.river]
    # Print error if no card in button
    selectedCard = btn2card(btn)
    for i in range(len(cardsInPlay)):
        if cardsInPlay[i] and selectedCard != '' and selectedCard.value == cardsInPlay[i][0].value and selectedCard.suit == cardsInPlay[i][0].suit:
            # If yes, remove from cardsInPlay and add back to deck
            if i == 0:
                player.hand1.pop()
            elif i == 1:
                player.hand2.pop()
            elif i == 2:
                board.flop1.pop()
            elif i == 3:
                board.flop2.pop()
            elif i == 4:
                board.flop3.pop()
            elif i == 5:
                board.turn.pop()
            elif i == 6:
                board.river.pop()
            deck_one.cards.append(selectedCard)
    #print(len(deck_one.cards))
    refreshUI(player, board, deck)
    return True

def selectionPaneClicked(btn, player, board, deck):
    cardsInPlay = [player.hand1, player.hand2, board.flop1, board.flop2, board.flop3, board.turn, board.river]
    # Checking cardsInPlay integrity, if not then reset all
    for i in range(len(cardsInPlay)):
        if cardsInPlay[i] and cardsInPlay[i][0] != cardsInPlay[i][-1]:
                print("ERROR : cardsInPlay integrity KO")
                player.hand1 = []
                player.hand2 = []
                board.flop1 = []
                board.flop2 = []
                board.flop3 = []
                board.turn = []
                board.river = []
                refreshUI(player, board, deck)
                return False
    # Creating card from btn value
    selectedCard = btn2card(btn)
    print('> selectionPaneClicked : ', end = '')
    print(selectedCard)
    # Check if selectedCard is in cardsInPlay
    for i in range(len(cardsInPlay)):
        if cardsInPlay[i] and selectedCard.value == cardsInPlay[i][0].value and selectedCard.suit == cardsInPlay[i][0].suit:
            # If yes, remove from cardsInPlay and add back to deck
            if i == 0:
                player.hand1.pop()
            elif i == 1:
                player.hand2.pop()
            elif i == 2:
                board.flop1.pop()
            elif i == 3:
                board.flop2.pop()
            elif i == 4:
                board.flop3.pop()
            elif i == 5:
                board.turn.pop()
            elif i == 6:
                board.river.pop()
            deck_one.cards.append(selectedCard)
            refreshUI(player, board, deck)
            return True
    # If not, remove from deck and add to cardsInPlay
    for i in range(len(cardsInPlay)):
        if not cardsInPlay[i]:
            for card in deck.cards:
                if card.value == selectedCard.value and card.suit == selectedCard.suit:
                    deck.cards.remove(card)
            if i == 0:
                player.hand1.append(selectedCard)
            elif i == 1:
                player.hand2.append(selectedCard)
            elif i == 2:
                board.flop1.append(selectedCard)
            elif i == 3:
                board.flop2.append(selectedCard)
            elif i == 4:
                board.flop3.append(selectedCard)
            elif i == 5:
                board.turn.append(selectedCard)
            elif i == 6:
                board.river.append(selectedCard)
            refreshUI(player, board, deck)
            return True
    refreshUI(player, board, deck)
    return False

def resetCardsInPlay(player, board, deck):
    # Reset button to reset all cards in play
    cardsInPlay = [player.hand1, player.hand2, board.flop1, board.flop2, board.flop3, board.turn, board.river]
    for i in range(len(cardsInPlay)):
        if cardsInPlay[i]:
            deck.cards.append(cardsInPlay[i][0])
    player.hand1 = []
    player.hand2 = []
    board.flop1 = []
    board.flop2 = []
    board.flop3 = []
    board.turn = []
    board.river = []
    definePlayersHandRanking(player)
    refreshUI(player, board, deck)
    print('> resetCardsInPlay : ', end = '')
    print(len(deck.cards))
    return True



window.mainloop()
