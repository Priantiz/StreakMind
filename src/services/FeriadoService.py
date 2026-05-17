from datetime import date

import requests


class FeriadoService:
    URL_API = "https://brasilapi.com.br/api/feriados/v1"

    def buscar_feriados_do_ano(self, ano):
        try:
            resposta = requests.get(f"{self.URL_API}/{ano}", timeout=5)
            resposta.raise_for_status()
            return resposta.json()

        except (requests.RequestException, ValueError):
            return []

    def verificar_feriado(self, data=None):
        if data is None:
            data = date.today()

        feriados = self.buscar_feriados_do_ano(data.year)
        data_formatada = data.strftime("%Y-%m-%d")

        for feriado in feriados:
            if feriado.get("date") == data_formatada:
                return {
                    "feriado": True,
                    "nome": feriado.get("name", "Feriado nacional"),
                    "data": data_formatada,
                }

        return {
            "feriado": False,
            "nome": "",
            "data": data_formatada,
        }