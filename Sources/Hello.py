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
C=pd.read_csv(dataC)

print(C)

##Vigas (Beam)
dataB = "Sources\Secciones\Vigas.csv"
B=pd.read_csv(dataB)

print(B)

##Muros (Wall)
dataW = "Sources\Secciones\Muros.csv"
W=pd.read_csv(dataW)

print(W)

##Losas
dataL = "Sources\Secciones\Losas.csv"
L=pd.read_csv(dataL)

print(L)


#Elementos
print("ELEMENTOS:")
##Columnas
dataCe = "Sources\Elementos\Columnas.csv"
Ce=pd.read_csv(dataCe)

print(Ce)

##Vigas
dataBeX = "Sources\Elementos\Vigas X.csv"
BeX=pd.read_csv(dataBeX)

print(BeX)

dataBeY = "Sources\Elementos\Vigas Y.csv"
BeY=pd.read_csv(dataBeY)

print(BeY)

##Muros
dataWeX = "Sources\Elementos\Muros X.csv"
WeX=pd.read_csv(dataWeX)

print(WeX)

dataWeY = "Sources\Elementos\Muros Y.csv"
WeY=pd.read_csv(dataWeY,)

print(WeY)

##Losas
dataLe = "Sources\Elementos\Losas.csv"
Le=pd.read_csv(dataLe)

print(Le)



#Peso de la estructura
##Vigas
Wvigx=0
for i in range(len(BeX.TIPO)):
  for j in range(len(B.SECCION)):
      if BeX.TIPO[i]==B.SECCION[j]:
          Wvigx=BeX.lb[i]*B.bb[j]*B.hb[j]*BeX.CANTIDAD[i]*λc+Wvigx           
print(Wvigx)

# Wvigy=0
# for i in range(len(BeY.TIPO)):
#     Wvigy=BeY.lb[i]*BeY.CANTIDAD[i]+Wvigy
# print(Wvigy)


##Columnas
Ac=[]
for i in range(len(C.SECCION)):
    Ac.append([C.SECCION[i],C.ac_X[i]*C.bc_Y[i]])
Ac=pd.DataFrame(Ac)
print(Ac)

#PPc=[]
#for i in range(len(Ce.TIPO)):
   # Ac.append([C.SECCION[i],C.ac_X[i]*C.bc_Y[i]])
#print(PPc)



##Muros
#Wmurx=0
#for i in range(len(WeX.TIPO)):
#    Wmurx=WeX.lb[i]*WeX.CANTIDAD[i]*WeX.nbe[i]+Wvigx
#print(Wvigx)