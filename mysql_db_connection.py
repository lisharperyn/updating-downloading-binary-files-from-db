import mysql.connector


# Anexando arquivo binário no banco de dados

def insert_data_to_db(file_name, file_content):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='representacoes',
        charset='utf8'
    )

    mycursor = db.cursor()

    query = "INSERT INTO representacoes_cadastro (Denominacao, Arquivo) VALUES (%s, %s);"   # query = comando
    values = (file_name, file_content)
    mycursor.execute(query, values)
    db.commit()

    mycursor.close()
    db.close()


# Fazendo download do arquivo binário

def download_data_from_db(file_name):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='representacoes',
        charset='utf8'
    )

    mycursor = db.cursor()

    query = "SELECT Arquivo FROM representacoes_cadastro WHERE Denominacao = %s;"
    mycursor.execute(query, (file_name,))

    result = mycursor.fetchone()

    mycursor.close()
    db.close()

    if result:
        return result[0]   # Retorna o conteúdo do arquivo
    else:
        return None


# Comando para exibição de lista de sugestões do nome do arquivo
def fetch_filenames_from_db(term):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='representacoes',
        charset='utf8'
    )

    mycursor = db.cursor()

    query = 'SELECT Denominacao FROM representacoes_cadastro WHERE Denominacao LIKE %s LIMIT 10;'
    like_term = f"{term}%"
    mycursor.execute(query, (like_term,))
    results = mycursor.fetchall()

    mycursor.close()
    db.close()

    return [results[0] for results in results]


"""
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='representacoes',
    charset='utf8'
)

cursor = conexao.cursor()

controle_2 = 12
comando = f'DELETE FROM representacoes_cadastro WHERE Controle = "{controle_2}";'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
"""

'''
# DEMONSTRAÇÃO CRUD COMPLETO

""" O cursor vai executar os comandos da conexão (db); toda conexão deve ser inicializada e logo após deve-se criar  
um cursor """

""" Da mesma forma que se inicia uma conexão logo no início do código, imediamente deve-se acrescentar o comando para 
finalizá-la, neste caso: cursor.close() e db.close() """


# CREATE
def create(file_name, file_content):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='representacoes',
        charset='utf8'
    )

    cursor = connection.cursor()

    comando = 'INSERT INTO representacoes_cadastro (Denominacao, Arquivo) VALUES (%, %);'
    valores = (file_name, file_content)
    cursor.execute(comando, valores)
    connection.commit()

    """ Quando você cria (Create), atualiza (Update) ou deleta (Delete) alguma informação do banco, necessita-se do 
    comando db.commit, no entanto, quando o objetivo é ler/pegar (Read) a informação, o commit não é necessário """

    """ Exemplo: o comando anterior para download do arquivo binário não necessitou do db.commit, e sim do result = 
    cursor.fetchone(), que armazena o dado (poderia-se usar fetchall() também dependendo da situação """

    cursor.close()
    connection.close()


# CREATE já passando o valor dos atributos
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='representacoes',
    charset='utf8'
)

cursor_2 = conexao.cursor()

denominacao = "Teste_CRUD_Create"
comando_2 = f'INSERT INTO representacoes_cadastro (Denominacao) VALUES ("{denominacao}");'
cursor_2.execute(comando_2)
conexao.commit()

cursor_2.close()
conexao.close()


# READ
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='representacoes',
    charset='utf8'
)

cursor = conexao.cursor()

comando = 'SELECT * FROM representacoes_cadastro;'
cursor.execute(comando)
resultado = cursor.fetchall()  # lê o banco de dados
print(resultado)

cursor.close()
conexao.close()


# UPDATE
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='representacoes',
    charset='utf8'
)

cursor = conexao.cursor()

comando = f'UPDATE representacoes_cadastro SET Denominacao = "Teste_CRUD_Update" WHERE Controle = 13;'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()


# DELETE
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='representacoes',
    charset='utf8'
)

cursor = conexao.cursor()

controle = 11
comando = f'DELETE FROM representacoes_cadastro WHERE Controle = "{controle}";'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
'''
