import psycopg2
import csv

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "",
                "host": "127.0.1",
                "port": "5432",
                "database": "pydb"
            }
        }
        
class Connection(Config):
    def __init__(self):
        super().__init__()
        try:
            self.conn = psycopg2.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)
            
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()
        
    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        self.connection.commit()
        
    def fetchall(self):
        self.cursor.fetchall()
        
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
    
class Pessoa(Connection):
    def __init__(self):
        super().__init__()
        
    def insert(self, *args):
        try:
            sql = "INSERT INTO pessoa(nome) VALUES(%s)"
        
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)
            
    def insert_csv(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding="utf-8"))
            for row in data:
                self.insert(row["nome"])
                print("Registro Inserido")
        except Exception as e:
            print("Erro ao inserir csv", e)
            
    def delete(self, id):
        try:
            sql_d = f"DELETE FROM pessoa WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            print("Registro deletado")
        except Exception as e:
            print("Erro ao deletar", e)
            
    def update(self, id, *args):
        try:
            sql = f"UPDATE pessoa SET nome = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro atualizado")
        except Exception as e:
            print("Erro ao atualizar", e)
            
if __name__ == "__main__":
    pessoa = Pessoa()
    pessoa.insert_csv("Aula06/data.csv") # Adicionando 6 registros
    pessoa.delete(14) # Removendo o registro Miguel
    pessoa.update(2, "Maria Antônio") # Atualizando para Maria Antônio