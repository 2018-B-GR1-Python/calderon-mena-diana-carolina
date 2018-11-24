# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:27:59 2018

@author: Carolina Calderon
"""

import pandas as pd
import os

df = pd.read_pickle("C://Users//Carolina//Documents//GitHub//calderon-mena-diana-carolina//03-Spyder//data//artwork_data_frame.pickle")


# loc indices y nombres de columnas
df.loc[1035, 'artist']
df.iloc[0,0]

#iloc cuando el indice es basado en cero
df.iloc[0:]
df.iloc[0:2,0:2]

df.loc[1035, 'height']

df_width = df['width']
df_con_sort_values= df['width'].sort_values()
df_con_sort_head = df['width'].sort_values().head(100)

width_numeric = pd.to_numeric(df['width'], errors='coerce')
height_numeric = pd.to_numeric(df['height'], errors='coerce')

width_numeric * height_numeric


df.loc[:,'width'] = width_numeric
df.iloc[:,5] =height_numeric

area = df['width'] * df['height']

df = df.assign(area=area)

df['area'].sort_values().head(5)

df['area'].max()
id_max_area = df['area'].idxmax()

df['area'].sort_values(ascending=False).head(1)
df['area'].sort_values().head(1)


mayor_area = df.loc[id_max_area,:]


##agregar un nuevo resgistro
artwork = [09393, 'Black', 'Sun', 'Lienzo', 2009, 300,700,9999]

##definir columnas
columnas_art = list(df)
columnas_art.insert(0,'id')

nuevo_dato =  pd.Series(artwork, index=columnas_art)
df2 = df.append(nuevo_dato, ignore_index=True)

dfaux=pd.DataFrame(nuevo_dato).transpose();
df2=df.append(dfaux, sort=True)
