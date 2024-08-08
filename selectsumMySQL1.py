import mysql.connector
from mysql.connector import Error

def sum_nAsignaturas():
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

            # Consulta SQL para sumar los valores de nAsignaturas
            query = "SELECT SUM(nAsignaturas) AS totalAsignaturas FROM curso"
            cursor.execute(query)

            # Obtener el resultado
            result = cursor.fetchone()
            total_asignaturas = result[0]

            # Imprimir el total
            print(f"Total de asignaturas: {total_asignaturas}")

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

    except Error as e:
        print("Error al conectar a MySQL", e)

if __name__ == "__main__":
    sum_nAsignaturas()