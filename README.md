# Introdução e arquivos simples

### Introdução

Arquivos **.csv** e **.txt** são considerados arquivos simples, sem relacionamentos estruturados. Estes arquivos podem conter dados em tabelas ou puramente texto. 


* **lendo um arquivo de texto-** utilizando a função básica open do _Python_:
```python
# mode r - abre apenas leitura
# mode w - abre para escrita
filename = 'huck_finn.txt'
file = open(filename, mode = 'r')
text = file.read()
file.close()
# sempre devemos fechar um arquivo que foi aberto
```
```python
# podemos imprimir na tela um arquivo 
# observando que text = file.read(), poderíamos passar file.read() diretamente no print
print(text)
```

* **context manager** - podemos declarar um bloco com _with_ em que o arquivo só permanece aberto dentro do gerenciador de contexto ( recomendável ):

```python
# desta forma não é necessário nos preocuparmos em fechar o arquivo
with open('huck_finn.txt', 'r') as file:
    print(file.read())
```
### A importância de arquivos simples em ciência de dados

* **flat files-** arquivos de texto que contém registros em tabela sem relacionamentos estrturados.
    * linhas - registros
    * colunas - atributos
    * header - primeira linha do arquivo, descreve o conteúdo de cada coluna (nomes das colunas)

* **extensão de arquivos**
    * .csv - comma separated values
    * .txt - text file
    * commas, tabs - delimitadores (além da vírgula, outros caracteres podem ser utilizado como separadores)

### Importando arquivos simples usando NumPy

* NumPy arrays - padrão para armazenar dados numéricos

* podemos fazer a leitura por meio de algumas funções como:
    * loadtxt()
    * genfromtxt()
    * recfromcsv()

```python
import numpy as np
filename = 'MNIST.txt'
data = np.loadtxt(filename, delimiter=',')
data
[[ 0. 0. 0. 0. 0.]
[ 86. 250. 254. 254. 254.]
[ 0. 0. 0. 9. 254.]
...,
[ 0. 0. 0. 0. 0.]
[ 0. 0. 0. 0. 0.]
[ 0. 0. 0. 0. 0.]]
```
```python
# podemos pular linha ao carregar o arquivo, como o header, por exemplo
import numpy as np
filename = 'MNIST_header.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1)
print(data)
[[ 0. 0. 0. 0. 0.]
[ 86. 250. 254. 254. 254.]
[ 0. 0. 0. 9. 254.]
...,
[ 0. 0. 0. 0. 0.]
[ 0. 0. 0. 0. 0.]
[ 0. 0. 0. 0. 0.]]
```
```python
# também podemos selecionar colunas específicas a serem importadas
import numpy as np 
filename ='MNIST_header.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1,usecols=[0,2])
print(data)

[[ 0. 0.] 
 [ 86. 254.]
 [ 0. 0.] 
 ..., 
 [ 0. 0.] 
 [ 0. 0.] 
 [ 0. 0.]]
```
```python
# podemos configurar o tipo de dado assumido pelos registros após a leitura
data = np.loadtxt(filename, delimiter=',', dtype=str)
```
### Importando arquivos simples usando Pandas

**O que um cientista de dados precisa:**
    * estrutura de dados bi-dimensional rotulada;
    * colunas com diferentes tipos de dados;
    * manipular, seccionar, reformatar, agrupar, unir, fundir
    * elaborar estatísticas;
    * trabalhar com dados em séries temporais;

**Pandas-** foi criada para suprir as necessidades acima, sem que seja necessário recorrer a linguagem R. Atualmente é boa prática
importar flat files como dataframe.

```python
import pandas as pd
filename = 'winequality-red.csv'
data = pd.read_csv(filename)
# por padrão, exibe as 5 primeiras linhas do dataframe
data.head()
```
___
# Importando dados de outros tipos de arquivos

### Introdução a outros tipos de arquivos

Alguns outros formatos de arquivos podem ser lidos, como :

    * planilhas de Excel
    * arquivos MATLAB
    * arquivos SAS
    * arquivos Stata
    * arquivos HDF5

* **pickled files-** tipo de arquivo nativo do Python. São arquivos serializados, convertidos em uma sequência de bytes.

```python
# devemos importar o pacote pickle
import pickle
# rb - read only binary
with open('pickled_fruit.pkl', 'rb') as file:
data = pickle.load(file)
print(data)

{'peaches': 13, 'apples': 4, 'oranges': 11}
```

* **planilhas do excel**
```python
import pandas as pd
file = 'urbanpop.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
['1960-1966', '1967-1974', '1975-2011']

df1 = data.parse('1960-1966') # nome de uma aba, como string
df2 = data.parse(0) # índice de uma aba, como float
```

### Importando arquivos SAS/Stata usando Pandas

* SAS - Statistical Analysis System. Análise de negócios e bioestatísticas. Os arquivos SAS são usados em:
    * análises avançadas;
    * análises multivariada;
    * inteligência de negócios;
    * manipulação de dados;
    * análise preditiva;
    * padrão para análise computacional;
<p></p>

* **importando arquivo SAS**
```python
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file:
    df_sas = file.to_data_frame()
```
* Stata - “Statistics” + “data”. Empregado em pesquisa acadêmica de ciências sociais.
<p></p>

* **importando arquivo Stata**
```python
import pandas as pd
data = pd.read_stata('urbanpop.dta')
``` 
### Importando arquivos HDF5

* Hierarchical Data Format version 5;
* Padrão para armazenar grandes quantidades de dados numéricos;
* Datasets podem ter centenas de gigabytes ou terabytes;
* HDF5 pode escalar a exabytes;

* **importando arquilo HDF5**
```python
import h5py
filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'
data = h5py.File(filename, 'r') # 'r' é para leitura
print(type(data))
<class 'h5py._hl.files.File'>
```

* **a estrutura de arquivos HDF5**
```python
for key in data.keys():
    print(key)
meta # meta dados do arquivo
quality # qualidade dos dados
strain # dados armazenados no arquivo
```
```python
for key in data['meta'].keys():
    print(key)

Description
DescriptionURL
Detector
Duration
GPSstart
Observatory
Type
UTCstart

print(np.array(data['meta']['Description']), np.array(data['meta']['Detector']))
b'Strain data time series from LIGO' b'H1'
```
### Importando arquivos MATLAB

* Matrix Laboratory;
* Padrão industrial na engenharia e ciência;
* Dados salvos como arquivos .mat;

<p></p>
A biblioteca scipy possui as seguintes funções :

* scipy.io.loadmat() - carrega arquivos .mat 
* scipy.io.savemat() - salva arquivos .mat 

* **importando um arquivo .mat**

```python
import scipy.io
filename = 'workspace.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))

<class 'dict'>
```
* keys - nomes das variáveis MATLAB
* values - objetos atribuidos a variáveis
```python
print(type(mat['x']))
<class 'numpy.ndarray'>
```
___
# Trabalhando com bancos relacionais em Python

### Introdução a bancos relacionais

Um banco de dados é composto por tabelas e cada tabela representa um tipo de entidade. Em um banco relacional, cada linha representa
uma instância da entidade e cada coluna, um atributo. É importante que cada coluna tenha um identificador único ( primary_key ). Em um banco relacional temos várias tabelas que se relacionam.

SQL - Structured Query Language - linguagem que descreve como nos comunicamos com um banco de dados, acessando os dados e os atualizando.

### Criando um database engine

Para acessar os dados em uma banco de dados precisamos inicialmente nos conectarmos ao banco e este acesso é feito mediante um engine, que é a ponte de conexão ao banco de dados. Podemos fazer acesso ao banco por meio de comandos do engine, mas isso não é 
recomendado.

* SQLite database - simples e rápido

* SQLAlchemy - trabalha com outros sistemas gerenciados de banco de dados como Postgres e MySQL

* **criando o database engine**
```python
from sqlalchemy import create_engine
# a função create_engine recebe como argumento o tipo e nome do banco
# connection string
engine = create_engine('sqlite:///Northwind.sqlite')
```
* **acessando os nomes das tabelas**
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Northwind.sqlite')

table_names = engine.table_names()
print(table_names)

['Categories', 'Customers', 'EmployeeTerritories','Employees', 'Order Details', 'Orders', 'Products',
'Region', 'Shippers', 'Suppliers', 'Territories']
```

### Fazendo buscas em bancos relacionais Python

Após criarmos o database engine podemos fazer acesso ao banco com as buscas desejadas. Normalmente seguimos as seguintes etapas :

* importar pacotes e funções;
* criar a engine;
* estabelecer uma conexão com a engine;
* fazer consultas aos dados no banco;
* salvar os resultados em dataframe;
* fechar a conexão;

```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
con = engine.connect() # cria a conexão com a engine
rs = con.execute("SELECT * FROM Orders") # executa a conexão com a query desejada
df = pd.DataFrame(rs.fetchall())  # fetcheall - retorna um array multidimensional com todas as linhas 
df.columns = rs.keys() # seta o nome das colunas
con.close() # fecha a conexão 
```
* **com context manager construct**
```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
with engine.connect() as con:
    rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
    df = pd.DataFrame(rs.fetchmany(size=5)) # fetchmany(size= N) - retorna N linhas 
    df.columns = rs.keys()
```
### Fazendo buscas em bancos relacionais diretamente com Pandas

Com Pandas podemos fazer em apenas uma linha a conexão ao banco e a execução da query desejada :

```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Orders")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
# utilizando a função read_sql_query passamos a query como primeiro argumento e a engine a qual desejamos nos conectar
df = pd.read_sql_query("SELECT * FROM Orders", engine)
```

### Buscas avançadas : explorando relacionamentos de tabelas

Podemos realizar buscas mais complexas fazendo JOIN de tabelas, tendo acesso aos campos contidos em cada uma delas.

* **INNER JOIN**
```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
# INNER JOIN cria uma nova tabela a partir do relacionamento da FK de uma tabela que corresponde a PK de outra
df = pd.read_sql_query("SELECT OrderID, CompanyName FROM Orders
INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID", engine)
print(df.head())
```
