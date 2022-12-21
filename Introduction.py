# importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Using NumPy to import flat files

Load the MNIST digit recognition dataset using the numpy function loadtxt() :

    The first argument will be the filename.
    The second will be the delimiter which, in this case, is a comma.
"""

# atribuindo o nome do arquivo à variável file
file = 'MNIST.csv'

# carregando o arquivo como um array
digits = np.loadtxt(file, delimiter=',')

# imprimindo o datatype do array digits
print(type(digits))

# selecionando e formatando uma linha
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# plotando os dados formatados 
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

"""
Customizing your NumPy import

There are a number of arguments that np.loadtxt() takes :

    * delimiter changes the delimiter that loadtxt() is expecting.
        You can use ',' for comma-delimited.
        You can use '\t' for tab-delimited.
    * skiprows allows you to specify how many rows (not indices) you wish to skip
    * usecols takes a list of the indices of the columns you wish to keep.

Importing different datatypes

The file seaslug.txt has a text header, consisting of strings is tab-delimited.
These data consists of percentage of sea slug larvae that had metamorphosed in a given time period. 

Due to the header, if you tried to import it as-is using np.loadtxt(), Python would throw you a ValueError and tell you 
that it could not convert string to float. There are two ways to deal with this: firstly, you can set the data type argument 
dtype equal to str (for string).

Alternatively, you can skip the first row as we have seen before, using the skiprows argument.
"""

# atribuindo o nome do arquivo à variável file
file = 'seaslug.txt'

# importando o arquivo file
# observando que delimiter = '\t' por que o arquivo é tabulado
data = np.loadtxt(file, delimiter='\t', dtype=str)

# imprimindo o primeiro elemento do array
print(data[0])

# carregando os dados como floats e pulando a primeira linha
data_float = np.loadtxt(file, delimiter='\t', dtype='float', skiprows=1)

# imprimindo o décimo elemento de data_float
print(data_float[9])

# plotando um scatterplot dos dados
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

"""
Working with mixed datatypes (1)

Much of the time you will need to import datasets which have different datatypes in different columns; one column may 
contain strings and another floats, for example. The function np.loadtxt() will freak at this. There is another function, 
np.genfromtxt(), which can handle such structures. If we pass dtype=None to it, it will figure out what types each column should be.

Import 'titanic.csv' using the function np.genfromtxt() as follows:

data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

Here, the first argument is the filename, the second specifies the delimiter , and the third argument names 
tells us there is a header. Because the data are of different types, data is an object called a structured array. 
Because numpy arrays have to contain elements that are all the same type, the structured array solves this by being a 1D array, 
where each element of the array is a row of the flat file imported. You can test this by checking out the array's shape in the 
shell by executing np.shape(data).

Accessing rows and columns of structured arrays is super-intuitive: to get the ith row, merely execute data[i] and to get 
the column with name 'Fare', execute data['Fare'].
"""

# imprimindo o conteúdo da coluna Survived
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None, encoding= 'utf-8')
print(data['Survived'])

"""
Working with mixed datatypes (2)

There is also another function np.recfromcsv()  that behaves similarly to np.genfromtxt(), except that its default dtype is None. 
"""

# atribuindo o nome do arquivo à variável file
file = 'titanic.csv'

# importando o arquivo file
d = np.recfromcsv(file, delimiter = ',', names = True, dtype = None, encoding = 'utf-8')

# imprimindo as três primeiras entradas de d
print(d[:3])

"""
Using pandas to import flat files as DataFrames (1)

we can easily import files of mixed data types as DataFrames using the pandas functions read_csv() and read_table().
"""

# atribuindo o nome do arquivo à variável file
file = 'titanic.csv'

# lendo o arquivo em um dataframe
df = pd.read_csv(file)

# exibindo a head ( por padrão - 5 primeiras linhas do dataframe )
print(df.head())

"""
Using pandas to import flat files as DataFrames (2)

We are able to import flat files into a pandas DataFrame. It is then straightforward 
to retrieve the corresponding numpy array using the attribute values. 

"""

# atribuindo o nome do arquivo à variável file
file = 'MNIST.csv'

# lendo as cinco primeiras linhas do arquivo em um dataframe
data = pd.read_csv(file, nrows = 5, header = None)

# construindo um array numpy a partir do dataframe. Basta utilizarmos o atributo values
data_array = data.values

# imprimindo o datatype de data_array
print(type(data_array))

"""
Customizing your pandas import

The pandas package is also great at dealing with many of the issues you will encounter when importing data as a data scientist, 
such as comments occurring in flat files, empty lines and missing values. Note that missing values are also commonly referred to 
as NA or NaN. To wrap up this chapter, you're now going to import a slightly corrupted copy of the 
Titanic dataset titanic_corrupt.txt, which

    * contains comments after the character '#'
    * is tab-delimited.

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')
"""

