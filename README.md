# Trabajo Práctico: Principio de Responsabilidad Única (SRP)

Este proyecto muestra un ejemplo de **violación** y de **aplicación correcta** del Principio de Responsabilidad Única (SRP) de SOLID.  

---

## Principio de Responsabilidad Única (SRP)

El SRP establece que:

> "Una clase debe tener una, y solo una, razón para cambiar."

En otras palabras, cada clase o módulo debe tener **una única responsabilidad** claramente definida.  
Esto facilita el mantenimiento, evita dependencias innecesarias y hace el código más flexible.

---

## Ejemplo Malo (violación de SRP)

La clase Reporte viola SRP porque concentra múltiples responsabilidades:

> Obtener datos → Si cambia la fuente (lista, archivo, base de datos).

> Procesar datos → Si cambia la forma de cálculo (promedio, mediana, filtrado).

> Generar salida → Si cambia el formato (JSON, texto plano, HTML, CSV).

> Guardar resultado → Si cambia el destino (archivo, pantalla, email, nube).

Esto genera 4 motivos de cambio en una sola clase, dificultando el mantenimiento.

## Conclusión

En el ejemplo malo, la clase Reporte tenía demasiadas responsabilidades.

En el ejemplo bueno, cada clase se encarga de una única tarea:

> FuenteDatos → obtiene la información.

> ProcesadorDatos → procesa/calcula.

> GeneradorSalida → genera el formato de salida.

> Almacenamiento → guarda el resultado.

Esto cumple con el Principio de Responsabilidad Única, haciendo el sistema más mantenible, escalable y fácil de modificar.
