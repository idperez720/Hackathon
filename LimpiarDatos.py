# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 03:41:09 2021

@author: pc
"""

import numpy as np
import pandas as pd

#l = longitud
#k = Latitud
#Margen = 0.02783796149


"""Desarrollo de codigo"""

path = "C:/Users/pc/OneDrive - Universidad de los andes/Septimo semestre/Hackathon/Datos/DatosEneroPrincipal.csv"
pathDias = "C:/Users/pc/OneDrive - Universidad de los andes/Septimo semestre/Hackathon/Datos/DatosPorDias.csv"
pathFinal = "C:/Users/pc/OneDrive - Universidad de los andes/Septimo semestre/Hackathon/Datos/DatosFinales.csv"
pathSegundos = "C:/Users/pc/OneDrive - Universidad de los andes/Septimo semestre/Hackathon/Datos/segundos.csv"

#Asi se lee.
segundos = pd.read_csv(pathSegundos)

datosDias = pd.read_csv(pathDias)

datos = pd.read_csv(path,sep=',')

print(datos['IDCIUDAD'].value_counts())

indexN = datos[datos['IDCIUDAD'] != 11001].index

datos.drop(indexN,inplace=True)

datos = datos.drop(["USUARIO","FECHALEGIBLE"],axis=1)
segundos.drop(indexN,inplace=True)
datosDias = datosDias.drop(["Unnamed: 3","Unnamed: 4","Unnamed: 5","Unnamed: 6"], axis = 1)

datosDias.drop(indexN,inplace=True)

datos["Dia"] = datosDias["Dia"]

datos["tiempo"] = segundos["Hora"]

datos = datos.drop("IDCIUDAD",axis=1)

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
datosDia = datos[["Dia"]]
DiasEncoder = encoder.fit_transform(datosDia)
DiasArray = DiasEncoder.toarray()

datos['Domingo'] = DiasArray[:,0]

datos['Jueves'] = DiasArray[:,1]
datos['Lunes'] = DiasArray[:,2]
datos['martes'] = DiasArray[:,3]
datos['miércoles'] = DiasArray[:,4]
datos['sábado'] = DiasArray[:,5]
datos['viernes'] = DiasArray[:,6]

datos.to_csv("C:/Users/pc/Documents/DatosFinales.csv",index = False)


#Ahora se toman los datos que nos sirven.
def distancia(centro,l,k,margen = 0.02783796149):
    punto = np.array([l,k])
    dist = np.linalg.norm(centro-punto)
    Esta = 0
    if dist < margen:
        Esta = 1
    return Esta


margen = 0.02783796149

#Centros:
centro1 = np.array([4.611507,-74.088609]) #Cerca de la universidad
centro2 = np.array([4.703968,-74.042630]) #Centro norte 1.
centro3 = np.array([4.696387,-74.084632]) #Centro occidente.
centro4 = np.array([4.629632,-74.136629]) #Centro Sur.
centro5 = np.array([4.736374,-74.059912]) #Centro norte 2 - Colina.


#Puntos de los datos ya organizados:
puntos = np.array([datos["LATITUD"],datos["LONGITUD"]]).T

#Distancia con respecto a cada centro:
distCentro1 = np.linalg.norm(centro1 - puntos,axis=1)
distCentro2 = np.linalg.norm(centro2 - puntos,axis=1)
distCentro3 = np.linalg.norm(centro3 - puntos,axis=1)
distCentro4 = np.linalg.norm(centro4 - puntos,axis=1)
distCentro5 = np.linalg.norm(centro5 - puntos,axis=1)


indexCentro1 = np.where(distCentro1 > margen)
indexCentro2 = np.where(distCentro2 > margen)
indexCentro3 = np.where(distCentro3 > margen)
indexCentro4 = np.where(distCentro4 > margen)
indexCentro5 = np.where(distCentro5 > margen)

indexCentro1 = indexCentro1[0]
indexCentro2 = indexCentro2[0]
indexCentro3 = indexCentro3[0]
indexCentro4 = indexCentro4[0]
indexCentro5 = indexCentro5[0]

#Datos de cada centro.

datosArray = datos.to_numpy()

datosCentro1 = np.delete(datosArray,indexCentro1,axis=0)
datosCentro2 = np.delete(datosArray,indexCentro2,axis=0)
datosCentro3 = np.delete(datosArray,indexCentro3,axis=0)
datosCentro4 = np.delete(datosArray,indexCentro4,axis=0)
datosCentro5 = np.delete(datosArray,indexCentro5,axis=0)

def cuantos(intervaloTiempo,datos):
    intervaloTiempo = intervaloTiempo * 60
    cantidadServicios=np.array([])
    dias=np.array([])
    i=1
    c=0
    k=0
    H = np.shape(datos)
    while(k<H[0]):
    
        if(datos[k,3]<i*intervaloTiempo):    
            c=c+1

        if(datos[k,3] >i*intervaloTiempo):
            i=i+1
            np.append(cantidadServicios,c)
            np.append(dias,datos[k,2])
            c=0

        if(i*intervaloTiempo>86400):
            i=1
        k=k
    return cantidadServicios,dias

cosa1,cosa2 = cuantos(10,datosCentro1)


    
    



