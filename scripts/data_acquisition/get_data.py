# Importamod paqutes base
import requests
# Definimos url de cada base de datos
url_db1 = 'https://www.ngdc.noaa.gov/mgg/sedthick/data/version3/GlobSed.zip'
url_db2 = 'https://datapub.gfz-potsdam.de/download/10.5880.FIDGEO.2023.008-VENOun/IHFC_2023_GHFDB.CSV'
# Definimos el folder de destino
data_folder = '/home/mofoko/Documents/Metodologias/tdsp_template/scripts/data_acquisition'
# Descargamos los datos para la db1
response = requests.get(url_db1)
print(f'status db1: {response}')
with open(data_folder+'/GlobSed.zip', "wb") as file:
    file.write(response.content)
# Descargamos los datos para la db2
response = requests.get(url_db2)
print(f'status db2: {response}')
with open(data_folder+'/IHFC_2023_GHFDB.csv', "wb") as file:
    file.write(response.content)