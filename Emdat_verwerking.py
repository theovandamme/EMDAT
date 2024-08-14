import pandas as pd
import Emdat_CSV_of_each_location as CSV_loc
import json as js
import ast
import numpy as np

filename = '/Users/theovandamme/Library/CloudStorage/OneDrive-VrijeUniversiteitBrussel/Bachelorproef/EM-DAT/EMDAT_Dataset_Final.csv'
df = pd.read_csv(filename)
locaties = []
lijst = []
for index, row in df.iterrows():
    #creation of a list with all the locations present in the dataset
    for x in (row)[47:]:
        if  pd.isna(x) == False and x not in lijst and x != "{'lat': nan, 'lon': nan}":
            lijst.append(x)
            #print(type(test))
            dict = ast.literal_eval(x)
            locaties.append(dict)
test = CSV_loc.CSV_van_events_binnen_Studiegebied(29.448, 28.987, -3.2, -3.5, df, 'Tanganyika')    
#CSV_loc.CSV_van_elke_locatie(locaties, df)

