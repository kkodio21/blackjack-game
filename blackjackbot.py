import random
import copy
import secrets
import matplotlib.pyplot as plt
decknumber=6
money=100000
bet=100
tudukeru = 1
counti=0
countilist=[]
moneylist=[]

deck=[2, 3,4,5,6,7,8,9, 10, 10, 10, 10, 11]*decknumber*4
reset=int(len(deck)*0.2)
def pickrandom(length): #random number
    pick = secrets.randbelow(length)
    return pick

def moneysub(now,after): #sub money
    return now-after

def moneyadd(now,after):# add money
    return now+after

def pickopp(): #pick opponent card
    global deck
    pick = pickrandom(len(deck)-1)
    oppcards.append(deck[pick])
    if pick == 11 and sum(oppcards)>=11:
        oppcards.append(-10)
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
    if money<0:
        break
    counti+=1
    countilist.append(counti)
    moneylist.append(money)
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
        money=moneyadd(money,int(bet*1.5))
        continue
    elif sum(selfcards[0])!=21 and sum(oppcards)==21 and oppcards[0]==11:
        print("opp "+ str(oppcards),sum(oppcards))
        print("lost")
        money = moneysub(money, bet)
        continue

    if sum(selfcards[0])==16 and (oppcards[0]==9 or oppcards[0]==10 or oppcards[0]==11):#surrender bot
        money=moneysub(money,int(bet*0.5))
        continue
    if sum(selfcards[0])==15 and oppcards[0]==10:
        money = moneysub(money, int(bet * 0.5))
        continue


    while handan==0: #for each deck till all deck is searched
        print(selfcards)
        for a in range(len(selfcards)): #deck num each ask
            print(f"your deck num {a+1} is {selfcards[a]}")
            if selfcards[a][0]==selfcards[a][1] and (selfcards[a][-1]!=0 or selfcards[a][-1]!="up"): #split
                if selfcards[a][0]==8 or selfcards[a][0]==11:
                    split(a)
                    del selfcards[a][1]
                    pickself(selfcards,a)
                    pickself(selfcards,-1)
                    break
                elif selfcards[a][0]==7 and oppcards[0]<8 or selfcards[a][0]==6 and oppcards[0]<7\
                        or (selfcards[a][0]==3 or selfcards[a][0]==2) and oppcards[0]<8:
                    split(a)
                    del selfcards[a][1]
                    pickself(selfcards, a)
                    pickself(selfcards, -1)
                    break
                elif selfcards[a][0]==4 and oppcards[0]<7 and oppcards[0]>4:
                    split(a)
                    del selfcards[a][1]
                    pickself(selfcards, a)
                    pickself(selfcards, -1)
                    break
                elif selfcards[a][0] == 9 and (oppcards[0] < 7 or oppcards[0] > 7 and oppcards[0<10]):
                    split(a)
                    del selfcards[a][1]
                    pickself(selfcards, a)
                    pickself(selfcards, -1)
                    break



            if selfcards[a][-1]!="up" and selfcards[a][-1]!=0:
                if sum(selfcards[a])==11 or sum(selfcards[a])==10 and oppcards[0]<10:#double up
                    pickself(selfcards,a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)
                    selfcards[a].append("up")  # if last is up dont hit
                elif sum(selfcards[a])==9 and (oppcards[0]<7 and oppcards[0]>2):
                    pickself(selfcards, a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)
                    selfcards[a].append("up")  # if last is up dont hit
                elif (selfcards[a][0]==11 and selfcards[a][1]==6 or selfcards[a][0]==6 and selfcards[a][1]==11)\
                    and (oppcards[0]<7 and oppcards[0]>2):
                    pickself(selfcards, a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)
                    selfcards[a].append("up")  # if last is up dont hit
                elif (selfcards[a][0]==11 and selfcards[a][1]==8 or selfcards[a][0]==8 and selfcards[a][1]==11)\
                    and oppcards[0]==6:
                    pickself(selfcards, a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)
                    selfcards[a].append("up")  # if last is up dont hit
                elif (selfcards[a][0] == 11 and selfcards[a][1] == 7 or selfcards[a][0] == 7 and selfcards[a][1] == 11) \
                    and oppcards[0] < 7:
                    pickself(selfcards, a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)
                    selfcards[a].append("up")  # if last is up dont hit
                elif (selfcards[a][0]==11 and (selfcards[a][1]==5 or selfcards[a][1]==4) or (selfcards[a][0]==5 or selfcards[a][1]==4)\
                      and selfcards[a][1]==11) and (oppcards[0]<7 and oppcards[0]>3):
                    pickself(selfcards, a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)
                    selfcards[a].append("up")  # if last is up dont hit
                elif (selfcards[a][0] == 11 and (selfcards[a][1] == 3 or selfcards[a][1] == 2) or (selfcards[a][0] == 3 or selfcards[a][1] == 2)\
                      and selfcards[a][1] == 11) and (oppcards[0] < 7 and oppcards[0] > 4):
                    pickself(selfcards, a)
                    if 11 in selfcards[a] and sum(selfcards[a]) > 21:
                        selfcards[a].append(-10)
                    selfcards[a].append("up")  # if last is up dont hit
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
            while(1):
                if (selfcards[a][0] == 11 and selfcards[a][1] == 9 or selfcards[a][0] == 9\
                          and selfcards[a][1] == 11):
                    break
                elif (selfcards[a][0] == 11 and selfcards[a][1] == 8 or selfcards[a][0] == 8\
                          and selfcards[a][1] == 11):
                    break
                elif (selfcards[a][0] == 11 and selfcards[a][1] == 7 or selfcards[a][0] == 7\
                          and selfcards[a][1] == 11) and (oppcards[0]==7 or oppcards[0]==8):
                    break
                elif sum(selfcards[a])>=17:
                    break
                elif sum(selfcards[a])>=13 and oppcards[0]<7:
                    break
                elif sum(selfcards[a]) == 12 and (oppcards[0] < 7 and oppcards[0]>3):
                    break
                else:
                    pickself(selfcards,a)
                    if 11 in selfcards[a] and -10 not in selfcards[a] and sum(selfcards[a][:-1]) > 21:
                        selfcards.append(-10)
                    print("you " + str(selfcards[a]), sum(selfcards[a]))
                    print("opp " + str(oppcards[0]))
                    if sum(selfcards[a])>21:
                        break



    print("opp " + str(oppcards), sum(oppcards))#result print out
    for a in range(len(selfcards)):
        if selfcards[a][-1]!="up":
            print(f"your deck num {a+1} is {selfcards[a]}, {sum(selfcards[a])}")
            if (selfcards[a][0]==10 and selfcards[a][1]==11 or selfcards[a][0]==11 and selfcards[a][1]==10) and sum(oppcards)<21 :
                print("Blackjack!")
                money =moneyadd(money,int(bet*1.5))
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


print(counti)
plt.plot(countilist, moneylist)
plt.show()