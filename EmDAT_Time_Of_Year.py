import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def make_time_of_year_graph_per_location(CSV_doc, loc_idx):
    Df = pd.read_csv(CSV_doc, sep = ';')
    TOY = Df['Start Month']
    plt.title('Time of year of the floods for location  '+ str(loc_idx))
    plt.ylabel("Frequency")
    plt.xlabel('Month')
    plt.hist(TOY, bins = 12, range=(1,13), align = 'left', edgecolor = 'black')
    plt.show()
    #plt.savefig('TOY_hist_Locatie' + str(loc_idx)+ '.png')

def make_time_of_year_graph_all_locations(CSV_doc_frequentie):
    Df = pd.read_csv(CSV_doc_frequentie, sep = ';')
    TOY = Df['most_common_month']
    plt.title('Most common time of year of the floods')
    plt.ylabel("Frequency")
    plt.xlabel('Month')
    plt.hist(TOY, bins = 12, range=(1,13), align = 'left', edgecolor = 'black')
    plt.show()