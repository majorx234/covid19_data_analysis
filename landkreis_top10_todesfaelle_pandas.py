import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

inhabitants = pd.read_csv('einwohner_kreise.odf.csv',dtype={'ags5': 'string'})

#replace shitty spaces in data
inhabitants['insgesamt'] = [int(str(val).replace(' ','')) for val in inhabitants['insgesamt'].values]

deaths = pd.read_csv('Todesfaelle_Corona_2021-10-05.csv',dtype={'ags5': 'string'})

# extract kr_tod_md_kum
kum_deaths = deaths.loc[deaths['variable']=='kr_tod_md_kum']

#merge deaths with inhabitants
kum_deaths_inhabitants = pd.merge(inhabitants, kum_deaths, on="ags5")
print(kum_deaths_inhabitants) 

last_column_name = kum_deaths_inhabitants.T.last_valid_index()
kum_deaths_inhabitants['deaths per inhabitants'] = kum_deaths_inhabitants[last_column_name]/kum_deaths_inhabitants['insgesamt']
print(kum_deaths_inhabitants)

kum_deaths_sort = kum_deaths_inhabitants.sort_values(['deaths per inhabitants'], ascending = False)
print(kum_deaths_sort)


