import csv
import pandas as pd

tempdata = pd.read_csv('planet_data_cleaned.csv')

del tempdata['Unnamed: 0']
del tempdata['Index']


tempdata.to_csv('planet_data.csv')  
#-----------------------------------------------

rows = []

with open('planet_data.csv','r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        rows.append(i)

headers = rows[0]

planet_datas = rows[1:]

#print(planet_datas)

g_vals = []

for planet_data in planet_datas:
    mass = planet_data[3]

    new_mass = float(mass) * 1.989 * (10**30)

    planet_data[3] = new_mass

    radius = planet_data[4]

    new_radius = float(radius) * 6.957 * (10**8)

    planet_data[4] = new_radius

    g = ((6.67 * (10**-11) * new_mass) / (new_radius**2))

    planet_data.append(g)


print(planet_datas)





