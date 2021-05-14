print("Jelou")
print("Programa para DDBD v1.0")

import numpy as np
import pandas as pd

#Materiales
fc=210                 #kgf/cm2        f'c del concreto
fy=4200                #kgf/cm2        Fy del acero
fu=6330                #kgf/cm2        Fu del acero
Ec=15000*np.sqrt(fc)   #kgf/cm2        Módulo de elasticidad del concreto
Es=2*10^6              #kgf/cm2        Módulo de elasticidad del acero
λc =2.4                #tnf/m3         Peso especifico del concreto

#Secciones
print("SECCIONES:")
##Columnas
    dataC = "Sources\Secciones\Columnas.csv"
    C=pd.read_csv(dataC,header=0)

    print(C)

##Vigas (Beam)
    dataB = "Sources\Secciones\Vigas.csv"
    B=pd.read_csv(dataB,header=0)

    print(B)

##Muros (Wall)
    dataW = "Sources\Secciones\Muros.csv"
    W=pd.read_csv(dataW,header=0)

    print(W)

##Losas
    dataL = "Sources\Secciones\Losas.csv"
    L=pd.read_csv(dataL,header=0)

    print(L)


#Elementos
print("ELEMENTOS:")
##Columnas
    dataCe = "Sources\Elementos\Columnas.csv"
    Ce=pd.read_csv(dataCe,header=0)

    print(Ce)

##Vigas
    dataBeX = "Sources\Elementos\Vigas X.csv"
    BeX=pd.read_csv(dataBeX,header=0)

    print(BeX)

    dataBeY = "Sources\Elementos\Vigas Y.csv"
    BeY=pd.read_csv(dataBeY,header=0)

    print(BeY)

##Muros
    dataWeX = "Sources\Elementos\Muros X.csv"
    WeX=pd.read_csv(dataWeX,header=0)

    print(WeX)

    dataWeY = "Sources\Elementos\Muros Y.csv"
    WeY=pd.read_csv(dataWeY,header=0,)

    print(WeY)

##Losas
    dataLe = "Sources\Elementos\Losas.csv"
    Le=pd.read_csv(dataLe,header=0)

    print(Le)



#Peso de la estructura
##Vigas
nWvig=len(range(BeX.TIPO))

Wvig=0
for i in nWvig:
    #le pongo -1 ya que el valor inicial de i es 1 y los dataframe de pandas empienzan con 0
    Wvig=BeX.lb[i]*BeX.CANTIDAD[i]*BeX.nbe[i]+Wvig

Wvigt=BeX.lb[0]*BeX.CANTIDAD[0]*BeX.nbe[0]
print(Wvig)
print(Wvigt)
#falta hacer la prueba... ya, no se pone un end for? o next? no, solo basta con la sangria
#No sale XD
#no veo el terminal, ya lo vi xd, estaba en otra pestaña
#jajaj, no quiere leer la linea 18 :o



##Columnas
#PPc=  
#nC=len(range(C.SECCION))
