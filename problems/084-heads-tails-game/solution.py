playCount = int(input())
player, hand = input().split()
player = int(player)

def changeHand(hand):
    return "R" if hand == "L" else "L"

def shiftPlayer(currentPlayer):
    if currentPlayer + 1 > 3:
        return 1
    return currentPlayer + 1


def handleSecondAction(currentPlayer:int, currentHand:str, actionPlayer:int, actionGiverHand:str, actionRecieverHand: str):
    player: int = currentPlayer
    hand: str = currentHand
    if currentPlayer == actionPlayer and hand == actionGiverHand:
        player = shiftPlayer(currentPlayer)
        hand = actionRecieverHand
    elif shiftPlayer(actionPlayer) == currentPlayer and currentHand == actionRecieverHand:
        player = actionPlayer
        hand = actionGiverHand
    return [player, hand]
    

for i in range(playCount):
    playRule = input().split()
    playRule[0] = int(playRule[0])
    playRule[1] = int(playRule[1])
    if playRule[0] == 1:
        if player == int(playRule[-1]):
            hand = changeHand(hand)
    elif playRule[0] == 2:
        player, hand = handleSecondAction(player, hand, playRule[1], playRule[2], playRule[3])
    
print(f"{player} {hand}")