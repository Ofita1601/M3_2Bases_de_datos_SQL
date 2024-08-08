import mysql.connector
from mysql.connector import Error


def update_record(idcurso, nuevo_nombre):
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

            # Consulta SQL para actualizar el nombreDescriptivo
            query = """
                UPDATE curso
                SET nombreDescriptivo = %s
                WHERE idcurso = %s
            """

            # Ejecutar la consulta
            cursor.execute(query, (nuevo_nombre, idcurso))

            # Confirmar los cambios en la base de datos
            connection.commit()

            print(f"Registro con idcurso {idcurso} actualizado correctamente")

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()

    except Error as e:
        print("Error al conectar a MySQL o al actualizar el registro", e)


if __name__ == "__main__":
    update_record(idcurso=1, nuevo_nombre='hola mundo')
