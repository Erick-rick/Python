#Criar Banco de dados

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
  database="mydatabase"
)

mycursor = mydb.cursor()

#Criar tabela
mycursor.execute("CREATE DATABASE mydatabase")

#Alterar tabela
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


#Inserir na tabela
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

#É necessário fazer as alterações, caso contrário, nenhuma alteração será feita na tabela
mydb.commit()

print(mycursor.rowcount, "record inserted.")

# Inserir varias linhas

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

#Para inserir várias linhas em uma tabela, use o executemany()método
# método é uma lista de tuplas, contendo os dados que você deseja inserir
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

#Selecionar uma tabela

mycursor.execute("SELECT * FROM customers")

#Usamos o fetchall() método, que busca todas as linhas da última instrução executada.
myresult = mycursor.fetchall()

for x in myresult:
  print(x)