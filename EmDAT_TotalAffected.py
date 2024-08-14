import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def Total_affected_graph(CSV_doc, loc_idx):
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(CSV_doc, sep = ';')
    column = Df['Total Affected']
    Total_affected = column.dropna()
    plt.title('total amount of people affected by floods for location '+ str(loc_idx))
    plt.ylabel("Frequency")
    plt.xlabel('amount of people')
    plt.hist(Total_affected, edgecolor = 'black')
    plt.show()
    #plt.savefig('Magnitude_locatie' + str(loc_idx)+ '.png')


def Average_affected_graph(CSV_doc):
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(CSV_doc, sep = ';')
    column = Df['Average_affected']
    Average_affected = column.dropna()
    plt.title('Average amount of people affected by floods for locations in dataset')
    plt.ylabel("Frequency")
    plt.xlabel('amount of people')
    plt.hist(Average_affected, edgecolor = 'black')
    plt.show()
    #plt.savefig('Average_magnitude' + '.png')