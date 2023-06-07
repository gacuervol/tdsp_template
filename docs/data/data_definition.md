# Definición de los datos

## Origen de los datos

Los datos utilizados en este proyecto fueron recopilados de diversas fuentes, incluyendo la [Total Sediment Thickness of the World's Oceans and Marginal Seas Version 3 (GlobSed)](https://www.ngdc.noaa.gov/mgg/sedthick/) y [The Global Heat Flow Database: Update 2023](https://ihfc-iugg.org/products/global-heat-flow-database/data).

Para obtener los datos de Grosor Sedimentario y Flujo de Calor, se utilizó el módulo `requests` en Python para realizar solicitudes a las API correspondientes de las bases de datos. Se establecieron las consultas necesarias y se enviaron las solicitudes HTTP para obtener los datos en formato ZIP y CSV.

## Especificación de los scripts para la carga de datos

```
# Importamos paqutes base
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
```

## Referencias a rutas o bases de datos origen y destino
- **Base de datos 1:** `https://www.ngdc.noaa.gov/mgg/sedthick/data/version3/GlobSed.zip`
- **Base de datos 2:** `https://datapub.gfz-potsdam.de/download/10.5880.FIDGEO.2023.008-VENOun/IHFC_2023_GHFDB.CSV`

### Rutas de origen de datos

- Los archivos de origen de los datos se encuentran almacenados en repositorios en la nube pertenecientes a instituciones como [NOAA data catalog](https://data.noaa.gov/dataset/)  y [GFZ data services](https://dataservices.gfz-potsdam.de/panmetaworks/showshort.php?id=38ab063c-9e6d-11ed-95b8-f851ad6d1e4b).
- Estructura de los datos:
    - Los datos obtenidos de la base de datos de *NOAA data catalog* son de tipo semiestructurado y se presentan en formato NC (NetCDF). Este formato permite almacenar datos científicos en una estructura jerárquica, lo que facilita la organización y la interoperabilidad de los datos. 
    - Los datos de la base de datos *GFZ Data Services* se presentan en formato CSV, lo que implica que están estructurados en forma tabular en filas y columnas.

- La transformación y limpieza de los datos, se realizó siguiendo un conjunto de pasos para garantizar la calidad y coherencia de los datos. Esto incluyó la eliminación de filas con valores faltantes o inconsistentes, la detección y manejo de valores atípicos, y la transformación de las variables en ciertos casos.

### Base de datos de destino

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.
