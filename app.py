import pandas as pd
import plotly.express as px
import streamlit as st

try:
    data = pd.read_csv('vehicles_us.csv')  # leer los datos
    st.header("Histograma de precios de vehículos")  # título de la aplicación

    # Botón para mostrar el histograma
    if st.button("Mostrar histograma"):
        st.write("Distribución de precios de vehículos:")
        fig = px.histogram(data, x='price', nbins=50,
                           title='Histograma de precios')
        st.plotly_chart(fig)

    # Botón para mostrar el gráfico de dispersión
    if st.button("Mostrar gráfico de dispersión"):
        st.write("🔍 Relación entre precio y kilometraje:")
        fig_scatter = px.scatter(data, x='odometer', y='price',
                                 title='Precio vs. Kilometraje',
                                 labels={'odometer': 'Kilometraje',
                                         'price': 'Precio'},
                                 color='manufacturer',  # opcional: colorear por fabricante
                                 hover_data=['model_year', 'model'])
        st.plotly_chart(fig_scatter)

except FileNotFoundError:
    st.error("El archivo 'vehicles_us.csv' no se encontró. Asegúrate de que esté en el mismo directorio.")
