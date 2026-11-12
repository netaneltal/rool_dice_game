import random
from gate import *
from Validations import *

def menu():
    print("""
================================
          ROLL DICE
================================

1. Start New Game
2. View Game History
3. View Statistics
4. Exit
       """)

def roll_dice():
    rand = random.randint(1,6)
    return rand
        
    
def play_round(name,number):
    game =  {
            "round": 0,
            "player_dice": 0,
            "computer_dice": 0,
            "winner": ""
            }
    game["round"] = number
    game["player_dice"] = roll_dice()
    game["computer_dice"] = roll_dice()
    if game["player_dice"] > game["computer_dice"]:
         game["winner"] = name
    elif game["player_dice"] == game["computer_dice"]:
         game["winner"] = "draw"
    else: 
         game["winner"] = "computer"  
    return game      

def start_game():
    count_winner_u = 0
    count_winner_c = 0
    count = 1
    rounds = []
    while True:
        name = input("enter your name: ")
        if check_name(name):
            number_round = input("Enter the number of games you would like to play 1-10: ")
            if check_number(number_round) and 0 <int(number_round) < 11:
                
                for game in range(int(number_round)):
                    rounds.append(play_round(name,count))
                    count += 1
                for game in rounds:
                    print(game)
                    if game["winner"] == name:
                        count_winner_u += 1
                    elif game["winner"] == "computer":
                        count_winner_c += 1  
                if count_winner_u > count_winner_c:
                    print("WINNER: ",name)
                elif count_winner_u == count_winner_c:
                        print("WINNER: draw")     
                else:
                    print("WINNER: computer")
                game =    {
                   "player_name": 0,
                   "rounds": 0,
                   "player_score": 0,
                   "computer_score": 0,
                   "winner": 0,
                   "results":  0
                            }
                game["player_name"] = name
                game["rounds"] = number_round
                game["player_score"] = count_winner_u
                game["computer_score"] = count_winner_c
                if count_winner_u > count_winner_c:
                    game["winner"] = name
                elif count_winner_u == count_winner_c:
                    game["winner"] = "draw"   
                else:
                    game["winner"] = "computer"
                game["results"] = rounds
                return game
            else:
                print("Please enter the name and number again.")
                continue
        else:
            print("Please enter the name again.")
            continue
            
def display_game_history():
    lst = load_from_json()
    if lst == []:
        print("No games to display")
    else:    
     for game in lst:
        print("==============================")
        print("Player Name:",game["player_name"])
        print("Number of rounds",game["rounds"])
        print("Player Score:",game["player_score"])
        print("computer Score:",game["computer_score"])
        print("The Winner:",game["winner"])
        print("==============================")

def display_statistics():
    lst = load_from_json()
    if lst == []:
        print("No games to display")
    else:
        count_games = 0
        count_winner_u = 0
        count_winner_c = 0
        count_draw = 0

        for game in lst:
            count_games += 1
            if game["winner"] == "computer":
                count_winner_c += 1
            elif game["winner"] == "draw": 
                count_draw += 1
            else:
                count_winner_u += 1
        print("Number of games played:",count_games)
        print("The number of games the player won:",count_winner_u)  
        print("The number of games the computer won:",count_winner_c)  
        print("Number of games that ended in a draw:",count_draw)  
        print(f"Players' Win Percentage: {count_winner_u * 100 // count_games}%" )          
            
           

def User_Selection():
    while True:
        menu()
        choice = input("Enter your choice: ")      
        if choice == "1":
            game = start_game()
            save_in_json(game)
        elif choice == "2":
            display_game_history()
        elif choice == "3":
            display_statistics() 
        elif choice == "4":
            exit()
        else:
            print("Press a number between 1 and 3; to exit, press 4.")                             





