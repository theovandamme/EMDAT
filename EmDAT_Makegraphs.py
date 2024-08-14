import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import EmDAT_Disaster_subtypes as DS
import EmDAT_Time_Of_Year as TOY
import EmDAT_Duration as DUR
import EmDAT_Magnitude as MA
import EmDAT_TotalAffected as TA
import seaborn as SB
import scipy

# input is the CSV file with each location, the frequency, the latitude, longitude, etc. and the file path where each event is individually saved.
# output is a number of graphs giving information about the flood such as the disaster subtype, the duration of each event 
# for each location individually that have at least 4 separate flood events. 
def make_graph_for_individual_locations(CSV_doc_frequentie, file_path):
    CSV_doc_frequentie = pd.read_csv(CSV_doc_frequentie, sep = ';')
    for index, row in CSV_doc_frequentie.iterrows():
        loc_idx = index
        if row['frequentie'] > 4:
            CSV_doc = file_path + '/locatie' + str(loc_idx) + '.csv' 
            DS.make_disaster_graph_per_location(CSV_doc, loc_idx)
            TOY.make_time_of_year_graph_per_location(CSV_doc, loc_idx)
            DUR.Duration_graph(CSV_doc, loc_idx)
            MA.Magnitude_graph(CSV_doc, loc_idx)
            TA.Total_affected_graph(CSV_doc, loc_idx)


def make_graph_for_all_locations(CSV_doc_frequentie):
    DS.make_disaster_graph_for_all_location(CSV_doc_frequentie)
    TOY.make_time_of_year_graph_all_locations(CSV_doc_frequentie)
    DUR.Average_duration_graph(CSV_doc_frequentie)
    MA.Average_Magnitude_graph(CSV_doc_frequentie)
    TA.Average_affected_graph(CSV_doc_frequentie)


def duration_vs_impact(csv_doc_frequentie):
    Df = pd.read_csv(csv_doc_frequentie, sep = ';')
    Average_duration = Df['Average_duration']
    Average_total_affected = Df['Average_affected']      
    AD = Average_duration.dropna()
    AT = Average_total_affected.dropna()
    plt.title('Duration versus total of people affected')
    plt.ylabel("people affected")
    plt.xlabel('Duration')
    SB.regplot(x =Average_duration,y = Average_total_affected)
    plt.show()

def Latitude_vs_timing(csv_doc_frequentie):
    Df = pd.read_csv(csv_doc_frequentie, sep = ';')
    lat = Df['lat']
    most_common_month = Df['most_common_month']
    plt.title('Month of flood occurence compared to the latitude of the event')
    plt.ylabel("latitude")
    plt.xlabel('most_common_month')
    SB.regplot(x =most_common_month,y = lat)
    #plt.scatter(Average_duration, Average_total_affected)
    plt.show()