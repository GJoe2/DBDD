print("hello")
print("Somos el equipo maravilla buena onda")

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
ac=[]                  #m         Ancho de columna (Longitud en el Eje X)
ac.append(0.5)
ac.append(0.5)
bc=[]              #m         Largo de columna (Longitud en el Eje Y)
bc.append(0.5)

##Vigas (Beam)
#bb(1)=0.25             #m         Ancho de viga (Longitud en el Eje X o Y)
#hb(1)=0.4              #m         Peralte de viga (Longitud en el Eje Z)

##Muros (Wall)
#tw(1)=0.25             #m         Espesor de muro
#Lw(1)=5                #m         Largo de muro

##Losas
#hl(1)=0.20             #m         Espesor de losa aligerada
#qp(1)=300              #kgf/m2    Peso de losa aligerada /m2


print(ac[1])



