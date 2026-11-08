[Skip to main content](https://matplotlib.org/stable/gallery/ticks/engineering_formatter.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/engineering_formatter.html#sphx-glr-download-gallery-ticks-engineering-formatter-py)
 to download the full example code.

Format ticks using engineering notation[#](https://matplotlib.org/stable/gallery/ticks/engineering_formatter.html#format-ticks-using-engineering-notation "Link to this heading")

==================================================================================================================================================================================

Use of the engineering Formatter.

![Full unit ticklabels, w/ default precision & space separator, SI-prefix only ticklabels, 1-digit precision & thin space separator](https://matplotlib.org/stable/_images/sphx_glr_engineering_formatter_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import [EngFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")

\# Fixing random state for reproducibility
[prng](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(19680801)

\# Create artificial data to plot.
\# The x data span over several decades to demonstrate several SI prefixes.
[xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(1, 9, 100)
[ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (0.8 + 0.4 \* [prng.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.uniform.html#numpy.random.RandomState.uniform "numpy.random.RandomState.uniform")
(size\=100)) \* [np.log10](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)\*\*2

\# Figure width is doubled (2\*6.4) to display nicely 2 subplots side by side.
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, figsize\=(7, 9.6))
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in ([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    [ax.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('log')

\# Demo of the default settings, with a user-defined unit label.
[ax0.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Full unit ticklabels, w/ default precision & space separator')
[formatter0](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
 \= [EngFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
(unit\='Hz')
[ax0.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([formatter0](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
)
[ax0.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax0.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Frequency')

\# Demo of the options \`places\` (number of digit after decimal point) and
\# \`sep\` (separator between the number and the prefix/unit).
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('SI-prefix only ticklabels, 1-digit precision & '
              'thin space separator')
[formatter1](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
 \= [EngFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
(places\=1, sep\="\\N{THIN SPACE}")  \# U+2009
[ax1.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([formatter1](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Frequency \[Hz\]')

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.728 seconds)

[`Download Jupyter notebook: engineering_formatter.ipynb`](https://matplotlib.org/stable/_downloads/fdddb47b056f5dfc3500338b8275b7a1/engineering_formatter.ipynb)

[`Download Python source code: engineering_formatter.py`](https://matplotlib.org/stable/_downloads/8e492fc8f71eb06947553943ecbf40cb/engineering_formatter.py)

[`Download zipped: engineering_formatter.zip`](https://matplotlib.org/stable/_downloads/da1c08aaf09a3ffb034c6d35929b7522/engineering_formatter.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)