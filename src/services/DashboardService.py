from datetime import datetime
class DashboardService:
    def __init__(self,sessao_service):
        self.sessao_service = sessao_service
    
    def quantidade_de_sessoes(self):
        return len(self.sessao_service.lista_sessoes)


    def calcular_tempo_total(self):
        tempo_total=0
        data_de_hoje = datetime.now().strftime("%Y-%m-%d")
        
        for sessao in self.sessao_service.lista_sessoes:
            if sessao.data == data_de_hoje:
                tempo_total+=sessao.tempo
        return tempo_total
    
    def calcular_tempo_cada_tarefa(self):
        data_de_hoje = datetime.now().strftime("%Y-%m-%d")

        tempo_cada_tarefa={}
        for sessao in self.sessao_service.lista_sessoes:
            if sessao.data == data_de_hoje:
                    if sessao.tarefa is None:
                        if 'Estudo livre' in tempo_cada_tarefa:
                            tempo_cada_tarefa['Estudo livre']+=sessao.tempo
                        else:
                            tempo_cada_tarefa['Estudo livre']= sessao.tempo
                    else:
                        if sessao.tarefa.nome in tempo_cada_tarefa:
                            tempo_cada_tarefa[sessao.tarefa.nome]+=sessao.tempo
                        else:
                            tempo_cada_tarefa[sessao.tarefa.nome]= sessao.tempo
        return tempo_cada_tarefa




    

