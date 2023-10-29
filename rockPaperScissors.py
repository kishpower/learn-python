# objects are dicts

import random
def get_choices():
    player_choice = input("Select (rock,paper,scissors): ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options) 
    print({"player_choice":player_choice,"computer_choice":computer_choice})
    return {"player_choice":player_choice,"computer_choice":computer_choice}

def check_win(choices):
    result = {"draw" : "Its a draw","computer" : "computer won!","player": "player won!"}
    if(choices["player_choice"] == "rock"):
        if(choices["computer_choice"] == "rock"):
            return result["draw"] 
        if(choices["computer_choice"] == "paper"):
            return result["computer"] 
        if(choices["computer_choice"] == "scissors"):
            return result["player"]

    if(choices["player_choice"] == "paper"):
        if(choices["computer_choice"] == "rock"):
            return result["player"]
        if(choices["computer_choice"] == "paper"):
            return result["draw"]
        if(choices["computer_choice"] == "scissors"):
            return result.scissors

    if(choices["player_choice"] == "scissors"):
        if(choices["computer_choice"] == "rock"):
            return result["computer"]
        if(choices["computer_choice"] == "paper"):
            return result["player"]
        if(choices["computer_choice"] == "scissors"):
            return result["draw"]

    return ValueError; 

# --- optimised code 
# def check_win(choices):
#     result = {"rock": {"rock": "draw", "paper": "computer", "scissors": "player"},
#               "paper": {"rock": "player", "paper": "draw", "scissors": "computer"},
#               "scissors": {"rock": "computer", "paper": "player", "scissors": "draw"}}

#     player_choice = choices["player_choice"]
#     computer_choice = choices["computer_choice"]

#     if player_choice in result and computer_choice in result[player_choice]:
#         return result[player_choice][computer_choice]
#     else:
#         raise ValueError("Invalid choices")

print(check_win(get_choices()))