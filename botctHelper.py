import random

# Blood these are the available roles in the game
script = [{"id":"clockmaker", "allianment":"townsfolk"},
         {"id":"grandmother", "allianment":"townsfolk"},
         {"id":"librarian", "allianment":"townsfolk"},
         {"id":"empath", "allianment":"townsfolk"},
         {"id":"fortune_teller", "allianment":"townsfolk"},
         {"id":"exorcist", "allianment":"townsfolk"},
         {"id":"flowergirl", "allianment":"townsfolk"},
         {"id":"oracle", "allianment":"townsfolk"},
         {"id":"undertaker", "allianment":"townsfolk"},
         {"id":"artist", "allianment":"townsfolk"},
         {"id":"slayer", "allianment":"townsfolk"},
         {"id":"seamstress", "allianment":"townsfolk"},
         {"id":"monk", "allianment":"townsfolk"},
         {"id":"lunatic", "allianment":"townsfolk"},
         {"id":"mutant", "allianment":"outsider"},
         {"id":"sweetheart", "allianment":"outsider"},
         {"id":"recluse", "allianment":"outsider"},
         {"id":"godfather" , "allianment":"minion"},
         {"id":"assassin", "allianment":"minion"},
         {"id":"scarlet_woman", "allianment":"minion"},
         {"id":"marionette" , "allianment":"minion"},
         {"id":"no_dashii" , "allianment":"demon"},
         {"id":"pukka", "allianment":"demon"},]

def gameinitiation():

    players = []
    gameSetup = []
    
    # Determin how many players are playing
    try:
        num_players = int(input("Enter the number of players: "))
        if num_players < 5 or num_players > 12:
            print("Number of players must be between 5 and 12.")
            return
        
        print("Number of players:", num_players)
         
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    try:
        for i in range(num_players):
            playerName = input(f"Enter the name of player {i+1}: ")
            players.append({"playerName": playerName})
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    
    # Filter script based of roles
    demonRoles = [role for role in script if role['allianment'] == 'demon']
    minionRoles = [role for role in script if role['allianment'] == 'minion']
    outsiderRoles = [role for role in script if role['allianment'] == 'outsider']
    townsfolkRoles = [role for role in script if role['allianment'] == 'townsfolk']

    # Select a random demon from players
    selectedDemon = random.choice(demonRoles)
    demonPlayer = random.choice(players)
    demonPlayer['character'] = selectedDemon
    players.remove(demonPlayer)
    gameSetup.append(demonPlayer)
    print(f"- Demon: {demonPlayer}")

    # Select a random minion from players
    selectedMinion = random.choice(minionRoles)
    minionPlayer = random.choice(players)
    minionPlayer['character'] = selectedMinion
    players.remove(minionPlayer)
    gameSetup.append(minionPlayer)
    print(f"- Minion: {minionPlayer}")
    
    # Select a random outsider from players
    if num_players >= 7:
        selectedOutsider = random.choice(outsiderRoles)
        outsiderPlayer = random.choice(players)
        outsiderPlayer['character'] = selectedOutsider
        players.remove(outsiderPlayer)
        gameSetup.append(outsiderPlayer)
        print(f"- Outsider: {outsiderPlayer}")
    
    for player in players:
        # Select a random townsfolk from players
        selectedTownsfolk = random.choice(townsfolkRoles)
        player['character'] = selectedTownsfolk
        gameSetup.append(player)
        print(f"- Townsfolk: {player}")
    
    print("Game setup:")
    for player in gameSetup:
        print(player)
                
    # Create a markdown file with the player's role and all roles     
    # with open("Blood.md", "w") as md_file:
    #     md_file.write("# Blood on the Clocktower ")
    #     md_file.write("\n## Player Roles\n")
    #     for player in players:
    #         md_file.write(f"- {player['playerName']}: {player['character']['id']}\n")
    #     md_file.write("\n## Script Roles\n")
    #     for role in Roles:
    #         md_file.write(f"- {role['id']}: {role['allianment']}\n")
    
    
    return players;


## Start the program
if __name__ == "__main__":
    playerRoles = gameinitiation()