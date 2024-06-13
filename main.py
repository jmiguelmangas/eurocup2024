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

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.goalsScoredPlayer = 0

class Team:
    def __init__(self, name, players=None):
        if players is None:
            players = []
        self.name = name
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
            print(f"{team.name}: Points={team.points}, Goals Scored={team.goalsScored}, Goals Received={team.goalsReceived}, Goal Difference={team.goalsScored - team.goalsReceived}")

Germany = Team("Germany", flags["Germany"])
Scotland = Team("Scotland", flags["Scotland"])
Switzerland = Team("Switzerland", flags["Switzerland"])
Hungary = Team("Hungary", flags["Hungary"])
Spain = Team("Spain", flags["Spain"])
Croatia = Team("Croatia", flags["Croatia"])
Albania = Team("Albania", flags["Albania"])
Italy = Team("Italy", flags["Italy"])
Slovenia = Team("Slovenia", flags["Slovenia"])
Denmark = Team("Denmark", flags["Denmark"])
Serbia = Team("Serbia", flags["Serbia"])
England = Team("England", flags["England"])
Poland = Team("Poland", flags["Poland"])
Netherlands = Team("Netherlands", flags["Netherlands"])
Austria = Team("Austria", flags["Austria"])
France = Team("France", flags["France"])
Belgium = Team("Belgium", flags["Belgium"])
Slovakia = Team("Slovakia", flags["Slovakia"])
Romania = Team("Romania", flags["Romania"])
Ukraine = Team("Ukraine", flags["Ukraine"])
Turkey = Team("Turkey", flags["Turkey"])
Georgia = Team("Georgia", flags["Georgia"])
Portugal = Team("Portugal", flags["Portugal"])
CzechRepublic = Team("CzechRepublic", flags["CzechRepublic"])

groupA = Group("A", [Germany, Scotland, Switzerland, Hungary])
groupB = Group("B", [Spain, Croatia, Albania, Italy])
groupC = Group("C", [Slovenia, Denmark, Serbia, England])
groupD = Group("D", [Poland, Netherlands, Austria, France])
groupE = Group("E", [Belgium, Slovakia, Romania, Ukraine])
groupF = Group("F", [Turkey, Georgia, Portugal, CzechRepublic])


# Partidos del grupo A
games_groupA = [
    Game(Germany, Scotland, "0-0"),
    Game(Switzerland, Hungary, "0-0"),
    Game(Scotland, Switzerland, "0-0"),
    Game(Hungary, Germany, "0-0"),
    Game(Germany, Switzerland, "0-0"),
    Game(Scotland, Hungary, "0-0")
]

# Partidos del grupo B
games_groupB = [
    Game(Spain, Croatia, "0-0"),
    Game(Italy, Albania, "0-0"),
    Game(Croatia, Albania, "0-0"),
    Game(Italy, Spain, "0-0"),
    Game(Spain, Albania, "0-0"),
    Game(Croatia, Italy, "0-0")
]

# Partidos del grupo C
games_groupC = [
    Game(Slovenia, Denmark, "0-0"),
    Game(Serbia, England, "0-0"),
    Game(England, Slovenia, "0-0"),
    Game(Denmark, Serbia, "0-0"),
    Game(Serbia, Slovenia, "0-0"),
    Game(England, Denmark, "0-0")
]

# Partidos del grupo D
games_groupD = [
    Game(Poland, Netherlands, "0-0"),
    Game(Austria, France, "0-0"),
    Game(France, Poland, "0-0"),
    Game(Netherlands, Austria, "0-0"),
    Game(Austria, Poland, "0-0"),
    Game(France, Netherlands, "0-0")
]

# Partidos del grupo E
games_groupE = [
    Game(Belgium, Slovakia, "0-0"),
    Game(Romania, Ukraine, "0-0"),
    Game(Ukraine, Slovakia, "0-0"),
    Game(Belgium, Romania, "0-0"),
    Game(Slovakia, Romania, "0-0"),
    Game(Ukraine, Belgium, "0-0")
]

# Partidos del grupo F
games_groupF = [
    Game(Turkey, Georgia, "0-0"),
    Game(Portugal, CzechRepublic, "0-0"),
    Game(Georgia, CzechRepublic, "0-0"),
    Game(Portugal, Turkey, "0-0"),
    Game(Turkey, CzechRepublic, "0-0"),
    Game(Portugal, Georgia, "0-0")
]

# Mostrar la clasificación de cada grupo
print("Group A Standings:")
groupA.display_standings()
print("\nGroup B Standings:")
groupB.display_standings()
print("\nGroup C Standings:")
groupC.display_standings()
print("\nGroup D Standings:")
groupD.display_standings()
print("\nGroup E Standings:")
groupE.display_standings()
print("\nGroup F Standings:")
groupF.display_standings()
