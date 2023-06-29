import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime,timedelta
import datetime
import plotly.express as px
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.dates as mdates
from matplotlib.widgets import RangeSlider
from PIL import Image

# Estilo de la página
st.markdown(
    """
    <style>
        .big-font {
            font-size: 24px;
            font-weight: bold;
            color: red;
            text-align: center;
            padding-bottom: 20px;
            font-family:cursive; 
        }
        .highlight {
            background-color: darkslategrey;
            padding: 10px;
            border-radius: 10px;
        }
        code {
            font-family: 'Arial', sans-serif; 
            font-size: 14px;
            color: red;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Cargar y mostrar el logo
logo = Image.open('Logo_Oficiall.png')
st.sidebar.image(logo)


# Ruta del archivo CSV
ruta_csv ="DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_4.csv"

# Lee el archivo CSV en un DataFrame
df = pd.read_csv(ruta_csv, encoding='latin-1')

#################################################################################

tabs = ['Nosotros', 'Datos Hidrometereológicos']
selected_tab = st.sidebar.selectbox('Selecciona una pestaña', tabs)

if selected_tab == 'Nosotros':
    # Encabezado
    st.markdown('<p style="text-align: center; font-size: 24px; font-weight: bold;">“Año de la unidad, la paz y el desarrollo”</p>', unsafe_allow_html=True)
    st.header('Universidad Peruana Cayetano Heredia')
    st.subheader('Curso:')
    st.write('- Programación Avanzada')
    st.subheader('Caso Escogido:')
    st.write('- Datos Hidrometereológicos Gobierno Regional Piura')
    st.subheader('Integrantes del Curso:')
    st.write('- Armas Castañeda Darlin Alberto')
    st.write('- Guerrero Suarez Cecilia')
    st.write('- Portugal Torres Jorge Alexander')
    st.write('- Lima Quispe Alexandra Nancy')

    st.subheader('Profesores:')
    st.write('- Moltalvo Garcia Peter Jonathan')
    st.write('- Alata Vences Enrique Plinio')
    st.write('- Castelo Fernandez Cesar Christian')

    st.header("¡Contáctanos!")
    st.markdown("""
    Si tienes alguna pregunta o comentario, no dudes en ponerte en contacto con nosotros. Estamos aquí para ayudarte.
    """)

    redes_contacto = ['Email', 'Teléfono', 'Whatsapp']
    red_seleccionada = st.selectbox('Elige la red de contacto', redes_contacto)

    if red_seleccionada == 'Email':
	    correos = ['darlin.armas@upch.pe', 'cecilia.guerrero@upch.pe','jorge.portugal@upch.pe','alexandra.lima@upch.pe']
	    st.write('Ponte en contacto con nosotros a través de nuestro correo electrónico:')
	    for correo in correos:
		    st.write(f'✉ [{correo}](mailto:{correo})')


    elif red_seleccionada == 'Teléfono':
	    telefonos = ['+51931001223','+51916727662','+51964388089','+51988954149']
	    st.write(f'Llámanos al nuestros números telefónicos para obtener asistencia inmediata:')
	    for telefono in telefonos:
		    st.write(f'📞 [{telefono}](tel:{telefono})')


    elif red_seleccionada == 'Whatsapp':
	    numeros_whatsapp = ['+51931001223', '+51916727662','+51964388089','+51988954149']
	    st.write(' Envíanos un mensaje por Whatsapp y te responderemos lo antes posible:')
	    for whatsapp in numeros_whatsapp:
		    st.write(f'📲 [{whatsapp}](https://wa.me/{whatsapp})')


else:
	st.markdown("<h1 class='big-font'>Análisis de Datos Hidrometeorológicos [Gobierno Regional Piura]</h1>", unsafe_allow_html=True)
	st.markdown(
    """
    En esta página de Streamlit, explorarás los datos hidrometeorológicos de la región. 
    Descubre patrones y tendencias relacionadas con el caudal y la precipitación en un formato interactivo y visualmente atractivo.
    """
	)
	show_info = False  # Variable de estado inicializada en False
	if st.button('Seguir leyendo'):
	    show_info = not show_info
	    st.write("Agua y Saneamiento")
	    st.write("Contiene los datos Hidrometeorológicos del Sistema Hidráulico Mayor a cargo del Proyecto Especial Chira Piura.")
	    st.header("Descripción del Dataset")
	    st.write("Este dataset muestra los datos hidrometeorológicos registrados de las presas, estaciones hidrológicas e hidrométricas.")
	    st.write("Esta información contiene el nombre de la cuenca, nombre de la estación, medida del caudal a las 007:00 horas, el promedio del caudal a las 24:00 horas, el caudal máximo a las 24:00 horas, niveles de presas a las 7:00 horas, nivel máximo de las presas a las 24:00 horas, el volumen de las presas a las 07:00 y precipitaciones.")
	    ruta_imagen = "https://servicios.regionpiura.gob.pe/servicios/datos/mapa/crear_mapa.php"
	    st.image(ruta_imagen, caption='Fuente: Gobierno Regional de Piura', use_column_width=True)
	# Convertir la columna 'FECHA... en formato de fecha

	df['FECHA_MUESTRA'] = pd.to_datetime(df['FECHA_MUESTRA'], format='%Y%m%d')
	df['FECHA_CORTE'] = pd.to_datetime(df['FECHA_CORTE'], format='%Y%m%d')

	# Formatear las fechas en formato año-mes-día
	df['FECHA_MUESTRA'] = df['FECHA_MUESTRA'].dt.strftime('%Y-%m-%d')
	df['FECHA_CORTE'] = df['FECHA_CORTE'].dt.strftime('%Y-%m-%d')

	# Muestra los datos en Streamlit
	st.write(df)

	st.header("Definiciones")
	st.write("La cuenca es una extensión de terreno en un valle, escurren aguas formando un río atravesando valles y escurriendo en el mar.")
	st.write("Una cuenca puede tener varias estaciones hidrometeorológicas.")
	st.write("El dato de precipitación es la lluvia acumulada entre las 7:00 horas del día anterior y las 7:00 horas de hoy (24 horas). Cuando se considera el campo vacío, indica que no se realizaron mediciones.")
	st.write("Para mayor información también puede ingresar a:")
	st.write("[http://servicios.regionpiura.gob.pe/datosh](http://servicios.regionpiura.gob.pe/datosh)")
	# Crear el gráfico de línea
	with st.expander("**Gráfico de línea**"):
		fig, ax = plt.subplots()
		plt.plot(df['FECHA_MUESTRA'], df['PROMEDIO24H'])
		plt.xlabel('Fecha muestra')
		plt.ylabel('Caudal promedio en 24 horas')
		plt.title('Caudal promedio en 24 horas vs. Fecha muestra')
		plt.xticks(rotation=90)
		plt.gca().xaxis.set_major_locator(plt.MaxNLocator())  # Establecer las etiquetas de fechas cada 12 rangos
		plt.gca().invert_xaxis()

		plt.tight_layout()  # Ajustar el espaciado
		plt.show()
		st.pyplot(fig)
		st.write("Este es un gráfico de línea que muestra el caudal promedio en 24 horas en función de la fecha muestra. El eje x representa las fechas y el eje y representa el caudal promedio. En la gráfica se muestra cómo varía el caudal a lo largo del tiempo.")

	#-----------------------------------
	# Convertir la columna 'FECHA_MUESTRA' en formato de fecha
	df['FECHA_MUESTRA'] = pd.to_datetime(df['FECHA_MUESTRA'])

	# Crear una columna con el nombre del mes
	df['MES'] = df['FECHA_MUESTRA'].dt.strftime('%b')

	# Crear una columna con el año
	df['ANIO'] = df['FECHA_MUESTRA'].dt.year

	# Obtener los años únicos en el DataFrame
	anios_unicos = df['ANIO'].unique()

	# Crear el gráfico de línea
	with st.expander("Caudal promedio en 24 horas vs. Mes"):
		fig, ax = plt.subplots()

		# Iterar sobre los años únicos y graficar los datos correspondientes
		for anio in anios_unicos:
		    datos_anio = df[df['ANIO'] == anio]
		    ax.plot(datos_anio['MES'], datos_anio['PROMEDIO24H'], label=str(anio))

		plt.xlabel('Mes')
		plt.ylabel('Caudal promedio en 24 horas')
		plt.title('Caudal promedio en 24 horas vs. Mes')
		plt.xticks(rotation=90)
		ax.legend()
		plt.tight_layout()  # Ajustar el espaciado
		plt.show()
		st.pyplot(fig)
		st.write("En este gráfico se muestra la variación del caudal promedio en 24 horas en función del mes. Cada línea representa un año diferente, y en el eje x se muestran los meses del año. El eje y representa el caudal promedio en 24 horas. Asi se permite identificar patrones estacionales en el caudal a lo largo de los años.")

	#----------------------------





	# Calcular la suma de la precipitación por distrito
	with st.expander("precipitación por Distrito"):
		precipitacion_por_Distrito = df.groupby(['DISTRITO'])['PRECIP24H'].sum()

		# Convertir los nombres de los departamentos a una lista de strings
		departamentos = [str(depto) for depto in precipitacion_por_Distrito.index]

		# Crear el gráfico de barras
		fig, ax = plt.subplots()
		ax.bar(range(len(departamentos)), precipitacion_por_Distrito)
		ax.set_xlabel('Distrito')
		ax.set_ylabel('Precipitación en 24 horas')
		ax.set_title('Precipitación en 24 horas por Distrito')

		# Establecer los ticks del eje x y etiquetas
		ax.set_xticks(range(len(departamentos)))
		ax.set_xticklabels(departamentos, rotation=45)

		# Mostrar el gráfico utilizando st.pyplot()
		st.pyplot(fig)
		st.write("Este gráfico de barras muestra la suma de la precipitación en 24 horas por distrito. Cada barra representa un distrito, donde se muestran los nombres de los distritos y la cantidad de precipitación en 24 horas. Asimismo nos permite comparar la precipitación entre los distintos distritos y identificar aquellos con mayor o menor acumulación de precipitación.")
	with st.expander("Caudal vs. Fecha"):
		fig, ax = plt.subplots()
		ax.plot(df['FECHA_MUESTRA'], df['CAUDAL07H'])
		ax.set_xlabel('Fecha')
		ax.set_ylabel('Caudal')
		ax.set_title('Caudal vs. Fecha')
		plt.xticks(rotation=45)
		st.pyplot(fig)
		st.write("En este gráfico de línea podemos ver la variación del caudal a lo largo del tiempo, el cual nos permite observar patrones o tendencias en el caudal a medida que transcurren las fechas. Se ha rotado el texto del eje x para mejorar la legibilidad. ")






	with st.expander("Promedio de Caudal por Provincia"):
		promedio_caudal_por_departamento = df.groupby('PROVINCIA')['PROMEDIO24H'].mean()

		fig, ax = plt.subplots()
		ax.bar(promedio_caudal_por_departamento.index, promedio_caudal_por_departamento)
		ax.set_xlabel('Departamento')
		ax.set_ylabel('Promedio de Caudal')
		ax.set_title('Promedio de Caudal por Provincia')
		plt.xticks(rotation=45)
		st.pyplot(fig)
		st.write("Este gráfico de barras muestra el promedio de caudal por provincia. Cada barra representa una provincia y en el eje x se muestran los nombres de las provincias. El eje y representa el promedio de caudal. Este permite comparar los promedios de caudal entre las distintas provincias y identificar aquellas con mayor o menor promedio. La rotación de las etiquetas en el eje x mejora la legibilidad del gráfico.")


	with st.expander("Gráfico de Pastel: Distribución de Estaciones por Tipo"):
		estaciones_por_tipo = df['TIPO_ESTACION'].value_counts()

		fig, ax = plt.subplots()
		ax.pie(estaciones_por_tipo, labels=estaciones_por_tipo.index, autopct='%1.1f%%', startangle=90)
		ax.set_title('Distribución de Estaciones por Tipo')
		st.pyplot(fig)
		st.write("Este gráfico de pastel nos permite visualizar la distribución de estaciones por tipo. Cada sector del pastel representa un tipo de estación y el tamaño del sector corresponde a la proporción de estaciones de ese tipo con respecto al total. Las etiquetas en el pastel indican el tipo de estación y el porcentaje correspondiente. El gráfico permite visualizar de manera clara la proporción de estaciones según su tipo.")

	with st.expander("precipitacion maxima"):
		fig, ax = plt.subplots()
		ax.scatter(df['MAXIMA24H'], df['PRECIP24H'])
		ax.set_xlabel('Máxima en 24 horas')
		ax.set_ylabel('Precipitación en 24 horas')
		ax.set_title('Caudal máximo vs. Precipitación en 24 horas')
		st.pyplot(fig)
		st.write("Este gráfico de dispersión muestra la relación entre la máxima precipitación en 24 horas y la precipitación en 24 horas. Cada punto representa una muestra de datos, donde el eje x representa la máxima precipitación y el eje y representa la precipitación en 24 horas. El gráfico permite identificar la relación entre estos dos valores y detectar posibles patrones o tendencias. La dispersión de los puntos puede indicar la variabilidad en la relación entre la máxima precipitación y la precipitación en 24 horas.")

	# Calcular el promedio de caudal por provincia y distrito
	promedio_caudal_por_provincia = df.groupby(['PROVINCIA', 'DISTRITO'])['PROMEDIO24H'].mean().unstack()

	with st.expander("Promedio de caudal por provincia y distrito"):
	    # Crear el gráfico de barras
	    fig, ax = plt.subplots()
	    promedio_caudal_por_provincia.plot(kind='bar', ax=ax)
	    ax.set_xlabel('Provincia')
	    ax.set_ylabel('Promedio de Caudal')
	    ax.set_title('Promedio de Caudal por Provincia y Distrito')
	    plt.xticks(rotation=45)
	
	    # Mostrar el gráfico en la aplicación
	    st.pyplot(fig)
	    st.write("En este gráfico podemos encontrar el promedio de caudal para cada provincia y distrito en el conjunto de datos. Cada barra representa el promedio de caudal para un determinado distrito dentro de una provincia que nos va permite comparar visualmente los promedios de caudal entre diferentes provincias y distritos, y así identificar patrones o diferencias significativas en el caudal promedio en diferentes áreas geográficas.")
	

#..........................................................

	# Convertir la columna 'FECHA_MUESTRA' al formato adecuado
	df['FECHA_MUESTRA'] = pd.to_datetime(df['FECHA_MUESTRA'], format='%Y%m%d')

	# Obtener la fecha mínima y máxima en el DataFrame
	fecha_minima = df['FECHA_MUESTRA'].min().date()
	fecha_maxima = df['FECHA_MUESTRA'].max().date()

	# Crear un selector de fechas para elegir el rango de fechas
	rango_fechas = st.date_input('Seleccione un rango de fechas', [fecha_minima, fecha_maxima], min_value=fecha_minima, max_value=fecha_maxima)

	# Convertir las fechas seleccionadas a objetos date
	fecha_inicio = date(rango_fechas[0].year, rango_fechas[0].month, rango_fechas[0].day)
	fecha_fin = date(rango_fechas[1].year, rango_fechas[1].month, rango_fechas[1].day)

	# Filtrar los datos por el rango de fechas seleccionado
	df_filtrado = df[(df['FECHA_MUESTRA'].dt.date >= fecha_inicio) & (df['FECHA_MUESTRA'].dt.date <= fecha_fin)]

	# Crear figura y ejes
	fig1, ax1 = plt.subplots()
	fig2, ax2 = plt.subplots()

	# Realizar acciones de trazado en los ejes
	ax1.plot(df_filtrado['FECHA_MUESTRA'], df_filtrado['PROMEDIO24H'])
	ax1.set_xlabel('Fecha')
	ax1.set_ylabel('Caudal Promedio en 24 horas')
	ax1.set_title('Caudal Promedio por fecha en el rango seleccionado')

	ax2.plot(df_filtrado['FECHA_MUESTRA'], df_filtrado['PRECIP24H'])
	ax2.set_xlabel('Fecha')
	ax2.set_ylabel('Precipitación en 24 horas')
	ax2.set_title('Precipitación por fecha en el rango seleccionado')

	# Mostrar los gráficos en Streamlit
	with st.expander("Caudal Promedio por fecha en el rango seleccionado"):
		plt.xticks(rotation=90)
		st.pyplot(fig1)
		st.write("El gráfico muestra el caudal promedio en 24 horas para las fechas seleccionadas.Este permite visualizar la variación del caudal a lo largo del rango de fechas seleccionado.")
	with st.expander("Precipitación por fecha en el rango seleccionado"):
		plt.xticks(rotation=90)
		st.pyplot(fig2)
		st.write("El gráfico muestra la precipitación en 24 horas para las fechas seleccionadas. El eje x representa la fecha y el eje y muestra la cantidad de precipitación.Asi podemos ver la variación de la precipitación a lo largo del rango de fechas seleccionado.")
	
	# Convertir la columna 'FECHA_MUESTRA' en formato de fecha
	df['FECHA_MUESTRA'] = pd.to_datetime(df['FECHA_MUESTRA'])
#....................................................................................
	# Gráfico de área: Distribución de Precipitación
	fig, ax = plt.subplots()
	df.plot(x='FECHA_MUESTRA', y='PRECIP24H', kind='area', ax=ax)
	ax.set_xlabel('Fecha de Muestra')
	ax.set_ylabel('Precipitación en 24 horas')
	ax.set_title('Distribución de Precipitación')
	with st.expander("Distribución de Precipitación"):
		plt.xticks(rotation=90)
		st.pyplot(fig)
		st.write("Aqui podemos ver la distribución de la precipitación en 24 horas a lo largo del tiempo. En el eje x  se representa la fecha de muestra y en el eje y muestra la cantidad de precipitación. El gráfico de área permite visualizar la variación de la precipitación a lo largo del tiempo de forma acumulativa.")
	
#....................................................

	# Gráfico de dispersión: Caudal vs Precipitación
	fig, ax = plt.subplots()
	df.plot(x='CAUDAL07H', y='PRECIP24H', kind='scatter', ax=ax)
	ax.set_xlabel('Caudal a las 07:00 horas')
	ax.set_ylabel('Precipitación en 24 horas')
	ax.set_title('Relación entre Caudal y Precipitación')
	with st.expander("Relación entre Caudal y Precipitación"):
		plt.xticks(rotation=90)
		st.pyplot(fig)
		st.write("Se muestra la relación entre el caudal a las 07:00 horas y la precipitación en 24 horas. Se utiliza un gráfico de dispersión para visualizar la dispersión de los datos, para asi poder analizar si existe alguna relación o patrón entre estas dos variables.")


	st.markdown(
	    """
	    
	    ¡Diviértete explorando los datos hidrometeorológicos y descubre nuevos conocimientos!
	    """
	)
	
# Footer
st.markdown("<p class='highlight' style='color:red;'>© Equipo#1 2023-1 Análisis de Datos Hidrometeorológicos. Todos los derechos reservados.</p>",
unsafe_allow_html=True)
