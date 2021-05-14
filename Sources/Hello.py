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
B=pandas.read_csv(dataB,header=0)

print(B)

##Muros (Wall)
dataW = "Sources\Secciones\Muros.csv"
W=pandas.read_csv(dataW,header=0)

print(W)

##Losas
dataL = "Sources\Secciones\Losas.csv"
L=pandas.read_csv(dataL,header=0)

print(L)


#Elementos
print("ELEMENTOS:")
##Columnas
dataCe = "Sources\Elementos\Columnas.csv"
Ce=pandas.read_csv(dataCe,header=0)

print(Ce)

##Vigas
dataBeX = "Sources\Elementos\Vigas X.csv"
BeX=pandas.read_csv(dataBeX,header=0)

print(BeX)

dataBeY = "Sources\Elementos\Vigas Y.csv"
BeY=pandas.read_csv(dataBeY,header=0)

print(BeY)

##Muros
dataWeX = "Sources\Elementos\Muros X.csv"
WeX=pandas.read_csv(dataWeX,header=0)

print(WeX)

dataWeY = "Sources\Elementos\Muros Y.csv"
WeY=pandas.read_csv(dataWeY,header=0,)

print(WeY)

##Losas
dataLe = "Sources\Elementos\Losas.csv"
Le=pandas.read_csv(dataLe,header=0)

print(Le)

print(Ce[0])

#Peso de la estructura
##Vigas
Wvig=df.BeX

##Columnas
#PPc=
print(Ce[0])
