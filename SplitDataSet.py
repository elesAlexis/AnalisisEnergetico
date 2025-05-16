import pandas as pd

class SplitDataSet:
    
    # Método para obtener los datos comerciales de Colombia (importaciones, exportaciones, producción y consumo) de los años 2020 a 2024
    @staticmethod
    def get_colombia_trade_data(df):
        # Filtramos los datos para Colombia, en el mes de diciembre, para los años entre 2020 y 2024 y con los productos de interés
        return df[
            (df['PAIS'] == 'Colombia') &  # Solo Colombia
            (df['ANIO'].isin([2020, 2021, 2022, 2023, 2024])) &  # Años entre 2020 y 2024
            (df['MES'] == 12) &  # Solo diciembre
            (df['PRODUCTO'].isin([  # Filtramos los productos relacionados con comercio y producción/consumo
                'Exportaciones totales',
                'Importaciones totales',
                'Producción neta de electricidad',
                'Consumo final'
            ]))
        ]


    # Método para calcular el cantidad de energía renovable por país y año
    @staticmethod
    def get_renewable_percentage(df):
         return df[
                    (df['ANIO'].isin([2020, 2021, 2022, 2023, 2024])) &  # Años entre 2020 y 2024
                    (df['MES'] == 12) &  # Solo diciembre
                    (df['PRODUCTO'].isin(['Renovables']))  # Productos de interés
                ]


    # Método para calcular el cantidad de energía no renovable por país y año
    @staticmethod
    def get_non_renewable_percentage(df):
        # Lista de productos no renovables
        return df[
                    (df['ANIO'].isin([2020, 2021, 2022, 2023, 2024])) &  # Años entre 2020 y 2024
                    (df['MES'] == 12) &  # Solo diciembre
                    (df['PRODUCTO'].isin(['No renovables']))  # Productos de interés
                ]


    # Método para obtener los datos de producción y exportación de energía de Colombia
    @staticmethod
    def get_colombia_energy_export_data(df):
        # Filtramos los datos para Colombia (años 2020-2024) y los productos de interés (producción y exportaciones)
        return df[
            (df['PAIS'] == 'Colombia') &  # Solo Colombia
            (df['ANIO'].isin([2020, 2021, 2022, 2023, 2024])) &  # Años entre 2020 y 2024
            (df['MES'] == 12) &  # Solo diciembre
            (df['PRODUCTO'].isin(['Producción neta de electricidad', 'Exportaciones totales']))  # Productos de interés
        ]


    # Método para obtener la distribución (en porcentaje) de consumo, pérdidas, exportaciones e importaciones 
    # sobre la producción neta de electricidad en Colombia para diciembre de 2024
    @staticmethod
    def get_distribution_over_net_production_colombia(df):
        # Productos clave
        productos_interes = [
            'Producción neta de electricidad',
            'Consumo final',
            'Pérdidas de distribución',
            'Exportaciones totales'
        ]

        # Filtrar Colombia, diciembre y productos relevantes
        df_filtrado = df[
            (df['PAIS'] == 'Colombia') &
            (df['MES'] == 12) &
            (df['PRODUCTO'].isin(productos_interes))
        ][['ANIO', 'PRODUCTO', 'ELECTRICIDAD_GENERADA_ACUMULADA']].copy()

        # Pivotear para tener cada producto como columna
        df_pivot = df_filtrado.pivot(index='ANIO', columns='PRODUCTO', values='ELECTRICIDAD_GENERADA_ACUMULADA').reset_index()

        # Calcular los porcentajes respecto a Producción neta
        df_pivot['% Consumo'] = (df_pivot['Consumo final'] / df_pivot['Producción neta de electricidad']) * 100
        df_pivot['% Pérdidas'] = (df_pivot['Pérdidas de distribución'] / df_pivot['Producción neta de electricidad']) * 100
        df_pivot['% Exportaciones'] = (df_pivot['Exportaciones totales'] / df_pivot['Producción neta de electricidad']) * 100

        # Unir resultados en formato largo
        df_resultado = pd.melt(
            df_pivot,
            id_vars='ANIO',
            value_vars=['Consumo final', 'Pérdidas de distribución', 'Exportaciones totales'],
            var_name='Categoría Energética',
            value_name='Electricidad (GWh)'
        )

        df_resultado['% sobre Producción Neta'] = pd.melt(
            df_pivot,
            id_vars='ANIO',
            value_vars=['% Consumo', '% Pérdidas', '% Exportaciones']
        )['value']

        # Renombrar para visualización
        df_resultado = df_resultado.rename(columns={'ANIO': 'año'})

        return df_resultado


    # Método para obtener los datos de energía renovable y no renovable de Colombia
    @staticmethod
    def get_renewable_and_nonrenewable_data(df):
        return df[
            (df['PAIS'] == 'Colombia') &  # Solo Colombia
            (df['ANIO'].isin([2020, 2021, 2022, 2023, 2024])) &  # Años entre 2020 y 2024
            (df['MES'] == 12) &  # Solo diciembre
            (df['PRODUCTO'].isin(['Renovables', 'No renovables']))  # Solo productos renovables y no renovables
        ]
    
    # Método para obtener la distribución de las fuentes de energía (hidroeléctrica, solar, etc.) en Colombia en un año específico
    @staticmethod
    def get_energy_source_distribution(df, year=2024, country='Colombia'):
        # Filtramos los datos para el país y año especificados, solo para diciembre y con los productos de interés
        df_filtered = df[
            (df['PAIS'] == country) &  # País específico (por defecto Colombia)
            (df['ANIO'] == year) &  # Año específico (por defecto 2024)
            (df['MES'] == 12) &  # Solo diciembre
            (df['PRODUCTO'].isin(['Hidroeléctrica', 'Solar', 'Renovables combustibles', 'Carbón', 'Petróleo', 'Gas natural', 'Otras renovables agregadas']))  # Productos de interés
        ]
        
        # Calculamos el total de electricidad generada en esas categorías
        total = df_filtered['ELECTRICIDAD_GENERADA_ACUMULADA'].sum()
        
        # Calculamos el porcentaje que representa cada fuente de energía respecto al total
        df_filtered['Porcentaje'] = (df_filtered['ELECTRICIDAD_GENERADA_ACUMULADA'] / total) * 100
        
        return df_filtered
    
    # Método para obtener la distribución de las fuentes de energía (hidroeléctrica, solar, etc.) en Colombia en un año específico
    @staticmethod
    def get_energy_source_distribution_american(df, year=2024, country=None):
        df_filtered = df[
            (df['ANIO'] == year) &
            (df['MES'] == 12) &
            (df['PRODUCTO'].isin([
                'Hidroeléctrica', 'Solar', 'Renovables combustibles', 
                'Carbón', 'Petróleo', 'Gas natural', 'Otras renovables agregadas'
            ]))
        ]

        if country is not None:
            df_filtered = df_filtered[df_filtered['PAIS'] == country]

        total = df_filtered['ELECTRICIDAD_GENERADA_ACUMULADA'].sum()
        df_filtered = df_filtered.copy()
        df_filtered['Porcentaje'] = (df_filtered['ELECTRICIDAD_GENERADA_ACUMULADA'] / total) * 100

        return df_filtered

