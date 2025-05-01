import random

def gameinitiation():
    
    num_players = input("Enter the number of players: ")
    print("Number of players:", num_players)
    
    players = []
    for i in range(int(num_players)):
        playername = input(f"Enter the name of player {i+1}: ")
        players.append({"name": playername, "role":  random.choice(Roles)})
    
    return players;

Roles = [{"id":"clockmaker", "allianment":"townsfolk"},
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

## Start the program
if __name__ == "__main__":
    role = gameinitiation()
    
    for player in role:
        print(f"Player: {player['name']}, Role: {player['role']['id']}, Allianment: {player['role']['allianment']}")
        
    # Create a markdown file with the player's role and all roles     
    with open("Blood.md", "w") as md_file:
        md_file.write("# Blood on the Clocktower ")
        md_file.write("\n## Player Roles\n")
        for player in role:
            md_file.write(f"- {player['name']}: {player['role']['id']}\n")
        for r in Roles:
            md_file.write(f"- {r['id']}\n")