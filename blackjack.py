import random
import copy
decknumber=6
money=1000000
bet=100
tudukeru = 1


deck=[2, 3,4,5,6,7,8,9, 10, 10, 10, 10, 11]*decknumber*4
reset=int(len(deck)*0.2)
def pickrandom(length): #random number
    pick = random.randint(0,length)
    return pick

def moneysub(now,after): #sub money
    return now-after

def moneyadd(now,after):# add money
    return now+after

def pickopp(): #pick opponent card
    global deck
    pick = pickrandom(len(deck)-1)
    oppcards.append(deck[pick])
    deck.pop(pick)

def pickself(decknum,a): #pick selfs card
    global deck
    pick = pickrandom(len(deck)-1)
    decknum[a].append(deck[pick])
    deck.pop(pick)

def firstcards(): #first round distribution
    global deck
    global selfcards
    pickself(selfcards,0)
    pickopp()
    pickself(selfcards,0)
    pickopp()


def deterwin(selfsum,oppsum): #determind the winloss
    if selfsum>21:
        return 0
    elif oppsum>21:
        return 1

    if selfsum-oppsum>0:
        return 1
    elif selfsum-oppsum==0:
        return 2
    else:
        return 0


def split(ba):# ask split
    selfcards.append([copy.copy(selfcards[ba][1])])




while(tudukeru):# main game start from here
    handan=0
    selfcards = [[]]
    oppcards = []

    if len(deck)<reset:
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * decknumber * 4
    print("You have " + str(money))
    # print("You bet " + str(bet))
    firstcards()
    # print(selfcards)
    # print(f"you {selfcards[0]}, {sum(selfcards[0])}")
    print("opp "+ str(oppcards[0]))



    if sum(selfcards[0])==21 and sum(oppcards)==21: #blackjack
        print("opp "+str(oppcards), sum(oppcards))
        print("push")
        continue
    elif sum(selfcards[0])==21 and sum(oppcards)!=21:
        print("won")
        money=moneyadd(money,bet*2.5)
        continue
    elif sum(selfcards[0])!=21 and sum(oppcards)==21 and oppcards[0]==11:
        print("opp "+ str(oppcards),sum(oppcards))
        print("lost")
        money = moneysub(money, bet)
        continue


    while handan==0: #for each deck till all deck is searched
        print(selfcards)
        for a in range(len(selfcards)): #deck num each ask
            print(f"your deck num {a+1} is {selfcards[a]}")
            if selfcards[a][0]==selfcards[a][1] and (selfcards[a][-1]!=0 or selfcards[a][-1]!="up"): #split
                ask = input(f"Do you want to split deck num {a+1}?")
                if ask == "1":
                    split(a)
                    del selfcards[a][1]
                    pickself(selfcards,a)
                    pickself(selfcards,-1)

                    break



            if selfcards[a][-1]!="up" and selfcards[a][-1]!=0:
                askdouble = input(f"Do you want to double up deck num {a+1}?") #double up
                if askdouble== "1":
                    pickself(selfcards,a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)

                    selfcards[a].append("up")  # if last is up dont hit
                    print(f"you { str(selfcards[a])},{sum(selfcards[a][:-1])}" )
                else:
                    selfcards[a].append(0)
            if a==len(selfcards)-1:
                handan=1
                # if 11 not in selfcards[a] and sum(selfcards[a])>21:
                #     print("you " + str(selfcards[a]), sum(selfcards[a]))
                #     print("lose")
                #     money = moneysub(money, bet * 2)
                #     handan=1
                #     continue


                # while (sum(oppcards) < 17):
                #     pickopp()
                #     if 11 in oppcards and -10 not in oppcards and sum(oppcards) > 21:
                #         oppcards.append(-10)
                #     print("opp " + str(oppcards), sum(oppcards))
                # result = deterwin(sum(selfcards[a]), sum(oppcards))
                #
                # if result == 1:
                #     print("won")
                #     money = moneyadd(money, bet*2)
                #     handan=1
                #
                # elif result == 2:
                #     print("push")
                #     handan=1
                #
                # else:
                #     print("lose")
                #     money = moneysub(money, bet*2)
                #     handan=1



    for a in range(len(selfcards)):#ask to hit
        if selfcards[a][-1]!="up":
            print(selfcards[a])
            asktocon=input(f"Do you want to hit deck num {a+1}?") #hit
            while(asktocon=="1"):
                pickself(selfcards,a)
                if 11 in selfcards[a] and -10 not in selfcards[a] and sum(selfcards[a][:-1]) > 21:
                    selfcards.append(-10)
                print("you " + str(selfcards[a]), sum(selfcards[a]))
                print("opp " + str(oppcards[0]))
                if sum(selfcards[a])>21:
                    break
                asktocon = input("Do you want to hit?")



    print("opp " + str(oppcards), sum(oppcards))#result print out
    for a in range(len(selfcards)):
        if selfcards[a][-1]!="up":
            print(f"your deck num {a+1} is {selfcards[a]}, {sum(selfcards[a])}")
            if (selfcards[a][0]==10 and selfcards[a][1]==11 or selfcards[a][0]==11 and selfcards[a][1]==10) and sum(oppcards)<21 :
                print("Blackjack!")
                money =moneyadd(money,bet*2.5)
                continue
            elif (selfcards[a][0]==10 and selfcards[a][1]==11 or selfcards[a][0]==11 and selfcards[a][1]==10) and sum(oppcards)==21:
                print("Push")
                continue
            if sum(selfcards[a])>21:
                print("lose")
                money = moneysub(money, bet)
                continue
            while(sum(oppcards)<17):
                pickopp()
                if 11 in oppcards and -10 not in oppcards and sum(oppcards)>21:
                    oppcards.append(-10)
                print("opp "+str(oppcards),sum(oppcards))
            result=deterwin(sum(selfcards[a]),sum(oppcards))
            if result==1:
                print("won")
                money=moneyadd(money,bet)
            elif result==2:
                print("push")
            else:
                print("lose")
                money=moneysub(money,bet)
        else:
            print(f"your deck num {a + 1} is {selfcards[a]}, {sum(selfcards[a][:-1])}")
            if sum(selfcards[a][:-1])>21:
                print("lose")
                money = moneysub(money, bet)
                continue
            while (sum(oppcards) < 17):
                pickopp()
                if 11 in oppcards and -10 not in oppcards and sum(oppcards) > 21:
                    oppcards.append(-10)
                print("opp " + str(oppcards), sum(oppcards))
            result = deterwin(sum(selfcards[a][:-1]), sum(oppcards))
            if result == 1:
                print("won")
                money = moneyadd(money, bet*2)
            elif result == 2:
                print("push")
            else:
                print("lose")
                money = moneysub(money, bet*2)

    print("//////////////////////////////////////////")