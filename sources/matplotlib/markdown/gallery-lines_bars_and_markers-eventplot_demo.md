[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventplot_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventplot_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-eventplot-demo-py)
 to download the full example code.

Eventplot demo[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventplot_demo.html#eventplot-demo "Link to this heading")

==========================================================================================================================================

An [`eventplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.eventplot.html#matplotlib.axes.Axes.eventplot "matplotlib.axes.Axes.eventplot")
 showing sequences of events with various line properties. The plot is shown in both horizontal and vertical orientations.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib

[matplotlib.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['font.size'\] \= 8.0

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

\# create random data
[data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(\[6, 50\])

\# set different colors for each set of positions
[colors1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[f'C{i}' for i in range(6)\]

\# set different line properties for each set of positions
\# note that some overlap
[lineoffsets1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\-15, \-3, 1, 1.5, 6, 10\]
[linelengths1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[5, 2, 1, 1, 3, 1.5\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2)

\# create a horizontal plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].eventplot([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, colors\=[colors1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, lineoffsets\=[lineoffsets1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                    linelengths\=[linelengths1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\# create a vertical plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].eventplot([data1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, colors\=[colors1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, lineoffsets\=[lineoffsets1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                    linelengths\=[linelengths1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, orientation\='vertical')

\# create another set of random data.
\# the gamma distribution is only used for aesthetic purposes
[data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.gamma](https://numpy.org/doc/stable/reference/random/generated/numpy.random.gamma.html#numpy.random.gamma "numpy.random.gamma")
(4, size\=\[60, 50\])

\# use individual values for the parameters this time
\# these values will be used for all data sets (except lineoffsets2, which
\# sets the increment between each data set in this usage)
[colors2](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'black'
[lineoffsets2](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 1
[linelengths2](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 1

\# create a horizontal plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].eventplot([data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, colors\=[colors2](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, lineoffsets\=[lineoffsets2](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
                    linelengths\=[linelengths2](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# create a vertical plot
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].eventplot([data2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, colors\=[colors2](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, lineoffsets\=[lineoffsets2](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
                    linelengths\=[linelengths2](https://docs.python.org/3/library/functions.html#int "builtins.int")
, orientation\='vertical')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![eventplot demo](https://matplotlib.org/stable/_images/sphx_glr_eventplot_demo_001_2_00x.png)

Tags: [plot-type: eventplot](https://matplotlib.org/stable/_tags/plot-type-eventplot.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

**Total running time of the script:** (0 minutes 1.137 seconds)

[`Download Jupyter notebook: eventplot_demo.ipynb`](https://matplotlib.org/stable/_downloads/5a259b2bb38e7c783fd49340a7dc686a/eventplot_demo.ipynb)

[`Download Python source code: eventplot_demo.py`](https://matplotlib.org/stable/_downloads/491e132174cc69dba0441dfe1697725d/eventplot_demo.py)

[`Download zipped: eventplot_demo.zip`](https://matplotlib.org/stable/_downloads/1a4328446a0b3445f382cefe46c49129/eventplot_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)