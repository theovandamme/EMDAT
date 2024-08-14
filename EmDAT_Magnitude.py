import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def Magnitude_graph(CSV_doc, loc_idx):
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(CSV_doc, sep = ';')
    column = Df['Magnitude']
    Magnitude = column.dropna()
    plt.title('Magnitude for location '+ str(loc_idx))
    plt.ylabel("Frequency")
    plt.xlabel('Area in km^2')
    plt.hist(Magnitude, edgecolor = 'black')
    plt.show()
    #plt.savefig('Magnitude_locatie' + str(loc_idx)+ '.png')


def Average_Magnitude_graph(CSV_doc):
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(CSV_doc, sep = ';')
    column = Df['Average_magnitude']
    Average_Magnitude = column.dropna()
    plt.title('Average Magnitude for locations in dataset')
    plt.ylabel("Frequency")
    plt.xlabel('Area in km^2')
    plt.hist(Average_Magnitude, edgecolor = 'black')
    plt.show()
    #plt.savefig('Average_magnitude' + '.png')