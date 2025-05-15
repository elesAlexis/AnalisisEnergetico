# Importamos Plotly Express para la creación de gráficos interactivos
import plotly.express as px

# Clase que contiene las funciones para la creación de gráficos
class GraphicsView:

    @staticmethod
    def plot_production_vs_consumption(data):
        """
        Crea un gráfico de barras agrupadas que muestra la producción neta de electricidad
        vs consumo final por país en el año 2024 para América Latina.

        Parámetros:
            data (DataFrame): Datos filtrados de producción y consumo de electricidad.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo de barras.
        """
        # Creamos un gráfico de barras agrupadas por país y producto
        fig = px.bar(
            data,
            x='PAIS',  # Eje X: Países
            y='ELECTRICIDAD_GENERADA_ACUMULADA',  # Eje Y: Electricidad generada
            color='PRODUCTO',  # Colores diferenciados por el tipo de producto (producción, consumo)
            barmode='group',  # Barras agrupadas para comparar producción y consumo
            title='Producción Neta vs Consumo Final (Países de América 2024)',  # Título del gráfico
            labels={
                'ELECTRICIDAD_GENERADA_ACUMULADA': 'Electricidad (GWh)',
                'PAIS': 'País'
            },
            log_y=True  # Usamos una escala logarítmica para visualizar mejor los valores grandes
        )
        return fig  # Retorna el gráfico generado


    @staticmethod
    def plot_renewable_trend(df_energy):
        """
        Crea un gráfico de líneas que muestra la evolución del cantidad de energía renovable
        en América Latina entre 2020 y 2024.

        Parámetros:
            df_energy (DataFrame): Datos con información sobre el cantidad de energía renovable por año y país.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo de líneas.
        """
        fig = px.line(
            df_energy,
            x='ANIO',  # Eje X: Años
            y='ELECTRICIDAD_GENERADA_ACUMULADA',  # Eje Y: Cantidad de energía renovable
            color='PAIS',  # Diferenciar por país con diferentes colores
            markers=True,  # Añadir marcadores a los puntos de datos
            title='Evolución del cantidad de Energía Renovable en América Latina (2020-2024)',
            labels={
                'ANIO': 'Año',
                'ELECTRICIDAD_GENERADA_ACUMULADA': 'Cantidad de Energía Renovable (GWH)',
                'PAIS': 'País'
            }
        )
        # Mejorar el diseño del gráfico
        fig.update_layout(
            xaxis=dict(dtick=1),  # Coloca un tick cada año
            yaxis=dict(ticksuffix=' GWH'),  # Agrega el símbolo de cantidad al eje Y
            legend_title_text='País',  # Título de la leyenda
            template='plotly_white'  # Usar el tema blanco de Plotly
        )
        return fig


    @staticmethod
    def plot_colombia_trade(data):
        """
        Crea un gráfico de líneas que muestra las exportaciones, importaciones y producción de electricidad
        en Colombia entre los años 2020 y 2024.

        Parámetros:
            data (DataFrame): Datos de comercio (exportaciones, importaciones) y producción de electricidad en Colombia.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo de líneas.
        """
        fig = px.line(
            data,
            x="ANIO",  # Eje X: Años
            y="ELECTRICIDAD_GENERADA_ACUMULADA",  # Eje Y: Electricidad generada en GWh
            color="PRODUCTO",  # Diferenciar por el tipo de producto (exportaciones, importaciones, producción)
            title="Exportaciones, Importaciones y Energía en Colombia (Diciembre 2020-2024)",
            labels={
                "ANIO": "Año",
                "ELECTRICIDAD_GENERADA_ACUMULADA": "Electricidad (GWh)"
            }
        )
        return fig


    @staticmethod
    def plot_non_renewable_trend(df_energy):
        """
        Crea un gráfico de líneas que muestra la evolución del cantidad de energía no renovable
        en América Latina entre 2020 y 2024.

        Parámetros:
            df_energy (DataFrame): Datos con información sobre el cantidad de energía no renovable por año y país.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo de líneas.
        """
        fig = px.line(
            df_energy,
            x='ANIO',  # Eje X: Años
            y='ELECTRICIDAD_GENERADA_ACUMULADA',  # Eje Y: Cantidad de energía no renovable
            color='PAIS',  # Diferenciar por país con diferentes colores
            markers=True,  # Añadir marcadores a los puntos de datos
            title='Evolución de Energía No Renovable en América Latina (2020-2024)',
            labels={
                'ANIO': 'Año',
                'ELECTRICIDAD_GENERADA_ACUMULADA': 'Cantidad de Energía No Renovable (GWH)',
                'PAIS': 'País'
            }
        )
        # Mejorar el diseño del gráfico
        fig.update_layout(
            xaxis=dict(dtick=1),  # Coloca un tick cada año
            yaxis=dict(ticksuffix=' GWH'),  # Agregar el símbolo de cantidad al eje Y
            legend_title_text='País',  # Título de la leyenda
            template='plotly_white'  # Usar el tema blanco de Plotly
        )
        return fig


    @staticmethod
    def plot_colombia_energy_export(df_colombia):
        """
        Crea un gráfico de barras que muestra la producción de electricidad vs la exportación de electricidad
        en Colombia entre 2020 y 2024.

        Parámetros:
            df_colombia (DataFrame): Datos de electricidad producida y exportada en Colombia.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo de barras.
        """
        fig = px.bar(
            df_colombia,
            x='ANIO',  # Eje X: Años
            y='ELECTRICIDAD_GENERADA_ACUMULADA',  # Eje Y: Electricidad acumulada generada
            color='PRODUCTO',  # Diferenciar por el tipo de producto (producción, exportación)
            barmode='group',  # Barras agrupadas por tipo de producto
            title='ELECTRICIDAD PRODUCIDA VS EXPORTADA (2020 - 2024)',
            labels={'ELECTRICIDAD_GENERADA_ACUMULADA': 'Electricidad (GWh)', 'PAIS': 'País'},
            log_y=True  # Usamos escala logarítmica en el eje Y para mejor visualización
        )

        # Mejoramos la presentación del gráfico
        fig.update_layout(
            xaxis_title='Año',
            yaxis_title='Electricidad (GWh)',
            template='plotly_white',  # Usamos el tema blanco
            legend_title_text='Producto'  # Título de la leyenda
        )
        return fig


    @staticmethod
    def plot_production_vs_consumption_colombia(df_colombia):
        """
        Crea un gráfico de barras agrupadas para comparar la producción neta de electricidad
        vs el consumo final en Colombia durante el año 2024.

        Parámetros:
            df_colombia (DataFrame): Datos de producción y consumo de electricidad en Colombia.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo de barras.
        """
        fig = px.bar(
            df_colombia,
            x='MES',  # Eje X: Meses
            y='ELECTRICIDAD_GENERADA_GWH',  # Eje Y: Electricidad generada en GWh
            color='PRODUCTO',  # Diferenciar por el tipo de producto (producción, consumo)
            barmode='group',  # Barras agrupadas por tipo de producto
            title='Producción Neta vs Consumo Final (Colombia 2024)',
            labels={'ELECTRICIDAD_GENERADA_GWH': 'Electricidad (GWh)', 'MES': 'Mes'},
            color_discrete_sequence=px.colors.qualitative.Set1  # Colores predefinidos
        )
        
        # Personalización del gráfico
        fig.update_layout(
            xaxis_title='Mes',
            yaxis_title='Electricidad Generada (GWh)',
            template='plotly_white'  # Usamos el tema blanco de Plotly
        )
        return fig


    @staticmethod
    def plot_renewable_and_nonrenewable_data(df_colombia):
        """
        Crea un gráfico de líneas que muestra las exportaciones, importaciones y producción de energía
        renovable y no renovable en Colombia entre 2020 y 2024.

        Parámetros:
            df_colombia (DataFrame): Datos de exportaciones, importaciones y producción de energía.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo de líneas.
        """
        fig = px.line(
            df_colombia,
            x="ANIO",  # Eje X: Años
            y="ELECTRICIDAD_GENERADA_ACUMULADA",  # Eje Y: Electricidad generada en GWh
            color="PRODUCTO",  # Diferenciar por el tipo de producto (renovables, no renovables, etc.)
            title="Exportaciones, Importaciones y Energía en Colombia (Diciembre 2020-2024)",
            labels={
                "ANIO": "Año",
                "ELECTRICIDAD_GENERADA_ACUMULADA": "Electricidad (GWh)"
            }
        )
        return fig


    @staticmethod
    def plot_energy_source_distribution(df_dist):
        """
        Crea un gráfico circular que muestra la distribución porcentual de las fuentes de energía
        utilizadas en Colombia durante el año 2024.

        Parámetros:
            df_dist (DataFrame): Datos de distribución de fuentes de energía.

        Retorna:
            fig (plotly.graph_objects.Figure): Gráfico interactivo circular.
        """
        fig = px.pie(
            df_dist,
            names='PRODUCTO',  # Diferenciar por tipo de fuente de energía
            values='Porcentaje',  # Valores correspondientes a los porcentajes
            title='Distribución porcentual por fuente de energía - Colombia 2024',
            hole=0.4  # Crear un gráfico de dona (agujero en el centro)
        )
        return fig
