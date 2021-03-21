import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
days = mdates.DayLocator()
months = mdates.MonthLocator()
years = mdates.YearLocator()
hours = mdates.HourLocator()
hours_fmt = mdates.DateFormatter('%h')
months_fmt = mdates.DateFormatter('%m')
days_fmt = mdates.DateFormatter('%D')
years_fmt = mdates.DateFormatter('%m/%Y')


fig, ax = plt.subplots()
df = pd.read_csv('final.csv', parse_dates=['date'])
#df['date'] = pd.to_datetime(df['date'])
#df = df.sort_values(by='date')
#df.to_csv('final_sorted.csv')
print(df['date'].head())
#ax.plot('date', 'compound', data=df)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
#ax.xaxis.set_minor_formatter(months_fmt)



print(str(df['date'][0]) + "FIRST DATE<---")
datemin = np.datetime64(df['date'][0], 'D')
datemax = np.datetime64(df['date'].iloc[-1], 'D') 
ax.set_xlim(datemin, datemax)
print(str(datemin) + " " + str(datemax))
ax.grid(True)

ax.format_xdata = mdates.DateFormatter('%d/%m/%Y')
fig.autofmt_xdate()
#df['compound'].plot(kind='bar')
plt.scatter(df['date'], df['compound'])


plt.show()
