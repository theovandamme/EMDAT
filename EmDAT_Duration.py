import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from datetime import date
import numpy as np

def calculate_duration(row):
    if (row[26:32].isna() == False).all():
        Start_Year = int(row['Start Year'])
        Start_Month = int(row['Start Month'])
        Start_Day = int(row['Start Day'])
        End_Year = int(row['End Year'])
        End_Month = int(row['End Month'])
        End_Day = int(row['End Day'])
        Start_date = date(Start_Year, Start_Month, Start_Day)
        End_date = date(End_Year, End_Month, End_Day)
        Duration = (End_date-Start_date).days
        return Duration
    
def Duration_graph(CSV_doc, loc_idx): 
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(CSV_doc, sep = ';')
    column = Df['Duration']
    Duration = column.dropna()
    binwidth = 5
    plt.hist(Duration, bins=np.arange(min(Duration), max(Duration) + binwidth, binwidth), edgecolor = 'black')
    plt.title('Flood duration for location '+ str(loc_idx))
    plt.ylabel("Frequency")
    plt.xlabel('Amount of Days')
    plt.show()
    #plt.savefig('Duration_Locatie' + str(loc_idx)+ '.png')

def Average_duration_graph(freq_doc):
    plt.style.use('seaborn-v0_8-darkgrid')
    Df = pd.read_csv(freq_doc, sep = ';')
    column = Df['Average_duration']
    binwidth = 5
    Duration = column.dropna()
    plt.hist(Duration, bins=np.arange(min(Duration), max(Duration) + binwidth, binwidth), edgecolor = 'black')
    plt.title('Average Flood duration for dataset')
    plt.ylabel("Frequency")
    plt.xlabel('Amount of Days')
    plt.show()



    