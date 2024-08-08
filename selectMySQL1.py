#Tania
import mysql.connector
import pandas as pd
from mysql.connector import Error

def export_to_excel():
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto por tu host
            database='u927419088_testing_sql',  # Cambia esto por el nombre de tu base de datos
            user='u927419088_admin',  # Cambia esto por tu usuario
            password='#Admin12345#'  # Cambia esto por tu contraseña
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")

            # Crear un cursor para ejecutar consultas
            cursor = connection.cursor()

            # Consultar los registros de la tabla 'curso'
            query = "SELECT * FROM curso"
            cursor.execute(query)

            # Obtener los nombres de las columnas
            columns = [desc[0] for desc in cursor.description]

            # Obtener los registros
            records = cursor.fetchall()

            # Crear un DataFrame de pandas
            df = pd.DataFrame(records, columns=columns)

            # Imprimir la columna 'nombreDescriptivo'
            print(df['nombreDescriptivo'])

            # Exportar a un archivo Excel
            df.to_excel('curso_registros.xlsx', index=False, engine='openpyxl')

            print("Datos exportados a curso_registros.xlsx")

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

    except Error as e:
        print("Error al conectar a MySQL", e)

if __name__ == "__main__":
    export_to_excel()
