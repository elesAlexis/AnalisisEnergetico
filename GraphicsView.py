import plotly.express as px

class GraphicsView:

    @staticmethod
    def plot_production_vs_consumption(data):
        """Gráfico de barras agrupadas: producción neta vs consumo final en América Latina 2024."""
        return px.bar(
            data,
            x='PAIS',
            y='ELECTRICIDAD_GENERADA_ACUMULADA',
            color='PRODUCTO',
            barmode='group',
            labels={'ELECTRICIDAD_GENERADA_ACUMULADA': 'Electricidad (GWh)', 'PAIS': 'País'},
            log_y=True
        )

    @staticmethod
    def plot_renewable_trend(df_energy):
        """Evolución de energía renovable en América Latina (2020-2024)."""
        fig = px.line(
            df_energy,
            x='ANIO',
            y='ELECTRICIDAD_GENERADA_ACUMULADA',
            color='PAIS',
            markers=True,
            labels={'ANIO': 'Año', 'ELECTRICIDAD_GENERADA_ACUMULADA': 'Energía Renovable (GWh)', 'PAIS': 'País'},
            log_y=True
        )
        fig.update_layout(xaxis=dict(dtick=1), yaxis=dict(ticksuffix=' GWh'), legend_title_text='País', template='plotly_white')
        return fig

    @staticmethod
    def plot_non_renewable_trend(df_energy):
        """Evolución de energía no renovable en América Latina (2020-2024)."""
        fig = px.line(
            df_energy,
            x='ANIO',
            y='ELECTRICIDAD_GENERADA_ACUMULADA',
            color='PAIS',
            markers=True,
            labels={'ANIO': 'Año', 'ELECTRICIDAD_GENERADA_ACUMULADA': 'Energía No Renovable (GWh)', 'PAIS': 'País'},
            log_y=True
        )
        fig.update_layout(xaxis=dict(dtick=1), yaxis=dict(ticksuffix=' GWh'), legend_title_text='País', template='plotly_white')
        return fig

    @staticmethod
    def plot_colombia_trade(data):
        """Exportaciones, importaciones y producción eléctrica en Colombia (2020-2024)."""
        return px.line(
            data,
            x="ANIO",
            y="ELECTRICIDAD_GENERADA_ACUMULADA",
            color="PRODUCTO",
            labels={"ANIO": "Año", "ELECTRICIDAD_GENERADA_ACUMULADA": "Electricidad (GWh)"}
        )

    @staticmethod
    def plot_colombia_energy_export(df_colombia):
        """Producción vs exportación eléctrica en Colombia (2020-2024)."""
        fig = px.bar(
            df_colombia,
            x='ANIO',
            y='ELECTRICIDAD_GENERADA_ACUMULADA',
            color='PRODUCTO',
            barmode='group',
            labels={'ELECTRICIDAD_GENERADA_ACUMULADA': 'Electricidad (GWh)', 'PAIS': 'País'},
            log_y=True
        )
        fig.update_layout(xaxis_title='Año', yaxis_title='Electricidad (GWh)', template='plotly_white', legend_title_text='Producto')
        return fig

    @staticmethod
    def plot_distribution_over_net_production_colombia(df_distribution):
        """Distribución porcentual sobre producción neta en Colombia."""
        fig = px.bar(
            df_distribution,
            x="año",
            y="% sobre Producción Neta",
            color="Categoría Energética",
            barmode="group",
            labels={"% sobre Producción Neta": "% sobre Producción Neta (%)", "año": "Año", "Categoría Energética": "Categoría Energética"}
        )
        fig.update_layout(xaxis_title="Año", yaxis_title="% sobre Producción Neta", legend_title="Categoría Energética", bargap=0.2)
        return fig

    @staticmethod
    def plot_renewable_and_nonrenewable_data(df_colombia):
        """Energías renovable y no renovable en Colombia (2020-2024)."""
        return px.line(
            df_colombia,
            x="ANIO",
            y="ELECTRICIDAD_GENERADA_ACUMULADA",
            color="PRODUCTO",
            labels={"ANIO": "Año", "ELECTRICIDAD_GENERADA_ACUMULADA": "Electricidad (GWh)"}
        )

    @staticmethod
    def plot_energy_source_distribution(df_dist):
        """Distribución porcentual de fuentes de energía en Colombia (2024)."""
        return px.pie(
            df_dist,
            names='PRODUCTO',
            values='Porcentaje',
            hole=0.4
        )
