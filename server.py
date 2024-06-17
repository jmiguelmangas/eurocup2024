from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import pandas as pd
import json
import os

app = Flask(__name__)
CORS(app)

# Cargar datos desde CSV
file_path = "./data/euro2024_players.csv"
players_df = pd.read_csv(file_path)

# Función para cargar jugadores por equipo
def load_players_by_team(players_df):
    teams_dict = {}
    for index, row in players_df.iterrows():
        team_name = row['Country']
        if team_name == 'Turkiye':
            team_name = 'Turkey'
        elif team_name == 'Czech Republic':
            team_name = 'CzechRepublic'
        player = {"name": row['Name'], "position": row['Position'], "goals": row['Goals']}
        if team_name not in teams_dict:
            teams_dict[team_name] = []
        teams_dict[team_name].append(player)
    return teams_dict

flags = {
    "Germany": "Germany.png",
    "Scotland": "Scotland.png",
    "Switzerland": "Switzerland.png",
    "Hungary": "Hungary.png",
    "Spain": "Spain.png",
    "Croatia": "Croatia.png",
    "Albania": "Albania.png",
    "Italy": "Italy.png",
    "Slovenia": "Slovenia.png",
    "Denmark": "Denmark.png",
    "Serbia": "Serbia.png",
    "England": "England.png",
    "Poland": "Poland.png",
    "Netherlands": "Netherlands.png",
    "Austria": "Austria.png",
    "France": "France.png",
    "Belgium": "Belgium.png",
    "Slovakia": "Slovakia.png",
    "Romania": "Romania.png",
    "Ukraine": "Ukraine.png",
    "Turkey": "Turkey.png",
    "Georgia": "Georgia.png",
    "Portugal": "Portugal.png",
    "CzechRepublic": "CzechRepublic.png"
}

players_by_team = load_players_by_team(players_df)

# Cargar los datos de los partidos desde matches.json
with open("./data/matches.json", "r") as file:
    games = json.load(file)

teams_stats = {
    "Group A": {
        "Germany": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Scotland": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Switzerland": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Hungary": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
    },
    "Group B": {
        "Spain": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Croatia": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Albania": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Italy": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
    },
    "Group C": {
        "Slovenia": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Denmark": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Serbia": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "England": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
    },
    "Group D": {
        "Poland": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Netherlands": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Austria": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "France": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
    },
    "Group E": {
        "Belgium": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Slovakia": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Romania": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Ukraine": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
    },
    "Group F": {
        "Turkey": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Georgia": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "Portugal": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
        "CzechRepublic": {"played": 0, "scored": 0, "conceded": 0, "points": 0},
    },
}

# Ruta para obtener los datos de todos los equipos
@app.route('/teams', methods=['GET'])
def get_teams():
    teams = {}
    for team, players in players_by_team.items():
        teams[team] = {
            "flag": flags[team],
            "players": players
        }
    return jsonify(teams)

# Ruta para obtener la clasificación de los grupos
@app.route('/standings', methods=['GET'])
def get_standings():
    standings = {}
    for group, teams in teams_stats.items():
        standings[group] = sorted(
            [
                {
                    "team": team,
                    "flag": flags[team],
                    "played": stats["played"],
                    "scored": stats["scored"],
                    "conceded": stats["conceded"],
                    "goal_difference": stats["scored"] - stats["conceded"],
                    "points": stats["points"]
                }
                for team, stats in teams.items()
            ],
            key=lambda x: (x["points"], x["goal_difference"], x["scored"]),
            reverse=True
        )
    return jsonify(standings)

# Ruta para obtener los partidos de los grupos
@app.route('/matches', methods=['GET'])
def get_matches():
    return jsonify(games)

# Ruta para actualizar los resultados de los partidos
@app.route('/matches', methods=['POST'])
def update_matches():
    data = request.json
    group = data['group']
    match_index = data['match_index']
    score = data['score']

    # Actualizar el resultado del partido
    games[group][match_index]['score'] = score

    # Guardar los cambios en matches.json
    with open("./data/matches.json", "w") as file:
        json.dump(games, file, indent=4)

    # Recalcular las estadísticas de los equipos
    recalculate_standings()

    return jsonify({"message": "Match updated successfully"})

def recalculate_standings():
    # Reiniciar estadísticas
    for group, teams in teams_stats.items():
        for team in teams:
            teams_stats[group][team] = {"played": 0, "scored": 0, "conceded": 0, "points": 0}

    # Recalcular estadísticas
    for group, matches in games.items():
        for match in matches:
            if match['score'] is None:
                continue
            team1 = match['team1']
            team2 = match['team2']
            score = match['score']
            goals1, goals2 = map(int, score.split('-'))

            teams_stats[group][team1]['played'] += 1
            teams_stats[group][team2]['played'] += 1
            teams_stats[group][team1]['scored'] += goals1
            teams_stats[group][team2]['scored'] += goals2
            teams_stats[group][team1]['conceded'] += goals2
            teams_stats[group][team2]['conceded'] += goals1

            if goals1 > goals2:
                teams_stats[group][team1]['points'] += 3
            elif goals2 > goals1:
                teams_stats[group][team2]['points'] += 3
            else:
                teams_stats[group][team1]['points'] += 1
                teams_stats[group][team2]['points'] += 1

# Ruta para servir las imágenes de las banderas
@app.route('/flags/<path:filename>')
def get_flag(filename):
    return send_from_directory('flags', filename)

if __name__ == '__main__':
    recalculate_standings()  # Inicializa las estadísticas
    app.run(debug=True)
