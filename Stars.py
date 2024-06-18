import requests
from bs4 import BeautifulSoup
import csv

# Definir la URL de inicio
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Encabezados para las columnas que queremos extraer
HEADERS = ["Name", "Distance", "Mass", "Radius"]

# Lista vacía para almacenar los datos de las estrellas
stars_data = []

# Obtener la página HTML
response = requests.get(START_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Inspeccionar la estructura HTML de la tabla en la página
star_table = soup.find('table', {'class': 'wikitable'})

# Extraer los datos de la tabla
for row in star_table.find_all('tr')[1:]:  # Saltar el encabezado de la tabla
    cells = row.find_all('td')
    
    if len(cells) > 0:
        name = cells[1].text.strip()
        distance = cells[3].text.strip()
        mass = cells[5].text.strip()
        radius = cells[6].text.strip()
        
        stars_data.append([name, distance, mass, radius])

# Guardar los datos en un archivo CSV
with open('brightest_stars.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADERS)
    writer.writerows(stars_data)

print("Datos extraídos y guardados en brightest_stars.csv")
