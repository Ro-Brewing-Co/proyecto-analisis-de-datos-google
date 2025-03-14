# -*- coding: utf-8 -*-
"""fitbit-proyecto-final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18suwhsYi0DzhjeuDQp_UQz3OzGYUYEgC
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

pip install dash plotly panda

"""# Caso práctico 2: ¿Cómo puede hacer una empresa tecnología para el bienestar para tomar decisiones inteligentes?

## Introducción

¡Bienvenido al caso práctico de análisis de datos de Bellabeat! En este caso práctico, realizarás muchas tareas del mundo real, típicas de un analista de datos júnior. Imaginarás que trabajas para Bellabeat, un fabricante de productos de alta tecnología orientados a la salud de la mujer, y conocerás a diferentes personajes y miembros del equipo. Para responder a las preguntas clave de la empresa, seguirás los pasos del proceso de análisis de datos: preguntar, preparar, procesar, analizar, compartir y actuar. En este proceso, las tablas del mapa de ruta de caso práctico, incluidas las preguntas orientativas y las tareas clave, te ayudarán a mantenerte en el camino correcto.

Al final de esta lección, tendrás un caso práctico listo para el portfolio. Descarga el paquete y consulta los detalles de este caso práctico en cualquier momento. Así, cuando empieces a buscar trabajo, tu caso práctico será una forma tangible de demostrar tus conocimientos y habilidades a los posibles empleadores.

## Escenario

Eres un analista de datos júnior que trabaja en el equipo de analistas de marketing de Bellabeat, fabricante de productos de alta tecnología orientados a la salud de la mujer. Bellabeat es una empresa pequeña exitosa, pero tiene el potencial para convertirse en un actor más grande en el mercado global de dispositivos inteligentes. Urška Sršen, cofundadora y directora creativa de Bellabeat, cree que analizar los datos de actividad física de los dispositivos inteligentes podría desplegar nuevas oportunidades de negocio para la empresa. Te han pedido que te concentres en uno de los productos de Bellabeat y analices los datos de los dispositivos inteligentes para conocer el uso que hacen los consumidores de sus dispositivos inteligentes. Los hallazgos que descubras ayudarán a orientar la estrategia de marketing de la empresa. Presentarás tu análisis al equipo ejecutivo de Bellabeat junto con tus recomendaciones de alto nivel para la estrategia de marketing de Bellabeat.

## Personajes y productos

### Personajes
- **Urška Sršen**: Cofundadora y directora creativa de Bellabeat.
- **Sando Mur**: Matemático y cofundador de Bellabeat, miembro clave del equipo ejecutivo.
- **Equipo de análisis computacional de datos de marketing**: Equipo encargado de recopilar, analizar e informar datos que guían la estrategia de marketing.

### Productos
- **Aplicación Bellabeat**: Monitorea actividad física, sueño, estrés, ciclo menstrual y hábitos de conciencia plena.
- **Leaf**: Dispositivo de seguimiento clásico para actividad física, sueño y estrés.
- **Time**: Reloj inteligente que combina diseño clásico y seguimiento de bienestar.
- **Spring**: Botella de agua inteligente para seguimiento de hidratación.
- **Membresía Bellabeat**: Programa de orientación personalizada en nutrición, actividad física, sueño y conciencia plena.

## Acerca de la empresa

Bellabeat fue fundada por Urška Sršen y Sando Mur en 2013 con el objetivo de desarrollar productos tecnológicos orientados al bienestar de la mujer. Creció rápidamente y se posicionó como una empresa líder en tecnología de bienestar femenino. Bellabeat vende sus productos en tiendas minoristas y online, empleando marketing tradicional y digital, con un enfoque particular en publicidad en Google Search, Facebook, Instagram, Twitter, YouTube y Google Display Network.

## Preguntar

Sršen solicita que analices los datos de dispositivos inteligentes externos para aplicarlos a un producto Bellabeat específico. Tus análisis deben responder:

1. ¿Cuáles son algunas tendencias de uso de dispositivos inteligentes?
2. ¿Cómo aplicar estas tendencias a los clientes de Bellabeat?
3. ¿Cómo estas tendencias pueden influir en la estrategia de marketing de Bellabeat?

Crearás un informe con:

- Resumen claro de la tarea empresarial.
- Fuentes de datos utilizadas.
- Limpiezas y manipulaciones de datos.
- Análisis resumido.
- Visualizaciones clave.
- Tres recomendaciones de contenido de alto nivel.

## Preguntar

- **Pregunta clave:** ¿Cuál es el problema que intentas resolver?
- **Tareas clave:** Identificar la tarea empresarial e interesados clave.
- **Entregable:** Una instrucción clara de la tarea empresarial.

## Preparar

Usarás datos públicos como:
- Datos de seguimiento de actividad física Fitbit (Kaggle, CC0).

- **Tareas clave:** Descarga y almacenamiento de datos, organización, orden y filtrado, evaluar credibilidad.
- **Entregable:** Descripción detallada de fuentes utilizadas.

## Procesar

- Descarga, organiza, limpia y filtra los datos.
- **Entregable:** Documentación de limpieza y manipulación.

## Analizar

- Explora datos para descubrir tendencias o relaciones.
- **Entregable:** Resumen del análisis.

## Compartir

- Visualiza datos para comunicar hallazgos clave.
- **Entregable:** Visualizaciones y hallazgos clave.

## Actuar

- Resume conclusiones y ofrece recomendaciones de estrategia.
- **Entregable:** Tres recomendaciones de alto nivel basadas en tu análisis.

## Preguntar:

Pregunta clave: ¿Cuál es el problema que intentas resolver?

Tareas clave: Identificar la tarea empresarial e interesados clave.

Entregable: Una instrucción clara de la tarea empresarial.

Aquí te dejo el contenido perfectamente estructurado para la **primera parte del análisis de datos**, siguiendo el enfoque solicitado:

---

## Primera Parte del Análisis de Datos

---

### **Pregunta Clave**  
**¿Cuál es el problema que intentas resolver?**

Bellabeat desea **aumentar la retención y el compromiso de sus usuarias** mediante un análisis profundo de los datos de uso de sus dispositivos inteligentes. El problema central es identificar **cómo los diferentes patrones de actividad física influyen en la fidelidad de las usuarias** y utilizar esta información para diseñar **estrategias personalizadas que incrementen la satisfacción y reduzcan la deserción (churn)**.

---

### **Tareas Clave**
1. **Identificar la tarea empresarial**  
   - Mejorar la **retención de usuarias** y promover el uso de funcionalidades premium en la app de Bellabeat.
   - Entender los **diferentes perfiles de usuarias** según su nivel de actividad física.
   - Proporcionar **recomendaciones personalizadas** basadas en los datos de actividad registrados.

2. **Identificar a los interesados clave**  
   - **Equipo de Marketing**: Encargado de diseñar campañas y estrategias de retención basadas en los perfiles de usuario detectados.
   - **Equipo de Producto**: Responsable de implementar nuevas funcionalidades en la app Bellabeat según las recomendaciones obtenidas.
   - **Equipo de UX/UI**: Adaptación de la experiencia de usuario según el comportamiento y las necesidades detectadas.
   - **Equipo Directivo**: Tomadores de decisión para asignación de recursos y priorización de iniciativas.

---

### **Entregable: Una Instrucción Clara de la Tarea Empresarial**

**Tarea Empresarial:**  
Analizar los datos de actividad física registrados por los dispositivos Bellabeat para **identificar patrones de uso** y **segmentar a las usuarias en grupos relevantes**, con el fin de desarrollar **estrategias personalizadas** que incrementen la **retención**, el **uso diario de la app y los dispositivos**, y fomenten la conversión hacia productos o planes **premium**.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil

"""## Preparar

Usarás datos públicos como:
- Datos de seguimiento de actividad física Fitbit (Kaggle, CC0).

- **Tareas clave:** Descarga y almacenamiento de datos, organización, orden y filtrado, evaluar credibilidad.
- **Entregable:** Descripción detallada de fuentes utilizadas.
"""

df = pd.read_csv('/content/dailyActivity_merged.csv')

df.head()

df.info()

"""## Analizar

- Explora datos para descubrir tendencias o relaciones.
- **Entregable:** Resumen del análisis.
"""

df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
df.dtypes

"""## Valores únicos"""

df.nunique().sort_values()

"""## Duplicados"""

df.duplicated().sum()

"""## Nulos"""

df.isna().sum().sort_values()

"""# EDA

## Análisis estadísticos
"""

def estadisticos_cont(df):
    estadisticos = df.describe().T
    estadisticos['median'] = df.median()
    return(estadisticos)

estadisticos_cont(df)

# Calcular la matriz de correlación
correlation_matrix = df.corr()

# Crear la figura para el heatmap
plt.figure(figsize=(12, 8))

# Generar el mapa de calor (heatmap)
sns.heatmap(correlation_matrix,
            annot=True,        # Muestra los valores dentro de cada celda
            cmap='coolwarm',   # Esquema de colores para los valores positivos/negativos
            linewidths=0.5,    # Separación entre celdas
            fmt='.2f'          # Formato de los números (2 decimales)
           )

# Título del gráfico
plt.title('Matriz de Correlación - Bellabeat Dataset', fontsize=16)

# Mostrar el gráfico
plt.show()

num = df.loc[:,'TotalSteps':]
num

"""## Compartir

- Visualiza datos para comunicar hallazgos clave.
- **Entregable:** Visualizaciones y hallazgos clave.
"""

def variables_continuas(num):
    filas = ceil(num.shape[1] / 2)
    f, ax = plt.subplots(nrows=filas, ncols=2, figsize=(16, 24))
    ax = ax.flat

    for cada, variable in enumerate(num):
        num[variable].plot.density(ax=ax[cada])
        ax[cada].set_title(variable, fontsize=12, fontweight='bold')
        ax[cada].tick_params(labelsize=12)

    plt.tight_layout()
    plt.show()

variables_continuas(num)

"""## 📋 **Tabla de Variables Analizadas en el Proyecto Bellabeat**

| **Variable**                | **Descripción del Dato**                                                       | **Análisis de Distribución**                                                                                           |
|-----------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **TotalSteps**              | Total de pasos registrados por día.                                            | Distribución sesgada a la derecha. Mayoría en 8000-15000 pasos. Valores negativos presentes (requieren limpieza).     |
| **TotalDistance**           | Distancia total recorrida en un día.                                           | Sesgo positivo. Pico en 5-12 unidades. Valores negativos presentes. Outliers recorren más de 30 unidades.             |
| **TrackerDistance**         | Distancia medida automáticamente por el dispositivo.                           | Similar a TotalDistance. Mayoría de usuarios en 5-12 unidades. Outliers y valores negativos detectados.               |
| **LoggedActivitiesDistance**| Distancia ingresada manualmente por el usuario (actividades registradas).      | La mayoría no registra actividades manuales (pico en 0). Algunos registros superan 6 unidades. Valores negativos.     |
| **VeryActiveDistance**      | Distancia recorrida durante actividades muy activas (ejercicio intenso).      | Pico en 0 (usuarios inactivos). Algunos valores extremos (>30). Valores negativos detectados.                         |
| **ModeratelyActiveDistance**| Distancia recorrida en actividades moderadas.                                  | Pico en 0. Pocos usuarios recorren entre 2 y 10 unidades. Valores negativos presentes.                                |
| **LightActiveDistance**     | Distancia recorrida en actividades ligeras (caminatas suaves).                 | Distribución bimodal (dos grupos de usuarios). Valores extremos hasta 15 unidades. Valores negativos presentes.       |
| **SedentaryActiveDistance** | Distancia recorrida en estado sedentario (teóricamente debería ser 0).        | La mayoría en 0. Existen valores negativos y algunos positivos pequeños que no tienen sentido.                        |
| **VeryActiveMinutes**       | Minutos de actividad muy intensa.                                              | Pico en 0 (usuarios que no hacen actividad intensa). Algunos superan los 200 minutos. Valores negativos detectados.   |
| **FairlyActiveMinutes**     | Minutos de actividad moderada.                                                 | Distribución similar a VeryActiveMinutes. Pico en 0. Algunos usuarios superan los 200 minutos. Valores negativos.     |
| **LightlyActiveMinutes**    | Minutos en actividades ligeras.                                                | Distribución bimodal. Algunos usuarios pasan más de 600 minutos activos al día. Valores negativos presentes.          |
| **SedentaryMinutes**        | Minutos en actividad sedentaria.                                               | Bimodal. Picos entre 500 y 1500 minutos. Hay usuarios que superan los 1440 minutos diarios (incoherente). Valores negativos. |
| **Calories**                | Calorías quemadas por día.                                                     | Pico en 1800-2500 calorías. Valores extremos >6000 calorías. Valores negativos, lo que es inconsistente.              |

---

## ✅ **Resumen del análisis de distribución**
- La mayoría de las variables tienen **sesgo positivo** (la mayoría de los valores son bajos, pocos valores muy altos).
- **Valores negativos** presentes en casi todas las métricas, lo cual es **inválido** para distancias, tiempos y calorías → **requiere limpieza de datos**.
- **Distribuciones bimodales** en algunas variables como `LightlyActiveDistance` y `SedentaryMinutes`, lo que sugiere la **existencia de distintos perfiles de usuarios** (activos y sedentarios).
- Algunas variables exceden **límites lógicos**, como más de 1440 minutos en un día o calorías negativas.

## Segmentación

### Por calorías
"""

# Definir los bins y etiquetas
bins = [float('-inf'), 1000, 2500, float('inf')]
labels = ['Menos de 1000', 'Entre 1000 y 2500', 'Más de 2500']

# Asignar los segmentos según las calorías
df['calorias_segmento'] = pd.cut(df['Calories'], bins=bins, labels=labels, include_lowest=True)

# Calcular el porcentaje de cada categoría
categoria_porcentajes = df['calorias_segmento'].value_counts(normalize=True) * 100

# Crear la gráfica de barras
plt.figure(figsize=(8, 6))
categoria_porcentajes.plot(kind='bar', color='blue')

# Agregar título y etiquetas de los ejes
plt.title('Porcentaje de segmentos de calorías')
plt.xlabel('Segmento de calorías')  # Corregido: xlabel
plt.ylabel('Porcentaje')

# Añadir líneas de cuadrícula horizontales
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mostrar valores encima de las barras
for index, value in enumerate(categoria_porcentajes):
    plt.text(index, value + 0.5, f'{value:.2f}%', color='grey', fontsize=10)

# Ajustar el diseño para que no se solapen los elementos
plt.tight_layout()

# Mostrar la gráfica
plt.show()

print(df.columns.tolist())

"""## Actuar

- Resume conclusiones y ofrece recomendaciones de estrategia.
- **Entregable:** Tres recomendaciones de alto nivel basadas en tu análisis.

---

#  **Interpretación del gráfico de barras: Porcentaje de segmentos de calorías**

##  **Qué muestra el gráfico**
- **Tipo de gráfico**: Barras verticales.
- **Título**: *Porcentaje de segmentos de calorías*.
- **Eje X (Categorías)**:
  1. **Entre 1000 y 2500**
  2. **Más de 2500**
  3. **Menos de 1000**
- **Eje Y (Porcentaje)**: Representa el porcentaje de usuarios dentro de cada rango de calorías quemadas.

- Cada barra muestra además el **valor porcentual exacto** en la parte superior.

---

##  **1. Segmento: Usuarios que queman menos de 1000 calorías (1.28%)**
###  **Perfil:**
- **Baja actividad física.**
- Probablemente tienen **hábitos sedentarios** o **no utilizan activamente el dispositivo/app**.
- Podrían ser **nuevos usuarios**, **usuarios que abandonaron** o **no han configurado bien su dispositivo**.

###  **Recomendaciones:**
1. **Campañas de activación inicial o reactivación:**
   - Enviar **recordatorios push personalizados** animando al usuario a dar sus primeros pasos de actividad.
   - Ofrecer un **tutorial interactivo** sobre cómo usar Bellabeat y sus beneficios (ej: “Cómo empezar a mejorar tu salud con Bellabeat”).

2. **Desafíos para principiantes:**
   - Crear **retos de bajo esfuerzo**, como caminar 500 pasos al día o 5 minutos de estiramiento, con **recompensas virtuales** (badges, puntos, etc.).
   - Ejemplo: *"Desafío 7 días activos: completa 7 días caminando al menos 1000 pasos y gana una medalla digital."*

3. **Programas de educación y concienciación:**
   - Notificaciones educativas con **beneficios de la actividad física moderada** (mejor sueño, más energía, control del estrés).
   - Ejemplo: *"Sabías que solo 10 minutos al día de actividad pueden mejorar tu estado de ánimo?"*

4. **Descuentos en productos Bellabeat (cross-selling):**
   - Ofrecer **descuentos exclusivos** en dispositivos más sencillos o en suscripciones premium para motivar la compra y el uso.

---

##  **2. Segmento: Usuarios que queman entre 1000 y 2500 calorías (62.87%)**
###  **Perfil:**
- Usuarios **moderadamente activos**.
- Mantienen un **nivel de actividad saludable**, pero aún tienen **potencial de mejorar**.
- Son el **grupo más representativo** del total de usuarios.

###  **Recomendaciones:**
1. **Mantenimiento de la motivación:**
   - Ofrecer **informes semanales de progreso** que destaquen los logros recientes.
   - Ejemplo: *"¡Felicitaciones! La semana pasada aumentaste tu actividad en un 10%."*

2. **Desafíos de actividad grupales (social engagement):**
   - Crear **comunidades** donde los usuarios compitan o colaboren en retos (ej: “Camina 30 km con amigos esta semana”).
   - Ofrecer **tablas de clasificación** (gamificación) para fomentar la competencia amistosa.

3. **Recomendaciones personalizadas de estilo de vida:**
   - Sugerencias de **rutinas de ejercicio** acorde a su perfil de actividad (cardio, fuerza, yoga).
   - Tips de **nutrición y bienestar** que complementen su nivel de ejercicio.

4. **Beneficios premium o freemium:**
   - Ofrecer **pruebas gratuitas de la app premium** o nuevas funcionalidades por su compromiso.
   - Ejemplo: acceso gratuito por 30 días a **entrenamientos personalizados** o **meditación guiada**.

---

##  **3. Segmento: Usuarios que queman más de 2500 calorías (35.85%)**
###  **Perfil:**
- Usuarios **altamente activos**, probablemente **deportistas regulares** o **muy comprometidos con su bienestar físico**.
- Pueden estar buscando **datos detallados de su rendimiento**, **desafíos avanzados**, y **coaching personalizado**.

###  **Recomendaciones:**
1. **Programas de entrenamiento avanzados:**
   - Ofrecer **planes premium** enfocados en **rendimiento deportivo**, **entrenamiento de alta intensidad (HIIT)** o **resistencia**.
   - Incorporar recomendaciones basadas en datos biométricos, como frecuencia cardíaca o sueño.

2. **Coaching personalizado (monetizable):**
   - Servicios de **coaching online** o **sesiones 1 a 1** a través de la app para quienes deseen un seguimiento experto.
   - Paquetes exclusivos para deportistas o perfiles fitness avanzados.

3. **Concursos y recompensas VIP:**
   - Crear **competencias internacionales** o **desafíos exclusivos** donde puedan obtener **premios tangibles** (equipamiento deportivo, membresías premium, etc.).
   - Ejemplo: *“Corre 200 km este mes y participa por un smartwatch premium.”*

4. **Datos avanzados y analítica personalizada:**
   - Ofrecer **informes detallados de performance**, como eficiencia de quema calórica por actividad, zonas de frecuencia cardíaca, VO2 max, etc.
   - Dashboards personalizados para **visualizar progreso a largo plazo**.

---

##  **4. Recomendaciones generales para todos los segmentos**
###  **Gamificación y motivación**  
- Sistema de **logros y medallas** según el progreso.
- Crear **niveles de usuario** (principiante, intermedio, avanzado) que motiven el avance.

###  **Recordatorios inteligentes y adaptativos**
- Notificaciones push **no invasivas** que **adapten su frecuencia y contenido** según el comportamiento del usuario.
- Por ejemplo, si no abren la app en 3 días → enviar una notificación amable recordándoles los beneficios.

###  **Integraciones con otras plataformas de salud**
- Integrar Bellabeat con **Google Fit**, **Apple Health**, o apps de nutrición como **MyFitnessPal** para una visión holística del bienestar.

---

##  **Beneficios esperados para Bellabeat**
1. **Aumento en la retención** de usuarios a largo plazo.
2. Mejora del **engagement diario** en la app y el uso de dispositivos.
3. Incremento de las **conversiones a planes premium** y **ventas adicionales** (cross-selling).
4. Fortalecimiento de la **experiencia del cliente (UX)** y la **satisfacción del usuario**.
5. Mejor **posicionamiento competitivo** en el mercado de wellness tech.

---

##  **Ejemplo de comunicación a los stakeholders**
> "Con base en el análisis del comportamiento de los usuarios de Bellabeat, hemos segmentado la base de usuarios según su actividad calórica diaria. Las estrategias propuestas personalizan la experiencia, incrementan la motivación y generan nuevas oportunidades de monetización, consolidando a Bellabeat como líder en salud digital femenina."

Link presentación o resumen ejecutivo: https://www.canva.com/design/DAGhoEz1k54/a1QdNGJXbOUxWBje9HM4nA/edit?utm_content=DAGhoEz1k54&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

"""

# Importación de librerías principales
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Cargar el dataset
# Cambia la ruta al nombre de tu dataset si es necesario
df = pd.read_csv('/content/dailyActivity_merged.csv')

# 🔵 CREAR LA COLUMNA calorias_segmento ANTES DE INICIAR EL DASHBOARD

# Definir los bins y etiquetas para segmentar usuarios por calorías
bins = [float('-inf'), 1000, 2500, float('inf')]
labels = ['Menos de 1000', 'Entre 1000 y 2500', 'Más de 2500']

# Crear la columna 'calorias_segmento'
df['calorias_segmento'] = pd.cut(df['Calories'], bins=bins, labels=labels, include_lowest=True)

# Revisa que se haya creado bien (opcional)
print(df['calorias_segmento'].value_counts())

# Inicializar la aplicación de Dash
app = dash.Dash(__name__)

# Título de la aplicación
app.title = 'Dashboard Bellabeat - Análisis de Actividad de Usuarios'

# Layout del dashboard
app.layout = html.Div(children=[

    html.H1('Dashboard de Actividad - Bellabeat', style={'textAlign': 'center'}),

    # Dropdown para seleccionar un segmento de calorías
    html.Div([
        html.Label('Segmento de Calorías:'),
        dcc.Dropdown(
            id='calories_segment',
            options=[{'label': seg, 'value': seg} for seg in df['calorias_segmento'].unique()],
            value=df['calorias_segmento'].unique()[0]
        )
    ], style={'width': '40%', 'margin': 'auto'}),

    # Gráfico de calorías
    dcc.Graph(id='calories_distribution'),

    # Gráfico de pasos totales
    dcc.Graph(id='steps_distribution'),

    # Gráfico de matriz de correlación
    dcc.Graph(id='correlation_heatmap')

])

# Callback para actualizar gráficos según el segmento seleccionado
@app.callback(
    [Output('calories_distribution', 'figure'),
     Output('steps_distribution', 'figure'),
     Output('correlation_heatmap', 'figure')],
    [Input('calories_segment', 'value')]
)
def update_graphs(selected_segment):
    # Filtrar por el segmento de calorías seleccionado
    filtered_df = df[df['calorias_segmento'] == selected_segment]

    # Gráfico de distribución de calorías
    fig_calories = px.histogram(filtered_df, x='Calories',
                                title=f'Distribución de Calorías - Segmento: {selected_segment}',
                                color_discrete_sequence=['#636EFA'])

    # Gráfico de distribución de TotalSteps
    fig_steps = px.histogram(filtered_df, x='TotalSteps',
                             title=f'Distribución de Pasos - Segmento: {selected_segment}',
                             color_discrete_sequence=['#EF553B'])

    # Matriz de correlación
    correlation = filtered_df[['TotalSteps', 'Calories', 'TotalDistance', 'VeryActiveMinutes']].corr()
    fig_corr = px.imshow(correlation,
                         text_auto=True,
                         color_continuous_scale='RdBu',
                         title=f'Matriz de Correlación - Segmento: {selected_segment}')

    return fig_calories, fig_steps, fig_corr

# Correr la app
if __name__ == '__main__':
    app.run_server(debug=True)