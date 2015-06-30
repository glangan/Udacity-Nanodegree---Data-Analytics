from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    #find five stations with most number of entries
    data_units = turnstile_weather.groupby('UNIT').sum()
    data_units = data_units.sort_index(by=['ENTRIESn_hourly'], ascending = False)
    data_units = data_units[0:5]
    #data to plot
    data_plot = turnstile_weather[turnstile_weather['UNIT'].isin(data_units.index)]
    data_plot = data_plot[['UNIT', 'ENTRIESn_hourly', 'Hour']]
    data_plot = data_plot.groupby(['Hour', 'UNIT']).sum().reset_index()

    plot = ggplot(data_plot, aes(x = 'Hour', y = 'ENTRIESn_hourly', color = 'UNIT')) + geom_line() + geom_point() + xlim(0,24) + scale_x_continuous(breaks=range(0,23)) + ggtitle('Entries by Hour of 5 stations with most number of entries') + xlab('Hour') + ylab('Entries')
    return plot
