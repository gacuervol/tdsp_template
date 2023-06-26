# Importamos paquetes
import numpy as np
import pandas as pd
import verde as vd
from ..evaluation import eval_loader
from .model_loader import datasplit_in_DB
from tqdm.notebook import tqdm
# Crea un df vacio con solo dos columnas 
def empty_dfCV():
    df_CV_block = pd.DataFrame({'block':[],
                                'fold': [],
                                })
    return df_CV_block
# Agrega al df vacio las columnas de las métricas
def add_metrics(df: pd.DataFrame, df_metrics: pd.DataFrame):
    for key in df_metrics.to_dict(orient='records')[0].keys():
        df[key]=[]
    return df
# Crea un diccionario para ser como fila del df anterior
def CV_row(block: int = None, fold: int= None,  df_metrics: pd.DataFrame=None):
    dic_block = {'block': [block], 'fold': [fold]}
    dic_block.update(df_metrics.to_dict(orient='records')[0])
    return dic_block
# Itera para cada tamano de bloque y cada fold avaluando el modelo
def BlockKFold_search(blocks: list= None, n_splits: int= 5, 
                      model=None, df: pd.DataFrame = None, features: list= None, 
                      target: str= None, coord_train_val: tuple= None, data_train_val: tuple= None,
                      random_state: int= None):
    state = 0
    for i, size in enumerate(blocks):
        # Create a progress bar for the current block
        block_progress_bar = tqdm(total=n_splits, desc=f'Block {i}', unit='fold')
        kfold = vd.BlockKFold(spacing=size, shuffle=True, n_splits=n_splits, random_state=random_state)
        folds = kfold.split(np.transpose(coord_train_val))
        df_train_val = datasplit_in_DB(df, data_train_val, features + [target])
        for i, fold in enumerate(folds):
            i_train, i_val = fold
            # Conjunto de train
            X_train = df_train_val[features].iloc[i_train].values
            y_train = df_train_val[target].iloc[i_train].values
            # Conjunto de vaidation
            X_val = df_train_val[features].iloc[i_val].values
            y_val = df_train_val[target].iloc[i_val].values
            # Create and train the SVR model
            model.fit(X_train, y_train)
            # Make predictions on the test set
            y_pred_val = model.predict(X_val)
            df_metric = eval_loader.eval_regres(y_pred_val, y_val)
            if state == 0:
                df_CV = add_metrics(empty_dfCV(), df_metric)
            else:
                dic_CV_row = CV_row(block=size, fold=i, df_metrics=df_metric)
                df_CV = pd.concat([df_CV, pd.DataFrame(dic_CV_row)], ignore_index=True)
            state += 1
            # Update the progress bar for the current block
            block_progress_bar.update(1)
        # Close the progress bar for the current block
        block_progress_bar.close()
    return df_CV