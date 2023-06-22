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
import streamlit.components.v1 as components

# Contenido de la aplicación
st.markdown(
    """
    <style>
    body {
        background-color: rgb(155, 222, 157);
        color: rgb(22, 21, 21);
    }
    .big-font {
        font-size: 24px;
        font-weight: bold;
        color: red;
        text-align: center;
        padding-bottom: 20px;
        font-family: cursive;
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

# Contenido de la aplicación
st.markdown("<p class='big-font'>Título de la aplicación</p>", unsafe_allow_html=True)
st.markdown("Este es un texto resaltado")
st.code("print('Hola, mundo!')")
# Cargar y mostrar el logo
logo = Image.open('Logo_Oficiall.png')
st.sidebar.image(logo)

import pandas as pd
import streamlit as st

import pandas as pd
import streamlit as st

# Ruta del archivo CSV
ruta_csv = "DATOS_HIDROMETEREOLOGICOS_GORE_PIURA_4.csv"

# Lee el archivo CSV en un DataFrame
df = pd.read_csv(ruta_csv, encoding='latin-1')
df['FECHA_MUESTRA'] = pd.to_datetime(df['FECHA_MUESTRA'], format='%Y%m%d')
df['FECHA_CORTE'] = pd.to_datetime(df['FECHA_CORTE'], format='%Y%m%d')

# Formatear las fechas en formato año-mes-día
df['FECHA_MUESTRA'] = df['FECHA_MUESTRA'].dt.strftime('%Y-%m-%d')
df['FECHA_CORTE'] = df['FECHA_CORTE'].dt.strftime('%Y-%m-%d')


# Slider para filtrar por fechas
st.subheader("Slider para Filtrar por Fecha")

fecha_min = pd.to_datetime(df['FECHA_MUESTRA']).min()
fecha_max = pd.to_datetime(df['FECHA_MUESTRA']).max()

fecha_inicio = st.date_input('Seleccione la fecha de inicio', value=fecha_min, min_value=fecha_min, max_value=fecha_max)
fecha_fin = st.date_input('Seleccione la fecha de fin', value=fecha_max, min_value=fecha_min, max_value=fecha_max)

if fecha_inicio <= fecha_fin:
    fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')
    fecha_fin = fecha_fin.strftime('%Y-%m-%d')
    df_filtrado = df[(df['FECHA_MUESTRA'] >= fecha_inicio) & (df['FECHA_MUESTRA'] <= fecha_fin)]
    # Mostrar los datos filtrados en Streamlit
    st.write(df_filtrado)
else:
    st.warning('Seleccione fechas válidas')
