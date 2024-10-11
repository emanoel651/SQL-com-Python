import pymysql

NOME_DA_TABELA = 'Pessoas'

# Criando a conexão com banco de dados
# conexao = pymysql.connect(
#     host='localhost',
#     user='my_user',
#     password='my_password',
#     database='my_database',
#     charset='utf8mb4'
# )

# # Criando tabela
# with conexao:
#     with conexao.cursor() as cursor:
#         cursor.execute(
#             f'CREATE TABLE {NOME_DA_TABELA} ('
#             'cpf VARCHAR(20) NOT NULL, '
#             'nome VARCHAR(50) NOT NULL, '
#             'idade INT NOT NULL, '
#             'sexo VARCHAR(15), '
#             'nacionalidade VARCHAR(20), '
#             'estado_civil VARCHAR(20), '
#             'estado VARCHAR(20), '
#             'profissao VARCHAR(20), '
#             'renda_mensal FLOAT NOT NULL, '
#             'PRIMARY KEY (cpf)'
#             ')'
#         )
#     conexao.commit()

# Dados a serem inseridos
# dados = [
#     ('123.456.789-00', 'Ana Silva', 30, 'Feminino', 'Brasileira', 'Solteira', 'SP', 'Engenheira', 6000.00),
#     ('987.654.321-11', 'João Souza', 45, 'Masculino', 'Brasileira', 'Casado', 'RJ', 'Médico', 12000.00),
#     ('456.123.789-22', 'Maria Oliveira', 28, 'Feminino', 'Brasileira', 'Solteira', 'MG', 'Professora', 4500.00),
#     ('321.654.987-33', 'Pedro Santos', 35, 'Masculino', 'Brasileira', 'Casado', 'RS', 'Advogado', 8000.00),
#     ('789.456.123-44', 'Lucas Pereira', 40, 'Masculino', 'Brasileira', 'Solteiro', 'PR', 'Arquiteto', 7500.00),
#     ('654.321.987-55', 'Carla Lima', 32, 'Feminino', 'Brasileira', 'Divorciada', 'SC', 'Designer', 5200.00),
#     ('147.258.369-66', 'Bruno Alves', 38, 'Masculino', 'Brasileira', 'Casado', 'BA', 'Engenheiro Civil', 9000.00),
#     ('258.369.147-77', 'Renata Gomes', 27, 'Feminino', 'Brasileira', 'Solteira', 'PE', 'Enfermeira', 3800.00),
#     ('369.147.258-88', 'Rafael Ferreira', 31, 'Masculino', 'Brasileira', 'Casado', 'ES', 'Programador', 6500.00),
#     ('741.852.963-99', 'Fernanda Rodrigues', 29, 'Feminino', 'Brasileira', 'Solteira', 'GO', 'Jornalista', 4200.00),
#     ('852.963.741-00', 'André Costa', 42, 'Masculino', 'Brasileira', 'Divorciado', 'CE', 'Gerente', 10000.00),
#     ('963.741.852-11', 'Juliana Barbosa', 34, 'Feminino', 'Brasileira', 'Casada', 'AM', 'Médica', 11500.00),
#     ('147.369.258-22', 'Gabriel Mendes', 37, 'Masculino', 'Brasileira', 'Solteiro', 'DF', 'Analista', 7800.00),
#     ('258.147.369-33', 'Larissa Araujo', 26, 'Feminino', 'Brasileira', 'Solteira', 'MT', 'Professora', 3900.00),
#     ('369.258.147-44', 'Marcelo Teixeira', 39, 'Masculino', 'Brasileira', 'Casado', 'MS', 'Engenheiro', 9500.00),
#     ('741.963.852-55', 'Amanda Rocha', 33, 'Feminino', 'Brasileira', 'Divorciada', 'PB', 'Administradora', 6700.00),
#     ('852.741.963-66', 'Daniel Ribeiro', 28, 'Masculino', 'Brasileira', 'Solteiro', 'AL', 'Contador', 5300.00),
#     ('963.852.741-77', 'Paula Nunes', 36, 'Feminino', 'Brasileira', 'Casada', 'SE', 'Psicóloga', 8200.00),
#     ('147.852.369-88', 'Felipe Martins', 41, 'Masculino', 'Brasileira', 'Divorciado', 'PI', 'Diretor', 11000.00),
#     ('258.963.147-99', 'Mariana Campos', 30, 'Feminino', 'Brasileira', 'Solteira', 'TO', 'Publicitária', 4800.00)

# ]


# # Inserindo dados
# with conexao:
#     with conexao.cursor() as cursor:
#         query = f'INSERT INTO {NOME_DA_TABELA} (cpf, nome, idade, sexo, nacionalidade, estado_civil, estado, profissao, renda_mensal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
#         cursor.executemany(query, dados)
#     conexao.commit()



#Criando uma query

def inserir_dados(cpf, nome, idade, sexo, nacionalidade, estado_civil, estado, profissao, renda_mensal):
    conexao = pymysql.connect(
        host='localhost',
        user='my_user',
        password='my_password',
        database='my_database',
        charset='utf8mb4'
    )
    
    with conexao:
        with conexao.cursor() as cursor:
            query = """
            INSERT INTO Pessoas (cpf, nome, idade, sexo, nacionalidade, estado_civil, estado, profissao, renda_mensal)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (cpf, nome, idade, sexo, nacionalidade, estado_civil, estado, profissao, renda_mensal))
        conexao.commit()

# Função para criar a view
def criar_view_estado_salario(estado, salario):
    conexao = pymysql.connect(
        host='localhost',
        user='my_user',
        password='my_password',
        database='my_database',
        charset='utf8mb4'
    )
    
    with conexao:
        with conexao.cursor() as cursor:
            query = f"""
            CREATE OR REPLACE VIEW view_estado_salario AS
            SELECT nome, estado, profissao, renda_mensal
            FROM Pessoas
            WHERE estado = %s AND renda_mensal > %s;
            """
            cursor.execute(query, (estado, salario))
        conexao.commit()


# Função para consultar e visualizar a view
def consultar_view():
    conexao = pymysql.connect(
        host='localhost',
        user='my_user',
        password='my_password',
        database='my_database',
        charset='utf8mb4'
    )
    
    with conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM view_estado_salario;")
            resultados = cursor.fetchall()
            for linha in resultados:
                print(linha)




def visualizar():
    conexao = pymysql.connect(
        host='localhost',
        user='my_user',
        password='my_password',
        database='my_database',
        charset='utf8mb4'
    )
    with conexao:
        with conexao.cursor() as cursor:
            cursor.execute(F"SELECT * FROM {NOME_DA_TABELA}")
            visao = cursor.fetchall()
            for linha in enumerate(visao):
                print(*linha)


visualizar()