# Importamos los modulos necesarios
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import seaborn as sns
import cartopy.crs as ccrs
# Mapa global
def plot_map(df, lon='lng', lat='lat', val=None, **kwargs):
    # Crear una figura y un eje utilizando la proyección cartopy
    fig = plt.figure(figsize=(14, 6))
    # Definimos el codigo de proyeccion
    epsg_code = 3395
    # Definimos el sistema de referencia proyectado en ax
    if 'ax' in kwargs:
        ax = kwargs['ax']
    else:
        ax = plt.axes(projection=ccrs.epsg(epsg_code))
    # Trazar los puntos en el mapa utilizando scatter
    if val != None:
        scater_map = ax.scatter(df[lon], df[lat], c=df[val], 
                                cmap='viridis', norm=colors.LogNorm(), 
                                s=0.1, alpha=0.5, transform=ccrs.PlateCarree())
        # Agregar barra de colores
        cbar = plt.colorbar(scater_map, label=r'q [$mW/m^2$]', pad=0.01, shrink=0.4)
    elif 'c' in kwargs:
        scater_map = ax.scatter(df[lon], df[lat], c=kwargs['c'], 
                                norm=colors.LogNorm(), s=0.1, alpha=0.5, label=kwargs['label'],
                                transform=ccrs.PlateCarree())
    else:
        print("Falta definir c='color'")
    # Agregar características del mapa, como la costa y los límites del país
    ax.coastlines(resolution='50m')
    # Agrega reticula
    gl = ax.gridlines(draw_labels=True, linewidth=0.1, color='k', alpha=0.5, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    # Titulo
    ax.set_title('Mapa de datos de flujo de calor')
# Pairplot personalizado
def kde_hexbin_pairplot(df):
    """
    Crea un pairplot con gráficos de hexbins y KDE.
    Parámetros:
        - df: DataFrame - El dataframe de entrada
    Retorna:
        - None
    """
    # Define funcion para heixbin 
    def hexbin(x, y, color, cmap="twilight"):
        plt.hexbin(x, y, gridsize=14, alpha = .8, cmap=cmap, mincnt=0.0001)
    # Crea el pairplot
    g = sns.pairplot(df, 
                    dropna=True, 
                    markers='.', 
                    diag_kind='hist',
                    plot_kws=dict(color="k", alpha = 0.2),
                    diag_kws=dict(color="k"))
    # Scatterplot para la diagonal inferior
    g.map_lower(sns.scatterplot, alpha=0.5, marker = '.', color='gray')
    # Gráfico de KDE para la diagonal inferior
    g.map_lower(sns.kdeplot, alpha=0.5, levels=6, color=".2", cmap='twilight',)
    # Gráfico de hexbins para la diagonal superior
    g.map_upper(hexbin)
# kfold map
def kfold_map(folds, df, lon='lng', lat='lat', block_size=None):
    """
    Utiliza el generador dado por vd.BlockKFold().fit()
    """
    crs = ccrs.PlateCarree()
    # Definimos el codigo de proyeccion
    epsg_code = 3395
    # Make Mercator maps of the two cross-validator folds
    fig, axes = plt.subplots(
        2,
        3,
        figsize=(12, 8),
        subplot_kw=dict(projection=ccrs.epsg(epsg_code)),
        sharex=True,
        sharey=True,
    )
    for i, (ax, fold) in enumerate(zip(axes.flatten(), folds)):
            i_train, i_val = fold
            ax.set_title(f'fold {i} testing points')
            # Use an utility function to setup the tick labels and the land feature
            ax.scatter(
                df[lon].iloc[i_train],
                df[lat].iloc[i_train],
                c="b",
                s=0.1,
                alpha=0.5,
                transform=crs,
                label="Train",
            )
            ax.scatter(
                df[lon].iloc[i_val],
                df[lat].iloc[i_val],
                c="r",
                s=0.1,
                alpha=0.5,
                transform=crs,
                label="Validation",
            )
            ax.coastlines(resolution='50m')
            # Agrega reticula
            gl = ax.gridlines(draw_labels=True, linewidth=0.1, color='k', alpha=0.5, linestyle='--')
            gl.top_labels = False
            gl.right_labels = False
    # Place a legend on the first plot
    axes[0, 2].legend(loc="upper right", bbox_to_anchor=(1.36, 1), markerscale=20).set_title(f'Block size: {block_size}')
    plt.subplots_adjust(
        #hspace=0.1, wspace=0.05, top=0.95, bottom=0.05, left=0.05, right=0.95
    )