# Importamos paquetes
import numpy as np
from sklearn.linear_model import RANSACRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
# Polinamial regresion model
class PolynomialRegression(object):
    """
    Clase para regresión polinomial.
    """
    def __init__(self, degree=3, coeffs=None, random_state=0):
        """Inicializa la clase."""
        self.degree = degree
        self.coeffs = coeffs
        self.random_state = random_state

    def fit(self, measured, predicted):
        """Ajusta el polinomio a los datos de entrenamiento."""
        self.coeffs = np.polyfit(measured.ravel(), predicted, self.degree)

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
    def __init__(self, degree=3, max_ransac_trials=5000):
        """Inicializa la clase."""
        self.degree = degree
        self.max_ransac_trials = max_ransac_trials
    def fit(self, measured, predicted):
        """Ajusta el RANSAC a los datos de entrenamiento."""
        samples = len(measured)
        polyreg = PolynomialRegression(degree=self.degree)
        # Crea un objeto RANSACRegressor con un modelo de regresión polinómica
        ransac_3 = RANSACRegressor(polyreg, 
                                   min_samples=samples, 
                                   max_trials=self.max_ransac_trials)
        ransac_3_fit = ransac_3.fit(measured.values.reshape(-1, 1), predicted)
        return ransac_3_fit