"# Visualizacion de Vehiculos Usados

Esta aplicacion web interactiva permite explorar datos de vehiculos usados en Estados Unidos utilizando graficos dinamicos construidos con Streamlit y Plotly Express.

## Que hace esta app

La aplicacion proporciona dos funcionalidades principales:

- Histograma de precios: Al hacer clic en el boton correspondiente, se genera un histograma que muestra la distribucion de precios de los vehiculos en el conjunto de datos.
- Grafico de dispersion: Otro boton permite visualizar la relacion entre el precio y el kilometraje (odometer) de los vehiculos, con puntos coloreados por fabricante y detalles adicionales como modelo y ano.

## Requisitos

- Python 3.7+
- Librerias:
  - streamlit
  - plotly
  - pandas


## Como ejecutar

1. Asegurate de tener el archivo vehicules_us.csv en el mismo directorio.
2. Ejecuta la aplicacion con:

streamlit run app.py

3. Abre el navegador en la direccion que Streamlit te indique para interactuar con los graficos.

