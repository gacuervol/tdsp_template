# Importamos los modulos necesarios
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs
# Mapa global
def plot_map(df, lon='lng', lat='lat', val='q'):
    # Crear una figura y un eje utilizando la proyección cartopy
    fig = plt.figure(figsize=(14, 6))
    # Definimos el codigo de proyeccion
    epsg_code = 3395
    # Definimos el sistema de referencia proyectado en ax
    ax = plt.axes(projection=ccrs.epsg(epsg_code))
    # Trazar los puntos en el mapa utilizando scatter
    scater_map = ax.scatter(df[lon], df[lat], c=df[val], 
            cmap='viridis', norm=colors.LogNorm(), s=0.1, alpha=0.5, transform=ccrs.PlateCarree())
    # Agregar barra de colores
    cbar = plt.colorbar(scater_map, label=r'q [$mW/m^2$]', pad=0.01, shrink=0.4)
    # Agregar características del mapa, como la costa y los límites del país
    ax.coastlines(resolution='50m')
    # Agrega reticula
    gl = ax.gridlines(draw_labels=True, linewidth=0.1, color='k', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    # Titulo
    ax.set_title('Mapa de datos de flujo de calor')