# Importamos paquetes
import numpy as np
import pandas as pd
from sklearn.linear_model import RANSACRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
# Variable global Grado del polinomio
degree_poly = None
# Polinamial regresion model
class PolynomialRegression(object):
    """
    Clase para regresión polinomial.
    """
    def __init__(self, coeffs=None, random_state=0):
        """Inicializa la clase."""
        self.coeffs = coeffs
        self.random_state = random_state

    def fit(self, measured, predicted):
        """Ajusta el polinomio a los datos de entrenamiento."""
        self.coeffs = np.polyfit(measured.ravel(), predicted, degree_poly)

    def get_params(self, deep=False):
        """Obtiene los parámetros de la regresión."""
        return {'coeffs': self.coeffs}

    def set_params(self, coeffs=None, random_state=0):
        """Establece los parámetros de la regresión."""
        self.coeffs = coeffs
        self.random_state = random_state

    def predict(self, measured):
        """Realiza predicciones utilizando el polinomio ajustado."""
        poly_eqn = np.poly1d(self.coeffs)
        y_hat = poly_eqn(measured.ravel())
        return y_hat

    def score(self, measured, predicted):
        """Calcula el puntaje de la regresión."""
        return mean_squared_error(predicted, self.predict(measured))
# Robustly fit linear model with RANSAC algorithm
class polyRegressionRANSAC(object):
    @classmethod
    def set_polyreg(cls, degree):
        """
        Modifica el grado de la clase PolynomialRegression
        """
        global degree_poly
        degree_poly = degree
    def __init__(self, degree=None, max_ransac_trials=5000):
        """Inicializa la clase."""
        polyRegressionRANSAC.set_polyreg(degree)
        self.degree = degree
        self.polyreg = PolynomialRegression()
        self.max_ransac_trials = max_ransac_trials
    def fit(self, measured, predicted):
        """Ajusta el RANSAC a los datos de entrenamiento."""
        samples = len(measured)
        global base_estimator
        base_estimator = self.polyreg
        # Crea un objeto RANSACRegressor con un modelo de regresión polinómica
        self.ransac_n = RANSACRegressor(estimator=base_estimator, 
                                   min_samples=samples, 
                                   max_trials=self.max_ransac_trials)
        ransac_3_fit = self.ransac_n.fit(measured.values.reshape(-1, 1), predicted)
        return ransac_3_fit
# Extrear los indeices de valores en el df para un subconjunto despues de hacer un blocksplit 
def get_id_db_after_blocksplit(df, matrix: np.ndarray=None, id_matrix: int= None):
    """
    Extrea el indice del df que conincide con la fila id_matrix de la matrix dada
    """
    bool_series = (df==matrix[id_matrix]).sum(axis=1)
    return bool_series.argmax()
# Extrae todos los indices que coinciden con el subconjunto generado del split
def SelectDB_from_DataSplit(subset_split: tuple=None, df: pd.DataFrame= None):
    """
    Retorna los datos del df que coinciden con el subset_split 
    """
    id_train_val = []
    matrix_train_val = np.transpose(subset_split)
    for id in range(matrix_train_val.shape[0]):
        idx = get_id_db_after_blocksplit(df, 
                                         matrix=matrix_train_val, 
                                         id_matrix=id,
                                         )
        id_train_val.append(idx)
    return id_train_val
# Retorna el db como subset de data split
def datasplit_in_DB(db: pd.DataFrame= None, data_split: tuple= None, features: list= None):
    id_suset = SelectDB_from_DataSplit(data_split, db[features])
    return db.iloc[id_suset]