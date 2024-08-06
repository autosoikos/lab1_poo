import os
import platform

from lab1_poo import (
    SegEtaInfantil,
    SegEtaGeneral,
    GestionSegEta,
)

def crear_articulo(id, nombre, autor, categoria, cantidad, precio):
    articulo = {
        'id': id,
        'nombre': nombre,
        'autor': autor,
        'categoria' : categoria,
        'cantidad': cantidad,
        'precio': precio
    }

