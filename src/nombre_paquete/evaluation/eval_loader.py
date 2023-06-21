import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Genera un df con la evaluacion de un modelo de regresion
def eval_regres(y_pred, y_test):
    df_eval = pd.DataFrame({'MSE': mean_squared_error(y_pred=y_pred, y_true=y_test), 
                            'MAE': mean_absolute_error(y_pred=y_pred, y_true=y_test), 
                            'R2': r2_score(y_pred=y_pred, y_true=y_test)}, index=[0])
    return df_eval