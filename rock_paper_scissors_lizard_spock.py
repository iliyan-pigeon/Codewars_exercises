def rpsls(pl1, pl2):
    elements_dict = {"scissors": ["paper", "lizard"], "paper": ["rock", "spock"], "rock": ["lizard", "scissors"],
                     "lizard": ["spock", "paper"], "spock": ["scissors", "rock"]}

    if pl1 == pl2:
        return "Draw!"
    elif pl2 in elements_dict[pl1]:
        return "Player 1 Won!"
    elif pl1 in elements_dict[pl2]:
        return "Player 2 Won!"
