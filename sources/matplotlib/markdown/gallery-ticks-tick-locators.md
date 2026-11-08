[Skip to main content](https://matplotlib.org/stable/gallery/ticks/tick-locators.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/ticks/tick-locators.html#sphx-glr-download-gallery-ticks-tick-locators-py)
 to download the full example code.

Tick locators[#](https://matplotlib.org/stable/gallery/ticks/tick-locators.html#tick-locators "Link to this heading")

======================================================================================================================

Tick locators define the position of the ticks.

This example illustrates the usage and effect of the most common locators.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as ticker

def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    \# only show the bottom spine
    ax.yaxis.set\_major\_locator([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
    ax.spines\[\['left', 'right', 'top'\]\].set\_visible(False)

    ax.xaxis.set\_ticks\_position('bottom')
    ax.tick\_params(which\='major', width\=1.00, length\=5)
    ax.tick\_params(which\='minor', width\=0.75, length\=2.5)
    ax.set\_xlim(0, 5)
    ax.set\_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform\=ax.transAxes,
            fontsize\=14, fontname\='Monospace', color\='tab:blue')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(8, 1, figsize\=(8, 6))

\# Null Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], title\="NullLocator()")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].xaxis.set\_major\_locator([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].xaxis.set\_minor\_locator([ticker.NullLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
())

\# Multiple Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], title\="MultipleLocator(0.5, offset=0.2)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].xaxis.set\_major\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(0.5, offset\=0.2))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].xaxis.set\_minor\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(0.1))

\# Fixed Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\], title\="FixedLocator(\[0, 1, 5\])")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].xaxis.set\_major\_locator([ticker.FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
(\[0, 1, 5\]))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].xaxis.set\_minor\_locator([ticker.FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.2, 0.8, 4)))

\# Linear Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\], title\="LinearLocator(numticks=3)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].xaxis.set\_major\_locator([ticker.LinearLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
(3))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3\].xaxis.set\_minor\_locator([ticker.LinearLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
(31))

\# Index Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\], title\="IndexLocator(base=0.5, offset=0.25)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\].plot(\[0\]\*5, color\='white')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4\].xaxis.set\_major\_locator([ticker.IndexLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator "matplotlib.ticker.IndexLocator")
(base\=0.5, offset\=0.25))

\# Auto Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\], title\="AutoLocator()")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\].xaxis.set\_major\_locator([ticker.AutoLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "matplotlib.ticker.AutoLocator")
())
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5\].xaxis.set\_minor\_locator([ticker.AutoMinorLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
())

\# MaxN Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\], title\="MaxNLocator(n=4)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\].xaxis.set\_major\_locator([ticker.MaxNLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
(4))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[6\].xaxis.set\_minor\_locator([ticker.MaxNLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
(40))

\# Log Locator
setup([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\], title\="LogLocator(base=10, numticks=15)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\].set\_xlim(10\*\*3, 10\*\*10)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\].set\_xscale('log')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[7\].xaxis.set\_major\_locator([ticker.LogLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
(base\=10, numticks\=15))

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tick locators](https://matplotlib.org/stable/_images/sphx_glr_tick-locators_001_2_00x.png)

References

The following functions, methods, classes and modules are used in this example:

*   [`matplotlib.axis.Axis.set_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
    
*   [`matplotlib.axis.Axis.set_minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator")
    
*   [`matplotlib.ticker.NullLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullLocator "matplotlib.ticker.NullLocator")
    
*   [`matplotlib.ticker.MultipleLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
    
*   [`matplotlib.ticker.FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
    
*   [`matplotlib.ticker.LinearLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LinearLocator "matplotlib.ticker.LinearLocator")
    
*   [`matplotlib.ticker.IndexLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.IndexLocator "matplotlib.ticker.IndexLocator")
    
*   [`matplotlib.ticker.AutoLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "matplotlib.ticker.AutoLocator")
    
*   [`matplotlib.ticker.MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
    
*   [`matplotlib.ticker.LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
    

Tags: [component: ticks](https://matplotlib.org/stable/_tags/component-ticks.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 1.855 seconds)

[`Download Jupyter notebook: tick-locators.ipynb`](https://matplotlib.org/stable/_downloads/8bad1e245db1adfa0be564e7a208370a/tick-locators.ipynb)

[`Download Python source code: tick-locators.py`](https://matplotlib.org/stable/_downloads/7dd629c030892b8738bc4c5e86dc6736/tick-locators.py)

[`Download zipped: tick-locators.zip`](https://matplotlib.org/stable/_downloads/a6ee3474c57e1b8e2abb5c1a407badb2/tick-locators.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)