import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gas = pd.read_csv('gas_prices.csv')
gas.columns

gas.head(3)
gas.tail(3)
gas.describe()

gas[['Canada', 'USA', 'Mexico']][:3]

plt.title('Comparing Gas Prices in 3 American Countries', color = '#031cfc', fontdict = {'fontsize':'bold', 'fontsize': 14})
# labels= ('USA', 'Canada', 'Mexico')
plt.xlabel('Year', fontdict = {'fontsize':'bold', 'fontsize': 14})
plt.ylabel('Prices $', fontdict = {'fontsize':'bold', 'fontsize': 14})
plt.plot(gas.Year, gas.USA, 'r.-', label = 'USA')
plt.plot(gas.Year, gas.Canada, 'y.-', label = 'Canada')
plt.plot(gas.Year, gas.Mexico, 'g.-', label = 'Mexico')

# Printing only for every two years
plt.xticks(gas.Year[:: 2]) 

# Adding 2010 to the list of Years
plt.xticks(gas.Year[:: 2].tolist() + [2010])

labels= ('USA', 'Canada', 'Mexico')

# Moving the legend out of the box // 
"""
leg = ax.get_legend()
leg.set_bbox_to_anchor((0., 0.1, 0.2, 0.2))
# Not working, hence I will need to work it out
"""
plt.legend()

# plt.show()

# BUILDING HISTOGRAMMES for GAS PRICES VARIATION IN USA-CANADA-MEXICO

gas
bins = [1, 1.5, 2, 2.5, 3, 3.5]
# bins = [1, 2, 3, 4]

plt.hist(gas.USA, bins = bins, color = '#32a83a')
plt.title('USA Gas Prices Variation', color = '#326fa8', fontdict = {'fontweight':'bold', 'fontsize':16})
plt.xlabel('Gas Prices Range', color = '#3232a8', fontdict = {'fontweight':'bold', 'fontsize':14})
plt.ylabel('Number Time Price Occurence', color = '#3232a8', fontdict = {'fontweight':'bold', 'fontsize':14})

# The gas prices in the US stayed very low for the majority of the time during the Te period 1990 to 2008. 
# This is the result of the US being themselves a big producer of oil and gas, combined with a good oil & gas politic in the International market. 
# In addition, they have a very good relationship with big producers of oil and gas such as Saudi Arabia.

plt.hist(gas.Canada, bins = bins, color = '#a86532')
plt.title('Canada Gas Prices Variation', color = '#326fa8', fontdict = {'fontweight':'bold', 'fontsize':16})
plt.xlabel('Gas Prices Range', color = '#3232a8', fontdict = {'fontweight':'bold', 'fontsize':14})
plt.ylabel('Number Time Price Occurence', color = '#3232a8', fontdict = {'fontweight':'bold', 'fontsize':14})

# The gas prices in Canada have also been low for most of the time between 1990 and 2008. 
# However, currently the complaint about high gas prices is due to taxes. 

bins = [1, 1.5, 2, 2.5, 3]
plt.hist(gas.Mexico, bins = bins, color = '#9432a8')
plt.title('Mexico Gas Prices Variation', color = '#326fa8', fontdict = {'fontweight':'bold', 'fontsize':16})
plt.xlabel('Gas Prices Range', color = '#3232a8', fontdict = {'fontweight':'bold', 'fontsize':14})
plt.ylabel('Number Time Price Occurence', color = '#3232a8', fontdict = {'fontweight':'bold', 'fontsize':14})

# The gas prices in Mexico have relatively low, but higher from 1998 to 2003. 
# However, the prices stayed lower compaire from 1998 until 2008 compaire to the others. 
# Indeed, they were the lowest in 2008. 
