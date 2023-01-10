import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor() # É a trabés desse cursos que vamos realizar todas as operações do nosso banco

# Cria a tabela
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

# Insere os dados no banco de dados
#cursor.execute("INSERT INTO pessoas VALUES('João Pedro', 23, 'emailGenerico@gmail.com')")

# Faz o commit para confirmar que estamos inserindo esses dados no nosso banco
#banco.commit()

# Seleciona todos os dados do nosso banco de dados pessoas
cursor.execute("SELECT * FROM pessoas")
# Comando para exibir os dados selecionados
print(cursor.fetchall())