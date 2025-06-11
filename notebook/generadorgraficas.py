import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataFrameAsistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

# GRAFICANDO

# 1. Gráfica de barras por estado
plt.figure(figsize=(8, 5))
sns.countplot(data=dataFrameAsistencia, x='estado')  # palette removed
plt.title('Cantidad de Registros por Estado de Asistencia')
plt.xlabel("Estado de Asistencia")
plt.ylabel("Cantidad de Registros")
plt.tight_layout()
plt.show()

# 2. Gráfica de torta por medio de transporte
conteoMedioTransporte = dataFrameAsistencia['medio_transporte'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct='%1.1f%%',
    colors=sns.color_palette("Blues", n_colors=len(conteoMedioTransporte))
)
plt.title("Distribución de Estudiantes por Medio de Transporte")
plt.tight_layout()
plt.show()

# 3. Gráfico de barras agrupadas por estado y medio de transporte
plt.figure(figsize=(10, 6))
sns.countplot(data=dataFrameAsistencia, x='estado', hue='medio_transporte', palette="Blues")
plt.title('Registros por Estado de Asistencia y Medio de Transporte')
plt.xlabel("Estado de Asistencia")
plt.ylabel("Cantidad de Registros")
plt.legend(title='Medio de Transporte')
plt.tight_layout()
plt.show()

# 4. Boxplot del estrato por estado de asistencia
plt.figure(figsize=(8, 5))
sns.boxplot(data=dataFrameAsistencia, x='estado', y='estrato', palette="Set2")
plt.title('Distribución de Estrato por Estado de Asistencia')
plt.xlabel('Estado de Asistencia')
plt.ylabel('Estrato')
plt.tight_layout()
plt.show()

# 5. Gráfico de barras del total de registros por grupo
conteoPorGrupo = dataFrameAsistencia['id_grupo'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
conteoPorGrupo.plot(kind='bar', color="#3fa99c")
plt.title('Cantidad de Registros por id_grupo')
plt.xlabel('id_grupo')
plt.ylabel('Cantidad de Registros')
plt.tight_layout()
plt.show()