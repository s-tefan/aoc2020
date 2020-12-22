class CombatPlayer:
    def __init__(self, cardlist = []):
        self.deck = cardlist.copy()
    def __repr__(self):
        return str(self.deck)
    def addcard(self, c):
        self.deck.append(c)
    def play(self):
        return self.deck.pop(0)
    def putback(self, clist):
        self.deck.extend(reversed(sorted(clist)))
    def lose(self):
        return not self.deck
    def score(self):
        sc = 0
        for k, card in enumerate(reversed(self.deck)):
            sc += (k+1)*card
        return sc
            

def playround(playerdict, verbose = False):
    cards = []
    clist = []
    for player in playerdict.values():
        card = player.play()
        cards.append((card, player))
        clist.append(card)
    if verbose: print(cards)
    _, winner = max(cards)
    winner.putback(clist)

def getplayers(filename):
    playerdict = {}
    with open(filename) as f:
        for line in f:
            stripline = line.strip(" \n\r")
            if  stripline[:6].lower() == "player":
                playername = stripline[6:].strip(" :")
                player = CombatPlayer()
                playerdict[playername] = player
            elif stripline:
                player.addcard(int(stripline))
    return playerdict
        
def partone(filename):
    playerdict = getplayers(filename)
    over = False
    while not over:
        playround(playerdict)
        for k in playerdict:
            if playerdict[k].lose():
                print("Player {} loses!".format(k))
                over = True
    for name, player in playerdict.items():
        print("Player {} scores {}".format(name, player.score()))

partone("input.txt")