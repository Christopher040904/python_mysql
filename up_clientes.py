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