from app.repository.repository_livros import ConsultaRepository
from app.schemas.schemas_livros import CriarConsultaSchema

class ConsultaService:
    def __init__(self, repository: ConsultaRepository):
        self.repository = repository

    def listar_todas(self):
        return self.repository.pegar_todas()
    
    def criar(self, consulta_data: dict):
        return self.repository.criar(consulta_data)
    
    def deletar(self, consulta_id: int):
        consulta = self.repository.pegar_por_id(consulta_id)
        return self.repository.deletar(consulta_id)
    
    #regras de negócio