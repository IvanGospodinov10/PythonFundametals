cards = list(input().split(" "))

team_a_cards = set()
team_b_cards = set()

game_terminate = False

for card_received in cards:
    team, player_number = card_received.split("-")
    if team == "A":
        if player_number not in team_a_cards:
            team_a_cards.add(player_number)
    elif team == "B":
        if player_number not in team_b_cards:
            team_b_cards.add(player_number)

    if 11-len(team_a_cards) < 7 or 11 - len(team_b_cards) < 7:
        game_terminate = True
        break

print(f"Team A - {11 - len(team_a_cards)}; Team B - {11 - len(team_b_cards)}")
if game_terminate:
    print("Game was terminated")



