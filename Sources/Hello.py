print("Jelou")
print("Programa para DDBD v1.0")

import numpy as np
#Materiales
fc=210                 #kgf/cm2        f'c del concreto
fy=4200                #kgf/cm2        Fy del acero
fu=6330                #kgf/cm2        Fu del acero
Ec=15000*np.sqrt(fc)   #kgf/cm2        Módulo de elasticidad del concreto
Es=2*10^6              #kgf/cm2        Módulo de elasticidad del acero
λc =2.4                #tnf/m3         Peso especifico del concreto



#Secciones
##Columnas
ac=0.5                  #m         Ancho de columna (Long. en X)
bc=0.5                  #m         Largo de columna (Long. en Y)
C1=[ac,bc]


##Vigas (Beam)
bb=0.25             #m         Ancho de viga
hb=0.4              #m         Peralte de viga
V1=[bb,hb]

##Muros (Wall)
tw=0.25             #m         Espesor de muro
Lw=5                #m         Largo de muro
W1=[tw,Lw]

##Losas
hl=0.20             #m         Espesor de losa aligerada
ql=300              #kgf/m2    Peso de losa aligerada /m2
L1=[hl,ql]

print(C1)



