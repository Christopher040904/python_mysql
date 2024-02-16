# Conexão do Python com o MySQL

!["Imagem Python com MySQL"](https://www.learntek.org/blog/wp-content/uploads/2019/06/Mysql-python.png)

## Drive de comunicação com o mysql
Para estabeler a comunicação entre o Python e o banco de dados mysql, iremos usar o seguinte drive:
<a href="https://pypi.org/project/mysql-connector-python/#history"> https://pypi.org/project/mysql-connector-python/#history </a>

### Comando para instalar o drive
```python
    python -m pip install mysql-connector-python
```
### Configuração do banco de dados MySQL
O nosso banco de dados está em um container de docker.Para acessá-lo será necessário criar o container, então faremos os seguintes comandos em um servidor Fedora com o docker instalado:

#### Criação do volume
```shell
mkdir dados clientes
```

#### Criação do container
<center>
<img src="https://cdn.iconscout.com/icon/free/png-256/free-docker-226091.png" height="100" width="100">
</center>

```shell
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql
```
### Criação do banco de dados e da tabela clientes

```sql
CREATE DATABASE banco;
USE banco;
CREATE TABLE clientes(
clientes_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20)
)
```

#### Arquivo clientes.py

```python
# importando a biblioteca de conexão com o banco
# de dados mysql
# vamos adicionar um alias a biblioteca
import mysql.connector as mc

# Vamos estabelecer a conexão com o banco
# de dados e para tal, iremos passar os
# seguintes dados:
# servidor, porta, usuario, senha, banco
conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# Estamos testando a conexão, pedindo para
# exibir o id da conexão. Caso exiba uma
# pilha de erros, então você tem um erro
# na linha de conexão
print(conexao)

# para se movimentar dentro da estrutura de
# banco de dados e retornar dos dados necessários
# iremos criar um cursor
cursor = conexao.cursor()

# Vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")

# cursor.execute("insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@uol.com.br','(54) 9976-3298')")

# Vamos selecionar todos os dados da tabela clientes
rs = cursor.execute("Select * from banco.clientes")
print(cursor)
for c in cursor:
    print(f"Id do Cliente: {c[0]}")
    print(f"Nome do Cliente: {c[1]}")
    print(f"E-mail: {c[2]}")

```

#### Arquivo de cadastro: cad_clientes.py

```python
import mysql.connector as mc

# Estabelecer a conexão com o banco
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# Verificar se a conexão foi estabelecida
print(cx)

# Criação de variáveis para o usuário passar os dados do cliente para cadastrar
nome = input("Digite o nome do cliente: ")
email = input("Digite o email do cliente: ")
telefone = input("Digite o telefone do cliente: ")

cursor = cx.cursor()
cursor.execute("insert into clientes(nome_cliente,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")
# Confirmar a inserção dos dados na tabela
print(cx.commit())


```

#### Arquivo de atualização up_clientes.py

```python
import mysql.connector as mc
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
cursor = cx.cursor()
cursor.execute("Select * from clientes")
for i in cursor:
    print(i)

print("O que você deseja atualizar, digite:")
print("1 - para Nome")
print("2 - para E-mail")
print("3 - para Telefone")
op = input("Digite a opção desejada: ")
id = input("Agora, digite o id do cliente: ")
dado = input("Digite a nova informação: ")
if(op=="1"):
    cursor.execute("update clientes set nome_cliente='"+dado+"' where clientes_id="+id)
elif(op=="2"):
    cursor.execute("update clientes set email='"+dado+"' where clientes_id="+id)
elif(op=="3"):
    cursor.execute("update clientes set telefone='"+dado+"' where clientes_id="+id)    
else:
    print("Opção inválida!")

cx.commit()
```

#### Criação do arquivo del_clientes.py

```python
import mysql.connector as mc
import os
con = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
os.system("cls")
cursor = con.cursor()
cursor.execute("select * from clientes")
for c in cursor:
    print(c)

id = input("Digite o id do cliente que deseja apagar: ")
rs = input("Você realmente deseja apagar este cliente. Digite (s ou n): ")
if(rs=="s" or rs=="S"):
    cursor.execute("delete from clientes where clientes_id="+id)
    con.commit()
else:
    print("-------- Opção inválida ---------")        
```