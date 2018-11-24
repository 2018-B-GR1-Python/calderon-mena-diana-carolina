# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:56:32 2018

@author: Carolina Calderon
"""

import pandas as pd
import os

CSV_PATH = "C://Users//Carolina//Documents//GitHub//calderon-mena-diana-carolina//03-Spyder//data//artwork_data.csv"

#leer archivos de texto csv jspn html
#leer archivos binarios
#leer relational database

data_frame_artwork = pd.read_csv(CSV_PATH, 
                                 index_col='id', 
                                 )

columnas_a_utilizar =  ['id','artist', 'title','medium', 'year','medium', 'height', 'width']

data_frame_artwork = pd.read_csv(CSV_PATH, index_col='id', 
                             low_memory=False, usecols =columnas_a_utilizar)



data_frame_artwork.shape

PATH_A_GUARDAR ="C://Users//Carolina//Documents//GitHub//calderon-mena-diana-carolina//03-Spyder//data//artwork_data_frame.pickle"
data_frame_artwork.to_pickle(PATH_A_GUARDAR)


