from random import randint

class Card:
  def __repr__(self):
    return self.__str__()
  def __str__(self):
    if self.number == 11:
      return ('Jack')+ ' of '+ self.suite
    elif self.number == 12:
      return ('Queen')+ ' of '+ self.suite
    elif self.number == 13:
      return ('King')+ ' of '+ self.suite
    elif self.number == 1:
      return ('Ace')+ ' of '+ self.suite
    return str(self.number)+ ' of '+ self.suite

  def __init__(self,suite,number):
    self.suite = suite
    self.number = number



class Deck:
  def __init__(self):
    self.cards = [ ]
    for i in range(1,14):
      for j in ('hearts','spades','diamonds','clubs'):
        self.cards.append (Card(j,i))

  def shuffleCard(self):
    for i in range(1,250):
      shuffle = randint(0,51)
      r = self.cards.pop(shuffle)
      self.cards.append(r)

  def topCard(self):
    return c.cards.pop(0)
    

class Player:
  def __repr__(self):
    return self.__str__()

  def __str__(self):#the hand,if ai,value of hand
    output = ''
    output = output + str(self.hand)
    #output = output + str(self.computer)
    output = output + str(self.valueofHand())
    return output 

  def __init__(self,computer):
    self.hand = [ ]
    self.computer = computer

  def storeCard(self,deck,number):
    for i in range(0,number):
      self.hand.append(deck.topCard())
    
  def valueofHand(self):
    value = 0
    qc = len(self.hand)#2 cards
    for i in range(0,qc):
      if self.hand[i].number > 10:
        value += 10
      elif self.hand[i].number > 1:
        value += self.hand[i].number
    for i in range(0,qc):
      if value < 10 and self.hand[i].number == 1:
        value += 11
      elif value > 10 and self.hand[i].number == 1:
        value += 1
    return value 


def gameWinner():
  hNl = ''
  hN = 0
  for i in range(1,len(playerList),1):
    if playerList[i].valueofHand() < 22 and playerList[i].valueofHand() > hN:
      hN = playerList[i].valueofHand()
  for j in range(0,len(playerList),1):
    if playerList[j].valueofHand() == hN: 
      hNl+=str(j+1)+', '  
  print(hN)
  print('The following player or players won - ',(hNl))

c = Deck()
playerList = [ ]

c.shuffleCard()
print(c.cards)
print( )

amtPlayer = int(input('How many players do you want?'))
for i in range(0,amtPlayer,1):
  playerList.append(Player(False))
  playerList[i].storeCard(c,2)

print(playerList)

for i in range(0,len(playerList)):
  while playerList[i].valueofHand() < 21:
    if playerList[i].valueofHand() < 21:
      print('player', i + 1, 'Do you want to hit or Do you want to stay')
      response = input(' ')
      if response == 'hit':
        playerList[i].storeCard(c,1)
      elif response == 'stay':
        break
      print(playerList)

  print(playerList)  

gameWinner()
    
 
    

      


    