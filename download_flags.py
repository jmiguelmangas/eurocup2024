import os
import requests
import cairosvg

# Diccionario de URLs de banderas
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

# Crear carpeta para guardar las banderas
if not os.path.exists('flags'):
    os.makedirs('flags')

# Descargar y convertir las banderas
for country, url in flags.items():
    svg_content = requests.get(url).content
    svg_path = f"./flags/{country}.svg"
    png_path = f"./flags/{country}.png"
    with open(svg_path, 'wb') as svg_file:
        svg_file.write(svg_content)
    cairosvg.svg2png(url=svg_path, write_to=png_path)
    os.remove(svg_path)  # Elimina el archivo SVG después de la conversión
