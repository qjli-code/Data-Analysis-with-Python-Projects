import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    r = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(x, r.slope * x + r.intercept, '-' , color='r')

    # Create second line of best fit
    x = df.loc[df['Year']>=2000, 'Year']
    y = df.loc[df['Year']>=2000, 'CSIRO Adjusted Sea Level']
    r = linregress(x=x, y=y)
    x = pd.Series(range(2000, 2051))
    plt.plot(x, r.slope * x + r.intercept, '--' , color='g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()