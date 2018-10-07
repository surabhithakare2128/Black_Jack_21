import random
import copy
import sys

#global variables
flags = False
betAmount = 0
balance = 0
cards = [['spade','A'], ['spade',2], ['spade',3], ['spade',4], ['spade',5], ['spade',6],['spade',7], ['spade',8], ['spade',9], ['spade',10], ['spade','J'], ['spade','Q'], ['spade','K'], ['clover','A'], ['clover',2], ['clover',3], ['clover',4], ['clover',5], ['clover',6],['clover',7], ['clover',8], ['clover',9], ['clover',10], ['clover','J'], ['clover','Q'], ['clover','K'], ['diamond','A'], ['diamond',2], ['diamond',3], ['diamond',4], ['diamond',5], ['diamond',6],['diamond',7], ['diamond',8], ['diamond',9], ['diamond',10], ['diamond','J'], ['diamond','Q'], ['diamond','K'], ['heart','A'], ['heart',2], ['heart',3], ['heart',4], ['heart',5], ['heart',6],['heart',7], ['heart',8], ['heart',9], ['heart',10], ['heart','J'], ['heart','Q'], ['heart','K']]
remainingCards = copy.deepcopy(cards)
assignedCard = []
dealerList = []
playerList = []
choose = ""
notBusted = 0
totalSum = 0
playGame = 1


print ("Welcome to BLACK JACK!!!\n")


def balanceCheck():
    while True:
        try:
            global balance
            balance = int(input("Enter your account Balance: "))
        except:
            print("Enter balance correctly!!!\n")
            continue
        else:
            if balance >= 5:
                print("\nYour account balance is ${}\n".format(balance))
                break
            else:
                print("The balance should be more than $5.\n")

def bettingAmount():
    while True:
        try:
            global betAmount
            betAmount = int(input("Enter the amount you want to bet: "))
            global flags
            flags = True
        except:
            print("Enter the bet amount correctly!!!\n")
            continue
        else:
            if betAmount >= 5 and betAmount <= balance:
                print("\nThe betting amount is ${}. Good Luck!\n".format(betAmount))
                break
            elif betAmount >= balance:
                print("\nYou have insufficient funds. Sorry!")
                print("Your account balance is ${}\n".format(balance))
            else:
                print ("The betting amount should be more than $5\n")

def shuffleCard():
        " " " This function shuffles cards " " "
        global remainingCards
        if len(remainingCards) <= 5:
            print ("As there are few cards left, the deck is getting reshuffled...!!!")

            remainingCards = copy.deepcopy(Deck.cards)

        indexOfCard = random.randint(0, len(remainingCards) - 1)
        # print (indexOfCard)

        global assignedCard
        assignedCard = remainingCards[indexOfCard]

        #print assignedCard
        remainingCards.pop(indexOfCard)
        return assignedCard

def deck():
    print ("------------------------------------------------------------")
    print ("                           DEALER\n")
    print ("        {}                \n\n\n\n\n".format(dealerList))
    print ("  {}\n".format(playerList))
    print ("                           PLAYER")
    print ("------------------------------------------------------------")


def addBalance(doubleOfBet):
    " " " This fucntion adds the double of betting amount if user wins " " "
    global balance
    balance = balance + doubleOfBet
    print ("Now you have ${} in your account".format(balance))
    return balance

def subtractBalance(bettingValue):
    " " " This function subtracts the betting value if user loses " " "
    global balance
    balance = balance - bettingValue
    print ("Now you have ${} in your account".format(balance))
    return balance

def choice():
    global choose
    choose = raw_input("Press 'H' to hit and 'S' to  stay ")
    return choose

def checkBust(listToBeChecked):
    j = 0

    numberList = []
    for i in listToBeChecked:
        numberList.append(listToBeChecked[j][1])
        j = j + 1
    #print (numberList)
    for numbers in numberList:
            indexCount = 0
            if numberList[indexCount] == 'A':
                numberList.pop(indexCount)
                numberList.append(11)
                #print(numberList)
            elif numberList[indexCount] == 'J' or numberList[indexCount] == 'Q' or numberList[indexCount] == 'K':
                numberList.pop(indexCount)
                numberList.append(10)
                #print(numberList)
            else:
                numberList.append(numberList[indexCount])
                numberList.pop(indexCount)


            indexCount = indexCount + 1
    #print (numberList)
    checkBusted(numberList)
    return numberList


def checkBusted(numberLi):
    #print (numberLi)
    sum = 0
    for digits in numberLi:
        sum = sum + digits
    if sum <= 21:
            #print (sum)
            print ("not busted")
    elif 11 in numberLi and sum <= 31:
            sum = sum - 10
            print ("sum is ", sum)
    else:
            print ("busted")
            global notBusted
            notBusted = 1

    return numberLi, notBusted

def sumForComparing(listToBeChecked):
    j = 0
    numberList = []
    for i in listToBeChecked:
        numberList.append(listToBeChecked[j][1])
        j = j + 1
    #print (numberList)
    for numbers in numberList:
            indexCount = 0
            if numberList[indexCount] == 'A':
                numberList.pop(indexCount)
                numberList.append(11)
                #print(numberList)
            elif numberList[indexCount] == 'J' or numberList[indexCount] == 'Q' or numberList[indexCount] == 'K':
                numberList.pop(indexCount)
                numberList.append(10)
                #print(numberList)
            else:
                numberList.append(numberList[indexCount])
                numberList.pop(indexCount)


            indexCount = indexCount + 1
    print (numberList)
    global totalSum
    totalSum = 0
    for digi in numberList:
        totalSum = totalSum + digi

    print (totalSum)
    return totalSum

def continuePlaying():
    global balance
    if balance >= 5:
        print("\nDo you want to play another game?")
        continueGame = raw_input("Press 'Y' for Yes and 'N' for No... ")
        if continueGame == 'y' or continueGame == 'Y':
            global playGame
            playGame = 1
        elif continueGame == 'n' or continueGame == 'N':
            global playGame
            playGame = 0
            quit()
        else:
            print("\nSelect correct option...\n")
            continuePlaying()
    else:
        print("Your account balance is low to continue.")
        playGame = 0
        sys.exit()
    return playGame

balanceCheck()
bettingAmount()


while (playGame == 1):
    if flags == True:



        dealerCard1 = shuffleCard()
        dealerCard2 = shuffleCard()
        playerCard1 = shuffleCard()
        #playerCard1 = ['spade', 'A']
        playerCard2 = shuffleCard()
        #playerCard2 = ['spade', 14]
        playerCard3 = shuffleCard()
        dealerList.append(dealerCard1)
        playerList.append(playerCard1)
        playerList.append(playerCard2)
        deck()

        while True:
            while notBusted == 0:
                choice()
                if choose == 'h' or choose == 'H':
                    """Code needs to be added"""
                    playerCard3 = shuffleCard()
                    playerList.append(playerCard3)
                    deck()
                    checkBust(playerList)
                    if notBusted == 1:
                        global betAmount
                        #print (betAmount)
                        subtractBalance(betAmount)

                elif choose == 's' or choose == 'S':
                    """Code needs to be added"""
                    dealerCard2 = shuffleCard()
                    dealerList.append(dealerCard2)
                    deck()
                    checkBust(dealerList)
                    if notBusted == 1:
                        print("The dealer got busted")
                        print("Congrats you get double of Betting Amount")
                        global betAmount
                        #print (betAmount)
                        doubleBetAmount = betAmount * 2
                        addBalance(doubleBetAmount)
                        continuePlaying()
                        break
                    else:
                        """Add code to compare """
                        sumForComparing(dealerList)
                        dealerTotal = totalSum
                        sumForComparing(playerList)
                        playerTotal = totalSum
                        print (dealerTotal, playerTotal)
                        if playerTotal >= dealerTotal:
                            print("You Win!")
                            doubleBetAmount = betAmount * 2
                            addBalance(doubleBetAmount)
                            continuePlaying()
                            break
                        else:
                            print("You lose...")
                            global betAmount
                            subtractBalance(betAmount)
                            continuePlaying()
                            break


                else:
                    print ("Choose correct option: ")
                    choice()


            continuePlaying()