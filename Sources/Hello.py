print("Jelou")
print("Programa para DDBD v1.0")

import numpy as np
from numpy.ma import array
import pandas as pd
from pandas.core.frame import DataFrame

#Materiales
fc=210                 #kgf/SCM2        f'c del concreto
fy=4200                #kgf/SCM2        Fy del acero
fu=6330                #kgf/SCM2        Fu del acero
Ec=15000*np.sqrt(fc)   #kgf/SCM2        Módulo de elasticidad del concreto
Es=2*10^6              #kgf/SCM2        Módulo de elasticidad del acero
λc =2.4                #tnf/m3         Peso especifico del concreto

#Secciones
#print("SECCIONES:")
##Columnas
dataC = "Sources\Secciones\Columnas.csv"
C=pd.read_csv(dataC)
#print(C)

##Vigas (Beam)
daSCM = "Sources\Secciones\Vigas.csv"
B=pd.read_csv(daSCM)
#print(B)

##Muros (Wall)
dataW = "Sources\Secciones\Muros.csv"
W=pd.read_csv(dataW)
#print(W)

##Losas
dataL = "Sources\Secciones\Losas.csv"
L=pd.read_csv(dataL)
#print(L)


#Elementos
#print("ELEMENTOS:")
##Columnas
dataCe = "Sources\Elementos\Columnas.csv"
Ce=pd.read_csv(dataCe)
#print(Ce)

##Vigas
daSCMeX = "Sources\Elementos\Vigas X.csv"
BeX=pd.read_csv(daSCMeX)
#print(BeX)

daSCMeY = "Sources\Elementos\Vigas Y.csv"
BeY=pd.read_csv(daSCMeY)
#print(BeY)

##Muros
dataWeX = "Sources\Elementos\Muros X.csv"
WeX=pd.read_csv(dataWeX)
#print(WeX)

dataWeY = "Sources\Elementos\Muros Y.csv"
WeY=pd.read_csv(dataWeY,)
#print(WeY)

##Losas
dataLe = "Sources\Elementos\Losas.csv"
Le=pd.read_csv(dataLe)
#print(Le)



#Peso de la estructura
##PP Columnas
Ac=[]
for i in range(len(C.SECCION)):
    Ac.append([C.SECCION[i],C.ac_X[i]*C.bc_Y[i]])
Ac=pd.DataFrame(Ac)
Ac.columns=["SECCION","Ac"]

N=Ce.NIVEL.max() #Número de pisos
Pc=[]
for i in range(1,N+1) :
    for j in range(len(Ce.NIVEL)):
        PPc=0
        if Ce.NIVEL[j]==i:
            for k in range(len(Ac.SECCION)):
                if Ce.TIPO[j]==Ac.SECCION[k]:
                    PPc=PPc+Ac.Ac[k]*Ce.Hc[j]*Ce.CANTIDAD[j]*λc
            Pc.append([i,PPc,Ce.Hc[j]])
PPc=pd.DataFrame(Pc)
PPc.columns=["NIVEL","PPc","Hc"]
#print(PPc) #Peso Propio de Columnas


##PP Vigas/piso
PPbx=0
for i in range(len(BeX.TIPO)):
  for j in range(len(B.SECCION)):
      if BeX.TIPO[i]==B.SECCION[j]:
          PPbx=BeX.lb[i]*B.bb[j]*B.hb[j]*BeX.CANTIDAD[i]*λc+PPbx           
#print(PPbx) #Peso Propio de Vigas en X

PPby=0
for i in range(len(BeY.TIPO)):
  for j in range(len(B.SECCION)):
      if BeY.TIPO[i]==B.SECCION[j]:
          PPby=BeY.lb[i]*B.bb[j]*B.hb[j]*BeY.CANTIDAD[i]*λc+PPby           
#print(PPby) #Peso Propio de Vigas en Y

PPb=PPbx+PPby
#print(PPb) #Peso Propio de Vigas por piso

##PP Losas /piso
PPlosa=0
for i in range(len(Le.TIPO)):
  for j in range(len(L.SECCION)):
      if Le.TIPO[i]==L.SECCION[j]:
           PPlosa=Le.L_X[i]*Le.L_Y[i]*Le.CANTIDAD[i]*L.ql[j]+PPlosa
#print(PPlosa) #Peso Propio de Losas por piso


##PP Muros /piso
Aw=[]
for i in range(len(W.SECCION)):
    Aw.append([W.SECCION[i],W.tw[i]*W.Lw[i]])
Aw=pd.DataFrame(Aw)
Aw.columns=["SECCION","Aw"]

PPwx=0
for i in range(len(WeX.TIPO)):
  for j in range(len(Aw.SECCION)):
      if WeX.TIPO[i]==Aw.SECCION[j]:
          PPwx=Aw.Aw[j]*λc+PPwx
#print(PPwx) #Peso de muros en x /altura de piso

PPwy=0
for i in range(len(WeY.TIPO)):
  for j in range(len(Aw.SECCION)):
      if WeY.TIPO[i]==Aw.SECCION[j]:
          PPwy=Aw.Aw[j]*λc+PPwy
#print(PPwy) #Peso de muros en y /altura de piso

PPw=PPwx+PPwy
#print(PPw) #Peso Propio de muros /altura de piso

##Peso Propio de la Estructura
N=len(PPc.index) #Número de pisos
PPi=[[0,0,0]]
Hi=0
for i in range(0,N):
    if i==N-1:
        Hi=Hi+PPc.Hc[i]
        PPi.append([PPc.NIVEL[i],(PPc.PPc[i]/2)+PPb+PPlosa+PPw*(PPc.Hc[i]/2),Hi])
    else:
        Hi=Hi+PPc.Hc[i]
        PPi.append([PPc.NIVEL[i],(PPc.PPc[i]/2+PPc.PPc[i+1]/2)+PPb+PPlosa+PPw*(PPc.Hc[i]/2+PPc.Hc[i+1]/2),Hi])
PP=pd.DataFrame(PPi)
PP.columns=["NIVEL","PP","Hi"]
#print(PP) #Peso Propio de la Estructura


##CARGAS VIVA Y SOBRECARGA MUERTA

dataCS1 = "Sources\Cargas\Cargas Viva.csv"
dataCS2= "Sources\Cargas\Carga Muerta.csv"
CS1=pd.read_csv(dataCS1)
CS2=pd.read_csv(dataCS2)
cvtl=0
scmtl=0

CV=[[0,0]]
for i in range(len(CS1.TIPO)):
    for j in range(len(Le.TIPO)):
      if CS1.TIPO[i]==Le.TIPO[j]:
           cvtl=CS1.CV[i]*Le.L_X[j]*Le.L_Y[j]*Le.CANTIDAD[j]+cvtl
           CV.append([CS1.NIVEL[i],CS1.CV[i]*Le.L_X[j]*Le.L_Y[j]*Le.CANTIDAD[j]])
CVt=pd.DataFrame(CV)
CVt.columns=["Nivel","CV"]

SCM=[[0,0]]
for i in range(len(CS2.TIPO)):
  for j in range(len(Le.TIPO)):
      if CS2.TIPO[i]==Le.TIPO[j]:
           scmtl=CS2.SCM[i]*Le.L_X[j]*Le.L_Y[j]*Le.CANTIDAD[j]+scmtl
           SCM.append([CS2.NIVEL[i],CS2.SCM[i]*Le.L_X[j]*Le.L_Y[j]*Le.CANTIDAD[j]])
SCMt=pd.DataFrame(SCM) 
SCMt.columns=["Nivel","SCM"]

#print(CVt)
#print(SCMt)


#PESO TOTAL
print("Peso Total de la Estructura: PT=CM+CV")
NIVEL=map(str,PP.NIVEL)
PPi=PP.PP
SCMi=SCMt.SCM
CVi=CVt.CV
PTi=PPi+SCMi+CVi
Hi=PP.Hi
PT=pd.DataFrame([NIVEL,PTi,Hi]).T
PT.columns=["NIVEL","PT","Hi"]
print(PT)

#PESO SISMICO
print("Peso Sísmico de la Estructura: PS=CM+25%CV")
NIVEL=map(str,PP.NIVEL)
PSi=PPi+SCMi+0.25*CVi
PS=pd.DataFrame([NIVEL,PSi,Hi]).T
PS.columns=["NIVEL","PS","Hi"]
print(PS)

#MASA SISMICA
print("Masa de la Estructura:")
NIVEL=map(str,PP.NIVEL)
Mi=(PPi+SCMi+0.25*CVi)/9.81
M=pd.DataFrame([NIVEL,Mi,Hi]).T
M.columns=["NIVEL","M","Hi"]
print(M)

#CÁLCULO DE ALTURA DE INFLEXIÓN
β=0.4         #Vframes para Vb=1

