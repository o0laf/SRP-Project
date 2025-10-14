import json

class ReporteController:
    def __init__(self, dao, service):
        self.dao = dao
        self.service = service

    def generar_reporte(self):
        datos = self.dao.obtener_datos()
        promedio = self.service.calcular_promedio(datos)
        reporte = {
            "datos": datos,
            "promedio": promedio
        }
        return reporte

    def guardar_reporte(self, reporte):
        with open("reporte.json", "w") as f:
            json.dump(reporte, f, indent=4)
        print("✅ Reporte guardado en reporte.json")
