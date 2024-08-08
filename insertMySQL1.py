import mysql.connector
from mysql.connector import Error

def insert_records():
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

            # Datos de ejemplo para insertar (omitimos el campo `id`)
            registros = [
                ('Curso de Python', 12),
                ('Curso de Data Science', 15),
                ('Curso de Machine Learning', 20),
                ('Curso de SQL', 10),
                ('Curso de JavaScript', 14),
                ('Curso de HTML y CSS', 8),
                ('Curso de Django', 16),
                ('Curso de Flask', 11),
                ('Curso de C++', 13),
                ('Curso de Ruby on Rails', 9)
            ]

            # Consulta SQL para insertar registros (omitimos `id`)
            query = """
                INSERT INTO curso (nombreDescriptivo, nAsignaturas)
                VALUES (%s, %s)
            """

            # Ejecutar la consulta para cada registro
            cursor.executemany(query, registros)

            # Confirmar los cambios en la base de datos
            connection.commit()

            print("Registros insertados correctamente")

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

    except Error as e:
        print("Error al conectar a MySQL o al insertar registros", e)

if __name__ == "__main__":
    insert_records()
