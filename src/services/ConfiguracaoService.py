class ConfiguracaoService:
    def __init__(
        self,
        configuracao,
        repositorio=None,
        tarefa_service=None,
        sessao_service=None,
        streak_service=None
    ):
        self.configuracao = configuracao
        self.repositorio = repositorio
        self.tarefa_service = tarefa_service
        self.sessao_service = sessao_service
        self.streak_service = streak_service

    def salvar_dados(self):
        if self.repositorio is not None:
            self.repositorio.salvar(
                tarefa_service=self.tarefa_service,
                sessao_service=self.sessao_service,
                configuracao=self.configuracao,
                streak_service=self.streak_service
            )

    def definir_meta_diaria(self, nova_meta):
        if not isinstance(nova_meta, int):
            raise TypeError('a meta diaria deve ser um inteiro')
        
        if nova_meta < 20:
            raise ValueError('a meta diaria deve ser igual ou maior que 20')
        
        self.configuracao.meta_diaria = nova_meta
        self.salvar_dados()

    def definir_dias_obrigatorios(self, dias_obrigatorios):
        if not isinstance(dias_obrigatorios, list):
            raise TypeError('os dias obrigatorios devem ser uma lista')
        
        for dia in dias_obrigatorios:
            if not isinstance(dia, int):
                raise TypeError('cada dia obrigatorio deve ser um inteiro')
            if dia < 0 or dia > 6:
                raise ValueError('cada dia obrigatorio deve estar entre 0 e 6')
        
        if len(dias_obrigatorios) != len(set(dias_obrigatorios)):
            raise ValueError('os dias obrigatorios nao podem ser repetidos')
        
        self.configuracao.dias_obrigatorios = dias_obrigatorios.copy()
        self.salvar_dados()