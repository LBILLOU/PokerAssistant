#!/usr/local/bin/python3
from classes import *
from functions import *
from tkinter import *

deck_one = Deck()
player_one = Player('Player 1')
board_one = Board()

window = Tk()
window.title('Poker Assistant')
window.resizable(height=False,width=False)
windowWidth = 726
windowHeight = 364
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
xCoord = (screenWidth/2) - (windowWidth/2)
yCoord = (screenHeight/2) - (windowHeight/2)
window.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,xCoord,yCoord))

# Colors
redCard = '#ff0000' #RED
blackCard = '#1e1e1e' #DARK GREY
handbg = '#000000'  #BLACK
flopbg = '#000000'  #BLACK
turnbg = '#000000'  #BLACK
riverbg = '#000000' #BLACK
resetbg = '#000000' #BLACK
current = '#00c120' #GREEN
aboveCurrent = '#ffffff' #WHITE
belowCurrent = '#707070' #GREY
final = '#707070' #GREY
bgColor = '#000000' #BLACK
fontColor = '#ffffff' #WHITE #Generic font color

selectionPane = Frame(window)
cardsPane = Frame(window)
combinationPane = Frame(window)

# Setting BackGround Color
window.configure(bg=bgColor)
cardsPane.configure(bg=bgColor)
combinationPane.configure(bg=bgColor)

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

# Cards Pane UI
# Player
lblCol0Space = Label(cardsPane,text='sdjs',width=2,anchor=W,bg=bgColor)
lblCol0Space.grid(row=0,column=0)
btnPH1 = Button(cardsPane,text='-',command=lambda:playersCardClicked(btnPH1,player_one,board_one,deck_one),width=3,highlightbackground=handbg)
btnPH2 = Button(cardsPane,text='-',command=lambda:playersCardClicked(btnPH2,player_one,board_one,deck_one),width=3,highlightbackground=handbg)
btnPH1.grid(row=1,column=1)
btnPH2.grid(row=1,column=2)
lblPName = Label(cardsPane,text=player_one.name.upper(),fg=fontColor,bg=bgColor)
lblPH = Label(cardsPane,text='Hand',fg=fontColor,bg=bgColor)
lblPName.grid(row=0,column=1,columnspan=2)
lblPH.grid(row=2,column=1,columnspan=2)
# Board
btnBF1 = Button(cardsPane,text='-',command=lambda:boardCardClicked(btnBF1,player_one,board_one,deck_one),width=3,highlightbackground=flopbg)
btnBF2 = Button(cardsPane,text='-',command=lambda:boardCardClicked(btnBF2,player_one,board_one,deck_one),width=3,highlightbackground=flopbg)
btnBF3 = Button(cardsPane,text='-',command=lambda:boardCardClicked(btnBF3,player_one,board_one,deck_one),width=3,highlightbackground=flopbg)
btnBT = Button(cardsPane,text='-',command=lambda:boardCardClicked(btnBT,player_one,board_one,deck_one),width=3,highlightbackground=turnbg)
btnBR = Button(cardsPane,text='-',command=lambda:boardCardClicked(btnBR,player_one,board_one,deck_one),width=3,highlightbackground=riverbg)
btnBF1.grid(row=1,column=3)
btnBF2.grid(row=1,column=4)
btnBF3.grid(row=1,column=5)
btnBT.grid(row=1,column=6)
btnBR.grid(row=1,column=7)
btnReset = Button(cardsPane,text='Reset',command=lambda:resetCardsInPlay(player_one,board_one,deck_one),width=5,highlightbackground=resetbg)
btnReset.grid(row=1,column=8)
lblCol9Space = Label(cardsPane,text='',width=2,anchor=W,bg=bgColor)
lblCol9Space.grid(row=0,column=9)

lblBoardName = Label(cardsPane,text='BOARD',fg=fontColor,bg=bgColor)
lblBoardName.grid(row=0,column=3,columnspan=5)
lblBFlop = Label(cardsPane,text='Flop',fg=fontColor,bg=bgColor)
lblBFlop.grid(row=2,column=3,columnspan=3)
lblBTurn = Label(cardsPane,text='Turn',fg=fontColor,bg=bgColor)
lblBTurn.grid(row=2,column=6,columnspan=1)
lblBRiver = Label(cardsPane,text='River',fg=fontColor,bg=bgColor)
lblBRiver.grid(row=2,column=7,columnspan=1)

# Combination Pane UI
lblRow1Spacing = Label(combinationPane,text='',width=7,anchor=W,bg=bgColor)
lblRow1Spacing.grid(row=0,column=0)
lblCol1Spacing = Label(combinationPane,text='',width=7,anchor=W,bg=bgColor)
lblCol1Spacing.grid(row=1,column=0)
lblRoyalFlush = Label(combinationPane,text='Royal Flush',width=12,anchor=W,fg=fontColor,bg=bgColor)
lblStrFlush = Label(combinationPane,text='Straight Flush',width=12,anchor=W,fg=fontColor,bg=bgColor)
lbl4oaKind = Label(combinationPane,text='Four of a Kind',width=12,anchor=W,fg=fontColor,bg=bgColor)
lblFullHouse = Label(combinationPane,text='Full House',width=12,anchor=W,fg=fontColor,bg=bgColor)
lblFlush = Label(combinationPane,text='Flush',width=12,anchor=W,fg=fontColor,bg=bgColor)
lblStraight = Label(combinationPane,text='Straight',width=12,anchor=W,fg=fontColor,bg=bgColor)
lbl3oaKind = Label(combinationPane,text='Three of a Kind',width=12,anchor=W,fg=fontColor,bg=bgColor)
lbl2Pairs = Label(combinationPane,text='Two Pairs',width=12,anchor=W,fg=fontColor,bg=bgColor)
lblPair = Label(combinationPane,text='Pair',width=12,anchor=W,fg=fontColor,bg=bgColor)
lblHighCard = Label(combinationPane,text='High Card',width=12,anchor=W,fg=fontColor,bg=bgColor)
lblRoyalFlush.grid(row=1,column=1)
lblStrFlush.grid(row=2,column=1)
lbl4oaKind.grid(row=3,column=1)
lblFullHouse.grid(row=4,column=1)
lblFlush.grid(row=5,column=1)
lblStraight.grid(row=6,column=1)
lbl3oaKind.grid(row=7,column=1)
lbl2Pairs.grid(row=8,column=1)
lblPair.grid(row=9,column=1)
lblHighCard.grid(row=10,column=1)
# Outs
outsRoyalFlush = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outsStrFlush = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outs4oaKind = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outsFullHouse = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outsFlush = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outsStraight = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outs3oaKind = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outs2Pairs = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outsPair = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outsHighCard = Label(combinationPane,text='',width=10,anchor=W,fg=fontColor,bg=bgColor)
outsRoyalFlush.grid(row=1,column=2)
outsStrFlush.grid(row=2,column=2)
outs4oaKind.grid(row=3,column=2)
outsFullHouse.grid(row=4,column=2)
outsFlush.grid(row=5,column=2)
outsStraight.grid(row=6,column=2)
outs3oaKind.grid(row=7,column=2)
outs2Pairs.grid(row=8,column=2)
outsPair.grid(row=9,column=2)
outsHighCard.grid(row=10,column=2)
lblCol3Spacing = Label(combinationPane,text='',width=1,anchor=W,bg=bgColor)
lblCol3Spacing.grid(row=0,column=3)

# Information Pane UI
lblHR = Label(combinationPane,text='-',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblHR.grid(row=1,column=4)
lblCClbl = Label(combinationPane,text='Current Combination',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblCClbl.grid(row=3,column=4)
lblCC = Label(combinationPane,text='-',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblCC.grid(row=4,column=4)
lblNUO = Label(combinationPane,text='Unique Outs -',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblNUO.grid(row=6,column=4)
lblUO1 = Label(combinationPane,text='-',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblUO1.grid(row=7,column=4)
lblUO2 = Label(combinationPane,text='-',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblUO2.grid(row=8,column=4)
lblUO3 = Label(combinationPane,text='-',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblUO3.grid(row=9,column=4)
lblUO4 = Label(combinationPane,text='-',width=16,anchor=CENTER,fg=fontColor,bg=bgColor)
lblUO4.grid(row=10,column=4)
lblUO5 = Label(combinationPane,text='',width=2,anchor=W,fg=fontColor,bg=bgColor)
lblUO5.grid(row=10,column=5)

selectionPane.pack(side=LEFT,fill=X)
combinationPane.pack(side=TOP,fill=X)
cardsPane.pack(side=LEFT,fill=X)

def refreshInfoPane(player, board, deck, bestCombination, outs):
    # Refreshing player's hand rank
    lblHR['text'] = 'Hand Rank ' + str(player_one.handRank) + '/10'
    # Refreshing Current Combination and Outs
    if len(createCardsToCheck(player,board)) >= 7:
        lblCClbl['text'] = 'Final Combination'
        lblCC['fg'] = current
        # Refreshing outs
        lblNUO['text'] = 'Unique Outs : n/a'
        lblUO1['text'] = ''
        lblUO2['text'] = ''
        lblUO3['text'] = ''
        lblUO4['text'] = ''
        lblUO5['text'] = ''
        # Refreshing cards in play color for bestCombination cards
        cardsBtns = [btnPH1, btnPH2, btnBF1, btnBF2, btnBF3, btnBT, btnBR]
        for card in bestCombination[-1]:
            for i in range(len(cardsBtns)):
                kard = btn2card(cardsBtns[i])
                if card.value == kard.value and card.suit == card.suit:
                    cardsBtns[i]['fg'] = current
    else:
        lblCClbl['text'] = 'Current Combination'
        lblCC['fg'] = fontColor
        # Refreshing outs
        flatOuts = [card for sublist in outs for card in sublist]
        flatOuts = list(set(flatOuts))
        flatOuts.sort(key=lambda card: card.value, reverse=True)
        lblNUO['text'] = 'Unique Outs : ' + str(len(flatOuts))
        lblUO1['text'] = flatOuts[:6]
        lblUO2['text'] = flatOuts[6:12]
        lblUO3['text'] = flatOuts[12:18]
        lblUO4['text'] = flatOuts[18:24]
        if len(flatOuts) > 24:
            lblUO5['text'] = '...'
        else:
            lblUO5['text'] = ''
        # Refreshing cards in play text color to default
        cardsBtns = [btnPH1, btnPH2, btnBF1, btnBF2, btnBF3, btnBT, btnBR]
        for i in range(len(cardsBtns)):
            cardsBtns[i]['fg'] = fontColor

    if bestCombination:
        lblCC['text'] = bestCombination[-1]
    else:
        lblCC['text'] = ''

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

    # Refreshing combination pane
    uiCombElems = [lblRoyalFlush, lblStrFlush, lbl4oaKind, lblFullHouse, lblFlush, lblStraight, lbl3oaKind, lbl2Pairs, lblPair, lblHighCard]
    uiOutsElems = [outsRoyalFlush, outsStrFlush, outs4oaKind, outsFullHouse, outsFlush, outsStraight, outs3oaKind, outs2Pairs, outsPair, outsHighCard]
    numberOfCardsInPlay = len(createCardsToCheck(player,board))
    if numberOfCardsInPlay >= 7:
        bestCombination, outs = checkPokerCombination(player, board, deck)
        bestCombIndex = len(bestCombination)-1
        for i in range(len(uiCombElems)):
            uiCombElems[i]['fg']= final
            uiOutsElems[i]['fg']= final
            uiOutsElems[i]['text'] = ''
        uiCombElems[bestCombIndex]['fg']= current
        uiOutsElems[bestCombIndex]['fg']= current
        uiOutsElems[bestCombIndex]['text'] = ''

    elif numberOfCardsInPlay >= 1:
        bestCombination, outs = checkPokerCombination(player, board, deck)
        for i in range(len(bestCombination)):
            if bestCombination[i] == False:
                uiCombElems[i]['fg']= aboveCurrent
                uiOutsElems[i]['fg']= aboveCurrent
                uiOutsElems[i]['text'] = str(len(outs[i])) + ' outs'
            else:
                uiCombElems[i]['fg']= current
                uiOutsElems[i]['fg']= current
                uiOutsElems[i]['text'] = str(len(outs[i])) + ' outs'
                for j in range(i+1,len(uiCombElems)):
                    uiCombElems[j]['fg']= belowCurrent
                    uiOutsElems[j]['fg']= belowCurrent
                    uiOutsElems[j]['text'] = ''
    else:
        bestCombination = []
        outs = []
        for i in range(len(uiCombElems)):
            uiCombElems[i]['fg']= fontColor
            uiOutsElems[i]['fg']= fontColor
            uiOutsElems[i]['text'] = ''
    # Refresh Info
    refreshInfoPane(player, board, deck, bestCombination, outs)
    # Resetting size dur to MacOS Mojave x pyinstaller button refresh issue
    # https://stackoverflow.com/questions/52529403/button-text-of-tkinter-not-works-in-mojave
    window.geometry(window.geometry()) #726x364+5+28
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
    print('> resetCardsInPlay, deck reset to ', end = '')
    print(len(deck.cards))
    return True



window.mainloop()
