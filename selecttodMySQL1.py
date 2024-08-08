#Tania
import mysql.connector
from mysql.connector import Error

def fetch_all_records():
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

            # Consulta SQL para seleccionar todos los registros
            query = "SELECT * FROM curso"
            cursor.execute(query)

            # Obtener todos los registros
            records = cursor.fetchall()

            # Imprimir los registros
            for record in records:
                print(record)

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

    except Error as e:
        print("Error al conectar a MySQL o al ejecutar la consulta", e)

if __name__ == "__main__":
    fetch_all_records()
