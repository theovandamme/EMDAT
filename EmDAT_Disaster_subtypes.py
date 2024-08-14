import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

def make_disaster_graph_per_location(CSV_doc, loc_idx):
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(CSV_doc, sep = ';')
    Dis_subtype = Df[Df.columns[8]]
    print(Dis_subtype)
    plt.hist(Dis_subtype)
    plt.title('Disaster subtypes for location '+ str(loc_idx))
    plt.ylabel("Frequency")
    plt.xlabel('Disaster subtype')
    plt.show()
    #plt.savefig('Disaster_subtype_hist_Locatie' + str(loc_idx)+ '.png')

def make_disaster_graph_for_all_location(csv_doc_frequentie):
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(csv_doc_frequentie, sep = ';')
    column = Df['most_common_disaster_subtype']
    plt.hist(column, edgecolor = 'black')
    plt.title('most common disaster subtypes')
    plt.ylabel("Frequency")
    plt.xlabel('Disaster subtype')
    plt.show()





