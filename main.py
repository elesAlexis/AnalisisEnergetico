# Importamos las bibliotecas necesarias
import streamlit as st  # Para crear la aplicación web interactiva
from CleanData import load_and_clean_data  # Función personalizada para cargar y limpiar los datos
from SplitDataSet import SplitDataSet  # Funciones personalizadas para filtrar y procesar los datos
from GraphicsView import GraphicsView  # Funciones personalizadas para generar gráficos

st.set_page_config(layout="wide", page_title="Análisis de Datos", page_icon="📊")

# Título de la aplicación
st.title("Análisis del Panorama Energético en América Latina y Colombia (2020-2024)")  # Este es el título que aparecerá en la página web
# Introducción general del proyecto
st.write("""
Este proyecto tiene como objetivo analizar el comportamiento del sector energético en América Latina, 
con especial énfasis en Colombia, durante el período 2020-2024. 
A través de gráficos interactivos, se exploran diferentes aspectos como la generación, consumo, exportaciones, 
importaciones, y el uso de fuentes renovables y no renovables de energía.

Los datos han sido limpiados y procesados para facilitar su visualización, permitiendo identificar tendencias, 
comparar entre países y comprender mejor los retos y avances en la transición energética de la región.
""")

# Cargamos y limpiamos los datos desde un archivo CSV
filepath = 'DataSet.csv'  # Ruta al archivo CSV con los datos
df = load_and_clean_data(filepath)  # Llamamos a la función que carga y limpia los datos desde el archivo CSV

#-------------------------------------------------------------
# Filtramos los datos según diferentes criterios
df_america_2024 = SplitDataSet.get_data_america_2024(df)  # Filtra los datos de América para 2024
df_renewable = SplitDataSet.get_renewable_percentage(df)  # Calcula el cantidad de energía renovable
df_non_renewable = SplitDataSet.get_non_renewable_percentage(df)  # Calcula el cantidad de energía no renovable
df_colombia_trade_data = SplitDataSet.get_colombia_trade_data(df)  # Filtra los datos comerciales de Colombia
df_colombia_energy_export = SplitDataSet.get_colombia_energy_export_data(df)  # Filtra los datos de exportación de energía de Colombia
df_distribution = SplitDataSet.get_energy_source_distribution(df)  # Filtra los datos de distribución de fuentes de energía
df_colombia_production_vs_consumption = SplitDataSet.get_colombia_production_vs_consumption_2024(df)  # Filtra los datos de producción y consumo en Colombia en 2024
df_renewable_and_nonrenewable_data = SplitDataSet.get_renewable_and_nonrenewable_data(df)  # Filtra los datos renovables y no renovables
#-------------------------------------------------------------
# Mostrar gráficos en la aplicación Streamlit

# 1. Producción Neta vs Consumo Final en América Latina
st.plotly_chart(GraphicsView.plot_production_vs_consumption(df_america_2024))
st.write("""
### Producción Neta vs Consumo Final en América Latina (2024)

Este gráfico muestra cómo se compara la electricidad generada en distintos países de América Latina con el consumo final de electricidad. Se destacan las diferencias en la producción de electricidad por país y por tipo de producto (renovables o no renovables).
""")
st.write("---")  # Agrega una línea divisoria


# 2. Evolución del cantidad de Energía Renovable en América Latina
st.plotly_chart(GraphicsView.plot_renewable_trend(df_renewable))
st.write("""
### Evolución del Cantidad de Energía Renovable en América Latina (2020-2024)

En este gráfico de líneas, observamos cómo ha cambiado el cantidad de electricidad renovable a lo largo de los años 2020 a 2024 en América Latina. Este análisis es crucial para entender las políticas energéticas de cada país y su transición hacia fuentes de energía más sostenibles.
""")
st.write("---")  # Línea divisoria

# 3. Evolución del Cantidad de Energía No Renovable en América Latina
st.plotly_chart(GraphicsView.plot_non_renewable_trend(df_non_renewable))
st.write("""
### Evolución del Cantidad de Energía No Renovable en América Latina (2020-2024)

De manera similar al gráfico anterior, este gráfico de líneas muestra la tendencia de la energía no renovable en la región. Se visualiza cómo los países han dependido de fuentes de energía como el carbón, gas y petróleo, y cómo este modelo ha evolucionado a lo largo de los últimos años.
""")
st.write("---")  # Línea divisoria

# 4. Comercio de Energía de Colombia
st.plotly_chart(GraphicsView.plot_colombia_trade(df_colombia_trade_data))
st.write("""
### Comercio de Energía de Colombia (2020-2024)

Este gráfico permite observar la relación entre las exportaciones e importaciones de electricidad de Colombia entre 2020 y 2024. Aquí, se destaca la cantidad de electricidad generada en el país y cómo ha sido comercializada con otros países de la región.
""")
st.write("---")  # Línea divisoria

# 5. Exportaciones e Importaciones de Electricidad en Colombia
st.plotly_chart(GraphicsView.plot_colombia_energy_export(df_colombia_energy_export))
st.write("""
### Exportaciones e Importaciones de Electricidad en Colombia (2020-2024)

A través de un gráfico de barras, mostramos las exportaciones y las importaciones de electricidad en Colombia. Este análisis permite ver cómo Colombia se ha integrado en el mercado regional de energía, además de mostrar la evolución de la electricidad generada y exportada.
""")
st.write("---")  # Línea divisoria

# 6. Producción Neta vs Consumo Final en Colombia
st.plotly_chart(GraphicsView.plot_energy_source_distribution(df_distribution))
st.write("""
### Producción Neta vs Consumo Final en Colombia (2024)

En este gráfico de barras, comparamos la electricidad generada con el consumo final en Colombia durante 2024. Aquí se puede observar la capacidad de producción del país en relación con sus necesidades energéticas, desglosado por mes y tipo de producto.
""")
st.write("---")  # Línea divisoria

# 7. Energía Renovable y No Renovable en Colombia
st.plotly_chart(GraphicsView.plot_production_vs_consumption_colombia(df_colombia_production_vs_consumption))
st.write("""
### Energía Renovable y No Renovable en Colombia (2020-2024)

Este gráfico muestra la producción de electricidad renovable y no renovable en Colombia entre 2020 y 2024. Permite visualizar cómo ha sido la transición energética en el país, comparando la proporción de ambas fuentes a lo largo del tiempo.
""")
st.write("---")  # Línea divisoria

# 8. Distribución de Fuentes de Energía en Colombia
st.plotly_chart(GraphicsView.plot_renewable_and_nonrenewable_data(df_renewable_and_nonrenewable_data))
st.write("""
### Distribución de Fuentes de Energía en Colombia (2024)

Este gráfico circular muestra la distribución porcentual de las fuentes de energía utilizadas en Colombia durante 2024. Al observar este gráfico, se puede entender qué porcentaje de la energía del país proviene de fuentes renovables frente a las no renovables.
""")
st.write("---")  # Línea divisoria

# #-------------------------------------------------------------
