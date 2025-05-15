#Se importa las librería que se van usar en la limpieza 
import pandas as pd

def load_and_clean_data(filepath):
    print("📥 Leyendo el archivo:", filepath)
    df = pd.read_csv(filepath, sep=',')

    # Validar años únicos
    print("\n📆 AÑOS DISPONIBLES")
    print("-" * 40)
    print(df['YEAR'].unique())

    # Validar valores nulos
    print("\n🧼 VALORES NULOS POR COLUMNA")
    print("-" * 40)
    print(df.isnull().sum())

    # Renombrar columnas
    df = df.rename(columns={
        "COUNTRY": "PAIS",
        "YEAR": "ANIO",
        "MONTH": "MES",
        "PRODUCT": "PRODUCTO",
        "VALUE": "ELECTRICIDAD_GENERADA_GWH",
        "yearToDate": "ELECTRICIDAD_GENERADA_ACUMULADA"
    })

    # Traducir PRODUCTOS
    traducciones_productos = {
        'Hydro': 'Hidroeléctrica',
        'Wind': 'Eólica',
        'Solar': 'Solar',
        'Geothermal': 'Geotérmica',
        'Other renewables': 'Otras renovables',
        'Nuclear': 'Nuclear',
        'Total combustible fuels': 'Total combustibles',
        'Coal': 'Carbón',
        'Oil': 'Petróleo',
        'Natural gas': 'Gas natural',
        'Combustible renewables': 'Renovables combustibles',
        'Other combustible non-renewables': 'Otros no renovables combustibles',
        'Not specified': 'No especificado',
        'Net electricity production': 'Producción neta de electricidad',
        'Total imports': 'Importaciones totales',
        'Total exports': 'Exportaciones totales',
        'Electricity supplied': 'Electricidad suministrada',
        'Used for pumped storage': 'Usado para almacenamiento por bombeo',
        'Distribution losses': 'Pérdidas de distribución',
        'Final consumption': 'Consumo final',
        'Electricity trade': 'Intercambio de electricidad',
        'Renewables': 'Renovables',
        'Non-renewables': 'No renovables',
        'Others': 'Otros',
        'Other renewables aggregated': 'Otras renovables agregadas',
        'Low carbon': 'Bajo carbono',
        'Fossil fuels': 'Combustibles fósiles'
    }
    df['PRODUCTO'] = df['PRODUCTO'].replace(traducciones_productos)

    # Mostrar productos únicos
    print("\n🔋 TIPOS DE PRODUCTOS ENERGÉTICOS")
    print("-" * 40)
    print(df['PRODUCTO'].unique())

    # Traducir PAÍSES
    traducciones_paises = {
        'Argentina': 'Argentina',
        'Brazil': 'Brasil',
        'Canada': 'Canadá',
        'Chile': 'Chile',
        'Colombia': 'Colombia',
        'Mexico': 'México',
        'United States': 'Estados Unidos',
        'Costa Rica': 'Costa Rica'
    }
    df['PAIS'] = df['PAIS'].replace(traducciones_paises)

    # Mostrar países únicos
    print("\n🌍 PAÍSES EN EL DATASET")
    print("-" * 40)
    print(df['PAIS'].unique())

    # Info general del DataFrame
    print("\n📊 INFORMACIÓN DEL DATASET")
    print("-" * 40)
    print(df.info())

    # Resumen estadístico
    print("\n📈 ESTADÍSTICAS DESCRIPTIVAS")
    print("-" * 40)
    print(df.describe())

    return df
