def declare_winner(player1, player2):
    '''
    param player1: (string) representing 5 cards
    param player2: (string) representing 5 cards
    return: (int) 1 if player1 wins, 2 if player 2 wins, 0 if draw
    '''
    result = 0

    win1 = 1
    win2 = 2
    draw = 0

    Suite = 'HCSD'
    Cards = "A23456789TJQK"
    hand1 = player1.split(" ")
    hand2 = player2.split(" ")
    for card in hand1:
        print card
    for card in hand2:
        print card

    return result
'''
The Hand ranking (best to worst)

    Five of a kind
    Straight Flush
    Four of a Kind
    Full House
    Flush
    Straight
    Three of a Kind
    Two pair
    One Pair
    High Card


https://en.wikipedia.org/wiki/List_of_poker_hand_categories

'''
royal_flush1 = "AH KH QH JH TH" # Royal flush with hearts
royal_flush2 = "AC KC QC JC TC" # Royal flush with clubs
trips1 = "8H 7C 8C 9H 8D" # three of a kind 8s
trips2 =  "5S 5H 9D 5D TS" # three of a kind 5s

declare_winner(trips1,royal_flush1)


'''
test.describe('Example Test Cases')
royal_flush1 = "AH KH QH JH TH" # Royal flush with hearts
royal_flush2 = "AC KC QC JC TC" # Royal flush with clubs
trips1 = "8H 7C 8C 9H 8D" # three of a kind 8s
trips2 =  "5S 5H 9D 5D TS" # three of a kind 5s

# Royal flush vs Royal flush => 0
test.assert_equals(declare_winner(royal_flush1, royal_flush2), 0, "Both players have royal flush so it is a draw!")

# Royal flush vs three of a kind => 1
test.assert_equals(declare_winner(royal_flush1, trips1), 1, "Royal flush beats three of a kind, player 1 wins!")

# Three of a kind (5s) vs Three of a kind (8s) => 2
test.assert_equals(declare_winner(trips2, trips1), 2, "Three of a kind fives loses to three of a kind eights, player 2 wins!")

# Three of a kind (8s) vs Three of a kind (5s) = > 1
test.assert_equals(declare_winner(trips1, trips2), 1, "Three of a kind eights beats thre
'''