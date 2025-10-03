from fuente_datos import FuenteDatos
from procesador_datos import ProcesadorDatos
from generador_salida import GeneradorSalida
from almacenamiento import Almacenamiento

def main():
    fuente = FuenteDatos()
    procesador = ProcesadorDatos()
    generador = GeneradorSalida()
    almacenamiento = Almacenamiento()

    datos = fuente.obtener_datos()
    promedio = procesador.calcular_promedio(datos)
    salida = generador.a_json(promedio)
    serializado = generador.serializar(salida)
    almacenamiento.guardar(serializado)

if __name__ == "__main__":
    main()
