cards_deck = list(input().split(" "))
shuffles = int(input())

deck_shuffles_cards = int(len(cards_deck) / 2)

for num_of_shuffles in range(shuffles):

    deck_1 = cards_deck[:deck_shuffles_cards]
    deck_2 = cards_deck[deck_shuffles_cards:]
    cards_deck = []
    for index in range(len(deck_1)):
        cards_deck.append(deck_1[index])
        cards_deck.append(deck_2[index])
print(cards_deck)