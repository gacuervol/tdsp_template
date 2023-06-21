# Importamos paquetes
import os
import pandas as pd
import xarray as xr
# Directorio actual del modulo actual
module_dir = os.path.dirname(__file__)
# Funcion que carga datos de flujo de calor
def load_heatflow_data():
    """
    Esta funcion carga los datos de flujo de calor sin preprocesar
    """
    data_folder = os.path.join(module_dir, 'IHFC_2023_GHFDB.csv')
    db1 = pd.read_csv(data_folder, sep=';', encoding="ISO-8859-1")
    return db1
# Funcion que carga datos de grasor sedimentario
def load_sedthick_data():
    """
    Esta funcion carga los datos de grosor sedimentario sin preprocesar
    """
    data_folder = os.path.join(module_dir, 'GlobSed-v3.nc')
    db2 = xr.load_dataarray(data_folder)
    return db2
# Funcion para cargar datos preprocesados
def load_data_prep():
    """
    Esta funcion carga el conjunto de datos fusionados:
    db flujo de calor +  db grosor sedimentario
    Estos datos ya pre-procesados
    """
    data_folder = os.path.join(module_dir, 'db12_prep.csv')
    db12_prep = pd.read_csv(data_folder)
    return db12_prep
# Funcion para cargar datos con features selecionadas
def load_data_feat():
    """
    Esta funcion carga el conjunto de datos con las features extraidas:
    db preprocess + spatial features
    """
    data_folder = os.path.join(module_dir, 'db12_features.csv')
    db12_feat = pd.read_csv(data_folder)
    return db12_feat
