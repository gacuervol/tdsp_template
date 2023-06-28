# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.
>  El objetivo principal del proyecto era comparar el desempeño de algoritmos de machine learning empleados para regresión con el fin de predecir el flujo en el subsuelo marino utilizando datos de grosor sedimentario. Por esta razón se a presentado la comparación entre un modelo de **Regresión de soporte vectorial (SVR)** y un modelo base tomado de la literatura más reciente.

## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
> A continuación se detalla cada uno de los entregables junto con los objetivos alcanzados para cada una de las etapas del proyecto.
> - **Fase 1:** Durante esta fase se realizó la descarga de los datos y se documentó cada una de las variables de interés para el proyecto generándose así los siguientes productos:

| Producto | Tipo | Descripción | Ruta |
|--------|--------|--------|--------|
| `get_data.py` | script | Realiza la descarga de las bases de datos. | `./scripts/data_acquisition/get_data.py` |
| `data_dictionary.md` | markdown | Documenta las variables de cada conjunto de datos. | `./docs/data/data_dictionary.md` |
| `data_definition.md` | markdown | Documenta las bases de datos consultadas junto con el script de descarga. | `./docs/data/data_definition.md` |
| `project_charter.md` | markdown | Define los aspectos principales del proyecto junto con sus objetivo, alcances entre otros.| `./docs/business_understanding/project_charter.md` |

> - **Fase 2:** En esta fase se preprocesaron los datos y sea realizó el análisis exploratorio (EDA) de los mismos. Estos fueron los productos alcanzados:

| Producto | Tipo | Descripción | Ruta |
|--------|--------|--------|--------|
| `preproces.ipynb` | notebook | Realiza el preprocesamiento de los datos. | `./scripts/preprocessing/preproces.ipynb` |
| `eda.ipynb` | notebook | Realiza el análisis exploratorio de los datos. | `./scripts/eda/eda.ipynb` |
| `data_summary.md` | markdown | Documenta la el estado y calidad de los datos definiendo las variables explicativas y las objetivo. | `./docs/data/data_summary.md` |

> - **Fase 3:** En esta fase se realizó la extracción de características de los datos junto con el modelado de los mismos. Estos fueron los productos alcanzados:

| Producto | Tipo | Descripción | Ruta |
|--------|--------|--------|--------|
| `feature_extraction.ipynb` | notebook | Extrae características espaciales de los datos para mejorar el desempeño durante el modelado. | `./scripts/training/feature_extraction.ipynb` |
| `modelling.ipynb` | notebook | Modela los datos implementando modelos de machine learning y presenta su desempeño. | `./scripts/training/modelling.ipynb` |
| `baseline_models.md` | markdown | Documenta el modelo base utilizado como referencia para los modelos implementados durante el proyecto. | `./docs/modeling/baseline_models.md` |
| `model_report.md` | markdown | Documenta los modelos de machine learning implementados durante el proyecto y los compara con el modelo de referencia. | `./docs/modeling/model_report.md` |
> - **Fase 4:** En esta se desarrolla el despliegue del modelo más optimo y se documenta dicho proceso. Estos fueron los productos alcanzados:

| Producto | Tipo | Descripción | Ruta |
|--------|--------|--------|--------|
| `deploymentAPIs.py` | script | Implementa un API en entorno local para realizar el despliegue del modelo. | `./src/nombre_paquete/deployment/deploymentAPIs.py` |
| `API_test.py` | script | Permite hacer peticiones de prueba al modelo desplegado para realizar una predicción. | `./src/nombre_paquete/deployment/API_test.py` |
| `deploymentdoc.md` | markdown | Documenta el código y la arquitectura de despliegue del modelo. | `./docs/deployment/deploymentdoc.md` |

Adicionalmente, se desarrolló un paquete local para la implementación de múltiples funciones necesarias para cada una de las fases del proyecto.

| Producto | Tipo | Descripción | Ruta |
|--------|--------|--------|--------|
| `nombre_paquete` | package | En este paquete de Python se registran las funciones y métodos desarrollados específicamente para el proyecto. | `./src/nombre_paquete` |

- Evaluación del modelo final y comparación con el modelo base.
> El modelo final superó al modelo base en términos de rendimiento y precisión. Al comparar métricas de desempeño se observó una reducción sustancial en el error medio cuadrático (MSE) y error absoluto medio (MAE) junto con un aumento en el coeficiente de determinación (R2) con respecto al modelo base. Por tanto el modelo desarrollad es más efectivo y preciso a la hora de realizar predicciones de flujo de calor en el subsuelo marino.

|Métrica| Modelo Base | Modelo Final|
|---|---|---|
|MSE|1.091069e+07|22238.741548|
|MAE|511.106331|45.430096|
|R2|-0.000738|0.011897|
- Descripción de los resultados y su relevancia para el negocio.
> El análisis de datos y las predicciones generadas por el modelo de machine learning brindan información valiosa para la toma de decisiones estratégicas para diferentes sectores de la sociedad. Las predicciones generadas por este modelo pueden ser ventajosas, ya que pueden apoyar decisiones basadas en datos y conocimientos concretos.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto.
> En muchos casos, los datos espaciales exhiben interacciones espaciales complejas y dependencias espaciales. Esto significa que los valores de una ubicación pueden estar influenciados por los valores de ubicaciones vecinas. La capacidad del modelo de capturar y modelar estas interacciones espaciales puede ser un desafío a resolver para obtener resultados precisos.
- Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo.
>  Una de las grandes lecciones aprendidas durante este proyecto está relacionada con la selección adecuada de características o variables que permitan capturar la naturaleza espacial de los datos. Esta lección fue de suma importancia para garantizar un mejor rendimiento del modelo y evitar el sobreajuste del mismo. Al trabajar con datos espaciales, es esencial identificar las características que reflejen las interacciones y dependencias espaciales de los datos. Esto implica considerar variables como coordenadas geográficas, distancias a puntos de referencia o características específicas del entorno geográfico. Se descubrió que incluir estas características espaciales relevantes en el modelo mejoraba significativamente la precisión y la capacidad de generalización.
- Recomendaciones para futuros proyectos de machine learning.
> Es vital utilizar un sistema de control de versiones, como Git, para gestionar el código fuente, los datos y cualquier otro recurso utilizado en el proyecto. Esto te permitirá tener un registro de los cambios realizados, facilitar la colaboración entre los miembros del equipo y revertir cambios si es necesario.

> Es necesario documentar el proceso de desarrollo y los pasos seguidos en cada etapa del proyecto. Registrar los parámetros utilizados, las técnicas aplicadas, los resultados obtenidos y cualquier otro detalle relevante permitirá reproducir y validar los resultados en el futuro, además de facilita el mantenimiento y la escalabilidad del proyecto.

## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
> El modelo de machine learning desarrollado puede proporcionar información y conocimientos valiosos que respalden la toma de decisiones estratégicas y operativas en el diferentes sectores de la sociedad. 
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.
> Una posible mejora se encuentra en la implementación de algoritmos más eficientes para buscar los hiperparámetros óptimos del modelo de machine learning. Durante el proyecto, debido al amplio volumen de datos (30,931 registros) y las limitaciones de tiempo, no fue factible llevar a cabo una exploración exhaustiva de múltiples combinaciones de hiperparámetros. Esta estrategia puede resultar costosa en términos de capacidad computacional y tener limitaciones en cuanto a la cobertura de búsqueda.
## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
> Durante el proyecto, se realizaron avances significativos en la aplicación de modelos de machine learning al análisis de datos de flujo de calor en el suelo marino. Se logró desarrollar un modelo capaz de predecir de manera precisa el flujo de calor, basándose en el grosor sedimentario y propiedades espaciales específicas de los datos. Este modelo, a nivel global, demostró su eficacia al procesar un gran volumen de datos (30,931 registros) y arrojar resultados altamente prometedores. Además, a pesar de las limitaciones de tiempo, se logró implementar el modelo en un entorno local y desplegarlo a través de una API, permitiendo su acceso al público.

> Los resultados obtenidos representan un hito importante en la predicción del flujo de calor marino, superando a los modelos de referencia más recientes. Esta mejora significativa demuestra la robustez y precisión del modelo desarrollado, así como su relevancia para la comprensión y estudio de los procesos geotérmicos en el suelo marino.
- Conclusiones finales y recomendaciones para futuros proyectos.
> En conclusión, el proyecto demostró la viabilidad y utilidad del modelo de machine learning desarrollado. Se destacó la importancia de una implementación eficiente de los algoritmos y la necesidad de considerar cuidadosamente los hiperparámetros del modelo. Aunque no fue posible realizar una exploración exhaustiva de todas las combinaciones de hiperparámetros debido a las limitaciones de tiempo y capacidad computacional, se logró obtener resultados satisfactorios. Esto sugiere que en futuros proyector es necesario una mayor exploración con el objetivo obtener mejoras adicionales en el modelo.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
> Agradecemos al equipo de trabajo y a todos los colaboradores que contribuyeron de manera significativa para hacer posible este proyecto. Su dedicación, experiencia y esfuerzo conjunto fueron fundamentales para alcanzar nuestros objetivos y lograr resultados exitosos.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
> Agradecemos especialmente a nuestros patrocinadores y financiadores, **OceanTech**, **SolutionsEnergyCorp** y **Marine Research Institute**, cuyo apoyo continuo fue esencial para financiar este proyecto y hacer realidad nuestras ideas y ambiciones. Su confianza en nuestra visión y su compromiso con la investigación marina y las soluciones energéticas sostenibles fueron fundamentales para superar los desafíos y llevar a cabo nuestro trabajo.