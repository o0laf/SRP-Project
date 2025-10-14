import sys
import os

# Permite importar módulos desde src/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controller.reporte_controller import ReporteController
from service.reporte_service import ReporteService
from dao.reporte_dao import ReporteDAO


def main():
    dao = ReporteDAO()
    service = ReporteService()
    controller = ReporteController(dao, service)

    reporte = controller.generar_reporte()
    controller.guardar_reporte(reporte)


if __name__ == "__main__":
    main()
