from pydantic import BaseModel

class ConsultaBaseSchema(BaseModel):
    id: int
    titulo: str
    autor: str

class CriarConsultaSchema(ConsultaBaseSchema):
    pass

class ConsultaSchema(ConsultaBaseSchema):
    class Config:
        orm_mode = True

#validação de dados