[Skip to main content](https://matplotlib.org/stable/gallery/ticks/scalarformatter.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/scalarformatter.html#sphx-glr-download-gallery-ticks-scalarformatter-py)
 to download the full example code.

The default tick formatter[#](https://matplotlib.org/stable/gallery/ticks/scalarformatter.html#the-default-tick-formatter "Link to this heading")

==================================================================================================================================================

By default, tick labels are formatted using a [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
, which can be configured via [`ticklabel_format`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "matplotlib.axes.Axes.ticklabel_format")
. This example illustrates some possible configurations:

*   Default.
    
*   `useMathText=True`: Fancy formatting of mathematical expressions.
    
*   `useOffset=False`: Do not use offset notation; see [`ScalarFormatter.set_useOffset`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter.set_useOffset "matplotlib.ticker.ScalarFormatter.set_useOffset")
    .
    

![default settings, useMathText=True, useOffset=False](https://matplotlib.org/stable/_images/sphx_glr_scalarformatter_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, .01)
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    3, 3, figsize\=(9, 9), layout\="constrained", gridspec\_kw\={"hspace": 0.1})

for [col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in [axs.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 1e5 + 1e10, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 1e-10 + 1e-5)
    [col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 1e5, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 1e-4)
    [col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].plot(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 1e5 \- 1e10, \-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 1e-5 \- 1e-10)

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\]:
    [ax.ticklabel\_format](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "matplotlib.axes.Axes.ticklabel_format")
(useMathText\=True)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 2\]:
    [ax.ticklabel\_format](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "matplotlib.axes.Axes.ticklabel_format")
(useOffset\=False)

[plt.rcParams.update](https://docs.python.org/3/library/stdtypes.html#dict.update "builtins.dict.update")
({"axes.titleweight": "bold", "axes.titley": 1.1})
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title("default settings")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title("useMathText=True")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].set\_title("useOffset=False")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 2.940 seconds)

[`Download Jupyter notebook: scalarformatter.ipynb`](https://matplotlib.org/stable/_downloads/660e59bc8f043bb56fdd07ceade033b4/scalarformatter.ipynb)

[`Download Python source code: scalarformatter.py`](https://matplotlib.org/stable/_downloads/d09144c4107ab96d8a55006e711872ef/scalarformatter.py)

[`Download zipped: scalarformatter.zip`](https://matplotlib.org/stable/_downloads/ceb8b537bae8b47cf358152b4736beed/scalarformatter.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)