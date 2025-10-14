import json

class Reporte:
    def __init__(self, datos):
        self.datos = datos

    def obtener_datos(self):
        return self.datos

    def procesar_datos(self):
        return sum(self.datos) / len(self.datos)

    def generar_salida(self, promedio):
        return json.dumps({"promedio": promedio})

    def guardar_resultado(self, salida):
        with open("reporte.json", "w") as f:
            f.write(salida)
        print("Reporte guardado en reporte.json")


if __name__ == "__main__":
    reporte = Reporte([10, 20, 30, 40])
    datos = reporte.obtener_datos()
    prom = reporte.procesar_datos()
    salida = reporte.generar_salida(prom)
    reporte.guardar_resultado(salida)

"""
La clase Reporte tiene múltiples "motivos de cambio":
1. Si cambia la forma de obtener datos → hoy es una lista, mañana puede ser un archivo o base de datos.
2. Si cambia la forma de procesar datos → en lugar de promedio, tal vez haya que calcular mediana, suma o filtrar.
3. Si cambia el formato de salida → JSON, texto plano, HTML, CSV, etc.
4. Si cambia el método de almacenamiento → guardarlo en archivo, mostrar en pantalla, enviarlo por email, etc.

Esto hace que una sola clase tenga demasiadas responsabilidades.
Cada motivo de cambio debería estar en una clase separada.
"""