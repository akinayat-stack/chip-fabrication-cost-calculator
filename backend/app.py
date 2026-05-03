from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)


def dies_per_wafer(wafer_diameter_mm: float, die_area_mm2: float) -> float:
    """
    Approximate Gross Dies Per Wafer (DPW):
    DPW = (pi * (D/2)^2 / A) - (pi * D / sqrt(2*A))
    """
    wafer_area = math.pi * (wafer_diameter_mm / 2) ** 2
    edge_loss = math.pi * wafer_diameter_mm / math.sqrt(2 * die_area_mm2)
    return max((wafer_area / die_area_mm2) - edge_loss, 0)


def murphy_yield(die_area_mm2: float, defect_density_per_cm2: float) -> float:
    """
    Murphy model (triangular):
    Y = ((1 - exp(-D0 * A_cm2)) / (D0 * A_cm2))^2
    """
    area_cm2 = die_area_mm2 / 100.0
    x = defect_density_per_cm2 * area_cm2
    if x == 0:
        return 1.0
    return ((1 - math.exp(-x)) / x) ** 2


def bose_einstein_yield(die_area_mm2: float, defect_density_per_cm2: float) -> float:
    """
    Common clustering variant (alpha=1):
    Y = 1 / (1 + D0 * A_cm2)
    """
    area_cm2 = die_area_mm2 / 100.0
    return 1.0 / (1.0 + defect_density_per_cm2 * area_cm2)