import pandas as pd 
import numpy as np
import os

path1 = "C:/Users/Maria Luisa/OneDrive/Documentos/MasterDataScience/BDRelacionales/Datasets/profeco"
cont1 = os.listdir(path1) #12 diferent folders

#numCont1=1 # done:[0,1 ] 
for i in range(2, len(cont1)): 
    numCont1 = i
    path2 = path1 + '/' + cont1[numCont1]   
    cont2 = os.listdir(path2) #138 diferent 

    arbol = []
    precios = []
    productos = []
    tiendas = []
    other = []
    zonasgeo=[]
    checkpoint = []

    for i in range(0, len(cont2)):
        item = cont2[i]
        if item.endswith('arbol'):
            arbol.append(item)
        elif item.endswith('precios'):
            precios.append(item)
        elif item.endswith('productos'):
            productos.append(item)
        elif item.endswith('tiendas'):
            tiendas.append(item)
        elif item.endswith('geograficas'):
            zonasgeo.append(item)
        elif item.endswith('point'):
            checkpoint.append(item)
        else:
            other.append(item)

    lenArb, lenPre, lenProd, lenTien, lenGeo, lenPoint = len(arbol), len(precios), len(productos), len(tiendas), len(zonasgeo), len(checkpoint)
    allItemsLists = sum([lenArb, lenPre, lenProd, lenTien, lenGeo, lenPoint])
    fileLen = len(cont2)
    itemDif = fileLen - allItemsLists

    #Por lista de tipo de sufijo, organizo

    ###############Arbol
    def arboles():

        '''
        Tiene la siguiente estructura:
        # codigo                descripcion
        0                     # ALIMENTOS                        NaN
        1    # ACEITES, GRASAS Y VINAGRES                        NaN
        2              # ACEITES Y GRASAS                        NaN

        Por el momento , no me importa lo que contienen solo me importa concatenarlos, 
        despues los agrupo conforme a categoria, producto y despues producto con su codigo y descripcion
        '''


        n = 0
        df1 = pd.read_csv( path2 + '/' + arbol[n] , sep = '|' )
        df1['tipo_arbol'] = arbol[n]

        df2 = pd.read_csv(path2 + '/' + arbol[n+1]  , sep = '|' )
        df2['tipo_arbol'] = arbol[n+1]

        df3 = pd.concat([df1, df2], axis=0) 

        for i in range(2, len(arbol)):
            df4 = pd.read_csv(path2 + '/' + arbol[i]  , sep = '|' )
            df4['tipo_arbol'] = arbol[i]
            df3 = pd.concat([df3, df4], axis=0) 

        df3.reset_index(inplace=True, drop=True) 
        df3['folder_id'] = cont1[numCont1]

        #
        return df3

    ###############Precios
    def Preciosdef():

        n = 0
        df4 = pd.read_csv(path2 +'/' + precios[n], sep='|')
        df4['profeco_precios_id'] = precios[n]
        df5 = pd.read_csv(path2 +'/' + precios[n+1], sep='|')
        df5['profeco_precios_id'] = precios[n+1]
        df6 = pd.concat([df4, df5], axis=0)

        for i in range(2, len(precios)):
                df7 = pd.read_csv(path2 + '/' + precios[i]  , sep = '|' )
                df7['profeco_precios_id'] = precios[i]
                df6 = pd.concat([df6, df7], axis=0) 

        df6.reset_index(inplace=True, drop=True) 
        df6['folder_id'] = cont1[numCont1]

        
        return df6

    ###############productos
    def Prodcutosdef():

        n = 0
        df8 = pd.read_csv(path2 +'/' + productos[n], sep='|')
        df8['profeco_productos_id'] = productos[n]
        df9 = pd.read_csv(path2 +'/' + productos[n+1], sep='|')
        df9['profeco_productos_id'] = productos[n+1]
        df10 = pd.concat([df8, df9], axis=0)

        for i in range(2, len(productos)):
                df11 = pd.read_csv(path2 + '/' + productos[i]  , sep = '|' )
                df11['profeco_productos_id'] = productos[i]
                df10 = pd.concat([df10, df11], axis=0) 

        df10.reset_index(inplace=True, drop=True) 

        df10['folder_id'] = cont1[numCont1]
        
        return df10

    ###############tiendas
    def tiendotas():
        n = 0
        df12 = pd.read_csv(path2 +'/' + tiendas[n], sep='|')
        df12['profeco_tiendas_id'] = tiendas[n]
        df13 = pd.read_csv(path2 +'/' + tiendas[n+1], sep='|')
        df13['profeco_tiendas_id'] = tiendas[n+1]
        df14 = pd.concat([df12, df13], axis=0)

        for i in range(2, len(tiendas)):
                df15 = pd.read_csv(path2 + '/' + tiendas[i]  , sep = '|' )
                df15['profeco_tiendas_id'] = tiendas[i]
                df14 = pd.concat([df14, df15], axis=0) 

        df14.reset_index(inplace=True, drop=True) 
        df14['folder_id'] = cont1[numCont1]
        return df14

    ###############zonasgeograficas
    def zonasgeograficas():
        df16 = pd.read_csv(path2 +'/' + zonasgeo[0], sep='|')
        df16['folder_id'] = cont1[numCont1]
        return df16


    ###############
    def checkpoint_1():
        df17 = pd.read_csv(path2 +'/' + checkpoint[0], sep='|')
        df17['folder_id'] = cont1[numCont1]
        return df17


    #################################################Exporto resultados a csv
    df_3 = arboles()
    df_3.to_csv(cont1[numCont1]+'arbol.csv')

    df_6 = Preciosdef()
    df_6.to_csv(cont1[numCont1]+'precios.csv')

    df_10 = Prodcutosdef()
    df_10.to_csv(cont1[numCont1]+'productos.csv')

    df_14= tiendotas()
    df_14.to_csv(cont1[numCont1]+'tiendas.csv')

    df_16 = zonasgeograficas()
    df_16.to_csv(cont1[numCont1]+'zonasgeograficas.csv')

    df_17 = checkpoint_1()
    df_17.to_csv(cont1[numCont1]+'checkpoint.csv')


#ctrl + shift + P : reload window