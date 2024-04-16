# import folium
# import pandas as pd
# from shapely.geometry import Polygon

# # Leer el archivo CSV
# zona_sur = pd.read_csv("zona_sur.csv")

# # Convertir la cadena de geometría en objetos geométricos Polygon
# zona_sur['geometry'] = zona_sur['geometry'].apply(lambda x: Polygon(eval(x)))

# # Crear el mapa de Folium
# m = folium.Map(location=[21.867710886500767, -102.30887026101101], zoom_start=12)

# # Agregar el GeoJSON al mapa
# folium.GeoJson("distrito_local_crdnds.geojson").add_to(m)

# # Agregar el Choropleth para la zona sur
# folium.Choropleth(
#     geo_data=zona_sur,
#     name='choropleth',
#     columns=['nombre', 'None'],
#     fill_color='blue',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     key_on='feature.geometry'
# ).add_to(m)

# # Añadir control de capas
# folium.LayerControl().add_to(m)

# # Guardar el mapa como un archivo HTML
# m.save("mapa_zona_sur.html")

import folium
import pandas as pd

# Lee el archivo GeoJSON
geojson_file = "distrito_local_crdnds.geojson"

# Crea un DataFrame con los datos de las zonas y sus valores
data = pd.DataFrame([
    {"id": "1", "value": 10},
    {"id": "2", "value": 20},
    {"id": "3", "value": 15},
    {"id": "4", "value": 25},
    {"id": "5", "value": 18},
    {"id": "6", "value": 30},
    {"id": "7", "value": 12},
    {"id": "8", "value": 22},
    {"id": "9", "value": 17},
    {"id": "10", "value": 28},
    {"id": "11", "value": 14},
    {"id": "12", "value": 24},
    {"id": "13", "value": 19},
    {"id": "14", "value": 29},
    {"id": "15", "value": 13},
    {"id": "16", "value": 23},
    {"id": "17", "value": 16},
    {"id": "18", "value": 27}
])

# Crea el mapa
m = folium.Map(location=(21.8818, -102.2916), zoom_start=10)

# Crea un choropleth a partir del GeoJSON y los datos
folium.Choropleth(
    geo_data=geojson_file,
    data=data,
    columns=['id', 'value'],
    key_on='feature.properties.ID',  # Actualiza la ruta para encontrar el 'id' en el GeoJSON
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
).add_to(m)

# Guarda el mapa como un archivo HTML
m.save("index.html")


