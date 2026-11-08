[Skip to main content](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-download-gallery-statistics-boxplot-demo-py)
 to download the full example code.

Boxplots[#](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#boxplots "Link to this heading")

================================================================================================================

Visualizing boxplots with matplotlib.

The following examples show off how to visualize boxplots with Matplotlib. There are many options to control their appearance and the statistics that they use to summarize the data.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# fake up some data
[spread](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(50) \* 100
[center](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(25) \* 50
[flier\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10) \* 100 + 100
[flier\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10) \* \-100
[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(([spread](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [center](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [flier\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [flier\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 3)

\# basic plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].boxplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title('basic plot')

\# notched plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].boxplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, notch\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title('notched plot')

\# change outlier point symbols
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].boxplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, sym\='gD')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].set\_title('change outlier\\npoint symbols')

\# don't show outlier points
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].boxplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, sym\='')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_title("don't show\\noutlier points")

\# horizontal boxes
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].boxplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, sym\='rs', orientation\='horizontal')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_title('horizontal boxes')

\# change whisker length
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].boxplot([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, sym\='rs', orientation\='horizontal', whis\=0.75)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].set\_title('change whisker length')

[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.08, right\=0.98, [bottom](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=0.05, [top](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=0.9,
                    hspace\=0.4, wspace\=0.3)

\# fake up some more data
[spread](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(50) \* 100
[center](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(25) \* 40
[flier\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10) \* 100 + 100
[flier\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10) \* \-100
[d2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(([spread](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [center](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [flier\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [flier\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
\# Making a 2-D array only works if all the columns are the
\# same length.  If they are not, then use a list instead.
\# This is actually more efficient because boxplot converts
\# a 2-D array into a list of vectors internally anyway.
[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [d2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [d2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[::2\]\]

\# Multiple box plots on one Axes
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

*   ![basic plot, notched plot, change outlier point symbols, don't show outlier points, horizontal boxes, change whisker length](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_001_2_00x.png)
*   ![boxplot demo](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_002_2_00x.png)

Below we'll generate data from five different probability distributions, each with different characteristics. We want to play with how an IID bootstrap resample of the data preserves the distributional properties of the original sample, and a boxplot is one visual tool to make this assessment

[random\_dists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['Normal(1, 1)', 'Lognormal(1, 1)', 'Exp(1)', 'Gumbel(6, 4)',\
                'Triangular(2, 9, 11)'\]
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 500

[norm](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(1, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[logn](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.lognormal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html#numpy.random.lognormal "numpy.random.lognormal")
(1, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[expo](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.exponential](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html#numpy.random.exponential "numpy.random.exponential")
(1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[gumb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.gumbel](https://numpy.org/doc/stable/reference/random/generated/numpy.random.gumbel.html#numpy.random.gumbel "numpy.random.gumbel")
(6, 4, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[tria](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.triangular](https://numpy.org/doc/stable/reference/random/generated/numpy.random.triangular.html#numpy.random.triangular "numpy.random.triangular")
(2, 9, 11, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Generate some random indices that we'll use to resample the original data
\# arrays. For code brevity, just use the same random indices for each array
[bootstrap\_indices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
(0, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    [norm](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [norm](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[bootstrap\_indices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\],\
    [logn](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [logn](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[bootstrap\_indices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\],\
    [expo](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [expo](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[bootstrap\_indices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\],\
    [gumb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [gumb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[bootstrap\_indices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\],\
    [tria](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [tria](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[bootstrap\_indices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\],\
\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 6))
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.canvas.manager.set\_window\_title('A Boxplot Example')
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.075, right\=0.95, [top](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=0.9, [bottom](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=0.25)

[bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [ax1.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, notch\=False, sym\='+', orientation\='vertical', whis\=1.5)
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['boxes'\], color\='black')
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['whiskers'\], color\='black')
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['fliers'\], color\='red', marker\='+')

\# Add a horizontal grid to the plot, but make it very light in color
\# so we can use it for reading data values but not be distracting
[ax1.yaxis.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib.axis.Axis.grid "matplotlib.axis.Axis.grid")
(True, linestyle\='-', which\='major', color\='lightgrey',
               alpha\=0.5)

[ax1.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(
    axisbelow\=True,  \# Hide the grid behind plot objects
    title\='Comparison of IID Bootstrap Resampling Across Five Distributions',
    xlabel\='Distribution',
    ylabel\='Value',
)

\# Now fill the boxes with desired colors
[box\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['darkkhaki', 'royalblue'\]
[num\_boxes](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[medians](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
([num\_boxes](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([num\_boxes](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    [box](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['boxes'\]\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
    [box\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
    [box\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
    for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(5):
        [box\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([box.get\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_xdata "matplotlib.lines.Line2D.get_xdata")
()\[[j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
        [box\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([box.get\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ydata "matplotlib.lines.Line2D.get_ydata")
()\[[j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
    [box\_coords](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[[box\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [box\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\])
    \# Alternate between Dark Khaki and Royal Blue
    [ax1.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
([box\_coords](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolor\=[box\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 % 2\]))
    \# Now draw the median lines back over what we just filled in
    [med](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['medians'\]\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
    [median\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
    [median\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
    for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(2):
        [median\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([med.get\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_xdata "matplotlib.lines.Line2D.get_xdata")
()\[[j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
        [median\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([med.get\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ydata "matplotlib.lines.Line2D.get_ydata")
()\[[j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
        [ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([median\_x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [median\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 'k')
    [medians](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \= [median\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\]
    \# Finally, overplot the sample averages, with horizontal alignment
    \# in the center of each box
    [ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
([med.get\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_xdata "matplotlib.lines.Line2D.get_xdata")
()), [np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]),
             color\='w', marker\='\*', markeredgecolor\='k')

\# Set the axes ranges and axes labels
[ax1.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0.5, [num\_boxes](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 0.5)
[top](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 40
[bottom](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= \-5
[ax1.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
([bottom](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [top](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[ax1.set\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
([np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")
([random\_dists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 2),
                    rotation\=45, fontsize\=8)

\# Due to the Y-axis scale being different across samples, it can be
\# hard to compare differences in medians across the samples. Add upper
\# X-axis tick labels with the sample medians to aid in comparison
\# (just use two decimal places of precision)
[pos](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([num\_boxes](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 1
[upper\_labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[str(round(s, 2)) for s in [medians](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]
[weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['bold', 'semibold'\]
for [tick](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [label](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 in zip(range([num\_boxes](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [ax1.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()):
    [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [tick](https://docs.python.org/3/library/functions.html#int "builtins.int")
 % 2
    [ax1.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([pos](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[tick](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], .95, [upper\_labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[tick](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\],
             transform\=[ax1.get\_xaxis\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_transform.html#matplotlib.axes.Axes.get_xaxis_transform "matplotlib.axes.Axes.get_xaxis_transform")
(),
             horizontalalignment\='center', size\='x-small',
             weight\=[weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], color\=[box\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[k](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])

\# Finally, add a basic legend
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.80, 0.08, f'{[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
} Random Numbers',
         backgroundcolor\=[box\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], color\='black', weight\='roman',
         size\='x-small')
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.80, 0.045, 'IID Bootstrap Resample',
         backgroundcolor\=[box\_colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\],
         color\='white', weight\='roman', size\='x-small')
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.80, 0.015, '\*', color\='white', backgroundcolor\='silver',
         weight\='roman', size\='medium')
[fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.815, 0.013, ' Average Value', color\='black', weight\='roman',
         size\='x-small')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Comparison of IID Bootstrap Resampling Across Five Distributions](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_003_2_00x.png)

Here we write a custom function to bootstrap confidence intervals. We can then use the boxplot along with this function to show these intervals.

def fake\_bootstrapper(n):
    """
    This is just a placeholder for the user's method of
    bootstrapping the median and its confidence intervals.

    Returns an arbitrary median and confidence interval packed into a tuple.
    """
    if n \== 1:
        [med](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= 0.1
        ci \= (\-0.25, 0.25)
    else:
        [med](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= 0.2
        ci \= (\-0.35, 0.50)
    return [med](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, ci

[inc](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.1
[e1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 1, size\=500)
[e2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 1, size\=500)
[e3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 1 + [inc](https://docs.python.org/3/library/functions.html#float "builtins.float")
, size\=500)
[e4](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 1 + 2\*[inc](https://docs.python.org/3/library/functions.html#float "builtins.float")
, size\=500)

[treatments](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[e1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [e2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [e3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [e4](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]
[med1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ci1](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= fake\_bootstrapper(1)
[med2](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ci2](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= fake\_bootstrapper(2)
[medians](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[None, None, [med1](https://docs.python.org/3/library/functions.html#float "builtins.float")\
, [med2](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\]
[conf\_intervals](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[None, None, [ci1](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [ci2](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pos](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([treatments](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)) + 1
[bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [ax.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
([treatments](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, sym\='k+', positions\=[pos](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
                notch\=True, bootstrap\=5000,
                usermedians\=[medians](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                [conf\_intervals](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[conf\_intervals](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('treatment')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('response')
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['whiskers'\], color\='k', linestyle\='-')
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([bp](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['fliers'\], markersize\=3.0)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![boxplot demo](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_004_2_00x.png)

Here we customize the widths of the caps .

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-7, 7, 140)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
(\[\-25, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, 25\])
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
(\[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\], notch\=True, capwidths\=\[0.01, 0.2\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![boxplot demo](https://matplotlib.org/stable/_images/sphx_glr_boxplot_demo_005_2_00x.png)

Tags: [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [plot-type: boxplot](https://matplotlib.org/stable/_tags/plot-type-boxplot.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
     / [`matplotlib.pyplot.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
    
*   [`matplotlib.artist.Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
     / [`matplotlib.pyplot.setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
    

**Total running time of the script:** (0 minutes 3.414 seconds)

[`Download Jupyter notebook: boxplot_demo.ipynb`](https://matplotlib.org/stable/_downloads/691a80253e42e8ca84fe26961b1ee684/boxplot_demo.ipynb)

[`Download Python source code: boxplot_demo.py`](https://matplotlib.org/stable/_downloads/62c71faf74da9063a3e8cccd6bfdbed9/boxplot_demo.py)

[`Download zipped: boxplot_demo.zip`](https://matplotlib.org/stable/_downloads/164f8527dcf6ccac1e75952ae289af6a/boxplot_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)