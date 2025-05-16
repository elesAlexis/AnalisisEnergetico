import plotly.express as px
import plotly.graph_objects as go  # Asegúrate de que esté importado arriba junto con plotly.express


class GraphicsView:

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

    @staticmethod
    def plot_radar_energy_comparison(df, selected_countries, year=2024):
        """Gráfico radar comparando la distribución porcentual de fuentes de energía entre varios países en un año específico."""

        from SplitDataSet import SplitDataSet  # Importación interna para evitar dependencia circular

        categorias = ['Hidroeléctrica', 'Solar', 'Renovables combustibles', 'Carbón', 'Petróleo', 'Gas natural', 'Otras renovables agregadas']
        fig = go.Figure()

        for country in selected_countries:
            data = SplitDataSet.get_energy_source_distribution(df, year=year, country=country)

            # Asegura que todas las categorías estén presentes
            valores = [data.loc[data['PRODUCTO'] == c, 'Porcentaje'].values[0] if c in data['PRODUCTO'].values else 0 for c in categorias]

            fig.add_trace(go.Scatterpolar(
                r=valores,
                theta=categorias,
                fill='toself',
                name=country
            ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 90])
            ),
            showlegend=True,
            template='plotly_white'
        )

        return fig
