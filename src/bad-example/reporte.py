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
