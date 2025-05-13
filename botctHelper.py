import random

# Blood these are the available roles in the game
script = [{"id": "clockmaker", "allianment": "townsfolk"},
          {"id": "grandmother", "allianment": "townsfolk"},
          {"id": "librarian", "allianment": "townsfolk"},
          {"id": "empath", "allianment": "townsfolk"},
          {"id": "fortune_teller", "allianment": "townsfolk"},
          {"id": "exorcist", "allianment": "townsfolk"},
          {"id": "flowergirl", "allianment": "townsfolk"},
          {"id": "oracle", "allianment": "townsfolk"},
          {"id": "undertaker", "allianment": "townsfolk"},
          {"id": "artist", "allianment": "townsfolk"},
          {"id": "slayer", "allianment": "townsfolk"},
          {"id": "seamstress", "allianment": "townsfolk"},
          {"id": "monk", "allianment": "townsfolk"},
          {"id": "lunatic", "allianment": "townsfolk"},
          {"id": "mutant", "allianment": "outsider"},
          {"id": "sweetheart", "allianment": "outsider"},
          {"id": "recluse", "allianment": "outsider"},
          {"id": "godfather", "allianment": "minion"},
          {"id": "assassin", "allianment": "minion"},
          {"id": "scarlet_woman", "allianment": "minion"},
          {"id": "marionette", "allianment": "minion"},
          {"id": "no_dashii", "allianment": "demon"},
          {"id": "pukka", "allianment": "demon"}, ]

nightOrder = {
    "firstNightOrder": [
        {"character": "lord_of_typhon", "order": 1},
        {"character": "kazali", "order": 2},
        {"character": "apprentice", "order": 3},
        {"character": "barista", "order": 4},
        {"character": "bureaucrate", "order": 5},
        {"character": "thief", "order": 6},
        {"character": "boffin", "order": 7},
        {"character": "philosopher", "order": 8},
        {"character": "alchemist", "order": 9},
        {"character": "poppy_grower", "order": 10},
        {"character": "yaggababble", "order": 11},
        {"character": "magician", "order": 12},
        {"character": "minion_info", "order": 13},
        {"character": "snitch", "order": 14},
        {"character": "lunatic", "order": 15},
        {"character": "summoner", "order": 16},
        {"character": "demon_info_and_bluffs", "order": 17},
        {"character": "king", "order": 18},
        {"character": "sailor", "order": 19},
        {"character": "marionette", "order": 20},
        {"character": "engineer", "order": 21},
        {"character": "preacher", "order": 22},
        {"character": "lil_monsta", "order": 23},
        {"character": "lleech", "order": 24},
        {"character": "xaan", "order": 25},
        {"character": "poisoner", "order": 26},
        {"character": "widow", "order": 27},
        {"character": "courtier", "order": 28},
        {"character": "wizard", "order": 29},
        {"character": "snake_charmer", "order": 30},
        {"character": "godfather", "order": 31},
        {"character": "organ_grinder", "order": 32},
        {"character": "devils_advocate", "order": 33},
        {"character": "evil_twin", "order": 34},
        {"character": "witch", "order": 35},
        {"character": "cerenovus", "order": 36},
        {"character": "fearmonger", "order": 37},
        {"character": "harpy", "order": 38},
        {"character": "mezepheles", "order": 39},
        {"character": "pukka", "order": 40},
        {"character": "pixie", "order": 41},
        {"character": "huntsman", "order": 42},
        {"character": "damsel", "order": 43},
        {"character": "amnesiac", "order": 44},
        {"character": "washerwoman", "order": 45},
        {"character": "librarian", "order": 46},
        {"character": "investigator", "order": 47},
        {"character": "chef", "order": 48},
        {"character": "empath", "order": 49},
        {"character": "fortune_teller", "order": 50},
        {"character": "butler", "order": 51},
        {"character": "grandmother", "order": 52},
        {"character": "clockmaker", "order": 53},
        {"character": "dreamer", "order": 54},
        {"character": "seamstress", "order": 55},
        {"character": "steward", "order": 56},
        {"character": "knight", "order": 57},
        {"character": "noble", "order": 58},
        {"character": "balloonist", "order": 59},
        {"character": "shugenja", "order": 60},
        {"character": "village_idiot", "order": 61},
        {"character": "bounty_hunter", "order": 62},
        {"character": "nightwatchman", "order": 63},
        {"character": "cult_leader", "order": 64},
        {"character": "spy", "order": 65},
        {"character": "ogre", "order": 66},
        {"character": "high_priestess", "order": 67},
        {"character": "general", "order": 68},
        {"character": "chambermaid", "order": 69},
        {"character": "mathematician", "order": 70}
    ],
    "nightOrder": [
        {"character": "barista", "order": 1},
        {"character": "bone_collector", "order": 2},
        {"character": "bureaucrate", "order": 3},
        {"character": "harlot", "order": 4},
        {"character": "thief", "order": 5},
        {"character": "philosopher", "order": 6},
        {"character": "poppy_grower", "order": 7},
        {"character": "sailor", "order": 8},
        {"character": "engineer", "order": 9},
        {"character": "preacher", "order": 10},
        {"character": "xaan", "order": 11},
        {"character": "poisoner", "order": 12},
        {"character": "courtier", "order": 13},
        {"character": "inkeeper", "order": 14},
        {"character": "wizard", "order": 15},
        {"character": "gambler", "order": 16},
        {"character": "acrobat", "order": 17},
        {"character": "snake_charmer", "order": 18},
        {"character": "monk", "order": 19},
        {"character": "organ_grinder", "order": 20},
        {"character": "devils_advocate", "order": 21},
        {"character": "witch", "order": 22},
        {"character": "cerenovus", "order": 23},
        {"character": "pit_hag", "order": 24},
        {"character": "fearmonger", "order": 25},
        {"character": "harpy", "order": 26},
        {"character": "mezepheles", "order": 27},
        {"character": "scarlet_woman", "order": 28},
        {"character": "summoner", "order": 29},
        {"character": "lunatic", "order": 30},
        {"character": "exorcist", "order": 31},
        {"character": "lycanthrope", "order": 32},
        {"character": "legion", "order": 33},
        {"character": "imp", "order": 34},
        {"character": "zombuul", "order": 35},
        {"character": "pukka", "order": 36},
        {"character": "shabaloth", "order": 37},
        {"character": "po", "order": 38},
        {"character": "fang_gu", "order": 39},
        {"character": "no_dashii", "order": 40},
        {"character": "vortox", "order": 41},
        {"character": "lord_of_typhon", "order": 42},
        {"character": "vigormortis", "order": 43},
        {"character": "ojo", "order": 44},
        {"character": "al_hadikhia", "order": 45},
        {"character": "lleech", "order": 46},
        {"character": "lil_monsta", "order": 47},
        {"character": "yaggababble", "order": 48},
        {"character": "kazali", "order": 49},
        {"character": "assassin", "order": 50},
        {"character": "godfather", "order": 51},
        {"character": "gossip", "order": 52},
        {"character": "hatter", "order": 53},
        {"character": "barber", "order": 54},
        {"character": "sweetheart", "order": 55},
        {"character": "sage", "order": 56},
        {"character": "banshee", "order": 57},
        {"character": "professor", "order": 58},
        {"character": "choirboy", "order": 59},
        {"character": "huntsman", "order": 60},
        {"character": "damsel", "order": 61},
        {"character": "amnesiac", "order": 62},
        {"character": "farmer", "order": 63},
        {"character": "tinker", "order": 64},
        {"character": "moonchild", "order": 65},
        {"character": "grandmother", "order": 66},
        {"character": "ravenkeeper", "order": 67},
        {"character": "empath", "order": 68},
        {"character": "fortune_teller", "order": 69},
        {"character": "undertaker", "order": 70},
        {"character": "dreamer", "order": 71},
        {"character": "flowergirl", "order": 72},
        {"character": "town_crier", "order": 73},
        {"character": "oracle", "order": 74},
        {"character": "seamstress", "order": 75},
        {"character": "juggler", "order": 76},
        {"character": "balloonist", "order": 77},
        {"character": "village_idiot", "order": 78},
        {"character": "king", "order": 79},
        {"character": "bounty_hunter", "order": 80},
        {"character": "nightwatchman", "order": 81},
        {"character": "cult_leader", "order": 82},
        {"character": "butler", "order": 83},
        {"character": "spy", "order": 84},
        {"character": "high_priestess", "order": 85},
        {"character": "general", "order": 86},
        {"character": "chambermaid", "order": 87},
        {"character": "mathematician", "order": 88}
    ]
}

def scriptNightOrderSetup(chosenScript):

    scriptFirstOrder = []

    for character in nightOrder["firstNightOrder"]:
        if character["character"] == chosenScript[0]:
            scriptFirstOrder.append(character)

    return scriptFirstOrder


def gameInit():
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
        0
        return

    try:
        for i in range(num_players):
            playerName = input(f"Enter the name of player {i + 1}: ")
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
        townsfolkRoles.remove(selectedTownsfolk)
        player['character'] = selectedTownsfolk
        gameSetup.append(player)
        print(f"- Townsfolk: {player}")

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


def writeGameInit(playerRoles):
    # Create a markdown file with the player's role and all roles     
    with open("Blood.md", "w") as md_file:
        md_file.write("# Blood on the Clocktower ")
        md_file.write("\n## Player Roles\n")
        for player in playerRoles:
            md_file.write(f"- {player['playerName']}: {player['character']['id']}\n")
        md_file.write("\n## Script Roles\n")
        for role in script:
            md_file.write(f"- {role['id']}: {role['allianment']}\n")
        md_file.write("\n## First Night order\n")


## Start the program
if __name__ == "__main__":
    playerRoles = gameInit()

    writeGameInit(playerRoles)

    print(scriptNightOrderSetup(script))

