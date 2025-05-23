class Consulta:
    def __init__(self, id: int, titulo: str, autor: str):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def para_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor
        }

#definição dos objetos

