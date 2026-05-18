from datetime import date

from src.services.FeriadoService import FeriadoService


def test_verificar_feriado_nacional_natal():
    feriado_service = FeriadoService()

    resultado = feriado_service.verificar_feriado(date(2026, 12, 25))

    assert resultado["feriado"] is True
    assert resultado["nome"] == "Natal"
    assert resultado["data"] == "2026-12-25"


def test_verificar_data_sem_feriado():
    feriado_service = FeriadoService()

    resultado = feriado_service.verificar_feriado(date(2026, 1, 2))

    assert resultado["feriado"] is False
    assert resultado["nome"] == ""
    assert resultado["data"] == "2026-01-02"