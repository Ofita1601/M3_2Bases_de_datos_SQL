import mysql.connector
import pandas as pd
from mysql.connector import Error

def fetch_and_print_records():
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

            # Consulta SQL
            query = """
                SELECT * FROM curso
                WHERE nAsignaturas >= 11
            """
            cursor.execute(query)

            # Obtener los resultados
            columns = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()

            # Crear un DataFrame de pandas
            cursos_registros = pd.DataFrame(records, columns=columns)

            # Imprimir el DataFrame
            print(cursos_registros)

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

    except Error as e:
        print("Error al conectar a MySQL", e)

if __name__ == "__main__":
    fetch_and_print_records()
