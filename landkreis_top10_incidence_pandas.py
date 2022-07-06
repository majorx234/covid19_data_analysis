import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

cmap=plt.get_cmap("jet")

inhabitants = pd.read_csv('einwohner_kreise.odf.csv',dtype={'ags5': 'string'})

#replace shitty spaces in data
inhabitants['insgesamt'] = [int(str(val).replace(' ','')) for val in inhabitants['insgesamt'].values]

deaths = pd.read_csv('Todesfaelle_Corona_2021-10-05.csv',dtype={'ags5': 'string'})

# extract kr_tod_md_kum
kum_deaths = deaths.loc[deaths['variable']=='kr_tod_md_kum']

#merge deaths with inhabitants
kum_deaths_inhabitants = pd.merge(inhabitants, kum_deaths, on="ags5")

last_column_name = kum_deaths_inhabitants.T.last_valid_index()

kum_deaths_inhabitants['deaths per inhabitants'] = kum_deaths_inhabitants[last_column_name]/kum_deaths_inhabitants['insgesamt']

kum_deaths_inhabitants_sort = kum_deaths_inhabitants.sort_values(['deaths per inhabitants'], ascending = False)

#05315
kum_deaths_inhabitants_cologne = kum_deaths_inhabitants.loc[kum_deaths_inhabitants['ags5'] == '05315']
inhabitants_cologne_series = kum_deaths_inhabitants_cologne['insgesamt']

print(inhabitants_cologne_series)
inhabitants_cologne = inhabitants_cologne_series.iat[0]
#print(kum_deaths_inhabitants_cologne)


kum_deaths_sort_data = kum_deaths_inhabitants_sort.loc[:,'d20200301':'d20211004']
kum_deaths_cologne_data = kum_deaths_inhabitants_cologne.loc[:,'d20200301':'d20211004']
#pandas series -> einfaches array
city_list = kum_deaths_inhabitants_sort["Kreis/Stadt"]
inhabitants = kum_deaths_inhabitants_sort["insgesamt"]
print(city_list)


numdays = kum_deaths_sort_data.shape[1] #length of x dataframe
base = dt.datetime.fromisoformat('2020-03-01')
date_list = [base + dt.timedelta(days=x) for x in range(numdays)]

N=10
for i in range(0,9):
    mycolor = cmap(i/N)
    plt.plot(date_list, kum_deaths_sort_data.iloc[i]/inhabitants[i] ,color=mycolor,label=city_list.iloc[i])

plt.plot(date_list,kum_deaths_cologne_data.iloc[0]/inhabitants_cologne ,color='red',label='Kölle')    
plt.legend()
plt.show()


