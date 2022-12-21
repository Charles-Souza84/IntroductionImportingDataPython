"""
Creating a database engine

Um engine é criado com o uso da função create_engine() do módulo create_engine da biblioteca sqlalchemy

engine = create_engine('sqlite:///Northwind.sqlite')

'sqlite:///Northwind.sqlite' é chamada de string de conexão ao banco SQLite  Northwind.sqlite (exemplo). 
"""

# importando o módulo necessário para criar o engine
from sqlalchemy import create_engine

# criando o engine
engine = create_engine('sqlite:///Chinook.sqlite')

# salvando os nomes das tabelas em uma lista
table_names = engine.table_names()

# impriminto os nomes das tabelas
print(table_names)

"""
O Hello World das consultas SQL

Abaixo um exemplo de como selecionar todas as colunas de uma tabela em um database.

"""

# importando pacote e biblioteca necessários
from sqlalchemy import create_engine
import pandas as pd

# criando o engine
engine = create_engine('sqlite:///Chinook.sqlite')

# abrindo uma conexão com o engine
con = engine.connect()

# fazendo a consulta
rs = con.execute("SELECT * FROM Album")

# salvando o resultado da consulta em um dataframe
df = pd.DataFrame(rs.fetchall())

# fechando a conexão
con.close()

# imprimindo o head do dataframe
print(df.head())

"""
Customizando o Hello World das consultas SQL 

Abaixo serão executas as serguintes tarefas :

    * selecionar colunas específicas de uma tabela;
    * selecionar um número específico de linhas;
    * importar nomes de colunas de uma tabela do banco de dados;
"""
# abrindo o angine em um context manager 
# realizando uma consulta e salvando o resultado em um dataframe
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size = 3))
    df.columns = rs.keys()

# imprimindo o tamanho do dataframe
print(len(df))

# imprimindo o head do dataframe
print(df.head())

"""
Filtrando os registros do banco usando utilizando WHERE do SQL

Podemos filtrar qualquer busca feita com SELECT por meio de uma condição com WHERE.

SELECT * FROM Customer WHERE Country = 'Canada'

Abaixo vamos selecionar todos os registros da tabela Employee com EmployeeId maior ou igual a 6.

"""

# criando o engine
engine = create_engine('sqlite:///Chinook.sqlite')

# abrindo o angine em um context manager 
# realizando uma consulta e salvando o resultado em um dataframe
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# imprimindo o head do dataframe
print(df.head())

"""
Ordenando os registros com ORDER BY

"SELECT * FROM Customer ORDER BY SupportRepId"

Na verdade podemos ordenar qualquer SELECT por qualquer coluna.

Abaixo serão selecionados todos os registros da tabela Employee e com ordenação pela coluna BirthDate.

"""

# criando o engine
engine = create_engine('sqlite:///Chinook.sqlite')

# abrindo o engine em um ontext manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # setando os nomes das colunas do dataframe
    df.columns = rs.keys()

# imprimindo o head do dataframe
print(df.head())

"""
Utilizando Pandas em consultas mais complexas

Por meio da função read_sql_query() do Pandas podemos realizar consultas mais complexas em uma linha apenas :

pd.read_sql_query("query desejada", engine criada para acessar o banco)

Abaixo será construído um dataframe contendo as linhas da tabela Employee nas quais EmployeeId seja maior ou igual a 6, além de 
ordenas os registros pela coluna BirthDate .

"""

# importando o pacote e a biblioteca necessários
from sqlalchemy import create_engine
import pandas as pd

# criando o engine
engine = create_engine('sqlite:///Chinook.sqlite')

# executando a consulta e salvando seu resultado no dataframe
df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate", engine)

# imprimindo o head do dataframe
print(df.head())

"""
O poder do SQL está no relacionamento entre as tabelas : INNER JOIN
Abaixo serão selecionados, para cada registro da tabela Album, o título e o nome do artista. As tabelas Album e Artist estão
relacionadas pela coluna ArtistID.

"""

# abrindo o engine em um context manager
# realizando a consulta e salvando o resultado em um dataframe
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# imprimindo o head do dataframe
print(df.head())

"""
FIltrando o INNER JOIN

Basta utilizarmos o comando WHERE do SQL para filtrar a tabela resultante do INNER JOIN.

"""

# realizando a consulta e salvando o resultado no dataframe
df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",engine)

# imprimindo o head do dataframe
print(df.head())
