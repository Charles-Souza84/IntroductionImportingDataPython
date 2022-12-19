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

### Importando arquivos HDF5

