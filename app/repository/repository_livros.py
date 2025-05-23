import psycopg2
from app.model.model_livros import Consulta

class ConsultaRepository:
    def __init__(self):
        self.db_config = {
            'dbname': 'catalogo',
            'user': 'postgres',
            'password': 'rafael2014',
            'host': 'localhost',
            'port': '5432'
        }

    def pegar_todas(self):
        conn = psycopg2.connect(**self.db_config)
        cur = conn.cursor()
        cur.execute("SELECT id, titulo, autor FROM livros_teste")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        return [{'id': row[0], 'titulo': row[1], 'autor': row[2]} for row in rows]
    
    def pegar_por_id(self, consulta_id: int):
        conn = psycopg2.connect(**self.db_config)
        cur = conn.cursor()
        cur.execute("SELECT id, titulo, autor FROM livros_teste WHERE id = %s", (consulta_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        
        if row:
            return {'id': row[0], 'titulo': row[1], 'autor': row[2]}
        return None

    def criar(self, consulta_data: dict):
        conn = psycopg2.connect(**self.db_config)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO livros_teste (titulo, autor) VALUES (%s, %s) RETURNING id",
            (consulta_data['titulo'], consulta_data['autor'])
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return {'id': new_id, 'titulo': consulta_data['titulo'], 'autor': consulta_data['autor']}

    def deletar(self, consulta_id: int):
        conn = psycopg2.connect(**self.db_config)
        cur = conn.cursor()
        
        cur.execute("DELETE FROM livros_teste WHERE id = %s RETURNING id, titulo, autor", (consulta_id,))
        deleted = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        if deleted:
            return {'id': deleted[0], 'titulo': deleted[1], 'autor': deleted[2]}
        return None

    
#Acesso a Dados


