def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))

        if num_teams >= 2 and num_teams % 2 == 0: 
            #can assume number is always even to simplify scope, but added condition
            break #leaves while loop, won't reach print, goes to return

        print("The minimum number of teams is 2, try again.")

    return num_teams 


def get_team_names(num_teams):
    team_names = []

    for idx in range(num_teams): #0 to the len(num_teams) -1 
        #if len(num_teams) == 5, the range of i will be 0,1,2,3,4
        while True:
            team_name = input(f"Enter the name for team #{idx + 1}: ")
            num_words = len(team_name.split(" ")) #split returns a list
            #len(team_name.split(" ")) > 2:
            if num_words > 2:
                print("Team names may have at most 2 words, try again.")
            elif len(team_name) < 2: #reject any team name characters of zero or one
                print("Team names must have at least 2 characters, try again.")
            else:
                break

        team_names.append(team_name)

    return team_names


def get_number_of_games_played(num_teams):
    while True:
        games_played = int(
            input("Enter the number of games played by each team: "))

        if games_played >= num_teams - 1:
            break

        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

    return games_played


def get_team_wins(team_names, games_played):
    team_wins = []

    for team in team_names:
        while True:
            wins = int(input(f"Enter the number of wins Team {team} had: "))

            if wins > games_played:
                print(
                    f"The maximum number of wins is {games_played}, try again.")
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                break

        team_wins.append((team, wins)) #appends the team name and corresponding wins to list team_wins

    return team_wins


def get_second_item(item):
    return item[1]


num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
sorted_teams = sorted(team_wins, key=get_second_item) #sorts by second element in list team_wins from least amount of wins to the most
game_pairings = []

#[("AA", 0), ("BB", 1), ("CC", 2), ("DD", 3)] 
games_to_make = len(sorted_teams)//2 #number of teams there are divided by 2

for game_num in range(games_to_make):
    home_team = sorted_teams[game_num][0] #homneteam is the team with the fewest wins
    #accessing index 0 because we want the first element in the tuple
    away_team = sorted_teams[num_teams - 1 - game_num][0] #team with the most wins, takes into account what the current game is
    game_pairings.append([home_team, away_team])

for pairing in game_pairings:
    home_team, away_team = pairing
    print(f"Home: {home_team} VS Away: {away_team}")
