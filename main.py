import sqlite3
""" import base64

path_image_bahia = 'image\estado_bahia.jpg'
with open(f"{path_image_bahia}", "rb") as image2string:
    empImage = base64.b64encode(image2string.read())
print(empImage)
 """

banco = sqlite3.connect('estados.db')

# É a través desse cursos que vamos realizar todas as operações do nosso banco
cursor = banco.cursor()
rows = cursor.fetchall()

add = True
id = len(rows)
federacao = str(input('Federação: ')).strip().upper()
estado = str(input('Estado: ')).strip().capitalize()
população = float(input('População: '))
idh = float(input('IDH: '))

while True:
    if federacao == '' or estado == '' or população == '' or idh == '':
        print('Erro em algum momento de preenchimento dos dados!')
        break
    else:
        id += 1

        # Cria a tabela
        #cursor.execute("CREATE TABLE IF NOT EXISTS estados (ID integer, Federação TEXT, Estado TEXT, População REAL, IDH REAL)")

        # Insere os dados no banco de dados
        cursor.execute("""
        INSERT INTO estados(ID, Federação, Estado, População, IDH) VALUES(?,?,?,?,?)""",(id, federacao, estado, população, idh))
        #cursor.execute(f"INSERT INTO estados VALUES(2, 'TO', 'Tocantins', 10.1, 0.678)")

        # Faz o commit para confirmar que estamos inserindo esses dados no nosso banco
        banco.commit()

        cont = str(input("Fazer novo registro? [S] / [N]")).upper().strip()
        if cont == 'N':
            print('Processo finalizado')
            break


# Seleciona todos os dados do nosso banco de dados estados
cursor.execute("SELECT * FROM estados")
# Comando para exibir os dados selecionados
for row in rows:
    print(row)