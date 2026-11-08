[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html#sphx-glr-download-gallery-lines-bars-and-markers-linestyles-py)
 to download the full example code.

Linestyles[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html#linestyles "Link to this heading")

==============================================================================================================================

Simple linestyles can be defined using the strings "solid", "dotted", "dashed" or "dashdot". More refined control can be achieved by providing a dash tuple `(offset, (on_off_seq))`. For example, `(0, (3, 10, 1, 15))` means (3pt line, 10pt space, 1pt line, 15pt space) with no offset, while `(5, (10, 3))`, means (10pt line, 3pt space), but skip the first 5pt line. See also [`Line2D.set_linestyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle "matplotlib.lines.Line2D.set_linestyle")
. The specific on/off sequences of the "dotted", "dashed" and "dashdot" styles are configurable:

*   `[rcParams["lines.dotted_pattern"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.dotted_pattern#rcparam-lines-dotted-pattern) ` (default: `[1.0, 1.65]`)
    
*   `[rcParams["lines.dashed_pattern"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.dashed_pattern#rcparam-lines-dashed-pattern) ` (default: `[3.7, 1.6]`)
    
*   `[rcParams["lines.dashdot_pattern"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.dashdot_pattern#rcparam-lines-dashdot-pattern) ` (default: `[6.4, 1.6, 1.0, 1.6]`)
    

_Note_: The dash style can also be configured via [`Line2D.set_dashes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "matplotlib.lines.Line2D.set_dashes")
 as shown in [Dashed line style configuration](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html)
 and passing a list of dash sequences using the keyword _dashes_ to the cycler in [property\_cycle](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#color-cycle)
.

import matplotlib.pyplot as plt
import numpy as np

[linestyle\_str](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
     ('solid', 'solid'),      \# Same as (0, ()) or '-'\
     ('dotted', 'dotted'),    \# Same as ':'\
     ('dashed', 'dashed'),    \# Same as '--'\
     ('dashdot', 'dashdot')\]  \# Same as '-.'

[linestyle\_tuple](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
     ('loosely dotted',        (0, (1, 10))),\
     ('dotted',                (0, (1, 5))),\
     ('densely dotted',        (0, (1, 1))),\
\
     ('long dash with offset', (5, (10, 3))),\
     ('loosely dashed',        (0, (5, 10))),\
     ('dashed',                (0, (5, 5))),\
     ('densely dashed',        (0, (5, 1))),\
\
     ('loosely dashdotted',    (0, (3, 10, 1, 10))),\
     ('dashdotted',            (0, (3, 5, 1, 5))),\
     ('densely dashdotted',    (0, (3, 1, 1, 1))),\
\
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),\
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),\
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))\]

def plot\_linestyles(ax, linestyles, title):
    X, Y \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 100, 10), [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(10)
    yticklabels \= \[\]

    for i, (name, linestyle) in enumerate(linestyles):
        ax.plot(X, Y+i, linestyle\=linestyle, linewidth\=1.5, color\='black')
        yticklabels.append(name)

    ax.set\_title(title)
    ax.set(ylim\=(\-0.5, len(linestyles)\-0.5),
           yticks\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(linestyles)),
           yticklabels\=yticklabels)
    ax.tick\_params(left\=False, bottom\=False, labelbottom\=False)
    ax.spines\[:\].set\_visible(False)

    \# For each line style, add a text annotation with a small offset from
    \# the reference point (0 in Axes coords, y tick value in Data coords).
    for i, (name, linestyle) in enumerate(linestyles):
        ax.annotate(repr(linestyle),
                    xy\=(0.0, i), xycoords\=ax.get\_yaxis\_transform(),
                    xytext\=(\-6, \-12), textcoords\='offset points',
                    color\="blue", fontsize\=8, ha\="right", family\="monospace")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(7, 8), height\_ratios\=\[1, 3\],
                               layout\='constrained')

plot\_linestyles([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [linestyle\_str](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[::\-1\], title\='Named linestyles')
plot\_linestyles([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [linestyle\_tuple](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[::\-1\], title\='Parametrized linestyles')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Named linestyles, Parametrized linestyles](https://matplotlib.org/stable/_images/sphx_glr_linestyles_001_2_00x.png)

Tags: [styling: linestyle](https://matplotlib.org/stable/_tags/styling-linestyle.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)

**Total running time of the script:** (0 minutes 1.233 seconds)

[`Download Jupyter notebook: linestyles.ipynb`](https://matplotlib.org/stable/_downloads/02d0c4a462fb00f782e5ac08185695e5/linestyles.ipynb)

[`Download Python source code: linestyles.py`](https://matplotlib.org/stable/_downloads/79cca01aa25ff65b23b051f7e4ca55f5/linestyles.py)

[`Download zipped: linestyles.zip`](https://matplotlib.org/stable/_downloads/0da42c93cf8dea70a69a957aaaec4f7e/linestyles.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)