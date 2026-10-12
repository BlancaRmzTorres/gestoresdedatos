
from pymongo import MongoClient

try:
    # Conectarse a MongoDB en esta computadora
    cliente = MongoClient(
        "mongodb://localhost:27017",
        serverSelectionTimeoutMS=5000
    )

    # Comprobar que MongoDB responde
    cliente.admin.command("ping")

    print("¡Conexión exitosa con MongoDB!")

    # Acceder a nuestra base de datos
    base_datos = cliente["seizeit2"]

    # Mostrar las colecciones disponibles
    print("Base de datos:", base_datos.name)
    print("Colecciones:", base_datos.list_collection_names())

except Exception as error:
    print("No se pudo conectar con MongoDB.")
    print("Detalle del error:", error)

finally:
    if "cliente" in locals():
        cliente.close()
