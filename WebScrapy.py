# Import necessary libraries
import os          # Para manejo de archivos (verificar existencia, tamaño, etc.)
import csv         # Para leer y escribir archivos CSV
import requests    # Para hacer peticiones HTTP (usando la API)
from pprint import pprint  # Para imprimir resultados en consola de forma legible


# Establece la bandera VERBOSE en True para imprimir información sobre cada solicitud a la API
VERBOSE = True

# Define los endpoints de la API para obtener los años, productos y países disponibles
api_list_template = 'https://api.iea.org/mes/list/%s'

# Define el endpoint de la API para obtener datos mensuales de un país, año, mes y producto específicos
api_information_template = 'https://api.iea.org/mes/latest/month?COUNTRY=%s&YEAR=%s&MONTH=%s&PRODUCT=%s&share=true'

# Obtiene las listas de años, productos y países disponibles desde la API
years = requests.get(api_list_template % 'YEAR').json()
years = [int(y) for y in years if int(y) >= 2020]  # Filtrar años desde 2020 en adelante
products = requests.get(api_list_template % 'PRODUCT').json()
countries = requests.get(api_list_template % 'COUNTRY').json()

# Lista de países de América para filtrar
paises_america = ['Argentina', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Mexico', 'United States']

# Define la fila de encabezado para el archivo CSV que almacenará los datos
header = [
    'COUNTRY',            # Nombre del país
    'YEAR',               # Año del punto de datos
    'MONTH',              # Mes del punto de datos como número (1-12)
    'PRODUCT',            # Tipo de producto energético (por ejemplo, Hydro, Wind, Solar)
    'VALUE',              # Cantidad de electricidad generada en gigavatios-hora (GWh)
    'yearToDate',         # Cantidad de electricidad generada en el año actual hasta el mes actual en GWh
]

# Si el archivo CSV está vacío
index_last_year, index_last_month, index_last_country, index_last_product = 0, 1, 0, 0

# Abre el archivo CSV para escritura
with open('DataSet.csv', 'a+', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)

    # Extrae los datos y los escribe en el archivo CSV
    for year in years[index_last_year:]:
        for month in range(index_last_month, 13):
            for country in countries[index_last_country:]:

                # Guardamos una copia legible del nombre del país antes de codificarlo para la URL
                country_name = country.strip().replace("'", "")

                # Solo continuar si el país está en la lista de América
                if country_name not in paises_america:
                    continue

                # Reemplaza apóstrofes en el nombre del país con %27 para crear una URL válida
                country = country.replace('\'', '%27')

                for product in products[index_last_product:]:
                    # Envía una solicitud a la API para obtener datos mensuales del país, año, mes y producto actuales
                    response = requests.get(
                        api_information_template % (country, year, month, product)
                    )

                    # Verifica si la respuesta de la API fue exitosa
                    if response.ok:
                        # Analiza la respuesta en formato JSON
                        response = response.json()

                        # Crea un diccionario con los datos que se escribirán en el archivo CSV
                        result = dict()

                        # Extrae los datos de la respuesta y los añade al diccionario, omitiendo 'CODE_TIME'
                        for key, value in response['latest'][0].items():
                            if key not in ['CODE_TIME', 'TIME', 'MONTH_NAME', 'DISPLAY_ORDER']:
                                result[key] = value
 
                        # Añade datos acumulados del año actual y anterior, así como participación
                        result['yearToDate'] = response['yearToDate']

                        # Escribe el diccionario en el archivo CSV
                        writer.writerow(result)

                        # Si el modo verbose está activado, imprime el resultado de este mes
                        if VERBOSE:
                            pprint(result, sort_dicts=False)
                            print('_________________________')

                index_last_product = 0
                index_last_month = 1
                index_last_country = 0

# NOTA: Este código puede tardar un tiempo en ejecutarse debido al gran número de solicitudes a la API que se realizan.
