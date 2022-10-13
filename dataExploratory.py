import re
from xml.etree.ElementInclude import include
import pandas as pd

pathPrices = 'tablasFinales\AllPrices.csv'
pathProducts ='tablasFinales\AllProducts.csv'
pathTiendas = 'tablasFinales\AllTiendas.csv'
pathTrees = 'tablasFinales\AllTrees.csv'
pathFolders = 'tablasFinales\Folders.csv'
pathZones = 'tablasFinales\zonasGeograficas.csv'

'''
I cannot read the data because I push it in git hub and it was too big , so git hub make it in another thing,
 and now I can't read it.
 But, after google it:
  git lfs install
  git lfs pull

After this 2 commands I can read the data :D 
'''

dfPrices = pd.read_csv(pathPrices) 
dfProd = pd.read_csv(pathProducts)
dfTiendas = pd.read_csv(pathTiendas)
dfTrees = pd.read_csv(pathTrees)
dfFolder = pd.read_csv(pathFolders)
dfZones =  pd.read_csv(pathZones)


priceInfo, priceDim, priceExam = dfPrices.info(), dfPrices.shape, dfPrices.iloc[0,:]
proInfo, proDim, proExam = dfProd.info(), dfProd.shape, dfProd.iloc[0,:]
tiendasInfo, tiendasDim, tiendasExam = dfTiendas.info(), dfTiendas.shape, dfTiendas.iloc[0,:]
treeInfo, treeDim, treeExam = dfTrees.info(), dfTrees.shape, dfTrees.iloc[0,:]
foldInfo, foldDim, foldExam = dfFolder.info(), dfFolder.shape, dfFolder.iloc[0,:] 
zoneInfo, zoneDim, zoneExam = dfZones.info(), dfZones.shape, dfZones.iloc[0,:] 


#Cambiamos fecha de prices esta en formato 07/06/2022 a formato YYYY-MM-DD

 
lst_date = []
for n in range(0, len(dfPrices)):
    year = dfPrices.fecha.iloc[n][6:]
    month = dfPrices.fecha.iloc[n][3:5]
    dia = dfPrices.fecha.iloc[n][0:2]
    fecha = year + '-' + month + '-' + dia
    lst_date.append(fecha)

len(lst_date)

dfPrices.fecha = lst_date

dfPrices.to_csv('AllPrices_1.csv')
