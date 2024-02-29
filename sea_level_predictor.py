import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(14.4, 10.8))
    plt.rc('font', size=15)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051, 1), first_line.slope * range(1880, 2051, 1) + first_line.intercept)

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    second_line = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), second_line.slope * range(2000, 2051, 1) + second_line.intercept)

    # Add labels and title
    plt.title('Rise in Sea Level', fontsize=25)
    plt.xlabel('Year', fontsize=20)
    plt.ylabel('Sea Level (inches)', fontsize=20)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    
