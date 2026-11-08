[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html#sphx-glr-download-gallery-subplots-axes-and-figures-subfigures-py)
 to download the full example code.

Figure subfigures[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html#figure-subfigures "Link to this heading")

===============================================================================================================================================

Sometimes it is desirable to have a figure with two different layouts in it. This can be achieved with [nested gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)
, but having a virtual figure with its own artists is helpful, so Matplotlib also has "subfigures", accessed by calling [`matplotlib.figure.Figure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
 in a way that is analogous to [`matplotlib.figure.Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
, or [`matplotlib.figure.Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 to make an array of subfigures. Note that subfigures can also have their own child subfigures.

import matplotlib.pyplot as plt
import numpy as np

def example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, fontsize\=12, hide\_labels\=False):
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(30, 30), vmin\=-2.5, vmax\=2.5)
    if not hide\_labels:
        [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x-label', fontsize\=fontsize)
        [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('y-label', fontsize\=fontsize)
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Title', fontsize\=fontsize)
    return [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680808)
\# gridspec inside gridspec
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\='constrained', figsize\=(10, 4))
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(1, 2, wspace\=0.07)

[axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].subplots(1, 2, sharey\=True)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_facecolor('0.75')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].suptitle('Left plots', fontsize\='x-large')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].colorbar([pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, shrink\=0.6, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, location\='bottom')

[axsRight](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].subplots(3, 1, sharex\=True)
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axsRight](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
    if [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 2:
        [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('xlabel')
    if [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 1:
        [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('ylabel')

[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_facecolor('0.85')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].colorbar([pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, shrink\=0.6, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axsRight](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].suptitle('Right plots', fontsize\='x-large')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Figure suptitle', fontsize\='xx-large')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Figure suptitle, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_subfigures_001_2_00x.png)

It is possible to mix subplots and subfigures using [`matplotlib.figure.Figure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
. This requires getting the gridspec that the subplots are laid out on.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 3, layout\='constrained', figsize\=(10, 4))
[gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].get\_subplotspec().get\_gridspec()

\# clear the left column for the subfigure:
for [a](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\]:
    [a.remove](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove.html#matplotlib.axes.Axes.remove "matplotlib.axes.Axes.remove")
()

\# plot data in remaining Axes:
for [a](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1:\].flat:
    [a.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10))

\# make the subfigure in the empty gridspec slots:
[subfig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 \= [fig.add\_subfigure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
([gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[:, 0\])

[axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfig.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots")
(1, 2, sharey\=True)
[subfig.set\_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.set_facecolor.html#matplotlib.figure.SubFigure.set_facecolor "matplotlib.figure.SubFigure.set_facecolor")
('0.75')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[subfig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle")
('Left plots', fontsize\='x-large')
[subfig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.colorbar.html#matplotlib.figure.SubFigure.colorbar "matplotlib.figure.SubFigure.colorbar")
([pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, shrink\=0.6, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, location\='bottom')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Figure suptitle', fontsize\='xx-large')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Figure suptitle, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_subfigures_002_2_00x.png)

Subfigures can have different widths and heights. This is exactly the same example as the first example, but _width\_ratios_ has been changed:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\='constrained', figsize\=(10, 4))
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(1, 2, wspace\=0.07, width\_ratios\=\[2, 1\])

[axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].subplots(1, 2, sharey\=True)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_facecolor('0.75')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].suptitle('Left plots', fontsize\='x-large')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].colorbar([pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, shrink\=0.6, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axsLeft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, location\='bottom')

[axsRight](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].subplots(3, 1, sharex\=True)
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axsRight](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
    if [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 2:
        [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('xlabel')
    if [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \== 1:
        [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('ylabel')

[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_facecolor('0.85')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].colorbar([pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, shrink\=0.6, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axsRight](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].suptitle('Right plots', fontsize\='x-large')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Figure suptitle', fontsize\='xx-large')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Figure suptitle, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_subfigures_003_2_00x.png)

Subfigures can be also be nested:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\='constrained', figsize\=(10, 8))

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('fig')

[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(1, 2, wspace\=0.07)

[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_facecolor('coral')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].suptitle('subfigs\[0\]')

[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_facecolor('coral')
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].suptitle('subfigs\[1\]')

[subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].subfigures(2, 1, height\_ratios\=\[1, 1.4\])
[subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].suptitle('subfigsnest\[0\]')
[subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_facecolor('r')
[axsnest0](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].subplots(1, 2, sharey\=True)
for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axsnest0](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
[subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].colorbar([pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axsnest0](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].suptitle('subfigsnest\[1\]')
[subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_facecolor('g')
[axsnest1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigsnest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].subplots(3, 1, sharex\=True)

[axsRight](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].subplots(2, 2)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![fig](https://matplotlib.org/stable/_images/sphx_glr_subfigures_004_2_00x.png)

Tags: [component: figure](https://matplotlib.org/stable/_tags/component-figure.html)
 [plot-type: pcolormesh](https://matplotlib.org/stable/_tags/plot-type-pcolormesh.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 7.498 seconds)

[`Download Jupyter notebook: subfigures.ipynb`](https://matplotlib.org/stable/_downloads/ca675a104825e0fc1f5523a07e03aec6/subfigures.ipynb)

[`Download Python source code: subfigures.py`](https://matplotlib.org/stable/_downloads/a60fd01ed70531c8e03f55f32b6c55ff/subfigures.py)

[`Download zipped: subfigures.zip`](https://matplotlib.org/stable/_downloads/15c76c1f97b82b13cf6a6312e11d8837/subfigures.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)