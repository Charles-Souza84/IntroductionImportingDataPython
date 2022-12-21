"""
Listing sheets in Excel files

Whether you like it or not, any working data scientist will need to deal with Excel spreadsheets at some point in time. 
You won't always want to do so in Excel, however!

Loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research Institute Oslo's (PRIO) dataset. 
This data contains age-adjusted mortality rates due to war in various countries over several years.

"""

# importando pandas
import pandas as pd

# atribuindo o nome do arquivo à variável file
file = 'battledeath.xlsx'

# carregando a planilha 
xls = pd.ExcelFile(file)

# imprimindo os nomes das abas da planilha
print(xls.sheet_names)

"""
Importing sheets from Excel files

Learning how to import any given sheet of your loaded .xlsx file as a DataFrame. 
    * specifying either the sheet's name or its index.

"""

# carregando uma aba da planilha em um dataframe : df1
df1 = xls.parse('2004')

# imprimindo o head do dataframe df1
print(df1.head())

# carregando uma aba da planilha em um dataframe : df2
df2 = xls.parse(0)

# imprimindo o head do dataframe df2
print(df2.head())

"""
Customizing your spreadsheet import

Parse your spreadsheets and use additional arguments to skip rows, rename columns and select only particular columns.

    * method parse() - additional arguments skiprows, names and usecols. 
These skip rows, name the columns and designate which columns to parse, respectively. All these arguments can be assigned to lists 
containing the specific row numbers, strings and column numbers, as appropriate.

"""

# carregando a primeira aba e renomeando as colunas : df1
df1 = xls.parse(0, skiprows= [0], names=['Country', 'AAM due to War (2002)'])

# imprimindo o head do dataframe df1
print(df1.head())

# carregando a primeira aba e renomeando as colunas : df1
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# imprimindo o head do dataframe df2
print(df2.head())

"""
Importing SAS files

Figure out how to import a SAS file as a DataFrame using SAS7BDAT and pandas.

"""

# importando matplotlib.pyplot
import matplotlib.pyplot as plt

# Import sas7bdat package
from sas7bdat import SAS7BDAT

# salvando o arquivo em um dataframe : df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# imprimindo o head do dataframe
print(df_sas.head())

# plotando um histograma com os atributos do dataframe
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

"""
Importing Stata files

Importing Stata files as DataFrames using the  pd.read_stata() function from pandas. 

"""

# carregando o arquivo stata em um dataframe : df
df = pd.read_stata('disarea.dta')

# imprimindo o head do dataframe 
print(df.head())

# plotando o histograma de uma coluna do dataframe
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

"""
Using h5py to import HDF5 files

Print out its datatype to confirm you have imported it correctly then study the structure of the file in order to see precisely 
what HDF groups it contains.

"""
# importando as bibliotecas NumPy e h5py
import numpy as np
import h5py

# atribuindo o nome do arquivo à variável file
file = 'LIGO_data.hdf5'

# carregando o arquivo file, atribuindo à variável data
data = h5py.File(file, 'r')

# imprimindo o datatype do arquivo carregado
print(type(data))

# imprimindo as chaves do arquivo
for key in data.keys():
    print(key)

"""
Extracting data from your HDF5 file

Extract some of the LIGO experiment's actual data from the HDF5 file and you'll visualize it.

To do so, you'll need to first explore the HDF5 group 'strain'
"""

# selecionando um grupo do arquivo HDF5
group = data['strain']

# imprimindo as chaves do grupo selecionado
for key in group.keys():
    print(key)

# atribuindo à variável strain a série temporal 
strain = np.array(data['strain']['Strain'])

# atribuindo o número de pontos temporais para amostra
num_samples = 10000

# atribuindo o vetor temporal
time = np.arange(0, 1, 1/num_samples)

# plotando os dados
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

"""
The file 'ja_data2.mat' contains gene expression data from the Albeck Lab at UC Davis. 
"""

# importando a biblioteca scipy
import scipy.io

# carregando o arquivo .mat
mat = scipy.io.loadmat('ja_data2.mat')

# imprimindo o datatype do arquivo 
print(type(mat))

# imprimindo as chaves do dicionário MATLAB
print(mat.keys())

# imprimindo o tipo de conteúdo correspondentes a chave 'CYratioCyt'
print(type(mat['CYratioCyt']))

# imprimindo o shape do conteúdo referente a chave 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# selecionando parte do array e plotando os dados
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()