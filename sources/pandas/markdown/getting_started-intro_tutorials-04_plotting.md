[Skip to main content](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/04_plotting.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/intro_tutorials/04_plotting.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/04_plotting.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/intro_tutorials/04_plotting.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/intro_tutorials/04_plotting.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/intro_tutorials/04_plotting.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/intro_tutorials/04_plotting.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/intro_tutorials/04_plotting.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/intro_tutorials/04_plotting.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/intro_tutorials/04_plotting.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/intro_tutorials/04_plotting.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/intro_tutorials/04_plotting.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

How do I create plots in pandas?[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html#how-do-i-create-plots-in-pandas "Link to this heading")

============================================================================================================================================================================

![../../_images/04_plot_overview.svg](https://pandas.pydata.org/docs/_images/04_plot_overview.svg)

In \[1\]: import pandas as pd

In \[2\]: import matplotlib.pyplot as plt

Copy to clipboard

Data used for this tutorial:

*   Air quality data
    
    For this tutorial, air quality data about 𝑁⁢𝑂2 is used, made available by [OpenAQ](https://openaq.org/)
     and using the [py-openaq](http://dhhagan.github.io/py-openaq/index.html)
     package. The `air_quality_no2.csv` data set provides 𝑁⁢𝑂2 values for the measurement stations _FR04014_, _BETR801_ and _London Westminster_ in respectively Paris, Antwerp and London.
    
    [To raw data](https://github.com/pandas-dev/pandas/tree/main/doc/data/air_quality_no2.csv)
    
    In \[3\]: air\_quality \= pd.read\_csv("data/air\_quality\_no2.csv", index\_col\=0, parse\_dates\=True)
    
    In \[4\]: air\_quality.head()
    Out\[4\]: 
                         station\_antwerp  station\_paris  station\_london
    datetime                                                           
    2019-05-07 02:00:00              NaN            NaN            23.0
    2019-05-07 03:00:00             50.5           25.0            19.0
    2019-05-07 04:00:00             45.0           27.7            19.0
    2019-05-07 05:00:00              NaN           50.4            16.0
    2019-05-07 06:00:00              NaN           61.9             NaN
    
    Copy to clipboard
    
    Note
    
    The `index_col=0` and `parse_dates=True` parameters passed to the `read_csv` function define the first (0th) column as index of the resulting `DataFrame` and convert the dates in the column to [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
     objects, respectively.
    

*   I want a quick visual check of the data.
    
    In \[5\]: air\_quality.plot()
    Out\[5\]: <Axes: xlabel='datetime'>
    
    In \[6\]: plt.show()
    
    Copy to clipboard
    
    ![../../_images/04_airqual_quick.png](https://pandas.pydata.org/docs/_images/04_airqual_quick.png)
    
    With a `DataFrame`, pandas creates by default one line plot for each of the columns with numeric data.
    

*   I want to plot only the columns of the data table with the data from Paris.
    
    In \[7\]: air\_quality\["station\_paris"\].plot()
    Out\[7\]: <Axes: xlabel='datetime'>
    
    In \[8\]: plt.show()
    
    Copy to clipboard
    
    ![../../_images/04_airqual_paris.png](https://pandas.pydata.org/docs/_images/04_airqual_paris.png)
    
    To plot a specific column, use a selection method from the [subset data tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset)
     in combination with the [`plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
     method. Hence, the [`plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
     method works on both `Series` and `DataFrame`.
    

*   I want to visually compare the 𝑁⁢𝑂2 values measured in London versus Paris.
    
    In \[9\]: air\_quality.plot.scatter(x\="station\_london", y\="station\_paris", alpha\=0.5)
    Out\[9\]: <Axes: xlabel='station\_london', ylabel='station\_paris'>
    
    In \[10\]: plt.show()
    
    Copy to clipboard
    
    ![../../_images/04_airqual_scatter.png](https://pandas.pydata.org/docs/_images/04_airqual_scatter.png)

Apart from the default `line` plot when using the `plot` function, a number of alternatives are available to plot data. Let’s use some standard Python to get an overview of the available plot methods:

In \[11\]: \[\
   ....:    method\_name\
   ....:    for method\_name in dir(air\_quality.plot)\
   ....:    if not method\_name.startswith("\_")\
   ....: \]
   ....: 
Out\[11\]: 
\['area',\
 'bar',\
 'barh',\
 'box',\
 'density',\
 'hexbin',\
 'hist',\
 'kde',\
 'line',\
 'pie',\
 'scatter'\]

Copy to clipboard

Note

In many development environments such as IPython and Jupyter Notebook, use the TAB button to get an overview of the available methods, for example `air_quality.plot.` + TAB.

One of the options is [`DataFrame.plot.box()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html#pandas.DataFrame.plot.box "pandas.DataFrame.plot.box")
, which refers to a [boxplot](https://en.wikipedia.org/wiki/Box_plot)
. The `box` method is applicable on the air quality example data:

In \[12\]: air\_quality.plot.box()
Out\[12\]: <Axes: >

In \[13\]: plt.show()

Copy to clipboard

![../../_images/04_airqual_boxplot.png](https://pandas.pydata.org/docs/_images/04_airqual_boxplot.png)

To user guide

For an introduction to plots other than the default line plot, see the user guide section about [supported plot styles](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization-other)
.

*   I want each of the columns in a separate subplot.
    
    In \[14\]: axs \= air\_quality.plot.area(figsize\=(12, 4), subplots\=True)
    
    In \[15\]: plt.show()
    
    Copy to clipboard
    
    ![../../_images/04_airqual_area_subplot.png](https://pandas.pydata.org/docs/_images/04_airqual_area_subplot.png)
    
    Separate subplots for each of the data columns are supported by the `subplots` argument of the `plot` functions. The builtin options available in each of the pandas plot functions are worth reviewing.
    

To user guide

Some more formatting options are explained in the user guide section on [plot formatting](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization-formatting)
.

*   I want to further customize, extend or save the resulting plot.
    
    In \[16\]: fig, axs \= plt.subplots(figsize\=(12, 4))
    
    In \[17\]: air\_quality.plot.area(ax\=axs)
    Out\[17\]: <Axes: xlabel='datetime'>
    
    In \[18\]: axs.set\_ylabel("NO$\_2$ concentration")
    Out\[18\]: Text(0, 0.5, 'NO$\_2$ concentration')
    
    In \[19\]: fig.savefig("no2\_concentrations.png")
    
    In \[20\]: plt.show()
    
    Copy to clipboard
    
    ![../../_images/04_airqual_customized.png](https://pandas.pydata.org/docs/_images/04_airqual_customized.png)

Each of the plot objects created by pandas is a [Matplotlib](https://matplotlib.org/)
 object. As Matplotlib provides plenty of options to customize plots, making the link between pandas and Matplotlib explicit enables all the power of Matplotlib to the plot. This strategy is applied in the previous example:

fig, axs \= plt.subplots(figsize\=(12, 4))        \# Create an empty Matplotlib Figure and Axes
air\_quality.plot.area(ax\=axs)                   \# Use pandas to put the area plot on the prepared Figure/Axes
axs.set\_ylabel("NO$\_2$ concentration")          \# Do any Matplotlib customization you like
fig.savefig("no2\_concentrations.png")           \# Save the Figure/Axes using the existing Matplotlib method.
plt.show()                                      \# Display the plot

Copy to clipboard

#### REMEMBER

*   The `.plot.*` methods are applicable on both Series and DataFrames.
    
*   By default, each of the columns is plotted as a different element (line, boxplot, …).
    
*   Any plot created by pandas is a Matplotlib object.
    

To user guide

A full overview of plotting in pandas is provided in the [visualization pages](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization)
.