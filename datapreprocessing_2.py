from importlib.resources import path
import pandas as pd 
import numpy as np
import os

from pyparsing import col

path_dp= "C:/Users/Maria Luisa/OneDrive/Documentos/MasterDataScience/BDRelacionales/Clase1-08-09/datapreprocessing1/"

############### acomodamos otra vez los nombres de los csv en su respectivo array 

cont1 = os.listdir(path_dp) 

#checar si todas las columnas si coinciden y si algun descriptivo (suma) / dimension varian de df a df 

arbol = [] #ok
precios = [] #ok 
productos = [] #ok
tiendas = [] # checar col names
zonasgeo=[] #revisar si todos son iguales 
 

for i in range(0, len(cont1)):
    item = cont1[i]
    if item.endswith('arbol.csv'):
        arbol.append(item)
    elif item.endswith('precios.csv'):
        precios.append(item)
    elif item.endswith('productos.csv'):
        productos.append(item)
    elif item.endswith('tiendas.csv'):
        tiendas.append(item)
    elif item.endswith('geograficas.csv'):
        zonasgeo.append(item)

############Funcion para validar que todos los df tengan las mismas columnas y se puedan concatenar
def val_cols(arregloConPaths):
     
    lst_tree = []
    for i in range(0, len(arregloConPaths)):
        dframe = path_dp + arregloConPaths[i]
        colnames, dim1, dim2  = pd.read_csv(dframe).columns.to_list() , pd.read_csv(dframe).shape[0], pd.read_csv(dframe).shape[1]
        lst_tree.append([colnames, dim1, dim2 ])
        print([colnames, dim1, dim2 ])
    print(len(lst_tree))
    return lst_tree

#Conclusioens de cada conjunto de datos
val_cols(arbol) ,#allOk len 10 pd.DataFrame(val_cols(arbol) ).sum() | allSamples = 153037
''' * Se observa que el ultimo csv tiene un formato diferente, por el momento lo desprecie y cambie todos los 
        archivos de esa fecha a la carpeta especialcase
    * Longitud 10
'''
val_cols(precios) #allOk len 10 pd.DataFrame(val_cols(precios) ).sum() | allSamples = 1848292
val_cols(productos)  #allOk, len 10 pd.DataFrame(val_cols(productos) ).sum() | allSamples =  448463
val_cols(tiendas)  #allOk, len 10, pd.DataFrame(val_cols(tiendas) ).sum() | allSamples = 12182
val_cols(zonasgeo) #No lee headers, agregarselos en el df, len 10, pd.DataFrame(val_cols(zonasgeo) ).sum() | allSamples = 

'''
Hasta aqui, son 10 csv/df con mismas columnas , se concatenaran axis= 0 
'''
############################Concatenar df del mismo conjunto
def concatenar(nameListSet):
    n=0
    path1 = path_dp + nameListSet[n]
    df_1 = pd.read_csv(path1) 
    path2 = path_dp + nameListSet[n + 1 ]
    df_2 = pd.read_csv(path2) 
    df_12n = pd.concat([df_1, df_2], axis=0)

    for n in range(2,len(nameListSet)):
        path_n =  path_dp + nameListSet[n]
        df_n = pd.read_csv(path_n) 
        df_12n = pd.concat([df_12n, df_n], axis=0)
    
    df_12n.reset_index(inplace=True, drop=True)

    if 'Unnamed: 0' in set(df_12n.columns.to_list()):
        df_12n.drop(columns='Unnamed: 0', inplace=True)

    return df_12n

AllTrees = concatenar(arbol) #153037 rows x 4 columns --> si coinciden :) 
AllPrices = concatenar(precios) #[1848292 rows x 7 columns] --> si coinciden :) 
AllProducts = concatenar(productos) #[448463 rows x 7 columns] --> si coinciden :) 
AllTiendas = concatenar(tiendas) #[12182 rows x 11 columns] --> si coinciden :) 

AllTrees.to_csv('AllTrees.csv')
AllPrices.to_csv('AllPrices.csv')
AllProducts.to_csv('AllProducts.csv')
AllTiendas.to_csv('AllTiendas.csv')


#############################Ver que onda con zonas geo

# lo hice mal -.- , entonces lo voy a arreglar 
 


path1 = "C:/Users/Maria Luisa/OneDrive/Documentos/MasterDataScience/BDRelacionales/Datasets/profeco"
cont1 = os.listdir(path1) #12 diferent folders
cont1.remove('scripts') #despreciamos scripts 
cont1.remove('data20220913')

lstZones = []
for cont1_i in range(0 , len(cont1)):

    path2 = path1 + '/' + cont1[cont1_i]
    cont2 = os.listdir(path2)  #todas las carpetas que estan en la data2020____
   
    zonasgeo=[]
    for i in range(0, len(cont2)):
        item = cont2[i]
        if item.endswith('geograficas'):
            zonasgeo.append(item)
        else:
            pass
    lstZones.append(zonasgeo)
lstZones1 = [item for sublist in lstZones for item in sublist]
 

def val_cols_zonas(arregloConPaths):
     
    lst_ = []
    for i in range(0, len(arregloConPaths)):
        
        dframe = path2 + '/' + arregloConPaths[i]
        colnames, dim1, dim2  = pd.read_csv(dframe, names= ['id_zona', 'zonaGeografica']).columns.to_list() , pd.read_csv(dframe).shape[0], pd.read_csv(dframe).shape[1]
        lst_.append([colnames, dim1, dim2 ])
        print([colnames, dim1, dim2 ])
    print(len(lst_),dframe)
    return lst_
val_cols_zonas(lstZones1) #allOk!! :D 

######validacion para ver si los df son iguales
def val_cols_zonas2(arregloConPaths):
     
    lst_ = []
    for i in range(0, len(arregloConPaths)):
        try:
            dframe_1 = path2 + '/' + arregloConPaths[i]
            df_z1 = pd.read_csv(dframe_1, names= ['id_zona', 'zonaGeografica'])

            dframe_2 = path2 + '/' + arregloConPaths[i +1 ]
            df_z2 = pd.read_csv(dframe_2, names= ['id_zona', 'zonaGeografica'])

            if dframe_1 == dframe_2:
                lst_.append([i, i + 1 ])
        except:
            print('nok')

    return  lst_
val_cols_zonas2(lstZones1) 

'''
efectivamente si son iguales entonces , solo necesito una tabla! :D 

'''

dframe_1 = path2 + '/' + lstZones1[2]
df_z1 = pd.read_csv(dframe_1, names= ['id_zona', 'zonaGeografica'],sep= '|')
#df_z1.to_csv('zonasGeograficas.csv')

'''Para git 
TENGO QUE ESTAR EN UNA CONSOLA DE POWERSHELL 
git status
git add .
git commit -m "Cambios en redaccion 3 "
to files too large : git lfs migrate import --include="*.csv" (100)  --- 100.00 MB
git push origin main

 '''