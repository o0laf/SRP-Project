import json

class GeneradorSalida:
    def a_json(self, promedio):
        return {"promedio": promedio, "formato": "JSON"}

    def serializar(self, datos):
        return json.dumps(datos)
