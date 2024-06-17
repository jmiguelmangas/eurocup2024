import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
from main import Player, Team, load_players_by_team

# Cargar el archivo CSV
file_path = "./data/euro2024_players.csv"
players_df = pd.read_csv(file_path)

# Cargar los jugadores por equipo
players_by_team = load_players_by_team(players_df)

# Crear equipos con sus banderas y jugadores
flags_folder = "./flags/"
teams = {
    "Germany": Team("Germany", f"{flags_folder}Germany.png", players_by_team["Germany"]),
    "Scotland": Team("Scotland", f"{flags_folder}Scotland.png", players_by_team["Scotland"]),
    "Switzerland": Team("Switzerland", f"{flags_folder}Switzerland.png", players_by_team["Switzerland"]),
    "Hungary": Team("Hungary", f"{flags_folder}Hungary.png", players_by_team["Hungary"]),
    "Spain": Team("Spain", f"{flags_folder}Spain.png", players_by_team["Spain"]),
    "Croatia": Team("Croatia", f"{flags_folder}Croatia.png", players_by_team["Croatia"]),
    "Albania": Team("Albania", f"{flags_folder}Albania.png", players_by_team["Albania"]),
    "Italy": Team("Italy", f"{flags_folder}Italy.png", players_by_team["Italy"]),
    "Slovenia": Team("Slovenia", f"{flags_folder}Slovenia.png", players_by_team["Slovenia"]),
    "Denmark": Team("Denmark", f"{flags_folder}Denmark.png", players_by_team["Denmark"]),
    "Serbia": Team("Serbia", f"{flags_folder}Serbia.png", players_by_team["Serbia"]),
    "England": Team("England", f"{flags_folder}England.png", players_by_team["England"]),
    "Poland": Team("Poland", f"{flags_folder}Poland.png", players_by_team["Poland"]),
    "Netherlands": Team("Netherlands", f"{flags_folder}Netherlands.png", players_by_team["Netherlands"]),
    "Austria": Team("Austria", f"{flags_folder}Austria.png", players_by_team["Austria"]),
    "France": Team("France", f"{flags_folder}France.png", players_by_team["France"]),
    "Belgium": Team("Belgium", f"{flags_folder}Belgium.png", players_by_team["Belgium"]),
    "Slovakia": Team("Slovakia", f"{flags_folder}Slovakia.png", players_by_team["Slovakia"]),
    "Romania": Team("Romania", f"{flags_folder}Romania.png", players_by_team["Romania"]),
    "Ukraine": Team("Ukraine", f"{flags_folder}Ukraine.png", players_by_team["Ukraine"]),
    "Turkey": Team("Turkey", f"{flags_folder}Turkey.png", players_by_team["Turkiye"]),
    "Georgia": Team("Georgia", f"{flags_folder}Georgia.png", players_by_team["Georgia"]),
    "Portugal": Team("Portugal", f"{flags_folder}Portugal.png", players_by_team["Portugal"]),
    "CzechRepublic": Team("CzechRepublic", f"{flags_folder}CzechRepublic.png", players_by_team["Czech Republic"])
}

current_team_index = 0
team_list = list(teams.keys())

# Función para mostrar información de un equipo
def show_team_info(team_name):
    global current_team_index
    current_team_index = team_list.index(team_name)
    display_team_info()

def display_team_info():
    team_name = team_list[current_team_index]
    team = teams[team_name]

    # Limpiar la pantalla
    for widget in root.winfo_children():
        widget.destroy()

    # Mostrar la bandera del equipo en el centro superior
    flag_image = Image.open(team.flag)
    flag_image = flag_image.resize((150, 150), Image.ANTIALIAS)
    flag_photo = ImageTk.PhotoImage(flag_image)
    flag_label = tk.Label(root, image=flag_photo, bg="#0052cc")
    flag_label.image = flag_photo
    flag_label.pack(pady=20)

    # Mostrar la información del equipo
    info_frame = tk.Frame(root, bg="#0052cc")
    info_frame.pack(fill="both", expand=True)

    team_info_label = tk.Label(info_frame, text=f"Equipo: {team.name}\nPuntos: {team.points}\nGoles Anotados: {team.goalsScored}\nGoles Recibidos: {team.goalsReceived}", justify=tk.LEFT, anchor="w", bg="#0052cc", fg="white")
    team_info_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Mostrar los jugadores por posición
    positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
    for i, position in enumerate(positions):
        players_label = tk.Label(info_frame, text=f"{position}s:", justify=tk.LEFT, anchor="w", bg="#0052cc", fg="white")
        players_label.grid(row=i + 1, column=0, padx=10, sticky="w")
        players_text = ""
        for player in team.players:
            if player.position == position:
                players_text += f"- {player.name}, Goles: {player.goalsScoredPlayer}\n"
        players_info_label = tk.Label(info_frame, text=players_text, justify=tk.LEFT, anchor="w", bg="#0052cc", fg="white")
        players_info_label.grid(row=i + 1, column=1, padx=10, sticky="w")

    # Mostrar la tabla de máximos goleadores
    top_scorers = sorted(team.players, key=lambda p: p.goalsScoredPlayer, reverse=True)[:5]
    top_scorers_text = "Máximos Goleadores:\n"
    for player in top_scorers:
        top_scorers_text += f"{player.name} - {player.goalsScoredPlayer} goles\n"
    top_scorers_label = tk.Label(info_frame, text=top_scorers_text, justify=tk.LEFT, anchor="w", bg="#0052cc", fg="white")
    top_scorers_label.grid(row=0, column=2, rowspan=5, padx=10, sticky="n")

    # Botones de navegación
    nav_frame = tk.Frame(root, bg="#0052cc")
    nav_frame.pack(pady=20)
    
    prev_button = tk.Button(nav_frame, text="Atrás", command=show_previous_team)
    prev_button.grid(row=0, column=0, padx=10)
    
    next_button = tk.Button(nav_frame, text="Adelante", command=show_next_team)
    next_button.grid(row=0, column=1, padx=10)
    
    team_label = tk.Label(nav_frame, text=team_name, bg="#0052cc", fg="white")
    team_label.grid(row=0, column=2, padx=10)

def show_previous_team():
    global current_team_index
    current_team_index = (current_team_index - 1) % len(team_list)
    display_team_info()

def show_next_team():
    global current_team_index
    current_team_index = (current_team_index + 1) % len(team_list)
    display_team_info()

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Eurocopa 2024 Tracker")
root.geometry("1920x1080")

# Fondo azul
canvas = tk.Canvas(root, width=1920, height=1080, bg="#0052cc")
canvas.pack(fill="both", expand=True)

# Cargar y mostrar banderas
x_positions = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700]
y_positions = [100, 300, 500, 700, 900]

flag_images = {}
for i, (team_name, team) in enumerate(teams.items()):
    x = x_positions[i % len(x_positions)]
    y = y_positions[i // len(x_positions)]
    image = Image.open(team.flag)
    image = image.resize((80, 80), Image.ANTIALIAS)
    flag_images[team_name] = ImageTk.PhotoImage(image)
    button = tk.Button(root, image=flag_images[team_name], command=lambda tn=team_name: show_team_info(tn))
    button.place(x=x, y=y)

# Ejecutar la interfaz
root.mainloop()
