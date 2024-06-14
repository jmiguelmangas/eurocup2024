import pandas as pd
import json
# Cargar el archivo CSV
file_path = "./data/euro2024_players.csv"
players_df = pd.read_csv(file_path)

def load_players_by_team(players_df):
    teams_dict = {}
    for index, row in players_df.iterrows():
        team_name = row['Country']
        player = Player(row['Name'], row['Position'])
        if team_name not in teams_dict:
            teams_dict[team_name] = []
        teams_dict[team_name].append(player)
    return teams_dict

flags = {
    "Germany": "https://upload.wikimedia.org/wikipedia/en/b/ba/Flag_of_Germany.svg",
    "Scotland": "https://upload.wikimedia.org/wikipedia/commons/1/10/Flag_of_Scotland.svg",
    "Switzerland": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Switzerland.svg",
    "Hungary": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Flag_of_Hungary.svg",
    "Spain": "https://upload.wikimedia.org/wikipedia/en/9/9a/Flag_of_Spain.svg",
    "Croatia": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Croatia.svg",
    "Albania": "https://upload.wikimedia.org/wikipedia/commons/3/36/Flag_of_Albania.svg",
    "Italy": "https://upload.wikimedia.org/wikipedia/en/0/03/Flag_of_Italy.svg",
    "Slovenia": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Flag_of_Slovenia.svg",
    "Denmark": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Denmark.svg",
    "Serbia": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Flag_of_Serbia.svg",
    "England": "https://upload.wikimedia.org/wikipedia/en/b/be/Flag_of_England.svg",
    "Poland": "https://upload.wikimedia.org/wikipedia/en/1/12/Flag_of_Poland.svg",
    "Netherlands": "https://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg",
    "Austria": "https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_Austria.svg",
    "France": "https://upload.wikimedia.org/wikipedia/en/c/c3/Flag_of_France.svg",
    "Belgium": "https://upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Belgium.svg",
    "Slovakia": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Flag_of_Slovakia.svg",
    "Romania": "https://upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Romania.svg",
    "Ukraine": "https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Ukraine.svg",
    "Turkey": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg",
    "Georgia": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_Georgia.svg",
    "Portugal": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Portugal.svg",
    "CzechRepublic": "https://upload.wikimedia.org/wikipedia/commons/c/cb/Flag_of_the_Czech_Republic.svg"
}


class Eurocup:
    def __init__(self, groups, groupmatches):
        self.groups = groups
        self.groupmatches = groupmatches
        self.eliminatorydraw = []

    def determine_qualifiers(self):
        firsts = []
        seconds = []
        thirds = []

        for group in self.groups:
            sorted_teams = sorted(group.teams, key=lambda x: (x.points, x.goalsScored - x.goalsReceived, x.goalsScored), reverse=True)
            firsts.append(sorted_teams[0])
            seconds.append(sorted_teams[1])
            thirds.append(sorted_teams[2])

        best_thirds = sorted(thirds, key=lambda x: (x.points, x.goalsScored - x.goalsReceived, x.goalsScored), reverse=True)[:3]

        return firsts, seconds, best_thirds

    def organize_eliminatory(self):
        firsts, seconds, best_thirds = self.determine_qualifiers()

        # Configure the eliminatory draw based on the image
        self.eliminatorydraw = [
            (firsts[0], seconds[1]),  # 1st A vs 2nd B
            (firsts[1], best_thirds[0]),  # 1st B vs 3rd: A/D/E/F
            (firsts[2], best_thirds[1]),  # 1st C vs 3rd: D/E/F
            (firsts[3], seconds[2]),  # 1st D vs 2nd E
            (firsts[4], seconds[3]),  # 1st E vs 2nd D
            (firsts[5], best_thirds[2]),  # 1st F vs 3rd: A/B/C
            (seconds[0], seconds[4]),  # 2nd A vs 2nd C
            (seconds[5], firsts[0])   # 2nd F vs 1st A
        ]

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.goalsScoredPlayer = 0

class Team:
    def __init__(self, name, flag, players=None):
        if players is None:
            players = []
        self.name = name
        self.flag = flag
        self.points = 0
        self.goalsScored = 0
        self.goalsReceived = 0
        self.players = players

class Game:
    def __init__(self, team1, team2, score="0-0", scorers_team1=None, scorers_team2=None):
        self.team1 = team1
        self.team2 = team2
        self.score = score
        self.scorers_team1 = scorers_team1 if scorers_team1 is not None else []
        self.scorers_team2 = scorers_team2 if scorers_team2 is not None else []

        self.goalsteam1, self.goalsteam2 = map(int, score.split("-"))
        if self.goalsteam1 > self.goalsteam2:
            self.team1.points += 3
        elif self.goalsteam2 > self.goalsteam1:
            self.team2.points += 3
        else:
            self.team1.points += 1
            self.team2.points += 1

        self.team1.goalsScored += self.goalsteam1
        self.team1.goalsReceived += self.goalsteam2
        self.team2.goalsScored += self.goalsteam2
        self.team2.goalsReceived += self.goalsteam1

        for player in self.scorers_team1:
            player.goalsScoredPlayer += 1

        for player in self.scorers_team2:
            player.goalsScoredPlayer += 1

class Group:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
    
    def display_standings(self):
        sorted_teams = sorted(self.teams, key=lambda x: (x.points, x.goalsScored - x.goalsReceived, x.goalsScored), reverse=True)
        for team in sorted_teams:
            print(f"{team.name} ({team.flag}): Points={team.points}, Goals Scored={team.goalsScored}, Goals Received={team.goalsReceived}, Goal Difference={team.goalsScored - team.goalsReceived}")


# Cargar los jugadores por equipo
players_by_team = load_players_by_team(players_df)

# Crear equipos con sus banderas y jugadores
teams = {
    "Germany": Team("Germany", flags["Germany"], players_by_team["Germany"]),
    "Scotland": Team("Scotland", flags["Scotland"], players_by_team["Scotland"]),
    "Switzerland": Team("Switzerland", flags["Switzerland"], players_by_team["Switzerland"]),
    "Hungary": Team("Hungary", flags["Hungary"], players_by_team["Hungary"]),
    "Spain": Team("Spain", flags["Spain"], players_by_team["Spain"]),
    "Croatia": Team("Croatia", flags["Croatia"], players_by_team["Croatia"]),
    "Albania": Team("Albania", flags["Albania"], players_by_team["Albania"]),
    "Italy": Team("Italy", flags["Italy"], players_by_team["Italy"]),
    "Slovenia": Team("Slovenia", flags["Slovenia"], players_by_team["Slovenia"]),
    "Denmark": Team("Denmark", flags["Denmark"], players_by_team["Denmark"]),
    "Serbia": Team("Serbia", flags["Serbia"], players_by_team["Serbia"]),
    "England": Team("England", flags["England"], players_by_team["England"]),
    "Poland": Team("Poland", flags["Poland"], players_by_team["Poland"]),
    "Netherlands": Team("Netherlands", flags["Netherlands"], players_by_team["Netherlands"]),
    "Austria": Team("Austria", flags["Austria"], players_by_team["Austria"]),
    "France": Team("France", flags["France"], players_by_team["France"]),
    "Belgium": Team("Belgium", flags["Belgium"], players_by_team["Belgium"]),
    "Slovakia": Team("Slovakia", flags["Slovakia"], players_by_team["Slovakia"]),
    "Romania": Team("Romania", flags["Romania"], players_by_team["Romania"]),
    "Ukraine": Team("Ukraine", flags["Ukraine"], players_by_team["Ukraine"]),
    "Turkey": Team("Turkey", flags["Turkey"], players_by_team["Turkiye"]),
    "Georgia": Team("Georgia", flags["Georgia"], players_by_team["Georgia"]),
    "Portugal": Team("Portugal", flags["Portugal"], players_by_team["Portugal"]),
    "CzechRepublic": Team("CzechRepublic", flags["CzechRepublic"], players_by_team["Czech Republic"])
}
# Creación de los grupos
groupA = Group("A", [teams["Germany"], teams["Scotland"], teams["Switzerland"], teams["Hungary"]])
groupB = Group("B", [teams["Spain"], teams["Croatia"], teams["Albania"], teams["Italy"]])
groupC = Group("C", [teams["Slovenia"], teams["Denmark"], teams["Serbia"], teams["England"]])
groupD = Group("D", [teams["Poland"], teams["Netherlands"], teams["Austria"], teams["France"]])
groupE = Group("E", [teams["Belgium"], teams["Slovakia"], teams["Romania"], teams["Ukraine"]])
groupF = Group("F", [teams["Turkey"], teams["Georgia"], teams["Portugal"], teams["CzechRepublic"]])

AllGroups = [groupA, groupB, groupC, groupD, groupE, groupF]

# Partidos del grupo A
games_groupA = [
    Game(teams["Germany"], teams["Scotland"], "0-0"),
    Game(teams["Switzerland"], teams["Hungary"], "0-0"),
    Game(teams["Scotland"], teams["Switzerland"], "0-0"),
    Game(teams["Hungary"], teams["Germany"], "0-0"),
    Game(teams["Germany"], teams["Switzerland"], "0-0"),
    Game(teams["Scotland"], teams["Hungary"], "0-0")
]

# Partidos del grupo B
games_groupB = [
    Game(teams["Spain"], teams["Croatia"], "0-0"),
    Game(teams["Italy"], teams["Albania"], "0-0"),
    Game(teams["Croatia"], teams["Albania"], "0-0"),
    Game(teams["Italy"], teams["Spain"], "0-0"),
    Game(teams["Spain"], teams["Albania"], "0-0"),
    Game(teams["Croatia"], teams["Italy"], "0-0")
]

# Partidos del grupo C
games_groupC = [
    Game(teams["Slovenia"], teams["Denmark"], "0-0"),
    Game(teams["Serbia"], teams["England"], "0-0"),
    Game(teams["England"], teams["Slovenia"], "0-0"),
    Game(teams["Denmark"], teams["Serbia"], "0-0"),
    Game(teams["Serbia"], teams["Slovenia"], "0-0"),
    Game(teams["England"], teams["Denmark"], "0-0")
]

# Partidos del grupo D
games_groupD = [
    Game(teams["Poland"], teams["Netherlands"], "0-0"),
    Game(teams["Austria"], teams["France"], "0-0"),
    Game(teams["France"], teams["Poland"], "0-0"),
    Game(teams["Netherlands"], teams["Austria"], "0-0"),
    Game(teams["Austria"], teams["Poland"], "0-0"),
    Game(teams["France"], teams["Netherlands"], "0-0")
]

# Partidos del grupo E
games_groupE = [
    Game(teams["Belgium"], teams["Slovakia"], "0-0"),
    Game(teams["Romania"], teams["Ukraine"], "0-0"),
    Game(teams["Ukraine"], teams["Slovakia"], "0-0"),
    Game(teams["Belgium"], teams["Romania"], "0-0"),
    Game(teams["Slovakia"], teams["Romania"], "0-0"),
    Game(teams["Ukraine"], teams["Belgium"], "0-0")
]

# Partidos del grupo F
games_groupF = [
    Game(teams["Turkey"], teams["Georgia"], "0-0"),
    Game(teams["Portugal"], teams["CzechRepublic"], "0-0"),
    Game(teams["Georgia"], teams["CzechRepublic"], "0-0"),
    Game(teams["Portugal"], teams["Turkey"], "0-0"),
    Game(teams["Turkey"], teams["CzechRepublic"], "0-0"),
    Game(teams["Portugal"], teams["Georgia"], "0-0")
]
# Crear una instancia de Eurocup con los grupos y los partidos de grupo
eurocup2024 = Eurocup(AllGroups, [games_groupA, games_groupB, games_groupC, games_groupD, games_groupE, games_groupF])

# Determinar los equipos clasificados y organizar el cuadro eliminatorio
eurocup2024.organize_eliminatory()

# Mostrar la clasificación de cada grupo
for group in eurocup2024.groups:
    print(f"\n{group.name} Standings:")
    group.display_standings()