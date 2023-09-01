import csv
import mysql.connector

# Criando a classe que controla os comandos do MySQL
class MySQLDB:
    # Dados do meu servidor
    db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'project_poo'
    }
    
    # Abrindo a conexão
    def __init__(self):
        self.connection = mysql.connector.connect(**self.db_config)
        self.cursor = self.connection.cursor()
        self.table_name = None
        self.column_names = None
    
    # Definindo a criação da tabela
    def create_table(self, table_name, column_names):
        self.table_name = table_name
        self.column_names = column_names

        
        # Transformando a lista de nomes em String pars o MySQL
        columns_str = ', '.join([f'{col} VARCHAR(255)' for col in column_names])
        
        # Criando a query
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
            {columns_str}
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()
        
    # Criando a função para inserir através do CSV
    def insert_from_csv(self, csv_file):
        # Lendo o arquivo
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            
            # Lendo e formatando as linhas para inserir no MySQL
            for row in csv_reader:
                formatted_values = []
                for value in row:
                    if not value.isdigit():
                        value = value.replace('\'', '\'\'')
                        value = f"'{value}'"
                    formatted_values.append(value)
            
                values = ', '.join(formatted_values)
                insert_query = f"INSERT INTO {self.table_name} ({', '.join(self.column_names)}) VALUES ({values})"
            
                self.cursor.execute(insert_query)
                
            self.connection.commit()
            
    # Fechando a conexão
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Inicio a conexao com BD
db = MySQLDB()

# Muda o nome da tabela de acordo com o CSV que eu persistir
table_name = ''   # Para o Masculino: world_cup_man_data    ||  Para o Feminino: world_cup_woman_data

# Insiro o nome da tabela e as colunas
db.create_table(table_name, ['year', 'tournament_id', 'match_id', 'stage_name', 'group_name', 'replayed', 'replay', 'match_date',
                             'match_time', 'stadium_id', 'stadium_name', 'city_name', 'country_name', 'team_a_id', 'team_a_name',
                             'team_a_code', 'team_b_id', 'team_b_name', 'team_b_id_code', 'score', 'team_a_score', 'team_b_score',
                             'team_a_score_margin', 'team_b_score_margin', 'extra_time', 'penalty_shootout', 'score_penalties',
                             'team_a_score_penalties', 'team_b_score_penalties', 'team_a_win', 'team_b_win', 'draw'])

# Muda o nome do CSV, como tenho dois arquivos para persistir, mudaria
csv_file = ''  # Os dois:   Project/worldcup_man.csv  ||  Project/worldcup_woman.csv
# Insiro através da função criada o arquivo CSV
db.insert_from_csv(csv_file)

# Fecho a conexão
db.close_connection()