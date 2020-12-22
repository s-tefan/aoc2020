class CombatPlayer:
    def __init__(self, cardlist = [], name = ""):
        self.deck = cardlist.copy()
        self.name = name
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
        return sum((k+1)*card for k, card in enumerate(reversed(self.deck)))

def playround(players, previous=[], verbose = False):
    cards = []
    clist = []
    for player in players:
        card = player.play()
        cards.append((card, player))
        clist.append(card)
    if verbose: print(cards)
    _, winner = max(cards)
    winner.putback(clist)
    #previous.append([player, ])

def getplayers(filename):
    players = set()
    with open(filename) as f:
        for line in f:
            stripline = line.strip(" \n\r")
            if  stripline[:6].lower() == "player":
                playername = stripline[6:].strip(" :")
                player = CombatPlayer(name = playername)
                players.add(player)
            elif stripline:
                player.addcard(int(stripline))
    return players
        
def partone(filename):
    players = getplayers(filename)
    over = False
    while not over:
        playround(players)
        for player in players:
            if player.lose():
                print("Player {} loses!".format(player.name))
                over = True
    for player in players:
        print("Player {} scores {}".format(player.name, player.score()))

partone("input.txt")