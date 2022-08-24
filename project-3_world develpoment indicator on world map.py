'''
1. In this project I have one JSON file which contain geographical location of all the countries.
2. I have world develpoment indicator database from the previous project
3. I crated one database of name stage which contain co2 emission metric ton per capita and in year 2011
4. from the stage database create another database of name plot data(countycode and value) which will going to use in choropleth (Choropleth maps bind Pandas Data Frames and json geometries)
5. now, will use folium.Map at one coordinate in this example i choose India's lattitude and longitude
6. now, will use choropleth to bind 'geographical location' and 'dataframe(plot data)'
'''

'''
Folium is a powerful Python library that helps you create several types of Leaflet maps.
By default, Folium creates a map in a separate HTML file.
Since Folium results are interactive, this library is very useful for dashboard building.
You can also create inline Jupyter maps in Folium.

Leaflet is a framework for presenting map data.

JSON (JavaScript Object Notation)
'''

import folium
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

#country_geo = "H:\DataScience\Day-28\26 JUNE 2022\Projects\data\world-countries.json"
country_geo = "C:/Users/Dell/OneDrive/Desktop/world-countries.json"


'''
lets read same world development indicator file
'''
df = pd.read_csv(r'H:\DataScience\Day-28\26 JUNE 2022\Projects\data\Indicators.bz2', compression='bz2')
print("Data Shape: \n",df.shape)

print("Sample Data: \n",df.head())

'''
#Select CO2 emissions for all countries in 2011
'''
hist_indicator = 'CO2 emissions \(metric'
hist_year = 2011
mask1 = df['IndicatorName'].str.contains(hist_indicator)
mask2 = df['Year'].isin([hist_year])
stage = df[mask1 & mask2]
stage.head()

'''
Setup the data for plotting
Create a data frame with just the country codes and the values we want to be plotted.

plot_data = stage['CountryCode']
print("plot_data\n", plot_data)

plot_data = stage['Value']
print("plot_data\n", plot_data)

plot_data = stage['CountryCode','Value']    ## this will won't work because of 1D
print("plot_data\n", plot_data)
'''
plot_data = stage[['CountryCode', 'Value']]
print("plot_data\n", plot_data)

hist_indicator = stage.iloc[0]['IndicatorName']
print(hist_indicator)

'''
Visualize CO2 emissions per capita using Folium.
Folium provides interactive maps with the ability to create sophisticated overlays for data visualization
Setup a folium map at a high-level zoom.
'''
map = folium.Map(location=[20.593684, 78.96288], titles = 'CO2 emission by countries', zoom_start=1.5)

'''
Choropleth maps bind Pandas Data Frames and json geometries.
This allows us to quickly visualize data combinations
'''
map.choropleth(geo_data = country_geo, data = plot_data, columns = ['CountryCode', 'Value'], key_on='feature.id', fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.1, legend_name=hist_indicator)

map.save('C:/Users/Dell/OneDrive/Desktop/plot_data1.html')

'''
import intercative session of folium file
'''
from IPython.display import HTML
HTML('<iframe src=saved_info/plot_data.html width=700 height=450></iframe>')
