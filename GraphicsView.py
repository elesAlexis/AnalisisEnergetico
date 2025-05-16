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
            labels={
                'ANIO': 'Año',
                'ELECTRICIDAD_GENERADA_ACUMULADA': 'Cantidad de Energía Renovable (GWh)',
                'PAIS': 'País'
            }
        )
        # Mejorar el diseño del gráfico
        fig.update_layout(
            xaxis=dict(dtick=1),  # Coloca un tick cada año
            yaxis=dict(ticksuffix=' GWh'),  # Agrega el símbolo de cantidad al eje Y
            legend_title_text='País',  # Título de la leyenda
            template='plotly_white'  # Usar el tema blanco de Plotly
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
            labels={
                'ANIO': 'Año',
                'ELECTRICIDAD_GENERADA_ACUMULADA': 'Cantidad de Energía No Renovable (GWh)',
                'PAIS': 'País'
            }
        )
        # Mejorar el diseño del gráfico
        fig.update_layout(
            xaxis=dict(dtick=1),  # Coloca un tick cada año
            yaxis=dict(ticksuffix=' GWh'),  # Agregar el símbolo de cantidad al eje Y
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
            labels={
                "ANIO": "Año",
                "ELECTRICIDAD_GENERADA_ACUMULADA": "Electricidad (GWh)"
            }
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
    def plot_distribution_over_net_production_colombia(df_distribution):
        fig = px.bar(
            df_distribution,
            x="año",
            y="% sobre Producción Neta",
            color="Categoría Energética",
            barmode="group",
            labels={
                "% sobre Producción Neta": "% sobre Producción Neta (%)",
                "año": "Año",
                "Categoría Energética": "Categoría Energética"
            }
        )
        fig.update_layout(
            xaxis_title="Año",
            yaxis_title="% sobre Producción Neta",
            legend_title="Categoría Energética",
            bargap=0.2
        )
        return fig


    @staticmethod
    def plot_renewable_and_nonrenewable_data(df_colombia):
        """
        Crea un gráfico de líneas que muestra las energías renovable y no renovable en Colombia entre 2020 y 2024.
        """
        fig = px.line(
            df_colombia,
            x="ANIO",  # Eje X: Años
            y="ELECTRICIDAD_GENERADA_ACUMULADA",  # Eje Y: Electricidad generada en GWh
            color="PRODUCTO",  # Diferenciar por el tipo de producto (renovables y no renovables)
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
            hole=0.4  # Crear un gráfico de dona (agujero en el centro)
        )
        return fig
