from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    plot_weather_data is passed a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.

    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning
    ridership and time of day in exercise #1, maybe look at weather and try to make a
    histogram in this exercise). Or try to use multiple encodings in your graph if
    you didn't in the previous exercise.

    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out the link
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather
    dataframe.

   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    #find ten stations with most number of entries
    data_units = turnstile_weather.groupby('UNIT').sum()
    data_units = data_units.sort_index(by=['ENTRIESn_hourly'], ascending = False)
    data_units = data_units[0:10]

    data_plot = turnstile_weather[turnstile_weather['UNIT'].isin(data_units.index)]
    data_plot = data_plot[['UNIT', 'ENTRIESn_hourly', 'rain']]
    data_plot = data_plot.groupby(['UNIT', 'rain']).sum().reset_index()
    plot = ggplot(data_plot, aes(x = data_plot.index, y = 'ENTRIESn_hourly', color = 'rain')) + geom_point(aes(size=30)) + scale_x_continuous(breaks=range(0,20), labels = ['R011', '', 'R012', '', 'R018', '', 'R022', '', 'R033', '', 'R046', '', 'R055', '', 'R084', '', 'R170', '', 'R179', '']) + xlab('Stations') + ylab('Total Entries') + ggtitle('Total number of entries at ten stations with most entries compared according to rain (Legend- Magenta: Rain, Cyan: No Rain)')
    return plot
