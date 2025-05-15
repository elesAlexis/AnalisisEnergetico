import pandas as pd

class SplitDataSet:
    
    # Método para obtener los datos de América para el año 2024
    @staticmethod
    def get_data_america_2024(df):
        # Filtramos el DataFrame para obtener los productos relacionados con la producción neta de electricidad y consumo final
        # Filtramos solo para el mes de diciembre de 2024
        # Seleccionamos las columnas necesarias: PAIS, PRODUCTO y ELECTRICIDAD_GENERADA_ACUMULADA
        return df[
            (df['PRODUCTO'].isin(['Producción neta de electricidad', 'Consumo final'])) &  # Filtramos los productos de interés
            (df['MES'] == 12) &  # Solo diciembre
            (df['ANIO'] == 2024)  # Solo el año 2024
        ][['PAIS', 'PRODUCTO', 'ELECTRICIDAD_GENERADA_ACUMULADA']]  # Seleccionamos las columnas que necesitamos


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


    # Método para obtener la comparación entre producción y consumo de energía en Colombia en 2024
    @staticmethod
    def get_colombia_production_vs_consumption_2024(df):
        # Diccionario para mapear los números de los meses a nombres
        meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
                 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
        
        # Filtramos los datos para Colombia, en el año 2024, y los productos de interés (producción y consumo)
        df_colombia = df[
            (df['PRODUCTO'].isin(['Producción neta de electricidad', 'Consumo final'])) &  # Filtramos los productos
            (df['ANIO'] == 2024) &  # Solo año 2024
            (df['PAIS'] == 'Colombia')  # Solo Colombia
        ][['MES', 'PRODUCTO', 'ELECTRICIDAD_GENERADA_GWH']]  # Seleccionamos las columnas necesarias
        
        # Convertimos el número del mes a su nombre correspondiente
        df_colombia['MES'] = df_colombia['MES'].map(meses)
        
        return df_colombia


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
