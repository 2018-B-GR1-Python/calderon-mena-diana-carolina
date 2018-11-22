# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:47:04 2018

@author: Carolina Calderon
"""

import pandas as pd
import os

directorio_pickle ="C://Users//Carolina//Documents//GitHub//calderon-mena-diana-carolina//03-Spyder//data//artwork_data_frame.pickle"

data_frame_guardado = pd.read_pickle(directorio_pickle)
artistas_df_duplicados = data_frame_guardado["artist"]

artistas_df_sin_duplicado = pd.unique(artistas_df_duplicados)
artistas_df_sin_duplicado
len(artistas_df_sin_duplicado)

artistas_filtro = data_frame_guardado["artist"] == 'Bacon, Francis'
artistas_filtro.value_counts()

serie_artistas = data_frame_guardado['artist'].value_counts()
serie_artistas['Bacon, Francis']
df_2 = data_frame_guardado[artistas_filtro] 
len(df_2)