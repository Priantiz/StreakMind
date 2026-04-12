from datetime import datetime, timedelta

class StreakService:
    def __init__(
        self,
        configuracao,
        dashboard_service,
        streak_atual=0,
        dia_ja_validado=False,
        data_ultimo_dia=None,
        cumpriu_meta_no_dia=False
    ):
        if not isinstance(streak_atual,int):
            raise TypeError('a streak deve ser um numero inteiro')
        if streak_atual <0:
            raise ValueError('a streak deve ser um numero positivo')
        if not isinstance(dia_ja_validado,bool):
            raise TypeError('o dia_ja_validado so pode ser ou True ou False')
        if not isinstance(cumpriu_meta_no_dia,bool):
            raise TypeError('o cumpriu_meta_no_dia so pode ser True ou False')
        if not isinstance(data_ultimo_dia, (type(None), str)):
            raise TypeError('a data_ultimo_dia so pode ser None ou uma data string')
        if data_ultimo_dia is not None:
            try:
                datetime.strptime(data_ultimo_dia, "%Y-%m-%d")
            except ValueError:
                raise ValueError("a data_ultimo_dia deve estar no formato YYYY-MM-DD")
        self.streak_atual = streak_atual
        self.configuracao = configuracao
        self.dia_ja_validado = dia_ja_validado
        self.data_ultimo_dia = datetime.now().strftime("%Y-%m-%d") if data_ultimo_dia is None else data_ultimo_dia
        self.cumpriu_meta_no_dia = cumpriu_meta_no_dia
        self.dashboard_service = dashboard_service

    def atualizar_streak(self):
        data_de_hoje = datetime.now().strftime("%Y-%m-%d")

        if data_de_hoje != self.data_ultimo_dia:
            data_anterior = datetime.strptime(self.data_ultimo_dia, "%Y-%m-%d")
            data_hoje_obj = datetime.strptime(data_de_hoje, "%Y-%m-%d")

            dia_da_semana_anterior = data_anterior.weekday()

            if dia_da_semana_anterior in self.configuracao.dias_obrigatorios:
                if self.cumpriu_meta_no_dia is False:
                    self.streak_atual = 0

            diferenca = (data_hoje_obj - data_anterior).days

            for i in range(1, diferenca):
                dia_intermediario = data_anterior + timedelta(days=i)
                dia_da_semana = dia_intermediario.weekday()

                if dia_da_semana in self.configuracao.dias_obrigatorios:
                    self.streak_atual = 0
                    break

            self.dia_ja_validado = False
            self.cumpriu_meta_no_dia = False
            self.data_ultimo_dia = data_de_hoje

        dia_da_semana_hoje = datetime.now().weekday()

        if self.dia_ja_validado is False:
            if dia_da_semana_hoje in self.configuracao.dias_obrigatorios:
                if self.dashboard_service.calcular_tempo_total() >= self.configuracao.meta_diaria:
                    self.streak_atual += 1
                    self.dia_ja_validado = True
                    self.cumpriu_meta_no_dia = True
                    
    def retornar_como_dicionario(self):
        return {
            'streak_atual': self.streak_atual,
            'dia_ja_validado': self.dia_ja_validado,
            'data_ultimo_dia': self.data_ultimo_dia,
            'cumpriu_meta_no_dia': self.cumpriu_meta_no_dia
    }