[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-legend-demo-py)
 to download the full example code.

Legend Demo[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html#legend-demo "Link to this heading")

======================================================================================================================================

There are many ways to create and customize legends in Matplotlib. Below we'll show a few examples for how to do so.

First we'll show off how to make a legend for specific lines.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.collections as mcol
from matplotlib.legend\_handler import [HandlerLineCollection](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLineCollection "matplotlib.legend_handler.HandlerLineCollection")
, [HandlerTuple](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
from matplotlib.lines import [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

[t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 2.0, 0.1)
[t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 2.0, 0.01)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# note that plot returns a list of lines.  The "l1, = plot" usage
\# extracts the first element of the list into l1 using tuple
\# unpacking.  So l1 is a Line2D instance, not a sequence of lines
[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [l3](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), '--o', [t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.log](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1 + [t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), '.')
[l4](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), 's-.')

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(([l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [l4](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
), ('oscillatory', 'damped'), loc\='upper right', shadow\=True)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('time')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('volts')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Damped oscillation')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Damped oscillation](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_001_2_00x.png)

Next we'll demonstrate plotting more complex labels.

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1)

\# Plot the lines y=x\*\*n for n=1..4.
for [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(1, 5):
    [ax0.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*[n](https://docs.python.org/3/library/functions.html#int "builtins.int")
, label\=f"{[n](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=}")
[leg](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax0.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\="upper left", bbox\_to\_anchor\=\[0, 1\],
                 ncols\=2, shadow\=True, title\="Legend", fancybox\=True)
[leg.get\_title](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_title "matplotlib.legend.Legend.get_title")
().set\_color("red")

\# Demonstrate some more complex labels.
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2, label\="multi\\nline")
[half\_pi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([half\_pi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([half\_pi](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), label\=r"$\\frac{1}{2}\\pi$")
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 2\*\*([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2), label\="$2^{x^2}$")
[ax1.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(shadow\=True, fancybox\=True)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![legend demo](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_002_2_00x.png)

Here we attach legends to more complex plots.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, layout\="constrained")
[top\_ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [middle\_ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [bottom\_ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[top\_ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(\[0, 1, 2\], \[0.2, 0.3, 0.1\], width\=0.4, label\="Bar 1",
           align\="center")
[top\_ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(\[0.5, 1.5, 2.5\], \[0.3, 0.2, 0.2\], [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\="red", width\=0.4,
           label\="Bar 2", align\="center")
[top\_ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[middle\_ax.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
(\[0, 1, 2\], \[2, 3, 1\], xerr\=0.4, fmt\="s", label\="test 1")
[middle\_ax.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
(\[0, 1, 2\], \[3, 2, 4\], yerr\=0.3, fmt\="o", label\="test 2")
[middle\_ax.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
(\[0, 1, 2\], \[1, 1, 3\], xerr\=0.4, yerr\=0.3, fmt\="^",
                   label\="test 3")
[middle\_ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[bottom\_ax.stem](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
(\[0.3, 1.5, 2.7\], \[1, 3.6, 2.7\], label\="stem test")
[bottom\_ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![legend demo](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_003_2_00x.png)

Now we'll showcase legend entries with more than one legend key.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, layout\='constrained')

\# First plot: two legend keys for a single entry
[p1](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 \= [ax1.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
(\[1\], \[5\], c\='r', marker\='s', s\=100)
[p2](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 \= [ax1.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
(\[3\], \[2\], c\='b', marker\='o', s\=100)
\# \`plot\` returns a list, but we want the handle - thus the comma on the left
[p3](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 5\], \[4, 4\], 'm-d')

\# Assign two of the handles to the same legend entry by putting them in a tuple
\# and using a generic handler map (which would be used for any additional
\# tuples of handles like (p1, p3)).
[l](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax1.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[([p1](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")\
, [p3](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
), [p2](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")\
\], \['two keys', 'one key'\], scatterpoints\=1,
               numpoints\=1, handler\_map\={tuple: [HandlerTuple](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
(ndivide\=None)})

\# Second plot: plot two bar charts on top of each other and change the padding
\# between the legend keys
[x\_left](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1, 2, 3\]
[y\_pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1, 3, 2\]
[y\_neg](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[2, 1, 4\]

[rneg](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [ax2.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([x\_left](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y\_neg](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, width\=0.5, [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\='w', hatch\='///', label\='-1')
[rpos](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [ax2.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([x\_left](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y\_pos](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, width\=0.5, [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\='k', label\='+1')

\# Treat each legend entry differently by using specific \`HandlerTuple\`s
[l](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax2.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[([rpos](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")\
, [rneg](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")\
), ([rneg](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")\
, [rpos](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")\
)\], \['pad!=0', 'pad=0'\],
               handler\_map\={([rpos](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
, [rneg](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
): [HandlerTuple](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
(ndivide\=None),
                            ([rneg](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
, [rpos](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
): [HandlerTuple](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
(ndivide\=None, pad\=0.)})
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![legend demo](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_004_2_00x.png)

Finally, it is also possible to write custom classes that define how to stylize legends.

class HandlerDashedLines([HandlerLineCollection](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLineCollection "matplotlib.legend_handler.HandlerLineCollection")
):
    """
    Custom Handler for LineCollection instances.
    """
    def create\_artists(self, legend, orig\_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        \# figure out how many lines there are
        numlines \= len(orig\_handle.get\_segments())
        xdata, xdata\_marker \= self.get\_xdata(legend, xdescent, ydescent,
                                             width, height, fontsize)
        leglines \= \[\]
        \# divide the vertical space where the lines will go
        \# into equal parts based on the number of lines
        ydata \= [np.full\_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
(xdata, height / (numlines + 1))
        \# for each line, create the line at the proper location
        \# and set the dash pattern
        for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(numlines):
            legline \= [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
(xdata, ydata \* (numlines \- [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
) \- ydescent)
            self.update\_prop(legline, orig\_handle, legend)
            \# set color, dash pattern, and linewidth to that
            \# of the lines in linecollection
            try:
                [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= orig\_handle.get\_colors()\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
            except IndexError:
                [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= orig\_handle.get\_colors()\[0\]
            try:
                dashes \= orig\_handle.get\_dashes()\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
            except IndexError:
                dashes \= orig\_handle.get\_dashes()\[0\]
            try:
                lw \= orig\_handle.get\_linewidths()\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
            except IndexError:
                lw \= orig\_handle.get\_linewidths()\[0\]
            if dashes\[1\] is not None:
                legline.set\_dashes(dashes\[1\])
            legline.set\_color([color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
            legline.set\_transform(trans)
            legline.set\_linewidth(lw)
            leglines.append(legline)
        return leglines

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 5, 100)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.prop\_cycle'\].by\_key()\['color'\]\[:5\]
[styles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['solid', 'dashed', 'dashed', 'dashed', 'solid'\]
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip(range(5), [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [styles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \- .1 \* [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, c\=[color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, ls\=[style](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

\# make proxy artists
\# make list of one line -- doesn't matter what the coordinates are
[line](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[(0, 0)\]\]
\# set up the proxy artist
[lc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 \= [mcol.LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
(5 \* [line](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, linestyles\=[styles](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
\# create the legend
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[[lc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")\
\], \['multi-line'\], handler\_map\={type([lc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
): [HandlerDashedLines](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLineCollection "matplotlib.legend_handler.HandlerLineCollection")
()},
          handlelength\=2.5, handleheight\=3)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![legend demo](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_005_2_00x.png)

See also

The [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 contains an in depth discussion on the configuration options for legends.

**Total running time of the script:** (0 minutes 3.913 seconds)

[`Download Jupyter notebook: legend_demo.ipynb`](https://matplotlib.org/stable/_downloads/4c0ce4a33804cb08f86ba70337fad464/legend_demo.ipynb)

[`Download Python source code: legend_demo.py`](https://matplotlib.org/stable/_downloads/6aa8e5919ce32e892d549350231357cd/legend_demo.py)

[`Download zipped: legend_demo.zip`](https://matplotlib.org/stable/_downloads/22e2fad02d0d1099c3a19206ebf4a960/legend_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)