[Skip to main content](https://matplotlib.org/stable/gallery/misc/table_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/table_demo.html#sphx-glr-download-gallery-misc-table-demo-py)
 to download the full example code.

Table Demo[#](https://matplotlib.org/stable/gallery/misc/table_demo.html#table-demo "Link to this heading")

============================================================================================================

Demo of table function to display a table within a plot.

![Loss by Disaster](https://matplotlib.org/stable/_images/sphx_glr_table_demo_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[ 66386, 174296,  75131, 577908,  32015\],\
        \[ 58230, 381139,  78045,  99308, 160454\],\
        \[ 89135,  80552, 152558, 497981, 603535\],\
        \[ 78415,  81858, 150656, 193263,  69638\],\
        \[139361, 331509, 343164, 781380,  52269\]\]

[columns](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
[rows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['%d year' % x for x in (100, 50, 20, 10, 5)\]

[values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2500, 500)
[value\_increment](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 1000

\# Get some pastel shades for the colors
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["BuPu"\]([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 0.5, len([rows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)))
[n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[index](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len([columns](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)) + 0.3
[bar\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.4

\# Initialize the vertical-offset for the stacked bar chart.
[y\_offset](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(len([columns](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
))

\# Plot bars and create text labels for the table
[cell\_text](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [row](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    [plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
([index](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[row](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [bar\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, bottom\=[y\_offset](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\=[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[row](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
    [y\_offset](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [y\_offset](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[row](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
    [cell\_text](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append(\['%1.1f' % (x / 1000.0) for x in [y\_offset](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
\# Reverse colors and text labels to display the last value at the top.
[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::\-1\]
[cell\_text](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.reverse()

\# Add a table at the bottom of the Axes
[the\_table](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")
 \= [plt.table](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#matplotlib.pyplot.table "matplotlib.pyplot.table")
(cellText\=[cell\_text](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                      rowLabels\=[rows](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                      rowColours\=[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
                      colLabels\=[columns](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
,
                      loc\='bottom')

\# Adjust layout to make room for the table:
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(left\=0.2, bottom\=0.2)

[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
(f"Loss in ${[value\_increment](https://docs.python.org/3/library/functions.html#int "builtins.int")
}'s")
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
([values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [value\_increment](https://docs.python.org/3/library/functions.html#int "builtins.int")
, \['%d' % val for val in [values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(\[\])
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Loss by Disaster')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: table_demo.ipynb`](https://matplotlib.org/stable/_downloads/bb9303d7a1c341aaf403bf82d17eede4/table_demo.ipynb)

[`Download Python source code: table_demo.py`](https://matplotlib.org/stable/_downloads/017058e784e2a359b3a7dd004a3e0379/table_demo.py)

[`Download zipped: table_demo.zip`](https://matplotlib.org/stable/_downloads/7b94c996f33ef9212219add18c5e17ae/table_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)