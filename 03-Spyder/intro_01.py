# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:34:33 2018

@author: Carolina Calderon
"""

import numpy as np
import pandas as pd

arreglo_randomico = np.random.rand(3)
arreglo_dos_dimensiones = np.random.rand(2,3)
 
#pandas series
serie_arreglo = pd.Series(arreglo_randomico)
serie_arreglo_v2 = pd.Series(arreglo_randomico, index = ["Uno", "Dos", "Tres"])

print(serie_arreglo[0])
print(serie_arreglo_v2[0])

serie_arreglo.index

#dataframes

data_frame = pd.DataFrame(arreglo_dos_dimensiones)

data_frame[0][0]
data_frame.columns = ["Uno", "Dos", "Tres"]
data_frame["Uno"][0]
