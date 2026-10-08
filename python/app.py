import os
import psycopg2


def conectar_y_consultar():
    print("Intentando conectar a PostgreSQL desde el contenedor Python...")
    try:
        conexion = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        cursor = conexion.cursor()
        print("¡Conexión exitosa a PostgreSQL!\n")

        cursor.execute("SELECT id, nombre, correo, fecha_registro FROM usuarios;")
        resultados = cursor.fetchall()
        
        print("Registros encontrados en la tabla 'usuarios':")
        for fila in resultados:
            print(f" - ID: {fila[0]} | Nombre: {fila[1]} | Correo: {fila[2]} | Fecha: {fila[3]}")

        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")

if __name__ == "__main__":
    conectar_y_consultar()