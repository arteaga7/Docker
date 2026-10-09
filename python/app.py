import os
import psycopg2

# Cargar las variables desde el entorno (inyectadas por el archivo .env)
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "db_1")
POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "1234")

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

        id = 1
        cursor.execute("SELECT * FROM usuarios WHERE id = %s;", (id,))
        resultados = cursor.fetchall()
        print(resultados)

        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")

if __name__ == "__main__":
    conectar_y_consultar()