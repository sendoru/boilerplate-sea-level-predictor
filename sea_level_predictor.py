import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df_recent = df[df['Year'] >= 2000]

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df_recent = df[df['Year'] >= 2000]

    # Create scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],
               label='Original Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level'])
    domain = range(df['Year'].min(), 2051)
    ax.plot(domain, intercept + slope*domain, 'r',
            label='Predicted Data with All Samples')

    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    domain = range(2000, 2051)
    ax.plot(domain, intercept + slope*domain,
            'g', label='Predicted Data with Samples after 2000')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.xaxis.set_label_text('Year')
    ax.yaxis.set_label_text('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
