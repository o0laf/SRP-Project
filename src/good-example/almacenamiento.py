class Almacenamiento:
    def guardar(self, contenido, archivo="reporte.json"):
        with open(archivo, "w") as f:
            f.write(contenido)
        print(f"Reporte guardado en {archivo}")
