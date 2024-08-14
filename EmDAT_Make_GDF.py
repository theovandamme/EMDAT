import pandas as pd
import geopandas
import matplotlib.pyplot as plt

# makes a shapefile of the frequency_CSV calculated in EMDAT_CSV_of_each_location
def make_geodataframe(CSV_frequenties):
    df = pd.read_csv(CSV_frequenties, sep = ';')
    gdf = geopandas.GeoDataFrame(df , geometry= geopandas.points_from_xy(df.lon, df.lat ), crs= 'EPSG: 4326' )
    gdf.to_file('/Users/theovandamme/Desktop/bachelorproef',crs= 'EPSG: 4326')
    return gdf



make_geodataframe('/Users/theovandamme/Desktop/bachelorproef/frequentie_Dataset_final.csv')