import pandas as pd
import EmDAT_Duration as DUR
import json as js
import ast
import numpy as np
from shapely.geometry import Point, MultiPoint
import geopandas

# make A CSV of each location in the geocoded EM-DAT document. The CSV of a locaton contains the event recorded 
# at that location. A second CSV is also made where all the locations are combined. For each location the number of events
# (frequency), the most common disaster subtype, the most common start month, the average duration, the average magnitude and 
# the average number of people is given. 
def CSV_van_elke_locatie(locaties,df):
    df_frequentie = pd.DataFrame()
    for l in locaties:
        idx = locaties.index(l)
        rampen = pd.DataFrame()
        frequentie = 0
        lat = locaties[idx]['lat']
        lon = locaties[idx]['lon']
        for index, row in df.iterrows():
            if str(l) in list(row):
                frequentie += 1
                Duration = pd.Series([DUR.calculate_duration(row)], index = ['Duration'])
                ramp = pd.Series(row[:47])
                ramp = pd.concat([ramp, Duration])
                rampen = pd.concat([rampen, ramp.to_frame().T], ignore_index = True)
        most_common_disaster_subtype = rampen['Disaster Subtype'].mode()[0]
        most_common_month = rampen['Start Month'].mode()[0]
        Average_duration = rampen['Duration'].mean()
        Average_magnitude = rampen['Magnitude'].mean()
        Average_affected = rampen['Total Affected'].mean()
        rampen.to_csv('/Users/theovandamme/Desktop/bachelorproef/Dataset_final/locatie' + str(idx) + '.csv', sep = ';')
        Series_frequentie = pd.Series([l,frequentie, lat, lon, most_common_disaster_subtype, most_common_month, Average_duration, Average_magnitude, Average_affected])
        df_frequentie = pd.concat([df_frequentie, Series_frequentie.to_frame().T], ignore_index= True)
    df_frequentie.columns = ['locatie', 'frequentie', 'lat', 'lon', 'most_common_disaster_subtype', 'most_common_month', 'Average_duration', 'Average_magnitude', 'Average_affected']
    df_frequentie.to_csv('/Users/theovandamme/Desktop/bachelorproef/frequentie_Dataset_final.csv', sep= ';')

# makes a CSV of the events having at least one location inside a given study area. A shapefile is also made of all the locations 
# where an event happened inside this study area. 
def CSV_van_events_binnen_Studiegebied(x_max, x_min, y_max, y_min, df, name_ROI):
    Events = pd.DataFrame()
    gdf = geopandas.GeoDataFrame()
    for index, row in df.iterrows():
        Event_in_ROI = False
        locaties = []
        for x in (row)[47:]:
            if  pd.isna(x) == False and x != "{'lat': nan, 'lon': nan}":
                dict = ast.literal_eval(x)
                lat = dict['lat']
                lon = dict['lon']
                if lon < x_max and lon > x_min and lat < y_max and lat > y_min:
                    Event_in_ROI = True
                    locaties.append((lon, lat))
        if Event_in_ROI == True:
            Events = pd.concat([Events, row[:47].to_frame().T], ignore_index = True)
            print(locaties)
            rij = pd.Series(row[:47]).to_frame().T
            geom = [MultiPoint(locaties)]
            geoseries  = geopandas.GeoDataFrame(rij, geometry = geom, crs = 'EPSG: 4326')
            gdf = pd.concat([gdf, geoseries],ignore_index = True)
            gdf.set_crs( epsg = '4326')
    gdf.to_csv('/Users/theovandamme/Desktop/bachelorproef/' + name_ROI + '.csv', sep= ';')     
    gdf.to_file('/Users/theovandamme/Desktop/bachelorproef/' + name_ROI ,crs= 'EPSG: 4326')  

