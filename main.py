"""
Aplicación Streamlit para la presentación interactiva del panorama energético en América y Colombia (2020-2024).

Este script carga, procesa y visualiza datos energéticos provenientes de un dataset CSV, utilizando funciones
modulares importadas desde los archivos CleanData.py, SplitDataSet.py y GraphicsView.py. Se presentan
gráficos y análisis sobre producción, consumo, comercio y evolución de fuentes renovables y no renovables.

Estructura:
- Configuración de la interfaz y estilo
- Carga y limpieza de datos
- Segmentación y filtrado específico de datos
- Visualización de gráficos con explicaciones
- Resultados y conclusiones
- Fuentes de datos y mensaje final

Requiere:
- Streamlit
- Módulos CleanData, SplitDataSet y GraphicsView
"""

# Importamos las bibliotecas necesarias
import streamlit as st
from CleanData import load_and_clean_data
from SplitDataSet import SplitDataSet
from GraphicsView import GraphicsView

# Configuración básica de la página Streamlit (tamaño, título e icono)
st.set_page_config(layout="wide", page_title="Panorama Energético en América y Colombia", page_icon="📊")

# CSS para ocultar elementos por defecto de la interfaz Streamlit para una presentación limpia
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Sección Portada de la presentación con título, subtítulo y descripción
st.markdown(
    """
    <div style='text-align: center; padding: 50px 0;'>
        <h1 style='font-size: 3.5em; color: #003366;'>📊 Panorama Energético en América y Colombia</h1>
        <h2 style='color: #006699;'>Análisis Interactivo del Sector Eléctrico (2020 - 2024)</h2>
        <p style='font-size: 1.2em; max-width: 800px; margin: auto;'>
            Esta presentación interactiva ofrece una mirada profunda al comportamiento del sistema eléctrico
            en América y Colombia, enfocándose en la generación, consumo, comercio y composición
            de fuentes energéticas durante los años 2020 a 2024.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Carga y limpieza de datos desde archivo CSV con indicador de progreso para el usuario
with st.spinner("Cargando datos..."):
    filepath = 'DataSet.csv'  # Ruta del archivo con los datos
    df = load_and_clean_data(filepath)  # Función importada para limpieza y carga

# Segmentación y filtrado de datos para cada análisis específico
energy_source_distribution_american = SplitDataSet.get_energy_source_distribution_american(df)
renewable_trend = SplitDataSet.get_renewable_percentage(df)
non_renewable_trend = SplitDataSet.get_non_renewable_percentage(df)
colombia_trade = SplitDataSet.get_colombia_trade_data(df)
colombia_export = SplitDataSet.get_colombia_energy_export_data(df)
dist_sources_colombia = SplitDataSet.get_energy_source_distribution(df)
dist_over_net_prod = SplitDataSet.get_distribution_over_net_production_colombia(df)
renovables_vs_no = SplitDataSet.get_renewable_and_nonrenewable_data(df)

# Visualizaciones y textos explicativos para cada sección del análisis energético

# Sección 1: Radar - Comparación de fuentes de energía entre países (por año)
st.header("1. Radar: Comparación de Fuentes de Energía entre Países (por Año)")

anios_disponibles = sorted(energy_source_distribution_american['ANIO'].unique(), reverse=True)
anio_seleccionado = st.selectbox("Selecciona el año", anios_disponibles)

df_anio = energy_source_distribution_american[energy_source_distribution_american['ANIO'] == anio_seleccionado]

paises_disponibles = sorted(df_anio['PAIS'].unique())
paises_seleccionados = st.multiselect("Selecciona los países a comparar", paises_disponibles, default=["Argentina", "Brasil", "Canadá", "Chile", "Colombia",  "México",  "Estados Unidos",  "Costa Rica"])

if len(paises_seleccionados) >= 2:
    radar_fig = GraphicsView.plot_radar_energy_comparison(energy_source_distribution_american, selected_countries=paises_seleccionados, year=anio_seleccionado)
    st.plotly_chart(radar_fig)
else:
    st.warning("Selecciona al menos dos países para comparar.")

st.markdown("""
Este gráfico de radar compara la distribución porcentual de diferentes fuentes de generación eléctrica
entre los países seleccionados para un año específico. Permite visualizar de forma clara y directa
las similitudes y diferencias en la matriz energética de cada nación, destacando la participación
de fuentes renovables y no renovables. Es una herramienta clave para entender la diversidad y el
grado de transición energética en la región americana.
""")
st.markdown("---")

# Sección 2: Energía Renovable en América
st.subheader("2. Evolución de la Generación de Energía Renovable en América")
st.plotly_chart(GraphicsView.plot_renewable_trend(renewable_trend))
st.markdown("""
Este gráfico muestra cómo ha evolucionado la participación de las fuentes de energía renovables en el mix de generación
eléctrica de América desde 2020 hasta 2024. Incluye tecnologías como hidroeléctrica, solar, eólica y biomasa. Permite
identificar tendencias de crecimiento sostenido, estancamiento o retroceso por país, evidenciando los compromisos reales
con la transición energética y el cumplimiento de metas climáticas.
""")
st.markdown("---")

# Sección 3: Energía No Renovable en América
st.subheader("3. Evolución de la Generación de Energía No Renovable en América")
st.plotly_chart(GraphicsView.plot_non_renewable_trend(non_renewable_trend))
st.markdown("""
Aquí se representa la trayectoria de la generación de energía eléctrica proveniente de fuentes no renovables,
principalmente térmicas a base de carbón, gas natural y petróleo. La visualización permite analizar qué países están
logrando disminuir su dependencia de combustibles fósiles y cuáles mantienen una matriz energética intensiva en carbono,
lo cual tiene implicaciones tanto ambientales como económicas.
""")
st.markdown("---")

# Sección 4: Comercio Energético de Colombia
st.subheader("4. Comercio de Electricidad en Colombia (2020-2024)")
st.plotly_chart(GraphicsView.plot_colombia_trade(colombia_trade))
st.markdown("""
Esta visualización expone el comportamiento del comercio internacional de electricidad de Colombia, mostrando las
cantidades exportadas e importadas año a año entre 2020 y 2024. Nos permite ver cómo ha evolucionado la balanza
energética del país, en qué momentos ha necesitado importar energía y cuándo ha sido capaz de exportar, revelando su
integración con los mercados regionales y la estabilidad de su sistema eléctrico.
""")
st.markdown("---")

# Sección 5: Producción vs Exportación en Colombia
st.subheader("5. Comparación de Producción y Exportación de Electricidad en Colombia")
st.plotly_chart(GraphicsView.plot_colombia_energy_export(colombia_export))
st.markdown("""
Este gráfico compara la producción nacional total de electricidad con las cantidades exportadas por Colombia en el mismo
período. Permite evaluar la capacidad del país para generar excedentes energéticos sostenibles que soporten las
exportaciones sin poner en riesgo el abastecimiento interno. También indica la eficiencia y confiabilidad de la
infraestructura energética local.
""")
st.markdown("---")

# Sección 6: Distribución por Fuente en Colombia (2024)
st.subheader("6. Distribución de Fuentes de Energía en Colombia (2024)")
st.plotly_chart(GraphicsView.plot_energy_source_distribution(dist_sources_colombia))
st.markdown("""
Este gráfico muestra la proporción de cada tipo de fuente energética utilizada para generar electricidad en Colombia
durante el año 2024. Distingue entre fuentes renovables (como hidroeléctrica, solar y eólica) y no renovables (térmicas
de carbón, gas o petróleo). Esta información es clave para entender el nivel de sostenibilidad de la matriz energética
del país y su vulnerabilidad ante eventos climáticos o precios internacionales del combustible.
""")
st.markdown("---")

# Sección 7: Distribución del Uso de la Producción Neta en Colombia
st.subheader("7. Distribución del Uso de la Producción Neta en Colombia")
st.plotly_chart(GraphicsView.plot_distribution_over_net_production_colombia(dist_over_net_prod))
st.markdown("""
En esta sección se detalla cómo se distribuyó la electricidad generada en Colombia durante el período analizado: qué
porcentaje se destinó al consumo interno, cuánto se perdió en el sistema (pérdidas técnicas y no técnicas), y qué parte
se dedicó al comercio internacional (exportaciones e importaciones). Este análisis permite evaluar la eficiencia del
sistema eléctrico y detectar áreas de mejora en infraestructura o gestión.
""")
st.markdown("---")

# Sección 8: Energía Renovable vs No Renovable en Colombia
st.subheader("8. Evolución de Energía Renovable y No Renovable en Colombia")
st.plotly_chart(GraphicsView.plot_renewable_and_nonrenewable_data(renovables_vs_no))
st.markdown("""
Esta visualización compara la evolución en el tiempo de la generación eléctrica a partir de fuentes renovables y no
renovables en Colombia. Es fundamental para entender el ritmo y la dirección de la transición energética nacional,
permitiendo identificar años clave de inflexión o retroceso, y evaluar si el país se está moviendo hacia una matriz más
limpia y resiliente.
""")

st.markdown("---")

# Resultados relevantes destacados en lista
st.subheader("📈 Resultados Relevantes")
st.markdown("""
<ul style='font-size: 1.1em;'>
    <li><strong>EE.UU. y Brasil</strong> lideran el consumo total de electricidad en América.</li>
    <li><strong>Costa Rica</strong> presenta el menor consumo relativo en comparación con el resto de países.</li>
    <li>Se observa un <strong>aumento sostenido de las energías renovables</strong> en gran parte de la región.</li>
    <li><strong>Colombia</strong> ha mostrado un crecimiento en sus exportaciones de electricidad desde el año <strong>2023</strong>.</li>
</ul>

<h4 style='padding-top: 10px;'>Matriz energética de Colombia en 2024:</h4>
<ul style='font-size: 1.05em;'>
    <li><strong>54.3%</strong> proviene de <strong>hidroeléctrica</strong>.</li>
    <li>La participación <strong>solar</strong> es aún baja, con un <strong>4.01%</strong>.</li>
    <li>Persistente uso de fuentes <strong>fósiles</strong> como gas, carbón y petróleo.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("---")

# Conclusiones generales extraídas del análisis
st.subheader("📌 Conclusiones Generales")
st.markdown("""
1. **América muestra un panorama energético mixto.** Algunos países son autosuficientes en su generación eléctrica, mientras otros aún dependen de importaciones, lo que genera desigualdades en seguridad energética.

2. **La participación de fuentes renovables está creciendo**, especialmente gracias a la energía hidroeléctrica y solar. Sin embargo, este avance no es uniforme: algunos países han mantenido o incluso reducido su generación limpia.

3. **La dependencia de fuentes fósiles persiste en muchos países**, lo que representa un reto ambiental y económico frente a la volatilidad de precios y los compromisos climáticos globales.

4. **Colombia ha mantenido una matriz energética predominantemente renovable**, principalmente por su uso de energía hidroeléctrica, aunque sigue habiendo espacio para diversificar hacia otras fuentes limpias como la solar o eólica.

5. **El comercio de electricidad en Colombia ha sido variable**, reflejando una interacción activa con sus vecinos, pero también cierta vulnerabilidad en momentos de baja generación o alta demanda.

6. **Las pérdidas en el sistema eléctrico colombiano siguen siendo un desafío.** Reducirlas podría significar un uso más eficiente de la energía generada.
""")

st.markdown("---")

# Proyección futura para el sector energético regional
st.subheader("🔮 Proyección a Futuro")
st.markdown("""
- Se espera que la región avance hacia una **mayor adopción de fuentes renovables**, especialmente con inversiones en energía solar y eólica.

- **Colombia tiene el potencial de convertirse en un exportador regional más fuerte**, si fortalece su infraestructura, mejora su eficiencia y mantiene su matriz limpia.

- A medida que aumente la presión por cumplir los compromisos climáticos, los países con matrices energéticas aún intensivas en carbono deberán acelerar sus procesos de transición.

- La **digitalización, el almacenamiento energético y la cooperación entre países** serán claves para una red eléctrica más estable, eficiente y sostenible en América.
""")
st.markdown("---")

# Fuente oficial de los datos usados en el análisis
st.subheader("📚 Fuente de los Datos")
st.markdown("""
Los datos utilizados en esta aplicación provienen de la <a href='https://www.iea.org/' target='_blank'>Agencia Internacional de Energía (IEA)</a>, 
una fuente reconocida a nivel mundial por su análisis energético detallado y confiable. La información ha sido procesada y organizada para fines
de visualización y análisis comparativo entre países de América y el caso particular de Colombia durante el periodo 2020–2024.
""", unsafe_allow_html=True)

st.markdown("---")

# Frase de cierre motivadora para la presentación
st.markdown("""
<div style='text-align: center; padding-top: 30px; font-size: 1.3em; color: #003366;'>
    <em>
        "El futuro energético de América no solo depende de sus recursos, sino de las decisiones inteligentes 
        que tomemos hoy. Apostar por una matriz más limpia, eficiente y solidaria es apostar por el bienestar de las próximas generaciones."
    </em>
</div>
""", unsafe_allow_html=True)